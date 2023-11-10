import os

from collections import defaultdict
from pathlib import Path
import matplotlib
import warnings
import json
import datetime
matplotlib.use('Agg')
warnings.filterwarnings('ignore')

from programs.model import Model
from programs.result import Result
from programs.summarize import summarize

import pandas as pd



def run(dir, cutoffs = [1.5, 2.5], input = "input/", output = "output/"):
    job = {
        'id': 1,
        'date': 1,
        'email-address': 1,
        'has-gams': False,
        'data-contrib': False,
        'cut-offs': [1.5, 2.5],
        'files': defaultdict()
    }

    model = Model(cutoffs=cutoffs)


    files = os.listdir(dir + input)

    # start analysis
    results = []
    for i, filename in enumerate(files):
        filename = dir + input + filename
        img = model.load_image(filename)
        pred = model.predict(job['has-gams'])
        print(pred)
        result = Result(str(i), filename, img, pred)
        result.plot_prediction(name=filename.split("/")[-1][:-4])
        results.append(result.to_output())
        print(results)

    df = pd.DataFrame(results)
    df.to_csv(dir + output + "results.csv")
    output = {
        'data': {
            'results': results,
            'summary': summarize(results)
        },
        'statusOK': True
    }

    return output

print(run("./tmp/"))