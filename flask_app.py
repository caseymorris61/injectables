from flask import Flask, render_template, request, json
#from flaskext.mysql import MySQL

#initializations
app = Flask(__name__)
#mysql = MySQL()
 
# MySQL configurations
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'nettuts'
# app.config['MYSQL_DATABASE_DB'] = 'testDB'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'

# mysql.init_app(app)
# conn = mysql.connect()
# cursor = conn.cursor()


@app.route("/")
@app.route("/index")
def main():
    drugs = []

    d1=('Makena','http://www.makena.com/resources','hydroxyprogesterone caproate','AMAG Pharmaceuticals')
    d2=('Humira','https://www.humira.com/humira-complete/injection','adalimumab','Abbvie')
    d3=('Enbrel','/index','etanercept','Amgen')
    d4=('Stelara','/index','ustekinumab','Janssen')
    d5=('Cimzia','/index','certoluzimab pegol','UCB')
    d6=('Rasuvo','http://www.rasuvo.com/using-rasuvo/how-to-use-rasuvo/','methotrexate','Medac Pharma')
    d7=('Epi Pen','/index','','Mylan')
    d8=('Epi Pen Junior','/index','','Mylan')
    d9=('Levemir','/index','detemir','Novo Nordisk')
    d10=('Lantus','/index','glargine','Sanofi')
    d11=('Basaglar','/index','glargine','Lilly')
    d12=('Toujeo','/index','glargine','Sanofi')
    d13=('Tresiba','/index','degludec','Novo Nordisk')
    d14=('Novolog','/index','aspart','NovoNordisk')
    d15=('Humalog','/index','lispro','Lilly')
    d16=('GLP1s','/index','','')
    d17=('Trulicity','/index','dulaglutide','Lilly')
    d18=('Taltz','/index','','Lilly')
    d19=('Lovenox','/index','','Sanofi')

    drugs.append(d1)
    drugs.append(d2)
    drugs.append(d3)
    drugs.append(d4)
    drugs.append(d5)
    drugs.append(d6)
    drugs.append(d7)
    drugs.append(d8)
    drugs.append(d9)
    drugs.append(d10)
    drugs.append(d11)
    drugs.append(d12)
    drugs.append(d13)
    drugs.append(d14)
    drugs.append(d15)
    drugs.append(d16)
    drugs.append(d17)
    drugs.append(d18)
    drugs.append(d19)

    drugs.sort(key=lambda x: x[0])

    return render_template('index.html', drugs=drugs)



@app.route('/residents')
def residents():
    return render_template('residents.html')




# @app.route('/signUp',methods=['POST']) 
# def signUp():
 
#     # read the posted values from the UI
#     _name = request.form['inputName']
#     _email = request.form['inputEmail']
#     _password = request.form['inputPassword']

#     out = "Name: '"+_name+"' Email: '"+_email+"'"
#     print "CASEY"
#     print out

#         # validate the received values
#     if _name and _email and _password:
# 		cursor.callproc('sp_createUser',(_name,_email,_password))#not using HASH. BAD.
# 		data = cursor.fetchall()
# 		if len(data) is 0:
# 			conn.commit()
# 			print "User: "+_name+" created successfully."
# 			return json.dumps({'message':'User created successfully !'})
# 		else:
# 			print "User: "+_name+" not created."
# 			return json.dumps({'error':str(data[0])})

#     else:
#         return json.dumps({'html':'<span>Enter the required fields</span>'})









if __name__ == "__main__":
    app.run()