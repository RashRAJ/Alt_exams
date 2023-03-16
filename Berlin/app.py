import os
from flask import Flask, request, render_template

app = Flask(__name__, template_folder="Templates", static_url_path='', static_folder='')

@app.route('/')
def root():
    return render_template('index.html')

PORT = int(os.environ.get("PORT", 8080))
if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=PORT)
