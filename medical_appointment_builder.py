import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeClassifier
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import svm
import matplotlib.pyplot as plt

from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.utils import resample
import joblib
from sklearn import metrics
import seaborn as sns

dataset = pd.read_csv('data/medical_appointment.csv', delimiter=',')

# Remove os registros com idade inválida
dataset = dataset[(dataset['Age'] >= 0) & (dataset['Age'] <= 95)]

# # Balanceamento
# # print(dataset['No-show'].value_counts())
# # majoritaria = dataset[dataset['No-show'] == 'No']
# # minoritaria = dataset[dataset['No-show'] == 'Yes']
# # minoritaria_upsample = resample(minoritaria, replace=True, n_samples=88168, random_state=None)
# # dataset = pd.concat([majoritaria, minoritaria_upsample])
# # print(dataset['No-show'].value_counts())

# Conversao para datetime
dataset['AppointmentDay'] = pd.to_datetime(dataset['AppointmentDay'])
dataset['ScheduledDay'] = pd.to_datetime(dataset['ScheduledDay'])

# Calculo da diferenca de dias entre o agendamento e a data da consulta
dataset['distance_day'] = (dataset['AppointmentDay'] - dataset['ScheduledDay']).dt.days
dataset['distance_day'] = pd.to_numeric(dataset['distance_day'])

rename = {
    'Age' : 'idade',
    'Scholarship' : 'auxilio_bolsa_familia',
    'Hipertension' : 'hipertensao',
    'Diabetes' : 'diabetes',
    'Alcoholism' : 'alcolismo',
    'Handcap' : 'deficienca',
    'SMS_received' : 'sms_recebido',
    'distance_day' : 'dias_para_consulta',
    'Gender' : 'genero',
    'No-show' : 'compareceu_consulta',
}
dataset = dataset.rename(columns=rename)

# Heatmap de Correlação
corr = dataset.corr()
sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns)
plt.show()

# Divide os dados em dois conjuntos: Atributos e Classes
classes = dataset['compareceu_consulta']
attributes = dataset.drop(['compareceu_consulta', 'PatientId', 'AppointmentID', 'ScheduledDay', 'AppointmentDay', 'Neighbourhood'], axis=1)

# Cria atributos "dummies" para as colunas que nao sao numericas no conjunto de dados
new_attributes = pd.get_dummies(attributes, columns=['genero'], drop_first=True)

SEED = 5
np.random.seed(SEED)

# Dividir os dados aleatoriamente em conjunto para aprendizado e conjunto para testes
X_train, X_test, y_train, y_test = train_test_split(new_attributes, classes, test_size = 0.33, stratify = classes)
print("Dados de treino com %d elementos e dados de teste com %d elementos" % (len(X_train), len(X_test)))

# Treinar o modelo - DecisionTreeClassifier
classifier_decision_tree = DecisionTreeClassifier()
classifier_decision_tree.fit(X_train, y_train)

acuracia_decision_tree = classifier_decision_tree.score(X_test, y_test) * 100
print("A acurácia do decision tree foi %.2f%%" % acuracia_decision_tree)

dummy_classifier = DummyClassifier()
dummy_classifier.fit(X_train, y_train)
acuracia_dummy = dummy_classifier.score(X_test, y_test) * 100

print("A acurácia do dummy classifier foi %.2f%%" % acuracia_dummy)

classifier_random_forest = RandomForestClassifier(n_estimators=100)
classifier_random_forest.fit(X_train, y_train)
acuracia_random_forest = classifier_random_forest.score(X_test, y_test) * 100

print("A acurácia do random forest foi %.2f%%" % acuracia_random_forest)

classifier_logit = LogisticRegression(solver='lbfgs', max_iter=500)
classifier_logit.fit(X_train, y_train)
acuracia_logit = classifier_logit.score(X_test, y_test) * 100

print("A acurácia do logistic regression foi %.2f%%" % acuracia_logit)

# Aplicar o modelo gerado sobre os dados separados para testes
y_pred = classifier_logit.predict(X_test)
probabilidades = classifier_logit.predict_proba(X_test)
print(probabilidades)

cm = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)
print("\nResultado da Avaliação do Modelo")
print(cm)
print(report)

especificidade = cm[0][0] / (cm[0][0] + cm[0][1])
sensibilidade = cm[1][1] / (cm[1][1] + cm[1][0])
print('especificidade:', especificidade)
print('sensibilidade: ', sensibilidade)

joblib.dump(classifier_logit, 'medical_appointment.joblib')