import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
# import plotly.express as px
# from scipy.special import values
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

pd.set_option('display.max_columns', None)  # Mostrar todas as colunas
pd.set_option('display.width', 1000)        # Ajustar a largura máxima da saída
pd.set_option('display.colheader_justify', 'right')
caminho_basedados = 'C:\\Users\\Usuario\\PROGRAMACAO_CENTRAL\\python\\outros\\CURSO_IA\\CONTEUDO_BAIXADO\\Bases de dados-20240902T151609Z-001\\Bases de dados\\census.csv'
basedados = pd.read_csv(caminho_basedados)

# PRINT DE DADOS COMO MEDIA MIN E MAX
# print(basedados.describe())

#VERIFICA SE HÁ DADOS NULOS
# print(basedados.isnull().sum())

#QTD DE PESSOAS QUE REBEM MAIS OU MENOS DE 50 MIL
# print(np.unique(basedados['income'],return_counts=True ))

#GRAFICO DE COLUNAS QUE MOSTRA A QTD DE PESSOAS QUE REBEM MAIS OU MENOS DE 50 MIL
# sns.countplot(x = basedados['income'])
# plt.show()

#GRAFICO DA QUANTIDADE DE PESSOAS POR IDADE
# plt.hist(basedados['age'])
# plt.show()

#GRAFICO DA QUANTIDADE DE PESSOAS POR ANOS DE ESTUDO
# plt.hist(basedados['education-num'])
# plt.show()

#GRAFICO DA QUANTIDADE DE PESSOAS POR HORAS DE TRABALHO SEMANAL
# plt.hist(basedados['hour-per-week'])
# plt.show()

#GRAFICO DO TIPO TREEMAP PARA MOSTRAR A QUANTIDADE DE PESSOAS POR CLASSE DE SERVIÇO
# grafico = px.treemap(basedados, path=['workclass'])
#OU
# grafico = px.treemap(basedados, path=['workclass','age'])
# grafico.show()

#GRAFICO DO TIPO TREEMAP PARA MOSTRAR A QUANTIDADE DE PESSOAS POR OCUPAÇÃO
# grafico = px.treemap(basedados, path=['occupation'])
# grafico.show()

#GRAFICO DE DOIDO APRESENTANDO RELAÇÃO ENTRE OCUPAÇÃO E ESTADO CIVIL
# grafico = px.parallel_categories(basedados,dimensions=['occupation','relationship'])
# grafico.show()


X_census = basedados.iloc[:, 0:14].values
Y_census = basedados.iloc[:, 14].values
label_encoder_teste = LabelEncoder()
# print(X_census[:,1])

#TRANSFORMA AS PROFISSÕES (X_census[:,1]) em numeros, para poderem ser lidas pelo sistema
# teste = label_encoder_teste.fit_transform(X_census[:,1])
# print(teste)

label_encoder_workclass = LabelEncoder()
label_encoder_education = LabelEncoder()
label_encoder_marital = LabelEncoder()
label_encoder_occupation = LabelEncoder()
label_encoder_relationship = LabelEncoder()
label_encoder_race = LabelEncoder()
label_encoder_sex = LabelEncoder()
label_encoder_country = LabelEncoder()

X_census[:, 1] = label_encoder_workclass.fit_transform(X_census[:, 1])
X_census[:,3] = label_encoder_education.fit_transform(X_census[:,3])
X_census[:, 5] = label_encoder_marital.fit_transform(X_census[:, 5])
X_census[:,6] = label_encoder_occupation.fit_transform(X_census[:,6])
X_census[:, 7] = label_encoder_relationship.fit_transform(X_census[:, 7])
X_census[:,8] = label_encoder_race.fit_transform(X_census[:,8])
X_census[:, 9] = label_encoder_sex.fit_transform(X_census[:, 9])
X_census[:,13] = label_encoder_country.fit_transform(X_census[:,13])

# print(X_census[0])


#Transforma os valores string em valores numerados com pesos para a leitura do algoritmo
# onehotencoder_census = ColumnTransformer(transformers=[('OneHot', OneHotEncoder(), [1,3,5,6,7,8,9,13])], remainder='passthrough')
# X_census = onehotencoder_census.fit_transform(X_census).toarray()
# print(X_census[0])


#Transforma os valores string em valores numerados com pesos para a leitura do algoritmo
# scaler_census = StandardScaler()
# X_census = scaler_census.fit_transform(X_census)
# print(X_census[0])


