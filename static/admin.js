

//timer code
let time = 120;

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
}
}



//Create table
document.write("<table class=\"center\"; border=\"1\">");
document.write("<tr><th>Question</th><th>Correct Answer</th><th>Input</th><th>Is Correct</th>")


//creates each row of the table
for(let x = 0; x < 20; x++) {
  document.write("<tr>");
  document.write("<th>");

  //input the QUESTION
  document.write(x);
  document.write("</th>");
  document.write("<th>");

  //input what the correct answer is
  document.write();
  document.write("</th>");
  document.write("<th id = input");
  document.write(x)
  document.write(">--");
  document.write("</th>");
  document.write("<th id = isCorrect");
  document.write(x);
  document.write(">--");
  document.write("</th>");
  document.write("</tr>");

}
document.write("</table>")


document.write("<p1> Puzzle Progress</p1>");


//This is where you will update what the user inputs
//fills the innerHTML of input
for(let i = 0; i < 20; i++) {
  const input = document.getElementById("input" + i);
  input.innerHTML = "A";
}

//Fills the innerHTML of Is Correct
for(let i = 0; i < 20; i++) {
  const input = document.getElementById("isCorrect" + i);
  input.innerHTML = "True";
}
