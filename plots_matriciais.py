import seaborn as sns
%matplotlib inline

flights = sns.load_dataset('flights')
tips = sns.load_dataset('tips')

crr = tips.corr()
sns.heatmap(crr,cmap='coolwarm',annot=True)


#crio uma tabela Mostrando quantos passageiro(values) houveram naquele mes (index), por ano (coluna)
pf = flights.pivot_table(values = 'passengers',index = 'month',columns='year')


sns.heatmap(pf,cmap = 'magma',linecolor='white',linewidths = 1)
