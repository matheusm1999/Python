import pandas as pd

sal = pd.read_csv("C:/Users/Mathe/OneDrive/Documentos/LABI/Python/MachineLearning/Pandas/Salaries.csv")

#print(sal.head())

print('Todas as colunas:\n')
print(list(sal))

#Média de basepay
print("Média do pagamento: {:.2f}U$".format(sal['BasePay'].mean()))

#Maior valor de OvertimePay
print(sal['OvertimePay'].max())

#Cargo de Joseph Driscoll
print('\n')
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'])

#Quanto ganha Joseph Driscoll
print('\n')
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'])

print("\nPessoa mais bem paga")
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()])

print("\nPessoa menos bem paga: ")
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()])

print("\nMédia de basepay de todos os funcinários por ano (2011-2014): ")
print(sal.groupby('Year')['BasePay'].mean() )

print("\nTrabalhos que nao se repetem: ")
print(sal['JobTitle'].nunique())

print("\nEmpregos mais comuns: ")
print(sal['JobTitle'].value_counts().head())

print("Quantos titulos de trabalhos foram representados por uma pessoa em 2013")
print(sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts()==1))

#Quantas pessoas tem a palavra "chefe" no seu título de trabalhos

def chief_string(title):
    if 'chief' in title.lower():
        return True
    else:
        return False
print("\nQuantas pessoas tem a palavra  no seu título de trabalhos: ")
print(sum(sal['JobTitle'].apply(lambda x: chief_string(x))))


sal['Tamanho da String'] = sal['JobTitle'].apply(len)
print(sal[['Tamanho da String','TotalPayBenefits']].corr())
