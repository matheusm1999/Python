import numpy as np
import pandas as pd

df = pd.read_csv('C:/Users/mathe/OneDrive/Documentos/LABI/Python/CursoML/Pandas/exemplo.csv',sep=',')
print(df)
df = df+1
df.to_csv('exemplo.csv',sep=';',decimal=',')

df = pd.read_excel('C:/Users/mathe/OneDrive/Documentos/LABI/Python/CursoML/Pandas/Exemplo_Excel.xlsx',sheet_name = 'Sheet1')
#com o meu sheetname = sheet1 , defino qual aba eu quero ler

#Exportando o arquivo
df.to_excel("exemplo.xlsx",sheet_name = 'Sheet1')

#Pegando os dados de uma url
