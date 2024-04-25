document.addEventListener("DOMContentLoaded", function () {
  let img = document.getElementById("imageRecognize");
  let imgInput = document.getElementById("fileImage");
  console.log(img);
  console.log(imgInput);

  img.onclick = function () {
    imgInput.click();
  };

  imgInput.onchange = function (event) {
    let reader = new FileReader();
    reader.onload = function () {
      if (reader.readyState == 2) {
        img.src = reader.result;
      }
    };
    reader.readAsDataURL(event.target.files[0]);
  };
});
