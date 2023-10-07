// 3D Scroll

let zSpacing = -1000,
    lastPos = zSpacing / 5,
    $frames = document.getElementsByClassName('frame'),
    frames = Array.from($frames),
    zVals = [],
    flagEnd = false

window.onscroll = function()
{


    let top = document.documentElement.scrollTop,
        delta = lastPos - top


    lastPos = top
    if(!flagEnd){
        frames.forEach(function(n, i)
        {
            zVals.push((i * zSpacing) + zSpacing * 1.5)
            zVals[i] += delta * -5


            let frame = frames[i],
                transform = `translateZ(${zVals[i]}px)`,
                opacity = zVals[i] < Math.abs(zSpacing) / 2 ? 1 : 0,
                $textBlurRight = frame.getElementsByClassName("textBlurRight"),
                $textBlurLeft = frame.getElementsByClassName("textBlurLeft")


            frame.setAttribute('style', `transform: ${transform}; opacity: ${opacity}`)

            if($textBlurRight.length != 0)
            {


                let textBlurRight = $textBlurRight[0],
                    left = zVals[i] < zSpacing ? 50 : 25
                    opacity = zVals[i] < zSpacing ? 0 : 1

            
                textBlurRight.setAttribute("style", `left: ${left}vw; opacity: ${opacity}`)
            }

            if($textBlurLeft.length != 0)
            {


                let textBlurLeft = $textBlurLeft[0],
                    right = zVals[i] < zSpacing / 2 ? -50 : -25
                    opacity = zVals[i] < zSpacing / 2 ? 0 : 1


                textBlurLeft.setAttribute("style", `left: ${right}vw; opacity: ${opacity}`)
            }
        })
    }
    
    str = frames[frames.length - 1].style.transform


    let leftBracket = str.indexOf("("),
        rightBracket = str.indexOf(")")

    
    number = Number(str.substr(leftBracket + 1, (rightBracket - leftBracket) - 3))
    if(number >= 1000)
    {

        flagEnd = true

        frames.forEach(function(n, i)
        {

            
            let frame = frames[i]


            frame.setAttribute('style', `opacity: ${0}`)
        })
        
        scroll(0, 0)

        flagEnd = false
    }

}

window.scrollTo(0, 1)