from flask import Flask, render_template, jsonify, request
from database import engine,get_content
import sqlalchemy
app = Flask(__name__)

JOBS = [
  {
    'id':'1',
    'title':'test demo 1',
    'location':'china jiangshu',
    'salary':'CNY 1000'
  },
  {
    'id':'2',
    'title':'test demo 2',
    'location':'china jiangshu',
    'salary':'CNY 1000'
  },
  {
    'id':'3',
    'title':'test demo 3',
    'location':'china jiangshu',
    'salary':'CNY 1000'
  },
  {
    'id':'4',
    'title':'test demo 4',
    'location':'china jiangshu',
    'salary':'CNY 1000'
  }
]
def get_sql():
  with engine.connect() as conn:
    result = conn.execute(sqlalchemy.text("SELECT * from jobs"))
    result_list = result.all()
  return result_list
    

@app.route("/")
def Hello_World():
  #jobs = get_sql()
  return render_template('home.html', jobs=JOBS)
@app.route("/jobs/<id>")
def jobs_ht(id):
  listt = get_content(id)
  return jsonify(listt)
@app.route("/jobs/<id>/apply")
def job_apple(id):
#  data = request.args
  data = request.form
  return jsonify(data)


@app.route("/jobs")
def jobs_list():
  return jsonify(JOBS)
if __name__ == '__main__':
  app.run('0.0.0.0', debug=True)
