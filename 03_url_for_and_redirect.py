# var rule anmd url building

#integrating differnt webpages
from flask import Flask,redirect,url_for

app=Flask(__name__)
@app.route("/")
def greet():
    return "Hello, Good Evening"


@app.route("/success/<int:score>")       
def success(score):
    return "<html><body><h1>Student is passed </html></body></h1> "


@app.route("/fail/<int:score>")
def fail(score):
    return "Student is Fail and marks is "+ str(score)    #check marks condition and send that marks value to score from that score execite that pages


##result check ->>fail/success
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