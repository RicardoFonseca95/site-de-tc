from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/contacto')
def contacto():
    return "Email: abcd@gmail.com"

@app.route('/about')
def about():
    return "Primeira WebApp criada em 2020"