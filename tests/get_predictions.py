import requests
import pickle


API_HOST = 'http://13.58.60.29:5000'
PREDICT_API = '/predict'
PREDICT_RAW_API = '/predict_raw'

Test_data = [{'bruises': 't',
  'cap-color': 'n',
  'cap-shape': 'x',
  'cap-surface': 's',
  'gill-attachment': 'f',
  'gill-color': 'k',
  'gill-size': 'n',
  'gill-spacing': 'c',
  'habitat': 'u',
  'odor': 'p',
  'population': 's',
  'ring-number': 'o',
  'ring-type': 'p',
  'spore-print-color': 'k',
  'stalk-color-above-ring': 'w',
  'stalk-color-below-ring': 'w',
  'stalk-root': 'e',
  'stalk-shape': 'e',
  'stalk-surface-above-ring': 's',
  'stalk-surface-below-ring': 's',
  'veil-color': 'w',
  'veil-type': 'p'},
 {'bruises': 't',
  'cap-color': 'y',
  'cap-shape': 'x',
  'cap-surface': 's',
  'gill-attachment': 'f',
  'gill-color': 'k',
  'gill-size': 'b',
  'gill-spacing': 'c',
  'habitat': 'g',
  'odor': 'a',
  'population': 'n',
  'ring-number': 'o',
  'ring-type': 'p',
  'spore-print-color': 'n',
  'stalk-color-above-ring': 'w',
  'stalk-color-below-ring': 'w',
  'stalk-root': 'c',
  'stalk-shape': 'e',
  'stalk-surface-above-ring': 's',
  'stalk-surface-below-ring': 's',
  'veil-color': 'w',
  'veil-type': 'p'}]

def load_data():
    data = pickle.load( open('mushroom_test_data', 'rb'))
    data = data.tolist()
    return data

def predict(passenger_data):
    print("Trying predict endpoint...")
    # Note that this is a POST request as we need to send the
    # passenger data to the server.
    # The requests library converts the passenger data into
    # JSON before sending it over. This is because the server
    # expects to receive the passenger data in the form of a JSON.
    r = requests.post(API_HOST + PREDICT_API,
                      json=passenger_data)

    # Also note that we're now using r.json(), not r.text.
    # This is because the server sends its response back as a
    # JSON object, which needs to be decoded by the requests
    
    if r.status_code == 200:
        print("Success!")
        print(r.json())
    else:
        print("Status code indicates a problem:", r.status_code)


def predict_raw(raw_data):
    print("Trying predict_raw endpoint...")
    # Note that this is a POST request as we need to send the
    # passenger data to the server.
    # The requests library converts the passenger data into
    # JSON before sending it over. This is because the server
    # expects to receive the passenger data in the form of a JSON.
    r = requests.post(API_HOST + PREDICT_RAW_API,
                      json=raw_data)

    # Also note that we're now using r.json(), not r.text.
    # This is because the server sends its response back as a
    # JSON object, which needs to be decoded by the requests
    
    if r.status_code == 200:
        print("Success!")
        print(r.json())
    else:
        print("Status code indicates a problem:", r.status_code)



def main():
    predict(load_data())
    predict_raw(Test_data)

# Entry point for application (i.e. program starts here)
if __name__ == '__main__':
    main()