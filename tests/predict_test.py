import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from sklearn.model_selection import train_test_split
import numpy as np

df = pd.read_csv("logs_100.csv")

#時間を数値に変換
# Convert end_time to float
def convert_time_to_float(time_str):
    h, m = map(int, time_str.split(":"))
    return h + m / 60

df["end_time_float"] = df["end_time"].apply(convert_time_to_float)

# Define X and y
X = df[["today_schedule", "start_location", "category", "end_time_float"]]
y = df["selected_subgenre"]

# Preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ("tfidf", TfidfVectorizer(), ["today_schedule","start_location"]),
        ("ohe", OneHotEncoder(), ["category"]),
        ("time", FunctionTransformer(lambda x: x.values.reshape(-1, 1)), "end_time_float")
    ],
    remainder="drop"
)

# Transform the features
X_transformed = preprocessor.fit_transform(X)

# Show shape of final feature matrix and first 5 feature names
feature_names = (
    preprocessor.named_transformers_["tfidf"].get_feature_names_out().tolist()
    + preprocessor.named_transformers_["ohe"].get_feature_names_out(["start_location", "category"]).tolist()
    + ["end_time_float"]
)

X_transformed.shape, feature_names[:5]