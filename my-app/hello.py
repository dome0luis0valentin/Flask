from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Registrarse')

#Función personalizada
def censurador(cadena):
    resultado = ""
    for i in range(len(cadena)):
        if i % 2 == 0:
            resultado += cadena[i]
        else:
            resultado += "*"
    return resultado


app = Flask(__name__)



app.config['SECRET_KEY'] = 'tu_clave_secreta'  # Cambia esto por una clave secreta segura.


@app.add_template_filter
def fun_decoradora(nombre):
	nuevo_nombre = nombre[0].upper()
	nuevo_nombre = "!"+nuevo_nombre+nombre[1::]+"!"
	return nuevo_nombre

@app.route("/links/")
def links():
	return render_template("links.html")

@app.route("/home/<name>/")
def home(name):
	return render_template('home.html', name = name)

@app.route('/')
def hello():
	return render_template('home.html')

@app.route('/tuberias')
def tuberias():

	nombres = ["Valentin", "Domé", "Mati", "Luis", "Macri"]

	return render_template('tuberias.html',
				 titulo = "Tuberias en Flask",
				 nombres = nombres,
				 censu = censurador)


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    form = RegisterForm()
    if form.validate_on_submit():
        # Aquí puedes procesar los datos del formulario, como guardar el usuario y la contraseña.
        # Por ejemplo, podrías almacenarlos en una base de datos.
        username = form.username.data
        password = form.password.data
        # Realiza aquí tu lógica de registro.

        return f'Registro exitoso para el usuario: {username}'

    return render_template('registro.html', form=form)

