const   elements = document.querySelectorAll(".card-title");
var     searchForm = document.forms[0]

searchForm.addEventListener('submit', function(event) {
    event.preventDefault();

    query = searchForm[0].value.toLowerCase()

    if (query == "")
    {
        for (let i = 0; i < elements.length; i++)
            elements[i].closest('.card').classList.remove('visually-hidden')
            
    }
    else
    {
        for (let i = 0; i < elements.length; i++)
        {
            title = elements[i].textContent.toLowerCase()

            if (!title.includes(query))
            elements[i].closest('.card').classList.add('visually-hidden')
        }
        
    }
})