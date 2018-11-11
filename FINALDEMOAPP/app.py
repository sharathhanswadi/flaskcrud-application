from flask import Flask,render_template,request,redirect,url_for,flash
from flask_mysqldb import  MySQL



app = Flask(__name__)

app.secret_key = "flash message"

app.config['MYSQL_HOST'] ='localhost'
app.config['MYSQL_USER'] ='root'
app.config['MYSQL_PASSWORD'] ='root'
app.config['MYSQL_DB'] ='sharath'

mysql = MySQL(app)





@app.route('/')

def Index():
	cur = mysql.connection.cursor()
	cur.execute("SELECT * from Persons;")
	data = cur.fetchall()
	cur.close()



	return render_template('index.html',Persons =data)





@app.route('/insert',methods = ['POST'])

def insert():


	if request.method == "POST":
		flash("Data Inserted Successfully")
		name = request.form ['name']
		occupation = request.form ['occupation']
		place = request.form ['place']
		age = request.form ['age']
		projects = request.form ['projects']


		cur = mysql.connection.cursor()
		cur.execute(" INSERT INTO Persons(name,occupation,place,age,projects) VALUES(%s,%s,%s,%s,%s)",(name,occupation,place,age,projects))
		mysql.connection.commit()
		return redirect(url_for('Index'))






@app.route('/update',methods=['POST','GET'])
def update():

 	if request.method == "POST":
 		flash("Data updated Successfully")
 		ID = request.form ['ID']
 		name = request.form ['name']
 		occupation = request.form ['occupation']
 		place = request.form ['place']
 		age = request.form ['age']
 		projects = request.form ['projects']


 		cur = mysql.connection.cursor()
 		cur.execute(""" update Persons set  name =%s,occupation =%s,place =%s,age =%s,projects=%s where ID =%s""",(name,occupation,place,age,projects))
 		flash ("Data updated Successfully")
 		mysql.connection.commit()
 		return redirect(url_for('Index'))







if __name__ == "__main__":
    app.run(debug =True, port =8000)	