from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello World</h1><p>This is a simple Flask app running from a single script.</p>"

if __name__ == "__main__":
    # Run the app on localhost:5000
    app.run(host="0.0.0.0", port=5000, debug=True)
