import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

iris = sns.load_dataset('iris')
iris.head()

iris['species'].value_counts()

g = sns.PairGrid(iris)
#g.map(plt.scatter)
g.map_diag(plt.hist)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)

sns.pairplot(iris, hue = 'species')
