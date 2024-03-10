
document.getElementById('burger-menu').addEventListener('click', function() {
  var menu = document.querySelector('.menu');
  var overlay = document.querySelector('.menu-overlay');
  var burger = document.querySelector('.plate');
  var body = document.querySelector('body');

  menu.classList.toggle('show');
  overlay.classList.toggle('show');
  burger.classList.toggle('active');
  body.classList.toggle('no-scroll');
});

document.querySelector('.menu-overlay').addEventListener('click', function() {
  var menu = document.querySelector('.menu');
  var overlay = document.querySelector('.menu-overlay');
  var burger = document.querySelector('.plate');
  var body = document.querySelector('body');

  if (menu.classList.contains('show')) {
    menu.classList.remove('show');
    overlay.classList.remove('show');
    burger.classList.remove('active');
    body.classList.remove('no-scroll');
  }
});
