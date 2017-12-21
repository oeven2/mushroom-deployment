import pandas as pd
from sklearn.linear_model import SGDClassifier
import numpy as np

MODEL_DIRECTORY = 'models'
MODEL_FILE_NAME = '%s/mushroom_model.pkl' % MODEL_DIRECTORY


def predict(input_df, model):
    import numpy as np
    input_array = np.array(input_df)
    predictions = model.predict(input_array)
    return predictions.tolist()

def predict_raw(input_df, model):
	input_df['stalk-root'] = input_df['stalk-root'].\
	apply(lambda x: None if x == '?' else x)
	input_df = input_df.dropna(subset = ['stalk-root'])
	input_df = input_df.apply(lambda x: pd.factorize(x)[0]+1)
	input_array = np.array(input_df)
	predictions = model.predict(input_array)
	return predictions.tolist()
    




