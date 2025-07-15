from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Addis Ababa, Ethiopia',
    'salary': ' ETB 50,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Addis Ababa, Ethiopia',
    'salary': ' ETB 100,000'
}, {
    'id': 3,
    'title': 'Frontend Developer',
    'location': 'Remote',
    'salary': ' ETB 80,000'
}, {
    'id': 4,
    'title': 'Backend Developer',
    'location': 'Adama, Ethiopia',
    'salary': ' ETB 120,000'
}]


@app.route("/")
def hello():
  return render_template('Home.html', jobs=JOBS, company_name='Jovian')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
