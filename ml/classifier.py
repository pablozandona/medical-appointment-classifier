import joblib
import os

classifier = joblib.load('medical_appointment.joblib')

#['idade', 'auxilio_bolsa_familia', 'hipertensao', 'diabetes',
# 'alcolismo', 'deficienca', 'sms_recebido', 'dias_para_consulta',
# 'genero_M']
instance=[
    [62, 0, 1, 0, 0, 0, 0, -1, 0],
    [23, 0, 0, 0, 0, 0, 0, 2, 0],
    [60, 1, 1, 1, 1, 1, 1, 5, 0],
    [50, 0, 0, 0, 0, 0, 1, 80, 0]
]
print(classifier.predict(instance))
