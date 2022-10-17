function show(){
    var x=document.querySelector(".password");
    var icon=document.querySelector(".fa-solid");
    if(x.type==="password"){
        x.type="text";
        icon.classList.remove("fa-eye");
        icon.classList.add("fa-eye-slash");
    }
    else {
        x.type = "password";
        icon.classList.add("fa-eye");
        icon.classList.remove("fa-eye-slash");
    }
}