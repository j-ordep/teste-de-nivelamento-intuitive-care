from flask import Flask, jsonify, request
from flask_cors import CORS
from pathlib import Path
from utils.leitor import buscar_csv, buscar_csv_cnpj

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

ARQUIVO_CSV = Path(__file__).parent.parent.parent / "teste3-data-base-sql" / "dados-das-operadoras" / "Relatorio_cadop.csv"

@app.route("/api/operadoras", methods=["GET"])
def buscar_operadora():
   
    nome_busca = request.args.get("nome", "").strip().lower()
    resultado_busca = buscar_csv(ARQUIVO_CSV, nome_busca)

    return jsonify(resultado_busca)

@app.route("/api/operadoras/<cnpj>", methods=["GET"])
def buscar_operadora_cnpj(cnpj):
    resultado = buscar_csv_cnpj(ARQUIVO_CSV, cnpj) 

    if resultado:
        return jsonify(resultado)
    
    return jsonify({"erro": "Operadora não encontrada"}), 404
    

if __name__ == "__main__":
    app.run(debug=True)