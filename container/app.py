from flask import Flask
from redis import Redis, RedisError
from flask import jsonify
import socket
import time

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/app", methods=['POST'])
def save_timestamp():
    try:
        timestamp = time.time()
        counter   = redis.rpush("timestamps", timestamp)
        status    = "saved"
    except RedisError:
        status    = "failed"

    return jsonify(status    = status,
                   timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp)),
                   hostname  = socket.gethostname(),
                   records   = counter,
                   epoch     = timestamp), 200 if status == "saved" else 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
