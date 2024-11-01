from flask import Flask, render_template


app = Flask(__name__)

# 현재는 모든 경로에서 index.html을 불러오는 것으로 되어있다

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def web(path):
    return render_template('index.html')



if __name__ == '__main__':
    app.run(host='127.0.0.1', port = 5001)
