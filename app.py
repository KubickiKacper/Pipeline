from flask import Flask,render_template
import numpy as np
from matplotlib import pyplot as plt

app = Flask(__name__)


@app.route('/')
def home():
    x=[]
    y=[]
    for i in range(100):
        x.append(i)
        y.append(np.random.randint(1,100))

    plt.figure()
    plt.plot(x, y)
    plt.savefig('static/css/picture.png')

    picture = 'static/css/picture.png'
    return render_template('view.html',picture=picture)


if __name__ == '__main__':
    app.run(debug=True)
