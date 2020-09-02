// Source code: https://codepen.io/kassandrasanch/details/mdevxPx
var elemets = document.querySelector('svg').children;

anime({
  targets: 'line',
  translateX: [
    {value: 270, duration: 1000, easing: 'easeOutSine'},
    {value: 0, duration: 1000, easing: 'easeOutSine'}
  ],
  // translateX: 270,
    borderRadius: ['0%', '50%'],
  easing: 'easeInOutQuad',
  delay: anime.stagger(200, {grid: [16,10], from: 7}),
  loop: true
})