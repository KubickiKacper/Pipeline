from flask import Flask,render_template
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier

app = Flask(__name__)

@app.route('/')
def home():
    iris=load_iris()
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7, random_state=0)
    #GNB
    GNB = GaussianNB()
    y_pred = GNB.fit(X_train, y_train).predict(X_test)
    GNBsum=(y_test != y_pred).sum()

    #KNC
    KNC=KNeighborsClassifier(3)
    y_pred = KNC.fit(X_train, y_train).predict(X_test)
    KNCsum = (y_test != y_pred).sum()

    #MLP
    MLPC=MLPClassifier(alpha=1, max_iter=1000)
    y_pred = MLPC.fit(X_train, y_train).predict(X_test)
    MLPCsum = (y_test != y_pred).sum()

    return render_template('view.html', len=len(iris.data), iris=iris,GNBXtestshape=X_test.shape[0],
                           GNBsum=GNBsum, KNCsum=KNCsum,MLPCsum=MLPCsum)


if __name__ == '__main__':
    app.run(debug=True)
