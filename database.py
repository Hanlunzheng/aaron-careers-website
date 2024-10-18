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