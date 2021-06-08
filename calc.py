from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("app.html")

@app.route("/calcular", methods=['POST'])
def calcular():
    num1 = request.form['num1']
    num2 = request.form['num2']
    operador = request.form['operador']
    if operador == 'sumar':
        resultado = float(num1) + float(num2)
        return render_template('app.html', resultado=resultado)
    elif operador == 'restar':
        resultado = float(num1) - float(num2)
        return render_template('app.html', resultado=resultado)
    elif operador == 'multiplicar':
        resultado = float(num1) * float(num2)
        return render_template('app.html', resultado=resultado)
    elif operador == 'dividir':
        resultado = float(num1) / float(num2)
        return render_template('app.html', resultado=resultado)
    else:
        return render_template('app.html')

if __name__ == "__main__":
    app.run(debug=True)
