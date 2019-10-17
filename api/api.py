from flask import Flask, request
import joblib

app = Flask(__name__)

# Update model path
with open(f'/home/salazar/Projects/medical-appointment-classifier/medical_appointment.joblib', 'rb') as f:
    model = joblib.load(f)

instance = [
    # Sample data
    # [62, 0, 1, 0, 0, 0, 0, -1, 0], => "No"
    # [23, 0, 0, 0, 0, 0, 0, 2, 0],  => "No"
    # [60, 1, 1, 1, 1, 1, 1, 5, 0],  => "No"
    # [50, 0, 0, 0, 0, 0, 1, 80, 0]  => "Yes"
]
  
@app.route('/greet')
def say_hello():
    return "Hello ML API :)"

@app.route("/medical-appointment-ml/api/predict", methods=['POST'])
def predict():
    payload = request.json
    for item in payload:
        values = [paciente[1] for paciente in item.items() if paciente[0] != 'nome_paciente']
        instance.insert(len(instance), values)
    
    prediction = model.predict(instance)
    lista_pacientes = []
    for i, item in enumerate(payload):
        lista_pacientes.insert(len(lista_pacientes), { item['nome_paciente']: prediction[i] })

    return { 'predictions' : lista_pacientes }