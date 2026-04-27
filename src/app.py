#'/api/v1/details'
#'/api/v1/health'

from flask import Flask, jsonify
import datetime,socket
app = Flask(__name__)


@app.route('/api/v1/details')
def details():
    return jsonify({
        "name": "John Doe",
        "age": 30,
        "email": "john.doe@example.com",
        "time": datetime.datetime.now().isoformat(),
        "hostname": socket.gethostname(),
        "message": "Hello, Niggatron!!!"
    })

@app.route('/api/v1/health')
def health():
    return jsonify({
        "status": "healthy"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0')