const lightTheme = document.querySelector('button#lightBtn');
const darkTheme = document.querySelector('button#darkBtn');
const bodyTag = document.querySelector('[data-tag="body"]');

lightTheme.addEventListener("click", function () {
    lightTheme.setAttribute('class', "dropdown-item active rounded-3");
    darkTheme.setAttribute('class', "dropdown-item rounded-3");
    bodyTag.setAttribute('data-bs-theme', "light");
});

darkTheme.addEventListener("click", function () {
    lightTheme.setAttribute('class', "dropdown-item rounded-3");
    darkTheme.setAttribute('class', "dropdown-item active rounded-3");
    bodyTag.setAttribute('data-bs-theme', "dark");
});
