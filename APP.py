from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola desde tu servidor local de Flask!'

@app.route('/contacto')
def contact_page():
    return 'Página de contacto'

@app.route('/saludo/<nombre>')
def saludar(nombre):
    return f'Hola, {nombre}!'

if __name__ == '__main__':
    app.run(debug=True)


