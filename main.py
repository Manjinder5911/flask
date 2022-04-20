from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/phantomcoding'
db = SQLAlchemy(app)

class Contacts(db.Model):
    # S/no.,Name,Email,Phone no.,Msg,date
    Sno = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80), unique=False, nullable=False)
    Email = db.Column(db.String(20), nullable=False)
    Phone_num = db.Column(db.String(12), nullable=False)
    Msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)


@app.route("/")
def home():  
    return render_template('Index.html')

@app.route("/about")
def about():    
    return render_template('about.html',)

@app.route("/contact",methods=["GET","POST"])
def contacts():
    if (request.method == 'POST'):
        """Add entry to the database"""
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        entry = Contacts(Name= name, Email= email, Phone_num= phone, Msg= message)
        db.session.add(entry)
        db.session.commit() 
        
    return render_template('contact.html')


@app.route("/post")
def post():
    return render_template('post.html')

app.run(debug=True)