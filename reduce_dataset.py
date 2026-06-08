import pandas as pd

df = pd.read_csv("data/final_dataset.csv")

df = df[["Title", "text", "sector"]]

df = df.drop_duplicates()

df.to_csv(
    "data/final_dataset_small.csv",
    index=False
)

print("Original shape:", df.shape)