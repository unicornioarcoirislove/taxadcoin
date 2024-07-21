from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)
try:
    app.config.from_pyfile('config.py')
    host = app.config.get('HOST', '0.0.0.0')
    debug = app.config.get('DEBUG', True)
    port = app.config.get('PORT', int(os.environ.get("PORT", 8000)))
except Exception:
    host = '0.0.0.0'
    debug = True
    port = int(os.environ.get("PORT", 8000))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def send_js(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(host=host, debug=debug, port=port)
