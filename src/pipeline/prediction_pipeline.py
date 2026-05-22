import pandas as pd

from src.utils.helpers import load_object


class PredictionPipeline:

    def predict(self, features):

        model_path = "artifacts/model.pkl"

        preprocessor_path = (
            "artifacts/preprocessor.pkl"
        )

        model = load_object(model_path)

        preprocessor = load_object(
            preprocessor_path
        )

        data_scaled = preprocessor.transform(
            features
        )

        preds = model.predict(data_scaled)

        return preds


class CustomData:

    def __init__(
        self,
        age,
        studytime,
        failures,
        absences,
        sex,
        internet
    ):

        self.age = age

        self.studytime = studytime

        self.failures = failures

        self.absences = absences

        self.sex = sex

        self.internet = internet

    def get_data_as_dataframe(self):

        custom_data_input_dict = {

            "age": [self.age],

            "studytime": [self.studytime],

            "failures": [self.failures],

            "absences": [self.absences],

            "sex": [self.sex],

            "internet": [self.internet]
        }

        return pd.DataFrame(
            custom_data_input_dict
        )