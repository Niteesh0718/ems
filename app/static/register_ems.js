let btn=document.getElementById("reg_btn")
btn.addEventListener("click",(a)=>{
    a.preventDefault() 
    let n=document.getElementById("name").value
    let e=document.getElementById("email").value
    let p=document.getElementById("password").value
    let c_p=document.getElementById("c_password").value
    let data={
        name:n,
        email:e,
        password:p,
        c_password:c_p
    }
    console.log(data)
    fetch('http://127.0.0.1:8000/register_details/',{
        method:'post',
        headers:{
            "content-Type":"application/json"
        },
        body:JSON.stringify(data)

    })
    .then((res)=>res.json())
    .then((res)=>{

       
       console.log(res.msg)

        
        if(res.success){
            alert(res.msg)
            document.getElementById("name").value = ""
            document.getElementById("email").value = ""
            document.getElementById("password").value = ""
            document.getElementById("c_password").value = ""
        }else{
            alert(res.msg)
        }
    })
})