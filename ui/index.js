clickMe = document.getElementById("click-me")
targets = document.querySelector(".targets ul")
clickMe.addEventListener('click',async (e)=>{
    
    const res = await pywebview.api.load_data()
    pywebview.api.log(res)
    for (r of res){
        child = document.createElement("li")
        child.textContent  = r["target"]
        targets.appendChild(child)
    }
    

})