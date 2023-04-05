
var count = 0;
var timer;
var target = document.querySelector("button");
target.addEventListener('click', change);

var target = document.getElementById("target");
var display = document.getElementById("display");
target.onclick = function (){
  count++;
  display.innerHTML = count;
}
const FULL_DASH_ARRAY = 283;
const WARNING_THRESHOLD = 10;
const ALERT_THRESHOLD = 5;

const COLOR_CODES = {
  info: {
    color: "green"
  },
  warning: {
    color: "orange",
    threshold: WARNING_THRESHOLD
  },
  alert: {
    color: "red",
    threshold: ALERT_THRESHOLD
  }
};

const TIME_LIMIT = 5;
let timePassed = 0;
let timeLeft = TIME_LIMIT;
let timerInterval = null;
let remainingPathColor = COLOR_CODES.info.color;

document.getElementById("app").innerHTML = `
<div class="base-timer">
  <svg class="base-timer__svg" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
    <g class="base-timer__circle">
      <circle class="base-timer__path-elapsed" cx="50" cy="50" r="45"></circle>
      <path
        id="base-timer-path-remaining"
        stroke-dasharray="283"
        class="base-timer__path-remaining ${remainingPathColor}"
        d="
          M 50, 50
          m -45, 0
          a 45,45 0 1,0 90,0
          a 45,45 0 1,0 -90,0
        "
      ></path>
    </g>
  </svg>
  <span id="base-timer-label" class="base-timer__label">${formatTime(
  timeLeft
)}</span>
</div>
`;
var modal = document.getElementById("myModal");
var span = document.getElementsByClassName("close")[0];
startTimer();
window.onclick = function(event) {
  if(event.target == modal) {
    modal.style.display="none";
  }
}
function onTimesUp() {
  clearInterval(timerInterval);
  modal.style.display="block";
}

function startTimer() {
  timerInterval = setInterval(() => {
    timePassed = timePassed += 1;
    timeLeft = TIME_LIMIT - timePassed;
    document.getElementById("base-timer-label").innerHTML = formatTime(
      timeLeft
    );
    setCircleDasharray();
    setRemainingPathColor(timeLeft);

    if (timeLeft === 0) {
      onTimesUp();
    }
  }, 1000);
}

function formatTime(time) {
  const minutes = Math.floor(time / 60);
  let seconds = time % 60;

  if (seconds < 10) {
    seconds = `0${seconds}`;
  }

  return `${minutes}:${seconds}`;
}

function setRemainingPathColor(timeLeft) {
  const { alert, warning, info } = COLOR_CODES;
  if (timeLeft <= alert.threshold) {
    document
      .getElementById("base-timer-path-remaining")
      .classList.remove(warning.color);
    document
      .getElementById("base-timer-path-remaining")
      .classList.add(alert.color);
  } else if (timeLeft <= warning.threshold) {
    document
      .getElementById("base-timer-path-remaining")
      .classList.remove(info.color);
    document
      .getElementById("base-timer-path-remaining")
      .classList.add(warning.color);
  }
}

function calculateTimeFraction() {
  const rawTimeFraction = timeLeft / TIME_LIMIT;
  return rawTimeFraction - (1 / TIME_LIMIT) * (1 - rawTimeFraction);
}

function setCircleDasharray() {
  const circleDasharray = `${(
    calculateTimeFraction() * FULL_DASH_ARRAY
  ).toFixed(0)} 283`;
  document
    .getElementById("base-timer-path-remaining")
    .setAttribute("stroke-dasharray", circleDasharray);
}

document.addEventListener('DOMContentLoaded', () => {
  let elements = []
  let container = document.querySelector('#container')
  // Add each row to the array
  container.querySelectorAll('.row').forEach(el => elements.push(el))
  // Clear the container
  container.innerHTML = ''
  // Sort the array from highest to lowest
  elements.sort((a, b) => b.querySelector('.score').textContent - a.querySelector('.score').textContent)
  // Put the elements back into the container
  elements.forEach(e => container.appendChild(e))
})

function onload() {
  var x;
  var y;
  target
}
function change() {
  var i = Math.floor(Math.random() * 800) + 1;
  var j = Math.floor(Math.random() * 500) + 1;
  target.style.left = i + "px";
  target.style.top = j + "px";
}   
