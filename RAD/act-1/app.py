from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calcular", methods=["POST"])
def calcular():
    try:
        dados = request.get_json()
        n1 = dados["num1"]
        n2 = dados["num2"]
        op = dados["operacao"]

        if op == "soma": 
            resultado = n1 + n2
        elif op == "subtracao": 
            resultado = n1 - n2
        elif op == "multiplicacao": 
            resultado = n1 * n2
        elif op == "divisao": 
            resultado = n1 / n2
        else: 
            return jsonify({"erro": "Operação inválida"})

        return jsonify({"resultado": resultado})
    
    except ZeroDivisionError:
        return jsonify({"erro": "Divisão por zero não é permitida"})
    except Exception:
        return jsonify({"erro": "Dados inválidos. Envie num1, num2 e operacao."})

if __name__ == "__main__":
    app.run(debug=True)