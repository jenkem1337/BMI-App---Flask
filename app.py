from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	bmi = ''
	if request.method=='POST' and 'kilo' in request.form:
		kilo = float(request.form.get('kilo'))
		boy = float(request.form.get('boy'))
		bmi = calcBMI(kilo, boy)
	return render_template('index.html',
							bmi=bmi)
def calcBMI(kilo, boy):
	return (kilo / ((boy / 100) ** 2))





app.run()