import pandas as pd
from sklearn.linear_model import SGDClassifier

MODEL_DIRECTORY = 'models'
MODEL_FILE_NAME = '%s/mushroom_model.pkl' % MODEL_DIRECTORY


def predict(input_df, model):
    import numpy as np
    input_array = np.array(input_df)
    predictions = model.predict(input_array)
    return predictions.tolist()


    




