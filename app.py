from flask import Flask, render_template,jsonify
from database import load_jobs_from_db
from sqlalchemy import create_engine,text




app = Flask(__name__)


# JOBS =[

#   {
#     'id':1,
#     'title':'Data Analyst',
#     'location':'CollegePark, Maryland',
#     # 'salary':'$100,000',
#   },
#   {
#     'id':2,
#     'title':'Frontend Engineer',
#     'location':'CollegePark, Maryland',
#     'salary':'$120,000',
#   },
# {
#   'id':3,
#   'title':'Backend Engineer',
#   'location':'CollegePark, Maryland',
#   'salary':'$140,000',
# },
#   {
#     'id':4,
#     'title':'FullStack Engineer',
#     'location':'CollegePark, Maryland',
#     'salary':'$180,000',
#   }
# ]

@app.route('/')
def hello():
  job_dict = load_jobs_from_db()
  return render_template('home.html',jobs = job_dict, company_name ="Aaron")
  
@app.route('/api/jobs')
def list_job():
  job_dict = load_jobs_from_db()
  return jsonify(job_dict)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)