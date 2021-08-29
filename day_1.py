from flask import Flask, request, render_template
from flask_cors import CORS
import os
from requests import get

app = Flask(__name__)
CORS(app)
port = int(os.environ.get("PORT", 5000))

@app.route("/")
def home():
    return render_template("index.html", title="Backend API")

@app.route("/getSalary/<experience>", methods=["GET"])
def get_user(experience):
    resp = get(f"http://localhost:9000/predict?exp={experience}")
    # Call backend service here to calculate the salary on the basis of experience and serve the response back
    return render_template("salary.html", experience=experience, salary=resp.text)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=port)