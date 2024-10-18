from flask import Flask, render_template,jsonify,request
from database import load_jobs_from_db, load_jobdetail_from_db, add_application_db
from sqlalchemy import create_engine,text
import os
from werkzeug.utils import secure_filename





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

@app.route('/job/<id>')
def show_job(id):
  job = load_jobdetail_from_db(id)
  if not job:
    return "Page Not Found",404
  return render_template('jobpage.html',job = job)
  # return jsonify(job)


@app.route('/job/<id>/apply', methods=['POST'])
def apply_job(id):
  # data = {
  #     "name": request.form.get("name"),
  #     "email": request.form.get("email"),
  #     "phone": request.form.get("phone"),
  #   "resume": request.form.get("resume")
  # }
  # # data = request.args
  # return jsonify(data)
  name = request.form.get("name")
  email = request.form.get("email")
  phone = request.form.get("phone")
  resume = request.files.get("resume")  

  
  if resume:
      
      filename = secure_filename(resume.filename)
      # Specify the path where you want to save the file
      if not os.path.exists("uploads"):
        os.makedirs("uploads")

      resume.save(os.path.join("uploads", filename))

  # Prepare data for response
  data = {
      "name": name,
      "email": email,
      "phone": phone,
      "resume_filename": filename if resume else None
  }

  # Call the add_application_db function to insert the data into the database
  add_application_db(id, data)
  return render_template('application_confirm_page.html', application=data)
  
  

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)