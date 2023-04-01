from flask import Flask, render_template, redirect, url_for
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit()
        return redirect(url_for('home'))
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrarionForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/')
def home():
    return "Bienvenido a la página de inicio"

if __name__ == '__main__':
    app.run()

