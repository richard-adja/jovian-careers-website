from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [
    {
        "id": 1,
        "title": "Software Engineer",
        "location": "San Francisco, USA",
        "salary": "$120,000"
    },
    {
        "id": 2,
        "title": "Data Analyst",
        "location": "New York, USA",
        "salary": "$100,000"
    },
    {
        "id": 3,
        "title": "Product Manager",
        "location": "London, UK",
        "salary": "$130,000"
    },
    {
        "id": 4,
        "title": "UX Designer",
        "location": "Berlin, Germany",
        "salary": "$110,000"
    },
    {
        "id": 5,
        "title": "Marketing Specialist",
        "location": "Sydney, Australia",
        "salary": "$90,000"
    }
]

@app.route("/")
def index():
  return render_template("home.html", jobs = jobs, comp_name="Jovian")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(jobs)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
