from flask import Flask, Response, render_template, stream_with_context,request,send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5011,debug=True,threaded=True)

    