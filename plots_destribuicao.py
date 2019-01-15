#%matplotlib inline
import seaborn as sns

tips = sns.load_dataset('tips')


print(tips.head())

#criando um histograma
sns.distplot(tips['total_bill'])

sns.jointplot(x='total_bill',y='tip',data=tips,kind ='hex')

sns.pairplot(tips, hue ='sex',palette = 'coolwarm')
