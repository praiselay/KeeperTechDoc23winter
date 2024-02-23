import flask
import requests
import re
import os
import subprocess
import tempfile
import ssl
from requests_oauthlib.oauth2_session import OAuth2Session
from os import environ #SECRET KEY 취약점 관련 코딩 시 필요
from flask import Flask
from flask import render_template
from flask import redirect

app = Flask(__name__)

@app.route('/')
def hello():
    return flask.render_template("index.html")

def detect_xss(html_code):
    can_xss = ["input", "textarea", "contenteditable"]
    for tag in can_xss:
        if tag in html_code:
            return tag
    return False

def detect_sql_injection(html_code):
    can_sql_injection = ["method", "login", "post"]
    # sql_injection_patterns = ["SELECT", "UPDATE", "DELETE", "INSERT", "EXEC"]
    for pattern in can_sql_injection:
        if pattern in html_code:
            return True
    return False

def detect_command_injection(command):
    if any([keyword in command for keyword in [";", "&&", "|", "`", "$", "(", ")", "{", "}", "[", "]", "<", ">", "eval"]]):
        return True
    return False

def detect_temp_file_creation():
    try:
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file_path = temp_file.name
        print(f"temp_file is at {temp_file_path}")
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
            return False
        else:
            return True
    except Exception:
        print("error: ", Exception)
        return True

def detect_ssl_weakness():
    try:
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.minimum_version = ssl.TLSVersion.TLSv1_3
        print("SSL/TLS ver.: ", context.minimum_version)
        return False 
    except ssl.SSLError:
        return True

@app.route('/process_url', methods=['POST'])
def process_url():
    # POST 요청으로부터 URL 가져오기
    data = flask.request.json
    url = data['url']
    
    # URL에 GET 요청 보내기
    response = requests.get(url)
    
    # 요청 성공 여부 확인
    if response.status_code == 200:
        # HTML 코드 가져오기
        html_code = response.text
        
        # 보안 취약점 탐지
        xss_detected = detect_xss(html_code)
        sql_injection_detected = detect_sql_injection(html_code)
        command_injection_detected = detect_command_injection(html_code)
        temp_file_creation_detected = detect_temp_file_creation()
        ssl_weakness_detected = detect_ssl_weakness()
        
        # 결과 반환
        results = []
        if xss_detected:
            results.append("XSS vulnerability detected")
        if sql_injection_detected:
            results.append("SQL injection vulnerability detected")
        if command_injection_detected:
            results.append("Command injection vulnerability detected")
        if temp_file_creation_detected:
            results.append("Insecure temporary file creation detected")
        if ssl_weakness_detected:
            results.append("Weak SSL/TLS protocol detected")
            
        if not results:
            return flask.jsonify("No security vulnerabilities detected")
        else:
            result_string = ", ".join(results)
            return flask.jsonify(result_string)
    else:
        # 요청 실패 시 에러 메시지 반환
        return f'error: {response.status_code}'

def safe_ping():
    host = requests.args.get("host", "www.google.com")
    status = subprocess.run(["ping", "-c", "1", "--", host]).returncode
    return str(status == 0)

def check_cookie(request):
    response = render_template(request, "index.html")
    if not "sessionid" in request.COOKIE:
        return redirect("/getcookie")
    return response

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
