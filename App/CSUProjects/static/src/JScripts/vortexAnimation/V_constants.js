/* ----- Константы для спирали ----- */

const   vCANVAS = document.querySelector("#vortex"),
        vGRAD_LOGO ="#e41b1b",                                 // Цвет логотипа
        vGRAD_VORTEX = "#8b0000",                              // Цвет спирали
        vFPS = 60,                                             // Частота кадров
        vCTX = vCANVAS.getContext("2d"),                       // Окно отрисовки
        vWIDTH = vCANVAS.width,                                // Ширина экрана
        vHEIGHT = vCANVAS.height,                              // Высота экрана
        vSCALE = (vHEIGHT / vWIDTH) * 1.6,                     // Соотношение сторон экрана
        vHEIGHT_LETTER = 8,                                    // Высота буквы
        vWIDTH_LETTER = 12,                                    // Ширина буквы
        vSTRETCH_WIDTH = vSCALE * 2,                           // Вытянутость спирали в ширину
        vSTRETCH_HEIGHT = vSCALE * 0.8,                        // Вытянутость спирали в высоту
        vBRANCH_STEP = 0.018,                                  // Длинна ветви
        vANGLE_STEP = 3,                                       // Шаг угла поворота ветви
        vSCALE_SIMBOL = 8,                                     // Коэффициент расстояния между символами
        vSTART_FRAME = 0.01,                                   // Начальный кадр
        vEND_FRAME = 10,                                       // Последний кадр
        vSPEED_ANIMATION = 0.015,                              // Скорость анимации
        vBRANCHES = [                                          // Массив с коэффициентами для веток спирали
            {speed: 5, deviation: 2.5, start: 1.6, end: 3.5},
            {speed: 6, deviation: 2.8, start: 1.4, end: 3.7},
            {speed: 7, deviation: 3.1, start: 2.0, end: 4.5},
            {speed: 7, deviation: 3.3, start: 2.1, end: 4.6},
            {speed: 7, deviation: 3.5, start: 2.1, end: 4.7},
            {speed: 9, deviation: 3.7, start: 2.3, end: 4.4},
            {speed: 2, deviation: 3.6, start: 3.7, end: 5.3},
            {speed: 2, deviation: 3.9, start: 4, end: 5.5},
            {speed: 2, deviation: 4.2, start: 3.5, end: 5.2}
        ],
        LOGO = [
            '      .... .... .... ....',
            '       ...  ... .... ....',
            '        ..  ... .... ....',
            '        ... ... .... ... ',
            '         ..  .. ...  ... ',
            '         ..  .. ...  ... ',
            '   .....  .  ..  ..  ... ',
            '  ....... ..  .. ..  ... ',
            ' ...   .....  .. ..  ... ',
            ' .. ... .. .  .. .  ...  ',
            '..  ... .. .  .  .  ...  ',
            '.. .. .  . .  . ..  ..   ',
            '.. .. .  . .  . .....    ',
            '.. .     . .... . ..     ',
            '.. .    ..  .. .. ..     ',
            '.. ..  ..      ....      ',
            '... ....  ...  . ..      ',
            ' ..      .....  ..       ',
            ' ...    ......  .        ',
            '  ............           ',
            '   ..........            ',
            '     ......              ',
        ];


/* ----- Настройки сцены спирали----- */

vCTX.translate(vWIDTH / 2, vHEIGHT / 2);
vCTX.scale(vSCALE, vSCALE);
vCTX.font = "20px Monospace";
vCTX.textBaseline = "middle";
vCTX.textAlign = "center";
vCTX.fillStyle = "black";
vCTX.strokeStyle = "black";
vCTX.lineWidth = 2;

const grdLogo = vCTX.createRadialGradient(0, 0, 100, 0, 0, 250),
      grdVortex = vCTX.createRadialGradient(0, 0, 100, 0, 0, 250);

grdLogo.addColorStop(0,"white");
grdLogo.addColorStop(1,"#8b0000");
grdVortex.addColorStop(0,'#e41b1b');
grdVortex.addColorStop(1,"#6b0804");