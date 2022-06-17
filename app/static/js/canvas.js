let canvas = document.getElementById('blackCanvas');
let context = canvas.getContext('2d');

context.width = 700;
context.height = 700;

context.fillStyle = "000";
context.fillRect(0,0,context.width, context.height);

context.strokeStyle = "#ffffff";

context.lineWidth = 70;
context.lineCap = 'round';
context.lineJoin = 'round';


let isWork = false;

canvas.addEventListener(
  "mousemove", (e) => {
    if(isWork){
      context.lineTo(e.offsetX, e.offsetY);
      context.stroke();
    }else{
      context.beginPath();
      context.moveTo(e.offsetX, e.offsetY);
    } // end of if-else
  }// end of arrow function 
); // end of addEventListener

canvas.addEventListener(
  "mousedown", (e) => {
    isWork = true;
  }
);
canvas.addEventListener(
  "mouseup", (e) => {
    isWork = false;
  }
);
canvas.addEventListener(
  "mouseleave", (e) => {
    isWork=false;
  }
);

let giveMeImg = () => {
  return canvas.toDataURL("image/png");
}

