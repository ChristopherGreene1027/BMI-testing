from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])



def hello_world():
    bmi=''
    underBMI=''
    normBMI=''
    overBMI=''
    obBMI=''
    if request.method=='POST' and 'userFeet' in request.form and 'userInches' in request.form and 'userPounds' in request.form:
        Weight=float(request.form.get('userPounds'))
        Feet=float(request.form.get('userFeet'))
        Inches=float(request.form.get('userInches'))
        Height=(Feet*12) + Inches
        bmi=round(float((Weight*703)/(Height*Height)), 2)
        
        if bmi > 0:
            if bmi <= 18.5:
                print("Classification: Underwight")
            elif 18.5 <= bmi < 24.9:
                print("Classification: Normal Weight")
            elif 25 <= bmi < 29.9:
                print("Classification: Overweight")
            elif 30 <= bmi:
                print("Classification: Obese")
            else:
                print("System error")

        #    bmi = underBMI
        #elif 18.5 <= bmi < 24.9:
        #    bmi = normBMI
        #elif 25 <= bmi < 29.9:
        #    bmi = overBMI
        #elif 30 <= bmi: 
        #    bmi = obBMI
        #else: 
        #    bmi = bmi
    return render_template('bmi.html', bmi=bmi)

