/* ----- Генератор спирали ----- */

var img = document.getElementById("test");


var frame = vSTART_FRAME,  // не удалять (на нее ссылаются!)
    isOpen = false;         // произошла ли анимация развертывания спирали (не удалять!)


// Конвернирует градусы в радианы
rad = (degree) => {return degree * (Math.PI / 180);}

// Вычисляет координаты точки спирали
calcX = (r, phi) => {return Math.trunc(r * Math.cos(phi) * vSTRETCH_WIDTH) * 12;}
calcY = (r, phi) => {return Math.trunc(r * Math.sin(phi) * vSTRETCH_HEIGHT) * 8;} 


// Анимирует вращения спирали (ссылается на глобальную переменную frame!!!)
keyframes = () => {if (frame > vEND_FRAME) frame = vSTART_FRAME; frame += vSPEED_ANIMATION;} 


/**
 * Возвращает коэффициент разлета ветки спирали.
 * @author Arseniy ELiseev
 * @param {number} deviationNow Разлет спирали на данный момент
 * @param {number} itr Индекс спирали
 * @returns {number}
 */
function deviation(deviationNow, itr)
{
    if (deviationNow > vEND_FRAME) isOpen = true;
    return (deviationNow < vBRANCHES[itr].deviation && !isOpen) ? deviationNow : vBRANCHES[itr].deviation;
}


/**
 * Вычисляет координаты каждой точки спирали
 * @author Arseniy ELiseev
 * @param {number} speed Скорость вращение спирали
 * @param {number} b Расстояние между ветками спирали
 * @param {number} start Коэффициент того, где нужно начать рисовать ветку
 * @param {number} end Коэффициент того, где нужно закончить рисовать ветку
 */
function vortex(speed, b, start, end)
{
    /* 

    a — отвечает за расстояние откуда начинается виток
    b — отвечает за расстояние между витками
    start — размер отступа от начала спирали
    angle — угол поворота витков
    phi — Угол поворта спирали
    r — коэффициент спирали

    */

    for (let a = 0, angle = 0; a < 3.5; a += vBRANCH_STEP, angle += vANGLE_STEP)
    {
        phi = rad(angle) - speed;
        r = a + b * rad(angle);

        x = calcX(r, phi);
        y = calcY(r, phi);

        if (a > start && a < end)
        {
            vCTX.fillText( '.', x, y);
            vCTX.fillText( '.', -x, -y);
        }
    }
}


/**
 * Рисует спираль
 * @author Arseniy ELiseev
 */
function drawVortex(color)
{
    vCTX.fillStyle = color;

    for (let i = 0; i < vBRANCHES.length; i++)
        vortex(
            frame * vBRANCHES[i].speed,
            deviation(frame, i),
            vBRANCHES[i].start,
            vBRANCHES[i].end
            );
}

function drawLogo(color)
{
    vCTX.fillStyle = color;

    for (i = 0; i < LOGO.length; i++)
        vCTX.fillText(LOGO[i], 0, (i * 8 - 88));
}

function draw()
{
    
    vCTX.clearRect(-vWIDTH, -vHEIGHT,vWIDTH * 2, vHEIGHT * 2);
    keyframes();
    drawVortex(grdLogo);
    drawLogo(grdVortex);
}



setInterval(draw, vFPS);