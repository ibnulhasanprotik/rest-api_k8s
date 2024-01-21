from flask import Flask, jsonify
import socket
import requests
import datetime

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Dhaka&appid=c1daa880a3d5012b1bc6b4fcee8a172c&units=metric')
    data = response.json()
    temp = data['main']['temp']
    return jsonify({
        'hostname': socket.gethostname(),
        'datetime': datetime.datetime.now().strftime("%Y%m%d%H%M"),
        'version': '1.0',
        'weather': {
            'dhaka': {
                'temperature': str(temp),
                'temp_unit': 'c'
            }
        }
    })

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

