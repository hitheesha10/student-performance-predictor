import os
import pandas as pd

from sklearn.model_selection import train_test_split


class DataIngestion:

    def initiate_data_ingestion(self):

        df = pd.read_csv(
            "data/student-mat.csv",
            sep=";"
        )

        os.makedirs("artifacts", exist_ok=True)

        train_set, test_set = train_test_split(
            df,
            test_size=0.2,
            random_state=42
        )

        train_path = "artifacts/train.csv"

        test_path = "artifacts/test.csv"

        train_set.to_csv(
            train_path,
            index=False
        )

        test_set.to_csv(
            test_path,
            index=False
        )

        return (
            train_path,
            test_path
        )