const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const button = document.querySelector('.loginn');
const close = document.querySelector('.close');

registerLink.addEventListener('click', () => {
    wrapper.classList.add('active');
});

loginLink.addEventListener('click', () => {
    wrapper.classList.remove('active');
});

button.addEventListener('click', () => {
    wrapper.classList.add('active-popup');
});

close.addEventListener('click', () => {
    wrapper.classList.remove('active-popup');
});