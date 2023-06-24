from datetime import datetime

from flask import Flask, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'MY SECRET KEY'
db = SQLAlchemy(app)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=True)
    value = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)


class DataForm(FlaskForm):
    name = StringField(
        'Введите название',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(1, 128)]
    )
    description = TextAreaField(
        'Введите описание'
    )
    value = IntegerField(
        'Введите значение',
        validators=[DataRequired(message='Обязательное поле')]
    )
    submit = SubmitField(
        'Добавить'
    )


@app.route('/')
def index_view():
    quantity = Data.query.count()
    if not quantity:
        return 'В базе нет данных'
    items = Data.query.all()
    labels = [item.id for item in items]
    data = [item.value for item in items]
    return render_template(
        'index.html',
        items=items,
        labels=labels,
        data=data
    )


@app.route('/add', methods=['GET', 'POST'])
def add_data_view():
    form = DataForm()
    if form.validate_on_submit():
        data = Data(
            name=form.name.data,
            description=form.description.data,
            value=form.value.data
        )
        db.session.add(data)
        db.session.commit()
        return redirect('/')
    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run()
