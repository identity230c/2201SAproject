let saveBtn = document.getElementById("saveBtn");

saveBtn.addEventListener(
  "click", () => {
    let ret = giveMeImg();
    console.log('이게 되나?');
    let aForDownload = document.createElement("a");
    aForDownload.href = ret; 
    aForDownload.download = "testSet";
    aForDownload.click();
  }
)