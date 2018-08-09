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

    # d1=('Makena','http://www.makena.com/resources','hydroxyprogesterone caproate','AMAG Pharmaceuticals')
    # d2=('Humira','https://www.humira.com/humira-complete/injection','adalimumab','Abbvie')
    # d3=('Enbrel','/index','etanercept','Amgen')
    # d4=('Stelara','/index','ustekinumab','Janssen')
    # d5=('Cimzia','/index','certoluzimab pegol','UCB')
    # d6=('Rasuvo','http://www.rasuvo.com/using-rasuvo/how-to-use-rasuvo/','methotrexate','Medac Pharma')
    # d7=('Epi Pen','/index','','Mylan')
    # d8=('Epi Pen Junior','/index','','Mylan')
    # d9=('Levemir','/index','detemir','Novo Nordisk')
    # d10=('Lantus','/index','glargine','Sanofi')
    # d11=('Basaglar','/index','glargine','Lilly')
    # d12=('Toujeo','/index','glargine','Sanofi')
    # d13=('Tresiba','/index','degludec','Novo Nordisk')
    # d14=('Novolog','/index','aspart','NovoNordisk')
    # d15=('Humalog','/index','lispro','Lilly')
    # d16=('GLP1s','/index','','')
    # d17=('Trulicity','/index','dulaglutide','Lilly')
    # d18=('Taltz','/index','','Lilly')
    # d19=('Lovenox','/index','','Sanofi')

    d1=('Lovenox','https://www.lovenox.com/patient-self-injection-video','','Sanofi')
    d2=('Makena','http://www.makena.com/resources','hydroxyprogesterone caproate','AMAG Pharmaceuticals')
    d3=('Humira','https://www.humira.com/humira-complete/injection','adalimumab','Abbvie')
    d4=('Enbrel','https://www.enbrel.com/support/how-to-take-enbrel?isipaid=true&utm_term=how%20to%20take%20enbrel&gclid=EAIaIQobChMI49aYxPjR3AIVCNRkCh2bHA8NEAAYASACEgI7fvD_BwE&gclsrc=aw.ds&dclid=CPW0tMb40dwCFcybZAodQL4Fzw','etanercept','Amgen')
    d5=('Stelara (Psoriasis)','https://www.stelarainfo.com/stelara-injection-support','ustekinumab','Janssen')
    d29=('Stelara (Crohns)','https://www.stelarainfo.com/crohns-disease/patient-support/injection-infusion-support','ustekinumab','Janssen')
    d6=('Cimzia','https://www.cimzia.com/injection-training','certoluzimab pegol','UCB')
    d7=('Rasuvo','http://www.rasuvo.com/using-rasuvo/how-to-use-rasuvo/','methotrexate','Medac Pharma')
    d8=('Epi Pen','https://www.epipen.com/en/about-epipen-and-generic/how-to-use-epipen','epinephrine','Mylan')
    d9=('Epi Pen Junior','https://www.epipen.com/en/about-epipen-and-generic/how-to-use-epipen','epinephrine','Mylan')
    d10=('Levemir','https://www.levemir.com/starting-on-levemir.html','detemir','Novo Nordisk')
    d11=('Lantus','https://www.lantus.com/using-solostar-insulin-pen','glargine','Sanofi')
    d12=('Basaglar','https://www.basaglar.com/en/beginning-basaglar#injection-instructions','glargine','Lilly')
    d13=('Toujeo','https://www.toujeo.com/how-to-use-toujeo-insulin','glargine','Sanofi')
    d14=('Tresiba','https://www.tresiba.com/tresiba-flextouch/using-tresiba-flextouch.html','degludec','Novo Nordisk')
    d15=('Novolog','https://www.rapidactinginsulin.com/novolog/using-novolog/videos-and-downloads.html','aspart','NovoNordisk')
    d16=('Humalog','https://www.humalog.com/type-2-diabetes/how-to-use-u-100-kwikpen/','lispro','Lilly')
    d17=('Trulicity','https://www.trulicity.com/how-to-use/non-insulin-pen/','dulaglutide','Lilly')
    d18=('Taltz','https://www.taltz.com/taking-taltz/how-to-inject','','Lilly')
    d19=('Victoza','https://www.victoza.com/get-started-using-victoza-/your-first-injection.html','liraglutide','')
    d20=('Bydureon (Pen)','https://www.bydureon.com/pen/taking-bydureon/your-first-bydureon-injection.html','exenatide','')
    d28=('Bydureon (B Cise)','https://www.bydureon.com/using-bcise/how-to-use-bydureon-bcise.html','exenatide','')
    d21=('Byetta','https://www.azpicentral.com/byetta/ifu_byetta.pdf#page=1','','')
    d22=('Fiasp','https://www.rapidactinginsulin.com/fiasp/using-fiasp/fiasp-flextouch-and-vial.html','aspart','Novo Nordisk')
    d23=('Tremfya','https://www.tremfya.com/what-is-tremfya','','')
    d24=('Ozempic','https://www.ozempic.com/how-to-use/the-ozempic-pen.html','semaglutide','')
    d25=('Orencia','https://www.orencia.bmscustomerconnect.com/how-to-take-orencia/clickject-autoinjector','','')
    d26=('Kineret','https://www.kineretrx.com/ra/using-kineret','','')
    d27=('Actemra','https://www.actemra.com/ra/taking-actemra/taking-actemra-sc-injections.html','','')


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
    drugs.append(d20)
    drugs.append(d21)
    drugs.append(d22)
    drugs.append(d23)
    drugs.append(d24)
    drugs.append(d25)
    drugs.append(d26)
    drugs.append(d27)
    drugs.append(d28)
    drugs.append(d29)

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