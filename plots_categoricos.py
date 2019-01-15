#%matplotlib inline
import seaborn as sns
import numpy as np

tips = sns.load_dataset('tips')

#fomra de plotar os dados
sns.barplot(x='sex',y='total_bill',data=tips)

sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std)


sns.countplot(x='sex',data=tips)


#Vejo como os meus dados estão destribuidos
sns.violinplot(x='day',y='tip',data=tips,hue='sex',split=True)

#jitter mostra uma densidade melhor do gráfico.
sns.stripplot(x='day',y='total_bill',data=tips,jitter=True,hue='sex',dodge=True)


#combinando o swarm com o violin
sns.swarmplot(x='day',y='total_bill',data=tips,color='black')
sns.violinplot(x='day',y='total_bill',data=tips)
