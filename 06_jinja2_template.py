# Jinja 2 Template
"""
    1. {%...%}  ->> for statement
    2. {{ }}    ->> send the output 
    3. {#..#}   ->> for comment

"""

from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
@app.route("/")
def greet():
    return render_template("04_05_form.html")


@app.route("/success/<int:score>")       
def success(score):
    
    return render_template("06_result_jinja.html",res=score)       #res must be same as in result.hrml file



### result checker html page

@app.route("/submit",methods=['POST','GET'])     #here /submit must be same in form action
def submit():
    total_score=0
    if request.method=="POST":          #check the method of form

        science=request.form['science']    # store the value of Science sub from form using name used in from is name="science"
        science=float(science)
        
        math=request.form['math']
        math=float(math)
        python=request.form['python']
        python=float(python)
        ds=request.form['ds']
        ds=float(ds)
        total_score=(science+math+python+ds)/4       #cal avg    

    return redirect(url_for('success',score=total_score))



if __name__=="__main__":
    app.run(debug=True)