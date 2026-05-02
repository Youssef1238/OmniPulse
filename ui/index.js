links = document.querySelectorAll(".link")

dashboard = document.getElementById('dashboard')


for(link of links){
    link.addEventListener('click',(e)=>{
        pywebview.api.route(e.target.getAttribute("href"))
    })
}



window.addEventListener("pywebviewready",async (e)=>{
    const data = await pywebview.api.load_data()
    
    for(row of data){
        const articleLink = await pywebview.api.get_link(row["url"],row["last_seen"]) 
        const item = document.createElement('tr')
        const name = document.createElement('td')
        const article = document.createElement('td') 
        name.setAttribute("href",row["url"])
        name.setAttribute("class","url")
        article.setAttribute("class","url")
        article.setAttribute("href",articleLink)
        name.innerHTML = row["name"]
        article.innerHTML = row["title"].length > 50 ? row["title"].slice(0,50) + "..." : row["title"]
        item.appendChild(name)
        item.appendChild(article)
        dashboard.appendChild(item)
    }

    urls = document.querySelectorAll(".url")

    for(url of urls){
        url.addEventListener('click',(e)=>{
            pywebview.api.redirect(e.target.getAttribute("href"))
        })
    }
})
