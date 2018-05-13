from flask import Flask, request
app = Flask(__name__)

@app.route('/xxx')
def hello():
    text = request.args.get('text')
    return text

if __name__ == '__main__':
    app.run()
