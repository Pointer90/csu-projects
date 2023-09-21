/* ----- Константы для заднего фона ----- */

const   B_CANVAS = document.querySelector("#background"),
        B_FPS = 40,                                            // Частота кадров
        B_CTX = B_CANVAS.getContext("2d"),                      // Окно отрисовки
        B_WIDTH = Number(B_CANVAS.getAttribute("width")),       // Ширина экрана
        B_HEIGHT = Number(B_CANVAS.getAttribute("height")),     // Высота экрана
        B_SCALE = (B_HEIGHT / B_WIDTH) * 1.2,                   // Соотношение сторон экрана
        B_SPEED_ANIMATION = 0.04,                               // Скорость анимации
        B_COLOR_TEXT = "black",                                 // Цвет текста
        B_FONT_SIZE = 30,                                       // Размер шрифта
        B_SPACE_LINES = 2.2,                                    // Расстояние между строками
        B_START_FRAME = 0,                                      // Кадр начала анимации
        B_END_FRAME = 250;                                      // Кадр окончания анимации