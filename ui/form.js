back = document.querySelector(".back")

back.addEventListener('click',(e)=>{
    pywebview.api.route("ui/index.html")
})