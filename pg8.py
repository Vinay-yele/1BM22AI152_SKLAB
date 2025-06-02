import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
iris = load_iris()
X = StandardScaler().fit_transform(iris.data)
kmeans = KMeans(n_clusters=3).fit(X)
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['True Class'] = [iris.target_names[i] for i in iris.target]
df['Cluster'] = kmeans.labels_
print(df.head())
print("\nCluster distribution:")
print(df[['True Class', 'Cluster']].value_counts())
plt.figure(figsize=(10, 6))
colors = ['red', 'green', 'blue']
for i in range(3):
    plt.scatter(X[df['Cluster']==i, 0], X[df['Cluster']==i, 1],
                c=colors[i], label=f'Cluster {i}')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.title('K-means Clustering of Iris Dataset')
plt.legend()
plt.show()