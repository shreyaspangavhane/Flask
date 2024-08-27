# integrating html with flask

from flask import Flask,redirect,url_for,render_template

app=Flask(__name__)
@app.route("/")
def greet():
    return render_template("index.html")


@app.route("/success/<int:score>")       
def success(score):
    return "<html><body><h1>Student is passed </html></body></h1> "


@app.route("/fail/<int:score>")
def fail(score):
    return "Student is Fail and marks is "+ str(score)    


@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))      



if __name__=="__main__":
    app.run(debug=True)