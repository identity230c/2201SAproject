let saveBtn = document.getElementById("saveBtn");

saveBtn.addEventListener(
  "click", () => {
    let ret = giveMeImg();
    let aForDownload = document.createElement("a");
    aForDownload.href = ret; 
    aForDownload.download = "testSet";
    aForDownload.click();
  }
)