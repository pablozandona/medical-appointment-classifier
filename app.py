from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import model
import utils
import os

static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'www/dist')

app = Flask(__name__)
cors = CORS(app)

instance = [
    # Sample data
    # [62, 0, 1, 0, 0, 0, 0, -1, 0], => "No"
    # [23, 0, 0, 0, 0, 0, 0, 2, 0],  => "No"
    # [60, 1, 1, 1, 1, 1, 1, 5, 0],  => "No"
    # [50, 0, 0, 0, 0, 0, 1, 80, 0]  => "Yes"
]

@app.route('/')
def root():
    return "Hello ML API :)"

@app.route("/predict", methods=['POST'])
def predict():
    payload = request.json

    print(payload)

    if 'body' in payload:
        payload = payload['body']

    print(payload)

    for item in payload:

        if not ('dias_para_consulta' in item):
            item['dias_para_consulta'] = utils.get_day_distance(item['data_consulta'], item['data_agendamento'])

        if not ('nome_paciente' in item):
            item['nome_paciente'] = 'Dummy'

        values = [item['idade'], item['auxilio_bolsa_familia'], item['hipertensao'],
                  item['diabetes'], item['alcolismo'], item['deficienca'], item['sms_recebido'],
                  item['dias_para_consulta'], item['genero']]
        values = list(map(int, values))

        instance.insert(len(instance), values)

    prediction = model.predict(instance)

    lista_pacientes = []
    for i, item in enumerate(payload):
        lista_pacientes.insert(len(lista_pacientes), {item['nome_paciente']: prediction[i]})

    return jsonify(lista_pacientes)
