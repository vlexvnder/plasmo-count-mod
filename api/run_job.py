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



def run(cutoffs = [1.5, 2.5]):
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


    files = ["./tmp/test.png", "./tmp/F152-day8-ZT0.png", "./tmp/F101-day8-ZT0.png", "./tmp/F107-day7-ZT12.png"]

    # start analysis
    results = []
    for i, filename in enumerate(files):
        img = model.load_image(filename)
        pred = model.predict(job['has-gams'])
        print(pred)
        result = Result(str(i), filename, img, pred)
        result.plot_prediction(name=str(cutoffs[0]), dir = filename.split("/")[-1][:-3])
        results.append(result.to_output())
        print(results)
    output = {
        'data': {
            'results': results,
            'summary': summarize(results)
        },
        'statusOK': True
    }

    return output

test_cutoffs = [1, 1.04, 1.1, 1.3, 1.5, 1.7]
for t in test_cutoffs:
    print(run(cutoffs= [t, 2.5]))