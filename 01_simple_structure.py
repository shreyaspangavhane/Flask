from flask import Flask     #import flask framework as Flask

app=Flask(__name__)     #it is communicating with server

@app.route("/")         #it is decorator and / is the url on which site is to handle

#when we go on that url(/) page inside function message shuld be display
def welcome():
    return "This is the staring of flask"     

@app.route("/greet")
def greet():
    return "Hello, Good morning"

if __name__=='__main__':
    # app.run()
    app.run(debug=True)   #when we use this debug=True then server is automatically restarted i.e it start from updated code