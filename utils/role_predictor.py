import pandas as pd
import re

from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "final_dataset_small.csv"

df = pd.read_csv(DATA_PATH)


def clean_title(title):

    title = str(title).lower()

    title = re.sub(
        r'[^a-zA-Z ]',
        ' ',
        title
    )

    title = re.sub(
        r'\s+',
        ' ',
        title
    ).strip()

    return title


df["Title"] = df["Title"].apply(
    clean_title
)

vectorizer = TfidfVectorizer(
    max_features=5000,
    stop_words="english"
)

vectorizer.fit(df["text"])


def shorten_title(title):

    words = title.split()

    if "human" in words and "assistant" in words:
        return "Human Resources Assistant"

    return " ".join(words[:5]).title()


def predict_role(
    input_text,
    sector
):

    sector_df = df[
        df["sector"] == sector
    ]

    if sector_df.empty:

        return (
            "Unknown",
            0.0
        )

    input_vec = vectorizer.transform(
        [input_text]
    )

    dataset_vec = vectorizer.transform(
        sector_df["text"]
    )

    similarity = cosine_similarity(
        input_vec,
        dataset_vec
    )

    idx = similarity.argmax()

    score = float(
        similarity[0][idx]
    )

    role = shorten_title(
        sector_df.iloc[idx]["Title"]
    )

    return role, score