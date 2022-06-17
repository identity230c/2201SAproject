let postMan = new XMLHttpRequest();

document.getElementById("sendBtn").addEventListener(
  "click", () => {
    let forms = new FormData();
    forms.append('file', giveMeImg());
    postMan.open('post', 'localhost:8080/upload', true);
    postMan.setRequestHeader('content-type', 'image/png');
    postMan.send(forms);
  }
)