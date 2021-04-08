from sklearn.datasets import load_iris

iris = load_iris()
features = iris.data.T

sepal_length = features[0]
sepal_width = features[1]
petal_length = features[2]
petal_width = features[3]

sepal_length_label = iris.feature_names[0]
sepal_width_label = iris.feature_names[1]
petal_length_label = iris.feature_names[2]
petal_width_label = iris.feature_names[3]


class Table:
    def __init__(self, name, *columns):
        self.name = name
        self.columns = [columns]

    def __setattr__(self, name, value):
        pass


iris_class = Table("iris_table", petal_width, petal_length, sepal_width, sepal_length)


print(iris_class.petal_width.__dict__)