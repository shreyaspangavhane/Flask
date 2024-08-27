# Building of URL dynamically

from flask import Flask

app=Flask(__name__)
@app.route("/")
def greet():
    return "Hello, Good Evening"


@app.route("/success/<int:score>")       #here sucess is url and <int:score> is appending value for retrival 
def sucess(score):
    return "Student is passed and marks is "+ str(score)

# http://127.0.0.1:5000/sucess/38  when we write on browers it  display result as " Student is passed and marks is 38 "
    

@app.route("/fail/<int:score>")
def fail(score):
    return "Student is Fail and marks is "+ str(score)    #output is get same as above



if __name__=="__main__":
    app.run(debug=True)