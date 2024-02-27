const lightTheme = document.querySelector('button#lightBtn');
const darkTheme = document.querySelector('button#darkBtn');
const bodyTag = document.querySelector('[data-tag="body"]');
const svgs = document.querySelectorAll('.svgObj');
const btns = document.querySelectorAll('.lastBtn');
const modalBtn = document.querySelector('.modalBtn');

themeMode = {DARK: 'dark', LIGHT: 'light'}

function setCookies(mode)
{
    theme = encodeURIComponent('theme') + '=' + encodeURIComponent(mode);
    document.cookie = theme;
}

function lightThemeActivation()
{
    if (lightTheme && darkTheme){
        lightTheme.setAttribute('class', "dropdown-item active rounded-3");
        darkTheme.setAttribute('class', "dropdown-item rounded-3");
    }
    bodyTag.setAttribute('data-bs-theme', "light");
    svgs.forEach(svg => {
        svg.setAttribute('fill', "white");
    });
    btns.forEach(btn =>{
        btn.setAttribute('class', "btn btn-outline-dark rounded-3 lastBtn");
    });
    if (modalBtn){
        modalBtn.setAttribute("class","btn btn-outline-dark rounded-3 col modalBtn")
    };
}

function darkThemeActivation()
{
    if (lightTheme && darkTheme){
        lightTheme.setAttribute('class', "dropdown-item rounded-3");
        darkTheme.setAttribute('class', "dropdown-item active rounded-3");
    }
    bodyTag.setAttribute('data-bs-theme', "dark");
    svgs.forEach(svg => {
        svg.setAttribute("fill", "#212529");
    });
    btns.forEach(btn =>{
        btn.setAttribute('class', "btn btn-outline-light rounded-3 lastBtn");
    });
    if (modalBtn){
        modalBtn.setAttribute("class","btn btn-outline-light rounded-3 col modalBtn");
    };
}

if (bodyTag.getAttribute('data-bs-theme') == themeMode.LIGHT)
{
    lightThemeActivation();
}
else{
    darkThemeActivation();
}

if (lightTheme && darkTheme){

    lightTheme.addEventListener("click", function ()
    {
        setCookies(themeMode.LIGHT);
        lightThemeActivation();
    });

    darkTheme.addEventListener("click", function ()
    {
        setCookies(themeMode.DARK);
        darkThemeActivation();
    });
}
