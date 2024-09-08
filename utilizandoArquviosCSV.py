import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.preprocessing import StandardScaler


caminho_basedados = 'C:\\Users\\Usuario\\PROGRAMACAO_CENTRAL\\python\\outros\\CURSO_IA\\CONTEUDO_BAIXADO\\Bases de dados-20240902T151609Z-001\\Bases de dados\\credit_data.csv'

base_credit = pd.read_csv(caminho_basedados)

#PRINT DO REGISTRO COM MENOR VALOR DE DIVIDA.
# print(base_credit[base_credit['loan'] <= 1.377630])


#PRINT DO NUMERO DE DEVEDORES E NÃO DEVEDORES.
# print(np.unique(base_credit['default'], return_counts=True))


#GRAFICO QTD DEVEDORES OU NÃO.
# def mostraGraficoColuna(value):
#     return sns.countplot(value), plt.show()
#
# mostraGraficoColuna(base_credit['default'])


#GRAFICO QTD IDADES.
# plt.hist(base_credit['age'])
# plt.show()


#PRINT VALOR DOS SALARIOS ANUAIS E A RESPECTIVA QUANTIDADE.
# plt.hist(base_credit['income'])
# plt.show()


#PRINT VALOR DAS DÍVIDAS E A RESPECTIVA QUANTIDADE.
# plt.hist(base_credit['loan'])
# plt.show()


#GRAFICO DE DISPERSÃO BASEADO EM SALARIO E IDADE, ANALISANDO PAGANTES OU NÃO DE DIVIDAS.
# grafico = px.scatter_matrix(base_credit,dimensions=['age', 'income', 'loan'],color='default')
# grafico.show()


#CRIA UM A NOVA TABELA COM A COLUNA DE IDADE APAGADA
# base_credit2 = base_credit.drop('age', axis=1)
# print(base_credit2)


#APAGA SOMENTE OS REGISTROS COM IDADE MENOR QUE 0
# basecredit3 = base_credit.drop(base_credit[base_credit['age'] < 0].index)
# print(basecredit3.head(30))


#FAZ A MEDIA DAS IDADES DA TABELA QUE TEM VALORES MAIOR DO QUE 0
#INSERE O VALOR MEDIO DAS IDADES NOS VALORES NEGATIVOS
#PRINTA OS 30 PRIMEIROS RESULTADOS. ALGUNS ERAM MENORES DO QUE 0
# print(base_credit['age'][base_credit['age']>0].mean())
base_credit.loc[base_credit['age']<0, 'age'] = 40.92
# print(base_credit.head(30))


#PRINT DE TODAS AS COLUNAS, MOSTRANDO QUANTOS REGISTROS NULLS EXISTEM EM CADA UMA
#PRINT DOS 35 PRIMEIROS REGISTROS
#PIRNT DE UM DIVISÓRIA
#SUBSTITUI REGISTROS QUE NÃO NULL POR 40.92
#PRINT DOS 35 PRIMEIROS REGISTROS PARA FAZER A VERIFICAÇÃO DAS MUDANÇAS
# print(base_credit.isnull().sum())
# print(base_credit.head(35))
# print("-------------------------------------------------------------------------------")
# base_credit.loc[base_credit['age'].isnull(), 'age'] = 40.92
# print(base_credit.head(35))



base_credit.loc[base_credit['age']<0, 'age'] = 40.92
base_credit.loc[base_credit['age'].isnull(), 'age'] = 40.92
X_credit = base_credit.iloc[:, 1:4].values

scaler_credit = StandardScaler()
X_credit = scaler_credit.fit_transform(X_credit)

a = X_credit[:,0].min(), X_credit[:,1].min(), X_credit[:,2].min()
b = X_credit[:,0].max(), X_credit[:,1].max(), X_credit[:,2].max()

print(a)
print(b)
