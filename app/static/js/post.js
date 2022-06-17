let sendImg = () => {
  let ret = giveMeImg();
  document.getElementById("img").value = ret;
  console.log("열일중");
}

/*
let postMan = new XMLHttpRequest();

postMan.onreadystatechange = function(event) {
  if(this.status == 200 && this.readyState == this.DONE){
    console.log('뭐가 오긴 왔음', this.responseText);
    document.write(this.responseText)
  }
};

let giveMeImgForReq = () =>{
  let raw = giveMeImg();
  const cooked = Buffer.from(raw, 'base64').toString('binary');
}

let testFunc = () => {
  let forms = new FormData();
  forms.append('file', giveMeImg());
  postMan.open('post', '/testImg/upload', true);
  console.log(giveMeImg());
  postMan.send(forms);
};

let canvasToJson = () =>{
  let raw = {
    file : giveMeImg()
  };
  let cooked = JSON.stringify(raw);
  return cooked
};

document.getElementById("sendBtn").addEventListener(
  "click", () =>{
    postMan.open('post', 'upload', true);
    postMan.setRequestHeader('Content-Type', 'application/json')
    postMan.crossOrigin = "Anonymous";
    postMan.send(canvasToJson());
  }
)
*/