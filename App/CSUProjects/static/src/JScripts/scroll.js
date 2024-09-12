var elements = [...document.querySelectorAll('.scroll-check')];
var wh = document.documentElement.clientHeight;
var current = elements.shift();

const border = 100;


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
        if(wt + wh >= et - border || eh + et - border < wh){
            current.classList.add(`appearance-${current.dataset.direction}-${current.dataset.delay}`);
            if(elements.length > 0)
                current = elements.shift();
        }
    
    })
}