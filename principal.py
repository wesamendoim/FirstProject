import pandas as pd


def read_excel(*args):
  dtframe = pd.read_excel('Arquivo_Teste_Python.xlsb')
  print(dtframe)

read_excel()
