from app import app
from flask import render_template, request
from app.forms import ContactForm

@app.route("/")
def index():
    return "Hello world"



@app.route('/registrasi', methods=["GET", "POST"])
def registrasi():
    berita = {'kabar':'baik', 'skala' : 200}
    if request.method == "POST":
           #store the form value
       username = request.form["username"]
       email = request.form["email"]
       password = request.form["password"]
       berita['skala'] = 100
       berita['kabar'] = 'registrasi sukses'
    return render_template('registrasi.html', data = berita)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data 
        email = form.email.data   
        message = form.message.data   

        return name + "<br /> " + email + "<br /> " + message

    return render_template('contact.html', form=form)