from joblib import load
import os

print(os.getcwd())

with open(os.getcwd() + '/medical_appointment.joblib', 'rb') as f:
    model = load(f)

def predict(instance):
    prediction = model.predict(instance)
    return prediction
