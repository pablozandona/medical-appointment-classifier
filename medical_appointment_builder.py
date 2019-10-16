import io
import pandas as pd
from google.colab import files
uploaded = files.upload()
csv = pd.read_csv(io.StringIO(uploaded['no-show.csv'].decode('utf-8')))

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.utils import resample
from sklearn import svm

dataset = csv

# dataset = pd.read_csv('https://drive.google.com/open?id=1Hx8uIoIqkb0emlSbpT5-QBGey4d1VjYY', delimiter=',')
print(dataset.head())

# Remove os registros com idade inválida
dataset = dataset[(dataset['Age'] >= 0) & (dataset['Age'] <= 95)]

# Balanceamento
# print(dataset['No-show'].value_counts())
# majoritaria = dataset[dataset['No-show'] == 'No']
# minoritaria = dataset[dataset['No-show'] == 'Yes']
# minoritaria_upsample = resample(minoritaria, replace=True, n_samples=88168, random_state=None)
# dataset = pd.concat([majoritaria, minoritaria_upsample])
# print(dataset['No-show'].value_counts())

# Conversão para datetime
dataset['AppointmentDay'] = pd.to_datetime(dataset['AppointmentDay'])
dataset['ScheduledDay'] = pd.to_datetime(dataset['ScheduledDay'])

# Cálculo da diferença de dias entre o agendamento e a data da consulta
dataset['distance_day'] = (dataset['AppointmentDay'] - dataset['ScheduledDay']).dt.days
dataset['distance_day'] = pd.to_numeric(dataset['distance_day'])

# Separa a classe dos atributos
classes = dataset['No-show']
attributes = dataset.drop(['No-show', 'PatientId', 'AppointmentID', 'ScheduledDay', 'AppointmentDay', 'Neighbourhood'], axis=1)

# Cria atributos "dummies" para as colunas que não são numericas no conjunto de dados
new_attributes = pd.get_dummies(attributes, columns=['Gender'], drop_first=True)
print(new_attributes.columns)

# Dividir os dados aleatoriamente em conjunto para aprendizado e conjunto para testes
X_train, X_test, y_train, y_test = train_test_split(new_attributes, classes, test_size=0.20) #20% do tamanho do arquivo será usado para testes

#### DecisionTreeClassifier
# Treinar o modelo
classifier_dt = DecisionTreeClassifier()
classifier_dt.fit(X_train, y_train)

# Aplicar o modelo gerado sobre os dados separados para testes
y_pred = classifier_dt.predict(X_test)

# Avaliar o modelo: Acurácia e matriz de contingência
print("Resultado da Avaliação do Modelo")
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Cross validation
scores = cross_val_score(classifier_dt, new_attributes, classes, cv=10)
print('DecisionTreeClassifier')
print(scores)
print('DecisionTreeClassifier Precisao media: ', scores.mean())

'''
#### SVC
# Treinar o modelo
classifier_svm = svm.SVC().fit(new_attributes, classes)
classifier_svm.fit(X_train, y_train)

# Aplicar o modelo gerado sobre os dados separados para testes
y_pred = classifier_svm.predict(X_test)

# Avaliar o modelo: Acurácia e matriz de contingência
print("Resultado da Avaliação do Modelo")
print('SCORE', classifier_svm.score(new_attributes, classes))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Cross validation
scores = cross_val_score(classifier_svm, new_attributes, classes, cv=10)
print('SVC')
print(scores)
print('SVC Precisao media: ', scores.mean())
'''
