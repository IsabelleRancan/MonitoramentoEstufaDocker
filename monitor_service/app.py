from flask import Flask, request, jsonify
from models import Estufa
from db import Session, init_db
from rabbitmq import send_to_queue

app = Flask(__name__)
init_db()

@app.route('/transmit', methods=['POST'])
def transmit_data():
    data = request.get_json()
    temperatura = data.get('temperatura')
    sensacao = data.get('sensacao_termica')
    umidade = data.get('umidade')

    if not all([temperatura, sensacao, umidade]):
        return jsonify({'error': 'Dados incompletos'}), 400

    session = Session()
    nova = Estufa(temperatura=temperatura, sensacao_termica=sensacao, umidade=umidade)
    session.add(nova)
    session.commit()

    if temperatura > 50 or umidade < 50 or sensacao > 65:
        send_to_queue(nova.to_dict())

    return jsonify(nova.to_dict()), 201

@app.route('/all', methods=['GET'])
def get_all():
    session = Session()
    dados = session.query(Estufa).all()
    return jsonify([d.to_dict() for d in dados])

@app.route('/critical', methods=['GET'])
def get_critical():
    session = Session()
    criticos = session.query(Estufa).filter(
        (Estufa.temperatura > 50) |
        (Estufa.umidade < 50) |
        (Estufa.sensacao_termica > 65)
    ).all()
    return jsonify([d.to_dict() for d in criticos])

if __name__ == '__main__':
    app.run(debug=True, port=5000)
