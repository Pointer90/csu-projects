const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const btn = document.querySelector('.subscribe');
const btnClose = document.querySelector('.icon-close');

btn.addEventListener('click', ()=> {
    wrapper.classList.add('active-appear');
});

btnClose.addEventListener('click', ()=> {
    wrapper.classList.remove('active-appear');
});