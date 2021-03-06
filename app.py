from flask import Flask, render_template, request
import numpy as np
import joblib

# create instance of flask
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route('/predict/', methods=['GET', 'POST'])
def predict():
    if request.method == "POST":

        # get form data
        sepal_length = request.form.get('sepal_length')
        sepal_width = request.form.get('sepal_width')
        petal_length = request.form.get('petal_length')
        petal_width = request.form.get('petal_width')

        # call preprocessDataAndPredict and pass inputs
        try:
            prediction = preprocessDataAndPredict(sepal_length,
                                                  sepal_width,
                                                  petal_length,
                                                  petal_width)
            # pass prediction to template
            return render_template('predict.html', prediction=prediction)

        except ValueError:

            return "Please enter valid values"

        pass
    pass


def preprocessDataAndPredict(sepal_length, sepal_width, petal_length, petal_width):

    # keep all inputs in array
    test_data = [sepal_length, sepal_width, petal_length, petal_width]
    # print(test_data)

    # convert value data into numpy array
    test_data = np.array(test_data)

    # reshape array
    test_data = test_data.reshape(1, -1)
    # print(test_data)

    # assign path to model
    model_folder = '../output/'
    path = model_folder + 'randomforest_model.pkl'

    # open file
    file = open(path, "rb")

    # load trained model
    trained_model = joblib.load(file)

    # predict
    prediction = trained_model.predict(test_data)
    print(prediction)
    return prediction


if __name__ == '__main__':
    app.run(debug=True)
