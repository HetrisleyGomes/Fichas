from flask import Flask, render_template,redirect, url_for, request
from flask_socketio import SocketIO, emit

app = Flask(__name__, template_folder='src/templates', static_folder='src/static')
app.secret_key = 'supersecretkey'
socketio = SocketIO(app)

ficha_atual = 0
guiches = [0,0,0,0,0,0,0,0]
ultimos = []

@app.route('/')
def index():
    return render_template('index.html', guiches=guiches, ficha_atual=ficha_atual, ultimos=ultimos)

@app.route('/guiches')
def guiche():
    gx = request.args.get("gx")
    return render_template('guixes.html', gx=gx, ficha_atual=ficha_atual)

@app.route('/proximo', methods=["POST"])
def proximo():
    gx = request.form.get("gx")
    print(gx)
    global ficha_atual
    global guiches
    ficha_atual += 1
    guiches[int(gx)-1] = ficha_atual
    adicionar_numero(ficha_atual)
    # Emite um evento para todos os clientes conectados
    socketio.emit('atualizar_ficha', {'ficha_atual': ficha_atual}, room=None)

    return redirect(url_for("guiche", gx=gx))

@app.route('/update/<var>')
def update(var):
    global ficha_atual
    print(var)
    print(type(var))
    ficha_atual = var
    ficha_atual = int(ficha_atual)
    return redirect('/guiches')

@app.route('/reset')
def reset():
    global guiches
    global ultimos
    guiches = [0,0,0,0,0,0,0,0]
    ultimos = []
    socketio.emit('atualizar_ficha', {'ficha_atual': ficha_atual}, room=None)
    return redirect('/guiches')

def adicionar_numero(novo_numero):
    # Verifica se a lista já tem 3 números
    if len(ultimos) == 5:
        # Remove o último elemento
        ultimos.pop()
    # Adiciona o novo número como primeiro elemento
    ultimos.insert(0, novo_numero)

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5001, debug=True)