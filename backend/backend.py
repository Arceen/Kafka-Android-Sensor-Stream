from flask import Flask, request, jsonify
from kafka import KafkaProducer
import json

app = Flask(__name__)

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8') 
)

@app.route('/kafka-proxy-endpoint', methods=['POST'])
def send_to_kafka():
    data = request.json 
    topic = 'my-topic'  

    try:
        producer.send(topic, value=data)
        producer.flush()
        return jsonify({'status': 'success'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)
