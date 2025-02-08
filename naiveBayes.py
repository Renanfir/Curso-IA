import pickle
from sklearn.metrics import accuracy_score, confusion_matrix
from yellowbrick.classifier import ConfusionMatrix
from sklearn.naive_bayes import GaussianNB


path = r'C:\Users\Renan\PROGRAMACAO_CENTRAL\CURSO-IA\CONTEUDO_BAIXADO-20250208T003706Z-001\CONTEUDO_BAIXADO\Bases de dados-20240902T151609Z-001\Bases de dados\credit.pkl'

with open(path, 'rb') as f:
    X_credit_treinamento, y_credit_treinamento, X_credit_teste, y_credit_teste = pickle.load(f)


# print(X_credit_treinamento.shape, y_credit_treinamento.shape)
# print(X_credit_teste.shape, y_credit_teste.shape)

#Treinamento
naive_credit_data = GaussianNB()
naive_credit_data.fit(X_credit_treinamento, y_credit_treinamento)


#Dados corretos
# print(y_credit_teste)

#Tenta fazer a previsão
previsoes = naive_credit_data.predict(X_credit_teste)
# print(previsoes)

# print(accuracy_score(y_credit_teste, previsoes))
# print(confusion_matrix(y_credit_teste, previsoes))
cm = ConfusionMatrix(naive_credit_data)
cm.fit(X_credit_treinamento, y_credit_treinamento)

cm.score(X_credit_teste, y_credit_teste)



