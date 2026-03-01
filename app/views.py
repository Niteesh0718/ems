from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import registerdetails,Event,Booking
from django.db import transaction
from django.utils import timezone  



def logout_view(request):
    request.session.flush()   # ✅ clears all session data (logs user out)
    return redirect("/login/")# redirect to login page

def ems_profile(request):
    user_email = request.session.get("user_email")
    if not user_email:
        return redirect("login")

    user = registerdetails.objects.get(email=user_email)
    bookings = Booking.objects.filter(email=user_email)

    total_bookings = bookings.count()
    upcoming_count = bookings.filter(event_date__gte=timezone.now().date()).count()
    past_count = bookings.filter(event_date__lt=timezone.now().date()).count()

    return render(request, "ems_profile.html", {
        "user": user,
        "total_bookings": total_bookings,
        "upcoming_count": upcoming_count,
        "past_count": past_count,
    })



def my_bookings(request):
    user_email = request.session.get("user_email")

    if not user_email:
        return redirect("login")

    bookings = Booking.objects.filter(email=user_email).order_by("event_date", "event_time")
    return render(request, "my_bookings.html", {"bookings": bookings})






@api_view(["POST"])
def book_event(request, id):
    name = request.data.get("name")
    input_email = request.data.get("email")  # 👈 email from form

    user_email = request.session.get("user_email")
    if not user_email:
        return Response({"status": False, "msg": "Please login to book"}, status=401)

    # ✅ Enforce same email as logged in
    if input_email and input_email.lower() != user_email.lower():
        return Response({
            "status": False,
            "msg": "Please book using your registered login email only."
        }, status=400)

    try:
        with transaction.atomic():
            event = Event.objects.select_for_update().get(id=id)

            if Booking.objects.filter(event_id=event.id, email=user_email).exists():
                return Response({"status": False, "msg": "Already booked"}, status=400)

            if event.vacancy <= 0:
                return Response({"status": False, "msg": "Event is sold out"}, status=400)

            event.vacancy -= 1
            event.save()

            Booking.objects.create(
                name=name,
                email=user_email,        # 👈 always save logged-in email
                event_id=event.id,
                event_name=event.event_name,
                event_date=event.date,
                event_time=event.time,
                event_img=event.img_url,
            )

        return Response({"status": True, "msg": "Thanks for booking! Check My Bookings."})

    except Event.DoesNotExist:
        return Response({"status": False, "msg": "Event not found"}, status=404)





def event_detail(req, id):
    event = Event.objects.get(id=id)
    return render(req, "event_detail.html", {"event": event})

@api_view(["GET"])
def get_events(req):
    events = Event.objects.all()
    data = []

    for e in events:
        data.append({
            "id": e.id,
            "event_name": e.event_name,
            "about_event": e.about_event,
            "date": e.date,
            "time": e.time,
            "venue": e.venue,
            "vacancy": e.vacancy,
            "ratings": float(e.ratings),
            "img_url": e.img_url,
            "instructions": e.instructions,
        })

    return Response(data)


   




def ems_dashboard(req):
    if "bookings" in req.path:
        template = "ems_bookings.html"
    elif "profile" in req.path:
        template = "ems_profile.html"
    else:
        template = "ems_dashboard.html"  # home

    return render(req, template)
    


@api_view(["POST"])
def login_details(request):
    email = request.data.get("email")
    password = request.data.get("password")

    if not email or not password:
        return Response({
            "status": False,
            "msg": "Email and password are required"
        }, status=400)

    try:
        user = registerdetails.objects.get(email=email)

        if user.password == password:
           
            request.session["user_email"] = email

            return Response({
                "status": True,
                "msg": "Logged in successfully",
                "ref": "ems_dashboard"
            })
        else:
            return Response({
                "status": False,
                "msg": "Incorrect password"
            }, status=400)

    except registerdetails.DoesNotExist:
        return Response({
            "status": False,
            "msg": "Email not registered"
        }, status=404)
   

    






def login(req):
    return render(req,"login.html")

@api_view(["POST"])
def register_details(req):
    n = req.data.get("name")
    e = req.data.get("email")
    p = req.data.get("password")
    c_p = req.data.get("c_password")

    #    Block duplicate email
    if registerdetails.objects.filter(email=e).exists():
        return Response({
            "status": False,
            "msg": "This email is already registered. Please login."
        }, status=400)

    if p == c_p:
        registerdetails.objects.create(name=n, email=e, password=p, c_password=c_p)
        return Response({"status": True, "msg": "Thanks for registering"})
    else:
        return Response({
            "status": False,
            "msg": "Passwords do not match. Please try again."
        }, status=400)


def login_page(req):
    return render(req,"login.html")

def register_page(req):
    return render(req,"register.html")


def home(req):
    return render(req,"home.html")

