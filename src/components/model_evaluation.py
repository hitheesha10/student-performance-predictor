import numpy as np

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


class ModelEvaluation:

    def evaluate_model(
        self,
        y_test,
        y_pred
    ):

        mae = mean_absolute_error(
            y_test,
            y_pred
        )

        mse = mean_squared_error(
            y_test,
            y_pred
        )

        rmse = np.sqrt(mse)

        r2 = r2_score(
            y_test,
            y_pred
        )

        return {

            "MAE": mae,

            "MSE": mse,

            "RMSE": rmse,

            "R2 Score": r2
        }