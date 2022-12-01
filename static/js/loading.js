function showLoading(){
    const loading = document.getElementById("load");

    loading.classList.add("loader");

    setTimeout(() => hideLoading(), 7000);
}

function hideLoading(){
    const loading = document.getElementById("load");
    const conect = document.getElementById("conect");
    const wrapperLogin = document.getElementById('wrapper-login-card')

    loading.classList.remove("loader");
    conect.classList.toggle("toggle");
    wrapperLogin.classList.toggle("toggle");
}

showLoading()