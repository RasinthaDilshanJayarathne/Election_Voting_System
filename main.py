from flask import Flask, render_template,request,url_for,flash
from werkzeug.utils import redirect
import mysql.connector

# mydb = mysql.connector.connect(
#   host="electionvoting.cx7qj2rz3vn4.us-east-2.rds.amazonaws.com",
#   user="Admin",
#   password="Admin1234",
#   database="election_voting"
# )

# mycursor = mydb.cursor()
#mycursor.execute("DROP TABLE IF EXISTS candidate")
#mycursor.execute("CREATE TABLE candidate (first_name VARCHAR(255), last_name VARCHAR(255), nic VARCHAR(64) PRIMARY KEY, email VARCHAR(255), gender VARCHAR(12), age int, election_party VARCHAR(255), vote_no int, password VARCHAR(255), conform_password VARCHAR(255))")
#mycursor.execute("DROP TABLE IF EXISTS voter")
#mycursor.execute("CREATE TABLE voter (first_name VARCHAR(255), last_name VARCHAR(255), nic VARCHAR(64) PRIMARY KEY, email VARCHAR(255), gender VARCHAR(12), age int, password VARCHAR(255), conform_password VARCHAR(255))")
#mycursor.execute("DROP TABLE IF EXISTS quota")
#mycursor.execute("CREATE TABLE quota (quota_name VARCHAR(255), quota_reg_no VARCHAR(64) PRIMARY KEY, no_of_people int, registerd_voters int)")
#mycursor.execute("CREATE TABLE students (id int(11) PRIMARY KEY, name varchar(255), email varchar(255), phone varchar(255))")


app = Flask(__name__)

@app.route('/')
def Index():
    # mycursor = mydb.cursor()
    # mycursor.execute("SELECT * FROM candidate")
    # data = mycursor.fetchall()
    # mycursor.close()

    # print(data)

    return render_template('index.html')

# @app.route('/insert', methods = ['POST'])
# def insert():
#     if request.method == "POST":
#         flash("Data Inserted Successfully")
#         firstName = request.form.get('first_name')
#         lastName = request.form.get('last_name')
#         nic = request.form.get('nic')
#         email = request.form.get('email')
#         gender = request.form.get('gender')
#         age = request.form.get('age')
#         electionParty = request.form.get('election_party')
#         voteNo = request.form.get('vote_no')
#         password = request.form.get('password')
#         confirmPassword = request.form.get('conform_password')
#         cur = mysql.cursor()
#         cur.execute("INSERT INTO students (first_name, last_name, nic, email, gender, age, election_party, vote_no, password, conform_password) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s, %s)", (firstName,lastName,nic,email, gender,age,electionParty,voteNo,password,confirmPassword))
#         mysql.connector.commit()
#         return redirect(url_for('Index'))
    
# @app.route('/get', methods=['GET'])
# def get_data():
#     mycursor = mydb.cursor()
#     mycursor.execute("SELECT * FROM voter")
#     data = mycursor.fetchall()
#     mycursor.close()

#     print(data)

#     return render_template('index.html', voter = data)




if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)