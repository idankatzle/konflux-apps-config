from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Map App</h1><p>Status: Online</p>"

# New endpoint for health checks
@app.route('/health')
def health_check():
    # In a real app, you would check DB connection here
    return jsonify(status="UP"), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
