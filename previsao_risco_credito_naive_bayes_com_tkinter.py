import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
import pickle
import tkinter as tk
from tkinter import ttk

def verifica_risco_credito(historico, divida, garantia, renda):
    path = 'C:\\Users\\Usuario\\PROGRAMACAO_CENTRAL\\python\\outros\\CURSO_IA\\CONTEUDO_BAIXADO\\Bases de dados-20240902T151609Z-001\\Bases de dados\\risco_credito.csv'
    base_risco_credito = pd.read_csv(path)


    X_risco_credito = base_risco_credito.iloc[:,0:4].values
    Y_risco_credito = base_risco_credito.iloc[:,4].values


    label_encoder_historia = LabelEncoder()
    label_encoder_divida = LabelEncoder()
    label_encoder_garantia = LabelEncoder()
    label_encoder_renda = LabelEncoder()


    #TRANSFORMA VALORES STRING EM VALORES INT, PARA ADICIONAR PESOS PARA OS VALORES.
    X_risco_credito[:,0] = label_encoder_historia.fit_transform(X_risco_credito[:,0])
    X_risco_credito[:,1] = label_encoder_divida.fit_transform(X_risco_credito[:,1])
    X_risco_credito[:,2] = label_encoder_garantia.fit_transform(X_risco_credito[:,2])
    X_risco_credito[:,3] = label_encoder_renda.fit_transform(X_risco_credito[:,3])

    # with open("risco_credito.pkl", 'wb') as f:
    #     pickle.dump([X_risco_credito, Y_risco_credito],f)

    naive_risco_credito = GaussianNB()
    naive_risco_credito.fit(X_risco_credito, Y_risco_credito)

    previsao = naive_risco_credito.predict([[historico,divida,garantia,renda]])

    return previsao


def verifica_tipos(historico, divida, garantia, renda):
    #historico: boa(0), desconhecida(1), ruim(2)
    #divida: alta(0), baixa(1)
    #garantia: adequada(0), nenhuma(1)
    #renda: <15(0), entre 15 e 35(1), maior 35(2)


    #verifica tipo historico
    if historico == 'Ruim':
        historico = 2
    elif historico == 'Boa':
        historico = 0
    else:
        historico = 1

    #verifica tipo divida
    if divida == 'Alta':
        divida = 0
    else:
        divida = 1

    #verifica tipo garantia
    if garantia == 'Adequada':
        garantia = 0
    else:
        garantia = 1

    #verifica tipo renda
    if renda == 'Menor do que 15':
        renda = 0
    elif renda == 'Entre 15 e 35':
        renda = 1
    else:
        renda = 2

    return historico, divida, garantia, renda
    





def apresenta_risco_credito():
    historico = combo1.get()
    divida = combo2.get()
    garantia = combo3.get()
    renda = combo4.get()

    dados = verifica_tipos(historico, divida, garantia, renda)
    
    # Obtém a previsão e atualiza o label
    resultado = verifica_risco_credito(dados[0], dados[1], dados[2], dados[3])
    
    # Atualiza o texto do labelResultado com o resultado
    labelResultado.config(text=f"O risco de crédito a esse cliente é: {resultado}")




janela = tk.Tk()
janela.title("Formulário Risco de Crédito")

# Criação dos labels e comboboxes
label1 = tk.Label(janela, text="Selecione o histórico do cliente:")
label1.pack()
combo1 = ttk.Combobox(janela, values=["Ruim", "Boa", "Desconhecida"])
combo1.pack()

label2 = tk.Label(janela, text="Selecione a dívida do cliente:")
label2.pack()
combo2 = ttk.Combobox(janela, values=["Alta", "Baixa"])
combo2.pack()

label3 = tk.Label(janela, text="Selecione a garantia do cliente:")
label3.pack()
combo3 = ttk.Combobox(janela, values=["Nenhuma", "Adequada"])
combo3.pack()

label4 = tk.Label(janela, text="Selecione a renda do cliente:")
label4.pack()
combo4 = ttk.Combobox(janela, values=["Menor do que 15", "Entre 15 e 35", "Maior do que 35"])
combo4.pack()

# Criação do botão que chama sua função
botao_enviar = tk.Button(janela, text="Enviar", command=apresenta_risco_credito)
botao_enviar.pack()

# Label para exibir o resultado
labelResultado = tk.Label(janela, text="O risco de crédito a esse cliente é: ")
labelResultado.pack()

# Inicia o loop da aplicação
janela.mainloop()



