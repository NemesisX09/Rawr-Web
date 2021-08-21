from flask import Flask, render_template,request
from replit import web, db

app = Flask(__name__)
db["emails"] = []

@app.route('/',methods=["GET","POST"])
def index():
    if request.method == "POST":
        email = request.form.get("email")
        if email == '' or None:
            return 'The form was not completed'
        emails = db["emails"]
        emails.append(email)
        db["emails"] = emails
    return render_template('index.html')

@app.get('/emails')
def viewEmails():
    data = str(db['emails'])
    return data


web.run(app)

