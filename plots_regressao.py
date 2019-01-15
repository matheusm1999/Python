import seaborn as sns
%matplotlib inline

tips = sns.load_dataset('tips')
sns.lmplot(x='total_bill',y='tip',data = tips,hue = 'sex',markers=['o','v'],scatter_kws = {'s':100},col = 'sex', row = 'time' )
