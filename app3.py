import flask
import requests

app = flask.Flask(__name__)

@app.route('/')
def hello():
    return flask.render_template("index.html")

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
        # XSS와 SQL Injection 가능성 검사
        can_xss = ["input", "textarea", "contenteditable"]
        can_sql_injection = ["method", "login", "post"]
        
        results = []
        # XSS 가능성 검사
        for tag in can_xss:
            if tag in html_code:
                results.append(f"Can perform XSS attack using '{tag}' tag")
        # SQL Injection 가능성 검사
        for tag in can_sql_injection:
            if tag in html_code:
                results.append(f"Can perform SQL injection attack using '{tag}' tag")
        
        # 결과 반환
        if not results:
            return flask.jsonify("No XSS or SQL injection vulnerabilities found")
        else:
            result_string = ", ".join(results)
            result_string = result_string.replace("[", "").replace("]", "").replace('"', "")
            return flask.jsonify(result_string)


    else:
        # 요청 실패 시 에러 메시지 반환
        return f'Error: {response.status_code}'

if __name__ == '__main__':
    # app.run(host='127.0.0.1', port=8080)
