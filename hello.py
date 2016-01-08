import os
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
app = Flask(__name__)

@app.route('/')
def hello():
    data = pd.read_csv('BudgetFood.csv')
    data = data.drop('Unnamed: 0', axis=1)
    graphData = data.head()
    return render_template('index.html', graphData=graphData.to_html())

if __name__ == '__main__':
    app.run(debug=True)
