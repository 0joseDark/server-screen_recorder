#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pip install flask
# video_server.py

from flask import Flask, Response, send_file
import os

app = Flask(__name__)
output_path = "/caminho/para/o/projeto/output/"
output_file = os.path.join(output_path, "captura.mp4")

@app.route('/')
def index():
    return '''
    <html>
    <body>
    <h1>Streaming de Vídeo</h1>
    <video width="640" height="480" controls>
      <source src="/video_feed" type="video/mp4">
    </video>
    </body>
    </html>
    '''

@app.route('/video_feed')
def video_feed():
    if os.path.exists(output_file):
        return send_file(output_file, mimetype='video/mp4')
    else:
        return "Arquivo de vídeo não encontrado", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, threaded=True)
