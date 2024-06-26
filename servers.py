from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
import json
from random import randint

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
    return render_template('form_answer.html', values=info, size=len(data.keys()))

@app.route('/distribution')
def distribution():
    data = ['Князь', "Илья Муромец", "Добрыня Никитич", "Алеша Попович", "Конь Юлий"]
    return render_template('distribution.html', size=len(data), people=data)

@app.route('/table/<string:gen>/<int:age>')
def table(gen, age):
    if gen == 'female':
        if age >= 21:
            r, g, b = 245, 55, 85
        else:
            r, g, b = 245, 172, 214
    if gen == 'male':
        if age >= 21:
            r, g, b = 42, 106, 245
        else:
            r, g, b = 91, 245, 69
    if age >= 21:
        return render_template('table.html', r=r, g=g, b=b, ref=url_for('static', filename='img/not_young_person_from_mars.png'))
    return render_template('table.html', r=r, g=g, b=b, ref=url_for('static', filename='img/young_person_from_mars.png'))

@app.route('/member')
def member():
    data = [{'name': "Князь",
                'surname': "",
                'photo': 'img/Knyaz.png',
                'jobs': ['правитель']},
               {'name': "Илья ",
                'surname': "Муромец",
                'photo': 'img/Bgtr_I.png',
                'jobs': ["богатырь", "дровосек", "повар"]},
               {"name": "Добрыня ",
                "surname": "Никитич",
                "photo" : "img/Bgtr_D.png",
                "jobs": ["богатырь", "охотник", "пилот Змея-Горыныча"]},
               {"name": "Алеша ",
                "surname": "Попович",
                "photo" : "img/Bgtr_A.png",
                "jobs": ["богатырь", "рыболов", "огородник"]},
               {"name": "конь Юлий ",
                "surname": "Цезарь",
                "photo" : "img/Yuliy.png",
               "jobs": ["богатырская лошадь", "библиотекарь", "переговорщик", "казначей", "специалист по радиационной защите"]}]
    num = randint(0, len(data) - 1)
    print(num)
    name = data[num]['name']
    print(name)
    surname = data[num]['surname']
    photo = data[num]['photo']
    list_of_jobs = data[num]['jobs']
    return render_template('card.html', name=name, surname=surname, list_of_jobs=sorted(list_of_jobs), size=len(list_of_jobs) ,ref=url_for('static', filename=photo))

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')