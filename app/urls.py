from django.urls import path
from .views import home,login_page,register_page,register_details,login,login_details,ems_dashboard,get_events,event_detail,book_event,my_bookings,ems_profile,logout_view

urlpatterns=[
    path("",home),
    # path("login_page/",login_page),
    # path("register_page/",register_page),
    # add name for login page url
    path("login_page/", login_page, name="login_page"),

# add name for register page url
    path("register_page/", register_page, name="register_page"),
    path("register_details/",register_details),
    # path("login/",login),
    path("login/", login, name="login"),
    path("login_details/",login_details),
    path("ems_dashboard/",ems_dashboard),
    # path("ems_dashboard/bookings/", ems_dashboard),
    # path("ems_dashboard/profile/", ems_dashboard),
    path("ems_dashboard/profile/", ems_profile),
    path("get_events/",get_events),
    path("ems_dashboard/event/<int:id>/", event_detail),
    path("book-event/<int:id>/", book_event),
    path("ems_dashboard/bookings/",my_bookings),

    path("logout/", logout_view),

            
            
            
             ]