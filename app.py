
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>My Flask CI/CD Project</h1><p>Website deployed successfully!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
