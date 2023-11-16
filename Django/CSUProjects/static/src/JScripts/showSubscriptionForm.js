const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const btns = document.querySelectorAll('.subscribeButton');
const btnClose = document.querySelector('.icon-close');
const createBtn = document.querySelector('#create-project');


btns.forEach(btn => {
    btn.addEventListener('click', ()=> {
        wrapper.classList.add('active-appear');
    });
})

btnClose.addEventListener('click', ()=> {
    console.log('YESS')
    wrapper.classList.remove('active-appear');
});

createBtn.addEventListener('click', ()=> {
    wrapper.classList.add('active-appear');
})