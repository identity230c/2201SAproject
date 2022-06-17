var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");

var grd = ctx.createRadialGradient(125, 125, 1, 125, 125, 20);
grd.addColorStop(0, "red");
grd.addColorStop(1, "white");

let isWork2 = false;
let beforeX=null, beforeY=null; 
let gradWidth = ['20', '18','16','14'];
let gradColor = ['#ddd', '#ddd', '#ddd', '#fff']

c.addEventListener(
  "mousemove", (e) => {
    let tmpX = e.offsetX;
    let tmpY = e.offsetY;
    for(i=0;i<4;i++){
      ctx.lineWidth = gradWidth[i];
      ctx.strokeStyle = gradColor[i];
      if(isWork){
        console.log('isWork가 거짓');
        ctx.lineTo(e.offsetX, e.offsetY);
        ctx.stroke();
      }else{
        console.log('isWork가 진실');
        ctx.beginPath();
        ctx.lineCap = 'round';
        ctx.lineJoin = 'round';
        ctx.moveTo(e.offsetX, e.offsetY);
      }
    }
    /*
    ctx.beginPath();
    var grd = ctx.createRadialGradient(tmpX, tmpY, 1, tmpX, tmpY, 20);
    grd.addColorStop(0, "red");
    grd.addColorStop(1, "white");
    ctx.arc(tmpX, tmpY, 30, 0, 2 * Math.PI);
    ctx.fillStyle = grd;
    ctx.fill();
    //
    var grd = ctx.createRadialGradient(tmpX, tmpY, 1, tmpX, tmpY, 20);
    grd.addColorStop(0, "red");
    grd.addColorStop(1, "white");
    ctx.fillStyle = grd;
    ctx.fillRect(tmpX-20, tmpY-20, 40,40);*/
}
);
c.addEventListener(
  "mousedown", (e) => {
    console.log("2마우스다운");
    isWork = true;
  }
);
c.addEventListener(
  "mouseup", (e) => {
    console.log("2마우스업");
    isWork = false;
  }
);
c.addEventListener(
  "mouseleave", (e) => {
    isWork=false;
  }
);
