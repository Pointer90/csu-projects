/* ----- Файл с реализацией "движка" заднего фона ----- */

var bNumbers = [],   // Массив чисел для рисования (не удалять!)
    bFrame = B_START_FRAME;

/**
 * Получить число в десятичной форме в указанном диапазоне
 * @author Arseniy ELiseev
 * @param {Number} min Минимальное значение диапазона
 * @param {Number} max Максимальное значение диапазона
 * @returns 
 */
function getNum(min, max) {return min + Math.trunc(Math.random() * 100000000000) % (max - min);}


/**
 * Конвертировать число в двоичный вид в указанном диапазоне
 * @author Arseniy ELiseev
 * @param {Number} min Минимальное значение диапазона
 * @param {Number} max Максимальное значение диапазона
 * @returns 
 */
function toBinary(min, max) {return (getNum(min, max)).toString(2);}


/**
 * Задает мигание строк
 * @param {Object} elem Объект "строка" с полями opacity и speed
 */
function blink (elem)
{
    if (elem.opacity > 0.99 || elem.opacity < 0.01) elem.direction *= -1;

    elem.opacity += elem.direction / 100;
    B_CTX.globalAlpha = elem.opacity;
}


/**
 * Изменяет положение строки, если она достигла края экрана
 * @param {Object} elem 
 */
function isTochedBorder (elem)
{
    let border = B_WIDTH * 1.5;

    if (elem.x > border || elem.x < -border)
    {
        if (elem.direction < 0)
            elem.x = getNum(-border, -border / 2);
        else
            elem.x = getNum(border / 2, border);
    }
}

/**
 *  Зацикливает анимацию
 * @author Arseniy ELiseev
 * @param {Number} frame Ключевой кадр анимации
 */
function keyframe() {if (bFrame >= B_END_FRAME) bFrame = B_START_FRAME; else bFrame += 1;}

/**
 * Заполняет массив чисел начальными значениями в виде строк
 * @author Arseniy ELiseev
 */
function createStrings()
{
    let rows = 12,    // Количество строк в высоту
        shifts = [8, 7, 9, 7, 8, 9, 7, 8, 9, 7, 8, 9],
        speeds = [3, -2, 1, 4, -1, 5, 2, 3, -5, 4, -1, 4];

    for(let row = 0; row < rows; row++)
    {
        bNumbers.push(
            {
                str: toBinary(16, 64),
                x: getNum(-B_WIDTH * 2, B_WIDTH * 2),
                y: row * B_SPACE_LINES,
                direction: 1,
                speedX: speeds[row],
                opacity: getNum(1, 8) / 10,
                shift: shifts[row]
            });
    }

}


/**
 * Изменяет значения чисел, положение, прозрачность, направление движения
 * @author Arseniy ELiseev
 */
function changeStrings(frame)
{
    for(let i = 0; i < bNumbers.length; i++)
    {
        isTochedBorder(bNumbers[i]);

        if (frame % bNumbers[i].shift == 0) bNumbers[i].str = toBinary(16, 64);
        bNumbers[i].x += bNumbers[i].speedX;
        blink(bNumbers[i]);

        B_CTX.fillText(" " + bNumbers[i].str, bNumbers[i].x, bNumbers[i].y * B_FONT_SIZE);
    } 
}

/**
 * Рисует задний фон
 * @author Arseniy ELiseev
 */
function drawBackground()
{
    
    B_CTX.clearRect(0, 0, B_WIDTH * 2, B_HEIGHT * 2);
    B_CTX.fillStyle = B_COLOR_TEXT;

    keyframe();
    changeStrings(bFrame);
}

function init()
{
    createStrings();
    setInterval(drawBackground, B_FPS);
}

init();