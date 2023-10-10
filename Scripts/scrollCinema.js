// 3D Scroll

let zSpacing = -1000,                                                   //Расстояние между рамками (frame)
    lastPos = zSpacing / 5,                                             //Последняя позиция рамки
    $frames = document.getElementsByClassName('frame'),                 //HTML Collection со всеми элементами класа frame
    frames = Array.from($frames),                       
    zVals = [],                                                         //Массив с координатами рамок
    flagEnd = false                                                     //Флаг останова



window.onscroll = function ()
{


    let top = document.documentElement.scrollTop,                       //Вехняя граница документа
        delta = lastPos - top


    lastPos = top
    if(!flagEnd){
        frames.forEach(function(n, i)
        {
            zVals.push((i * zSpacing * 2) + zSpacing * 1.5)                 //Вычисляем положение рамки на странице
            zVals[i] += delta * -5


            let frame = frames[i],
                transform = `translateZ(${zVals[i]}px)`,                //создаём атрибут трансформации для рамки - сместиться на zVals[i]пиксель
                opacity = zVals[i] < Math.abs(zSpacing) / 2 ? 1 : 0,    //создаём отрибут видимости рамки
                $textBlurRight = frame.getElementsByClassName("textBlurRight"),
                $textBlurLeft = frame.getElementsByClassName("textBlurLeft")


            frame.setAttribute('style', `transform: ${transform}; opacity: ${opacity}`)

            if($textBlurRight.length != 0)
            {


                let textBlurRight = $textBlurRight[0],
                    left = zVals[i] < zSpacing * 1.5 ? 50 : 35
                    opacity = zVals[i] < zSpacing * 1.5 ? 0 : 1

            
                textBlurRight.setAttribute("style", `left: ${left}vw; opacity: ${opacity}`)
            }

            if($textBlurLeft.length != 0)
            {


                let textBlurLeft = $textBlurLeft[0],
                    right = zVals[i] < zSpacing * 1.5 / 2 ? -50 : -35
                    opacity = zVals[i] < zSpacing * 1.5 / 2 ? 0 : 1


                textBlurLeft.setAttribute("style", `left: ${right}vw; opacity: ${opacity}`)
            }
        })
    }
    
    str = frames[frames.length - 1].style.transform                     //Берём последний существующий фрэйм


    let leftBracket = str.indexOf("("),
        rightBracket = str.indexOf(")")

    
    number = Number(str.substr(leftBracket + 1, (rightBracket - leftBracket) - 3))  //Получаем положение последней рамки
    if(number >= 1000)
    {

        flagEnd = true

        frames.forEach(function(n, i)
        {

            
            let frame = frames[i]


            frame.setAttribute('style', `opacity: ${0}`)
        })
        
        scroll(0, 0)                                                    //Возвращаемся в начало страницы при достяжении её конца

        flagEnd = false
    }

}

window.scrollTo(0, 1)