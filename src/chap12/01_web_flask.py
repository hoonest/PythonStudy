# 플라스크(Flask)를 임포트합니다.
from flask import Flask
from flask import request

# 플라스크 앱을 생성합니다.
app = Flask(__name__)

# 편의를 위한 디버그 모드를 활성화합니다.
app.debug = True

# URL 경로에 따라 실행할 함수에 데코레이터를 사용합니다.
# 데코레이터의 파라메터는 URL 경로입니다.
@app.route("/")
def hello():    # 위 경로에 접근하면 실행 할 함수입니다.
    return "Hello World!!!"

@app.route("/hello/<name>")  # <name> 자리에 오는 문자열은 name에 할당되어 함수로 전달합니다.
def hello_to(name):
    return "Hello, {0}!".format(name)

@app.route("/hello")
def hello_to_get_param():
    # /hello?name=kang 와 같은 형식의 요청을 받아서
    # ?name=<이름>의 값이오면, <이름>을 name에 저장합니다.
    name = request.args.get("name")
    return "Hello, {0}!".format(name)


# 이 파일을 바로 실행할 때 함께 실행할 코드를 작성한다.
if __name__ == "__main__":
    app.run()     # 위에서 생성한 플라스크 애플리케이션을 실행합니다.









