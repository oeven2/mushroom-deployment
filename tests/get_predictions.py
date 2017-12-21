import requests
import pickle


API_HOST = 'http://13.58.60.29:5000'
PREDICT_API = '/predict'

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


def main():
    predict(load_data())

# Entry point for application (i.e. program starts here)
if __name__ == '__main__':
    main()