from flask import Flask, render_template,jsonify




app = Flask(__name__)


JOBS =[

  {
    'id':1,
    'title':'Data Analyst',
    'location':'CollegePark, Maryland',
    # 'salary':'$100,000',
  },
  {
    'id':2,
    'title':'Frontend Engineer',
    'location':'CollegePark, Maryland',
    'salary':'$120,000',
  },
{
  'id':3,
  'title':'Backend Engineer',
  'location':'CollegePark, Maryland',
  'salary':'$140,000',
},
  {
    'id':4,
    'title':'FullStack Engineer',
    'location':'CollegePark, Maryland',
    'salary':'$180,000',
  }
]

@app.route('/')
def hello():
    return render_template('home.html',jobs = JOBS, company_name ="Aaron")
  
@app.route('/api/jobs')
def list_job():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)