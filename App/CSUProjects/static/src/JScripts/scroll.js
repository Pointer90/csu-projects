var elements = [...document.querySelectorAll('.scroll-check')];
var wh = document.documentElement.clientHeight;
var current = elements.shift();


function elementsOnScreen(){
    while (current.offsetTop < wh){
        current.classList.add(`appearance-${current.dataset.direction}-${current.dataset.delay}`);
        if(elements.length > 0)
            current = elements.shift();
    }
}

if(elements.length > 0){
    elementsOnScreen();

    window.addEventListener('scroll', () =>{
        var wt = window.scrollY;
        wh = document.documentElement.clientHeight;
    
        var et = current.offsetTop;
        var eh = current.clientHeight;
        if(wt + wh >= et || eh + et < wh){
            current.classList.add(`appearance-${current.dataset.direction}-${current.dataset.delay}`);
            if(elements.length > 0)
                current = elements.shift();
        }
    
    })
}