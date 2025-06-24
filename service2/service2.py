from flask import Flask, jsonify

app = Flask (__name__)

@app.route("/service2")
def service2_endpoint():
    return jsonify({"message":"Hello from service 2"})

if __name__ == '__main__':
    app.run(port = 5001)
