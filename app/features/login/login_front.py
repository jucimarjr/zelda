from login_negocio import LoginNegocio

@app.route('/login', methods=['GET', 'POST'])
def login():
    return LoginNegocio.exibir()