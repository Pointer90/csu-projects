const lightTheme = document.querySelector('button#lightBtn');
const darkTheme = document.querySelector('button#darkBtn');
const bodyTag = document.querySelector('[data-tag="body"]');
const svgs = document.querySelectorAll('.svgObj');
console.log(svgs);

lightTheme.addEventListener("click", function () {
    lightTheme.setAttribute('class', "dropdown-item active rounded-3");
    darkTheme.setAttribute('class', "dropdown-item rounded-3");
    bodyTag.setAttribute('data-bs-theme', "light");
    svgs.forEach(svg => {
        svg.setAttribute("fill", "white")
    });
});

darkTheme.addEventListener("click", function () {
    lightTheme.setAttribute('class', "dropdown-item rounded-3");
    darkTheme.setAttribute('class', "dropdown-item active rounded-3");
    bodyTag.setAttribute('data-bs-theme', "dark");
    svgs.forEach(svg => {
        svg.setAttribute("fill", "#212529");
        console.log(svg);
    });
});
