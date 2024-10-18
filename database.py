from sqlalchemy import create_engine,text
import os


my_secret = os.environ['DB_CONNECTION_STRING']
connection_string = my_secret

# connection_test ="mysql+mysqlconnector://4KBTJsfpHfbJ3nf.root:28JCZIS44kvSYg5Y@gateway01.us-east-1.prod.aws.tidbcloud.com:4000/test?ssl_ca=/etc/ssl/cert.pem&ssl_verify_cert=true&ssl_verify_identity=true"


engine = create_engine(connection_string)


# with engine.connect() as conn:
#   job_dict = []
#   result = conn.execute(text("select * from jobs"))
#   print(result.all())
#   print("type of result is",result)
  # print("type of result are",type(result.all()))

def load_jobs_from_db():
  with engine.connect() as conn:
    job_dict = []
    result = conn.execute(text("select * from jobs"))
    columns = result.keys()  # Get the column names from the result

  # Convert each row to a dictionary
    for row in result:
        row_dict = dict(zip(columns, row))
        job_dict.append(row_dict)

  # Print the list of dictionaries
  return job_dict


def load_jobdetail_from_db(id):
  with engine.connect() as conn:
    params = {'val': id}
    result = conn.execute(text("select * from jobs where id = :val"), params)
    # rows = result.all()

    # if len(rows) == 0:
    #   return None
    # else:
    #   return dict(rows[0]) 
    rows = result.mappings().all()  # This gives you a list of dictionaries

    if len(rows) == 0:
        return None
    else:
        return dict(rows[0])
      
# def add_application_db(job_id, application):
#   with engine.connect() as conn:
#     query = text("INSERT INTO applications (job_id, full_name, email, phone, resume) VALUES (:job_id, :full_name, :email, :phone, :resume)")
#     params = {
#         'job_id': job_id,
#         'name': application['full_name'],
#         'email': application['email'],
#         'phone': application['phone'],
#         'resume': application['resume']
#     }
def add_application_db(job_id, application):
  with engine.connect() as conn:
      query = text("INSERT INTO applications (job_id, name, email, phone, resume_filename) VALUES (:job_id, :name, :email, :phone, :resume_filename)")
      params = {
          'job_id': job_id,
          'name': application['full_name'],  
          'email': application['email'],     
          'phone': application['phone'],      
          'resume_filename': application['resume'] 
      }
      conn.execute(query, params)
