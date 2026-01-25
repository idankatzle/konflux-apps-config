from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Map App Builder</h1>
    <p>Status: Online</p>
    <p>Welcome to your OpenShift application!</p>
    """

if __name__ == '__main__':
    # Important: OpenShift requires the app to run on 0.0.0.0
    app.run(host='0.0.0.0', port=8080)
