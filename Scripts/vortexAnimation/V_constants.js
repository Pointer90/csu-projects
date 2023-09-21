/* ----- Константы для спирали ----- */

const   V_CANVAS = document.querySelector("#vortex"),
        V_FPS = 60,                                             // Частота кадров
        V_CTX = V_CANVAS.getContext("2d"),                      // Окно отрисовки
        V_WIDTH = Number(V_CANVAS.getAttribute("width")),       // Ширина экрана
        V_HEIGHT = Number(V_CANVAS.getAttribute("height")),     // Высота экрана
        V_SCALE = (V_HEIGHT / V_WIDTH) * 1.9,                   // Соотношение сторон экрана
        V_WIDTH_VORTEX = V_SCALE * 2,                           // Вытянутость спирали в ширину
        V_HEIGHT_VORTEX = V_SCALE * 0.8,                        // Вытянутость спирали в высоту
        V_BRANCH_STEP = 0.018,                                  // Длинна ветви
        V_ANGLE_STEP = 3,                                       // Шаг угла поворота ветви
        V_SCALE_SIMBOL = 12,                                    // Коэффициент расстояния между символами
        V_START_FRAME = 0.01,                                   // Начальный кадр
        V_END_FRAME = 10,                                       // Последний кадр
        V_SPEED_ANIMATION = 0.01,                               // Скорость анимации
        V_COLOR_VORTEX = "black",                               // Цвет спирали
        V_BRANCHES = [                                          // Массив с коэффициентами для веток спирали
            {speed: 5, deviation: 1.5, start: 0.6, end: 1.5},
            {speed: 6, deviation: 1.8, start: 0.4, end: 1.7},
            {speed: 7, deviation: 2.1, start: 1.0, end: 2.5},
            {speed: 7, deviation: 2.3, start: 1.1, end: 2.6},
            {speed: 7, deviation: 2.5, start: 1.1, end: 2.7},
            {speed: 9, deviation: 2.7, start: 1.3, end: 2.4},
            {speed: 2, deviation: 2.6, start: 2.7, end: 3.3},
            {speed: 2, deviation: 2.9, start: 3, end: 3.5},
            {speed: 2, deviation: 3.2, start: 2.5, end: 3.2}
        ];