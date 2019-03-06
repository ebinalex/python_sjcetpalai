from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return"hello thala it's time for food"

@app.route("/home")
def home():
    return"welcome to thala food court"
@app.route("/contact")
def contact():
    return"Mr.Thala,Puthoor House,Pala,Kottayam"
@app.route("/about")
def about():
    return"thala cooking workshop is the most perfect solution that can be study from the world"        
if(__name__=="__main__"):
    app.run()

