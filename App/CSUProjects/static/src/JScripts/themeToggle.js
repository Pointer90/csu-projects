const lightTheme = document.querySelector('button#lightBtn');
const darkTheme = document.querySelector('button#darkBtn');
const bodyTag = document.querySelector('[data-tag="body"]');
const svgs = document.querySelectorAll('.svgObj');
const themeSvg = document.querySelector('#themeSvg');

themeMode = {DARK: 'dark', LIGHT: 'light'};

function setTheme(mode)
{
    theme = encodeURIComponent('theme') + '=' + encodeURIComponent(mode) + encodeURI();
    document.cookie = `theme=${mode}; path=/; max-age=${60 * 60 * 24 * 31}`;
}

function getCookies()
{
    let data = document.cookie.split(';');
    let cookie = {};

    for (let i = 0; i < data.length; i++)
    {
        let tmp = data[i].split('=')
        cookie[tmp[0].trim()] = tmp[1]
    }

    return cookie
}

function lightThemeActivation()
{
    lightTheme.setAttribute('class', "dropdown-item d-flex justify-content-center align-items-center rounded-3 active");
    darkTheme.setAttribute('class', "dropdown-item d-flex justify-content-center align-items-center rounded-3");
    themeSvg.setAttribute('class', "bi bi-brightness-high-fill");
    const path = themeSvg.querySelector('path');
    path.setAttribute('d', "M12 8a4 4 0 1 1-8 0 4 4 0 0 1 8 0M8 0a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 0m0 13a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 13m8-5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2a.5.5 0 0 1 .5.5M3 8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2A.5.5 0 0 1 3 8m10.657-5.657a.5.5 0 0 1 0 .707l-1.414 1.415a.5.5 0 1 1-.707-.708l1.414-1.414a.5.5 0 0 1 .707 0m-9.193 9.193a.5.5 0 0 1 0 .707L3.05 13.657a.5.5 0 0 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0m9.193 2.121a.5.5 0 0 1-.707 0l-1.414-1.414a.5.5 0 0 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .707M4.464 4.465a.5.5 0 0 1-.707 0L2.343 3.05a.5.5 0 1 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .708");
    bodyTag.setAttribute('data-bs-theme', themeMode.LIGHT);
    svgs.forEach(svg => {
        svg.setAttribute('fill', "white");
    });
}

function darkThemeActivation()
{
    lightTheme.setAttribute('class', "dropdown-item d-flex justify-content-center align-text-center rounded-3");
    darkTheme.setAttribute('class', "dropdown-item d-flex justify-content-center align-text-center rounded-3 active");
    themeSvg.setAttribute('class', "bi bi-moon-fill");
    const path = themeSvg.querySelector('path');
    path.setAttribute('d', "M6 .278a.77.77 0 0 1 .08.858 7.2 7.2 0 0 0-.878 3.46c0 4.021 3.278 7.277 7.318 7.277q.792-.001 1.533-.16a.79.79 0 0 1 .81.316.73.73 0 0 1-.031.893A8.35 8.35 0 0 1 8.344 16C3.734 16 0 12.286 0 7.71 0 4.266 2.114 1.312 5.124.06A.75.75 0 0 1 6 .278");
    bodyTag.setAttribute('data-bs-theme', themeMode.DARK);
    svgs.forEach(svg => {
        svg.setAttribute("fill", "#212529");
    });
}

cookie = getCookies();

if (cookie['theme'] == themeMode.LIGHT || !('theme' in cookie))
    lightThemeActivation();
else
    darkThemeActivation();

lightTheme.addEventListener("click", function ()
{
    setTheme(themeMode.LIGHT);
    lightThemeActivation();
});

darkTheme.addEventListener("click", function ()
{
    setTheme(themeMode.DARK);
    darkThemeActivation();
});
