//timer code
let time = 30;
const timer = document.getElementById('timer');

setInterval(Countdown, 1000);

function Countdown() {
  const min = Math.floor(time / 60);
  let sec = time % 60;

  if (sec > 9) {
  timer.innerHTML = min + ":" + sec;
}
else if (sec <= 9) {timer.innerHTML = min + ":" + "0" + sec;}

if (time > 0) {
  time--;
}
else {
  timer.style.color = "red";
  location.href = "/uLost";
}
}

