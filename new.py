from flask import Flask
app = Flask(__name__)

@app.route("/")
def mymethod():
    return "Data Recvied "

if __name__ =="__main__":
    app.run(debug=True)