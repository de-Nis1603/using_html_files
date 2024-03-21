from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index/<site_name>')
def index(site_name):
    return render_template('index.html', title=site_name)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')