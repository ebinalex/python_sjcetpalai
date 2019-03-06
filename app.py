from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")
@app.route("/contact")
def contact():
    return"Mr.Thala,Puthoor House,Pala,Kottayam"
@app.route("/about")
def about():
    return"thala cooking workshop is the most perfect solution that can be study from the world"        
if(__name__=="__main__"):
    app.run(debug=True)

