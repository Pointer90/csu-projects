/* ----- Генератор "шум слова" ----- */

const   ELEMENT = document.querySelector("#title"),
        WORD = ELEMENT.innerText,
        SIMBOLS = "!@#$%&/[]{}?<>0123456789";

var fps = 200,
    noise = [];
        

/**
 * Выбирает в случайном порядке индекс элемента из массива SIMBOLS
 * @author Arseniy Eliseev
 * @returns 
 */
function getIndexSimbol() {return Math.floor(Math.random() * 100) % SIMBOLS.length;}


/**
 * Генерирует начальный шум в слове
 * @author Arseniy Eliseev
 * @param {String} word 
 */
function genNoise(word)
{
    for ( let i = 0; i < word.length; i++)
        noise.push(getIndexSimbol());
}


/**
 *  Псевдо-поиск перебором символов слова
 * @author Arseniy Eliseev
 * @returns 
 */
function enumeration()
{
    let result = "",
        isDone = true;
        
        for (let i = 0; i < noise.length; i++)
        {
            if (noise[i] == 0){
                result += WORD[i];
            }
            else
            {
            result += SIMBOLS[getIndexSimbol()];
            noise[i]--;
            isDone = false;
        }
    }

    ELEMENT.innerHTML = result;

    return isDone;
}

genNoise(WORD);

animation = setInterval(stopAnimation, fps);

function stopAnimation()
{
    if (enumeration())
    {
        clearInterval(animation);
        ELEMENT.innerHTML = WORD.substr(0, WORD.length - 1) + "<span class='blink'>_</span>"
    }
}
