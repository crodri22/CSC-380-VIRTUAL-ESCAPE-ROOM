			let time = 300;

const timer = document.getElementById('timer');

setInterval(Countdown, 1000);

function Countdown() {
  const min = Math.floor(time / 60);
  let sec = time % 60;

  if (sec > 9) {
  document.getElementById('timer').innerHTML = min + ":" + sec;
}
else if (sec <= 9) {document.getElementById('timer').innerHTML = min + ":" + "0" + sec;}

if (time > 0) {
  time--;
}
else {
  document.getElementById('timer').style.color = "red";
}
}