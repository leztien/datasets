import sklearn.datasets, sklearn.cluster, sklearn.metrics

bunch = sklearn.datasets.load_digits()
pn = bunch.images
X = bunch.data
y = bunch.target
classes = bunch.target_names
