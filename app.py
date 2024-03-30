from flask import Flask, request, render_template
import os
import numpy as np
import pandas as pd
from wineQuality.pipeline.stage_06_prediction import PredictionPipeline

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return render_template("index.html")