from flask import Flask, render_template, jsonify

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
@app.route("/")
def Hello_World():
  return render_template('home.html', jobs=JOBS)

@app.route("/jobs")
def jobs_list():
  return jsonify(JOBS)
if __name__ == '__main__':
  app.run('0.0.0.0', debug=True)
