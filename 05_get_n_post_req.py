## get and post request
from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
@app.route("/")
def greet():
    return render_template("form.html")


@app.route("/success/<int:score>")       
def success(score):
    result=""
    if(score>=50):
        result="Pass"

    else:
        result="Fail"

    return render_template("result.html",res=result)       #res must be same as in result.hrml file


# @app.route("/fail/<int:score>")
# def fail(score):
#     return "Student is Fail and marks is "+ str(score)    


# #result checker
# @app.route('/results/<int:marks>')
# def results(marks):
#     result=""
#     if marks<50:
#         result='fail'
#     else:
#         result='success'
#     return redirect(url_for(result,score=marks))      


### result checker html page
@app.route("/submit",methods=['POST','GET'])     #here /submit must be same in form action
def submit():
    total_score=0
    if request.method=="POST":          #check the method of form

        science=float(request.form['science'])    # store the value of Science sub from form using name used in from is name="science"
        math=float(request.form['math'])
        python=float(request.form['python'])
        ds=float(request.form['ds'])

        total_score=int((science+math+python+ds)/4)       #cal avg    

    return redirect(url_for('success',score=total_score))



if __name__=="__main__":
    app.run(debug=True)