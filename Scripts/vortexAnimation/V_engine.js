/* ----- Генератор спирали ----- */

var frame = V_START_FRAME,  // не удалять (на нее ссылаются!)
    isOpen = false;         // произошла ли анимация развертывания спирали (не удалять!)


// Конвернирует градусы в радианы
rad = (degree) => {return degree * (Math.PI / 180);}


// Вычисляет координаты точки спирали
calcX = (r, phi) => {return Math.trunc(r * Math.cos(phi) * V_WIDTH_VORTEX) * V_SCALE_SIMBOL;}
calcY = (r, phi) => {return Math.trunc(r * Math.sin(phi) * V_HEIGHT_VORTEX) * V_SCALE_SIMBOL;} 


// Анимирует вращения спирали (ссылается на глобальную переменную frame!!!)
keyframes = () => {if (frame > V_END_FRAME) frame = V_START_FRAME; frame += V_SPEED_ANIMATION;} 


/**
 * Возвращает коэффициент разлета ветки спирали.
 * @author Arseniy ELiseev
 * @param {number} deviationNow Разлет спирали на данный момент
 * @param {number} itr Индекс спирали
 * @returns {number}
 */
function deviation(deviationNow, itr)
{
    if (deviationNow > V_END_FRAME) isOpen = true;
    return (deviationNow < V_BRANCHES[itr].deviation && !isOpen) ? deviationNow : V_BRANCHES[itr].deviation;
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

    for (let a = 0, angle = 0; a < 3.5; a += V_BRANCH_STEP, angle += V_ANGLE_STEP)
    {
        phi = rad(angle) - speed;
        r = a + b * rad(angle);

        x = calcX(r, phi);
        y = calcY(r, phi);

        if (a > start && a < end)
        {
            V_CTX.fillText( '.', x, y);
            V_CTX.fillText( '.', -x, -y);
        }
    }
}


/**
 * Рисует спираль
 * @author Arseniy ELiseev
 */
function drawVortex(){

    V_CTX.clearRect(-V_WIDTH, -V_HEIGHT, V_WIDTH * 2, V_HEIGHT * 2);
    V_CTX.fillStyle = "white";
    V_CTX.fillRect(-V_WIDTH, -V_HEIGHT, V_WIDTH * 2, V_HEIGHT * 2);
    V_CTX.fillStyle = V_COLOR_VORTEX;
    
    keyframes();

    for (let i = 0; i < V_BRANCHES.length; i++)
        vortex(
            frame * V_BRANCHES[i].speed,
            deviation(frame, i),
            V_BRANCHES[i].start,
            V_BRANCHES[i].end
            );

}

setInterval(drawVortex, V_FPS);