from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

@app.route("/")
def home():
    return "<h1>welcom to home page</h1>"

@app.route("/product",methods=['GET','POST'])
def product():
    if request.method =='POST':
        name=request.form['name1']
        return f'hello my friend {name}?'
    return render_template('form.html')
 
#@app.route("/submit",methods=['GET','POST'])
#def submit():
#    if request.method =='POST':
#        name=request.form['name1']
#        return f'hello my friend {name} , you just submit your name.?'
#    return render_template('form.html')

##VARIABLE RULE
@app.route("/success/<int:score>")
def success(score):
    return "your score is :" + str(score)

@app.route("/result/<int:marks>")
def result(marks):
    res=''
    if marks<=33:
        res='fail'
    else:
        res='pass'
    return render_template('result.html',result=res)

@app.route("/resultdict/<int:marks>")
def resultdict(marks):
    res=''
    if marks<=33:
        res='fail'
    else:
        res='pass'
    exp={'key':marks,'value':res}
    return render_template('resultdict.html',result=exp)

@app.route("/getres",methods=['GET','POST'])
def getres():
    total=0
    if request.method == 'POST':
        sci=float(request.form['science'])
        maths=float(request.form['maths'])
        physics=float(request.form['physics'])

        total=(sci+maths+physics)/3        
    
    else:
       return render_template('getres.html')
        
    return redirect(url_for('result',result=int(total)))

if __name__=="__main__":
    app.run(debug=True)