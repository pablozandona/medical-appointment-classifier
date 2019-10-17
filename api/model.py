from joblib import load

with open(f'../medical_appointment.joblib', 'rb') as f:
    model = load(f)


def predict(instance):
    prediction = model.predict(instance)
    return prediction
