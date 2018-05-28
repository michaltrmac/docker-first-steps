import socket

import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World! Hostname: {hostname} | Version: {version}'.format(
            hostname=socket.gethostname(),
            version=open('./VERSION.md').read().rstrip('\n')
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
