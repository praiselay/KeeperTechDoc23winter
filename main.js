// URL 입력 후, 엔터키 입력 시 파이썬 코드 작동
// 입력 값이 없을 경우, 안내문 필요
function isValidURL(URL) {
  // var RegExp =
  //   /(ftp|http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?/;
  if (RegExp.test(URL)) {
    return true;
  } else {
    return false;
  }
}


function SendURL(e) {
  if (e.keyCode == 13) {
    console.log("entered")
    var URL = document.getElementById('urlInput').value;
    console.log(URL);
    //유효한 url 검증
    if (isValidURL(URL)) {
      alert("This is the valid URL.");
      //자바스크립트의 입력값을 파이썬 코드의 인자로 전달 후 실행
      const spawn = require('child_process').spawn;
      const result = spawn("python", ["./crawling.py"], URL);
      result.stdout.on('data', function(data) {
        console.log(data.toString());
      })
    } else if (URL.length == 0) {
      alert("Type the URL.");
      return false;
    } else {
      alert("Type the valid URL.");
      return false;
    }
    //파이썬 코드 실행하는 함수
    DetectURL(URL.value);
  }
}

//파이썬 코드 실행하는 함수
function DetectURL(urlValue) {
  console.log(urlValue);
}