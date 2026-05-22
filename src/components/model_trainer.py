from sklearn.linear_model import LinearRegression

from sklearn.tree import (
    DecisionTreeRegressor
)

from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor
)

from src.utils.helpers import (
    save_object,
    evaluate_models
)


class ModelTrainer:

    def initiate_model_trainer(
        self,
        train_array,
        test_array
    ):

        X_train = train_array[:, :-1]

        y_train = train_array[:, -1]

        X_test = test_array[:, :-1]

        y_test = test_array[:, -1]

        models = {

            "Linear Regression":
            LinearRegression(),

            "Decision Tree":
            DecisionTreeRegressor(),

            "Random Forest":
            RandomForestRegressor(),

            "Gradient Boosting":
            GradientBoostingRegressor()

        }

        model_report = evaluate_models(
            X_train,
            y_train,
            X_test,
            y_test,
            models
        )

        best_model_score = max(
            sorted(model_report.values())
        )

        best_model_name = list(
            model_report.keys()
        )[
            list(model_report.values()).index(
                best_model_score
            )
        ]

        best_model = models[best_model_name]

        print(
            "Best Model Found :",
            best_model_name
        )

        print(
            "R2 Score :",
            best_model_score
        )

        save_object(
            file_path="artifacts/model.pkl",
            obj=best_model
        )

        return best_model_score