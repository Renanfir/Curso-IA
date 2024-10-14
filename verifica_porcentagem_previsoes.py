import pickle

from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.naive_bayes import GaussianNB
from yellowbrick.classifier import ConfusionMatrix


path = 'C:\\Users\\Usuario\\PROGRAMACAO_CENTRAL\\python\\outros\\CURSO_IA\\CONTEUDO_BAIXADO\\Bases de dados-20240902T151609Z-001\\Bases de dados\\credit.pkl'
with open(path, 'rb') as f:
    X_credit_treinamento, Y_credit_treinamento, X_credit_teste, Y_credit_teste = pickle.load(f)

naive_credit_data = GaussianNB()
naive_credit_data.fit(X_credit_treinamento, Y_credit_treinamento)

previsoes = naive_credit_data.predict(X_credit_teste)


print(accuracy_score(Y_credit_teste, previsoes))
print(confusion_matrix(Y_credit_teste, previsoes))

cm = ConfusionMatrix(naive_credit_data)
cm.fit(X_credit_treinamento, Y_credit_treinamento)
cm.score(X_credit_teste, Y_credit_teste)
cm.show()

