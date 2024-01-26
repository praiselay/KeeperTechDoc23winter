// URL 입력 후, 엔터키 입력 시 파이썬 코드 작동
// 입력 값이 없을 경우, 안내문 필요
var URL = document.getElementById("urlInput");
function SendURL(e) {
    if (e.keyCode == 13) {
        if (URL.value.length == 0) {
            alert('Type the URL');
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