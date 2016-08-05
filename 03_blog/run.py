from flask import  Flask, render_template,session
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import  StringField, SubmitField
from wtforms.validators import Required
from flask_moment import Moment

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dsadfdsafasdf'
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

class Nameform(Form):
    name = StringField('what is u name?', validators=[Required()])
    submit = SubmitField('submit')


@app.errorhandler(404)
def page_not_found(e):
    render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500

@app.route('/', methods=['GET','POST'])
def index():
    name = None
    form = Nameform()
    if form.validate_on_submit():
        session['name'] = form.name.data
        form.name.data= ''
    return render_template('index.html', form = form, name = session.get('name'))

# @app.route('/user/<name>')
# def index(name):
#     return render_template('index.html',name=name)


if __name__ == '__main__':
    manager.run()
