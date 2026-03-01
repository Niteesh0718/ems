 let btn = document.getElementById("login_btn");

  if (btn) {  // ✅ prevent null error if ID is wrong
    btn.addEventListener("click", (a) => {
      a.preventDefault();

      let e = document.getElementById("email").value;
      let p = document.getElementById("password").value;

      let data = { email: e, password: p };

      fetch("/login_details/", {
        method: "post",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": getCSRFToken() // ✅ add ONLY if you see 403 Forbidden
        },
        body: JSON.stringify(data)
      })
      .then((res) => res.json())
      .then((res) => {
        if (res.status) {
          alert(res.msg);
          window.location.href = `/${res.ref}/`;  // /ems_dashboard/
        } else {
          alert(res.msg);
        }
      })
      .catch((err) => {          // ✅ catch network/server errors
        console.error(err);
        alert("Server error. Check console.");
      });
    });
  }

  // OPTIONAL: Only if Django throws 403 Forbidden
  function getCSRFToken() {
    let name = "csrftoken";
    let cookies = document.cookie.split(";");

    for (let cookie of cookies) {
      cookie = cookie.trim();
      if (cookie.startsWith(name + "=")) {
        return cookie.substring(name.length + 1);
      }
    }
    return "";
  }
