import pandas as pd
import numpy as np

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import (
    StandardScaler,
    OneHotEncoder
)

from src.utils.helpers import save_object


class DataTransformation:

    def get_data_transformer_object(self):

        numerical_columns = [
            "age",
            "studytime",
            "failures",
            "absences"
        ]

        categorical_columns = [
            "sex",
            "internet"
        ]

        num_pipeline = Pipeline(
            steps=[
                ("scaler", StandardScaler())
            ]
        )

        cat_pipeline = Pipeline(
            steps=[
                (
                    "one_hot_encoder",
                    OneHotEncoder()
                ),
                (
                    "scaler",
                    StandardScaler(with_mean=False)
                )
            ]
        )

        preprocessor = ColumnTransformer(
            [
                (
                    "num_pipeline",
                    num_pipeline,
                    numerical_columns
                ),
                (
                    "cat_pipeline",
                    cat_pipeline,
                    categorical_columns
                )
            ]
        )

        return preprocessor

    def initiate_data_transformation(
        self,
        train_path,
        test_path
    ):

        train_df = pd.read_csv(train_path)

        test_df = pd.read_csv(test_path)

        selected_columns = [
            "age",
            "studytime",
            "failures",
            "absences",
            "sex",
            "internet",
            "G3"
        ]

        train_df = train_df[selected_columns]

        test_df = test_df[selected_columns]

        target_column_name = "G3"

        preprocessing_obj = (
            self.get_data_transformer_object()
        )

        input_feature_train_df = train_df.drop(
            columns=[target_column_name]
        )

        target_feature_train_df = train_df[
            target_column_name
        ]

        input_feature_test_df = test_df.drop(
            columns=[target_column_name]
        )

        target_feature_test_df = test_df[
            target_column_name
        ]

        input_feature_train_arr = (
            preprocessing_obj.fit_transform(
                input_feature_train_df
            )
        )

        input_feature_test_arr = (
            preprocessing_obj.transform(
                input_feature_test_df
            )
        )

        train_arr = np.c_[
            input_feature_train_arr,
            np.array(target_feature_train_df)
        ]

        test_arr = np.c_[
            input_feature_test_arr,
            np.array(target_feature_test_df)
        ]

        save_object(
            file_path="artifacts/preprocessor.pkl",
            obj=preprocessing_obj
        )

        return (
            train_arr,
            test_arr
        )