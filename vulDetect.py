#Flask secret keys should not be disclosed
# from flask import Flask
# import os
# app = Flask(__name__)
# app.config['SECRET_KEY'] = os.environ["SECRET_KEY"]


#Credentials should not be hard-coded
# from os import environ
# from requests_oauthlib.oauth2_session import OAuth2Session
# scope = ['https://www.api.example.com/auth/example.data']
# oauth = OAuth2Session(
#   'example_client_id',
#   redirect_uri='https://callback.example.com/uri',
#   scope=scope
# )
# password = environ.get('OAUTH_SECRET')
# token = oauth.fetch_token(
#   'https://api.example.com/o/oauth2/token',
#   client_secret=password
# )

#OS commands should not be vulnerable to command injection attacks
# import requests
# import subprocess
# def safe_ping():
#     host = requests.args.get("host", "www.google.com")
#     status = subprocess.run(["ping", "-c", "1", "--", host]).returncode
#     return str(status == 0)

#Insecure temporary file creation methods should not be used
# import tempfile
# tmp_file1 = tempfile.NamedTemporaryFile(delete=False)
# tmp_file2 = tempfile.NamedTemporaryFile()

#Weak SSL/TLS protocols should not be used
# import ssl
# context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# context.minimum_version = ssl.TLSVersion.TLSv1_3

#Applications should not create session cookies fro untrusted input
# from django.http import HttpResponseRedirect
# from django.shortcuts import render
# def check_cookie(request):
#     response = render(request, "welcome.html")
#     if not "sessionid" in request.COOKIE:
#         return HttpResponseRedirect("/getcookie")
#     return response


#악성 파일 검증

#중요 정보의 암호화 여부

#SQL 삽입 위험성 판단

#크로스사이트 스크립트 피해 가능성 판단