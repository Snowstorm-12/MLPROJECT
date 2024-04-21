# Writing API.
from flask import Flask, request, jsonify
import config
from Project.utils import MedicalInsurance
import numpy as np

app  = Flask(__name__)

@app.route('/')
def get_home():
    return 'Hey There!'


@app.route('/predict_charges', methods = ['POST', 'GET'])
# While testing we can use GET Method. POST is Secured Method, while GET is not.

def get_insurance():
    if request.method == 'POST':
        data = request.form
         # Form will have key and values of features that stores data given by the User.
        print('User Input data is: ', data)

        age = eval(data['age'])
        gender = data['gender']
        bmi = eval(data['bmi'])
        children = int(data['children'])
        smoker = data['smoker']
        region = data['region']

        med_obj = MedicalInsurance(age, gender, bmi, children, smoker, region)
        charges = med_obj.get_predict_charges()

        return jsonify({'Result':f'Predicted Medical Insurance Premium Charges for given data is:{charges[0]}'})


if __name__ == '__main__':
    app.run()



