from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

class LoginForm(FlaskForm):
    username_crew = StringField('id астронавта', validators=[DataRequired()])
    password_crew = PasswordField('Пароль астронавта', validators=[DataRequired()])
    username_cap = StringField('id капитана', validators=[DataRequired()])
    password_cap = PasswordField('пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Войти')

@app.route('/')
@app.route('/index/<site_name>')
def index(site_name):
    return render_template('index.html', title=site_name)

@app.route('/training/<prof>')
def find_job(prof):
    return render_template('training.html', job=prof)

@app.route('/list_prof/<param>')
def print_list(param):
    return render_template('prof_list.html', p=param)

@app.route('/login', methods=['GET', 'POST'])
def login_form_creator():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('emergency_login.html', title='Авторизация', form=form)

@app.route('/success')
def successful_login():
    return 'success'

@app.route('/auto_answer')
@app.route('/answer')
def answer():
    data = {
        'surname': "Романов",
        'name': "Петр",
        'education': "Алексеевич",
        'profession': "Царь",
        'sex': "male",
        'motivation': "Прорубим окно на Марс!",
        'ready': True,
    }
    info = list(map(lambda x: x, data.values()))
    return render_template('form_answer.html', link=url_for('static', filename='css/mars_style.css'), values=info,
                           size=len(data.keys()))

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')