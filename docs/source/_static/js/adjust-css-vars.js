$(document).ready(function () {
  var r = document.querySelector(':root');
  /* Solid blocks on firstinspires.org are drawn in FIRST ink, so grid card
     headers use it too. Kept in sync with the :root block in ftc-rtd.css. */
  r.style.setProperty('--sd-color-secondary', '#231F20');
  r.style.setProperty('--sd-color-secondary-text', '#FFFFFF');
});
