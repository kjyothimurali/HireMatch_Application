import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

HISTORY_FILE = (
    BASE_DIR
    / "data"
    / "analysis_history.csv"
)


def create_history_file():

    if not HISTORY_FILE.exists():

        df = pd.DataFrame(
            columns=[
                "Type",
                "Sector",
                "Role",
                "Score"
            ]
        )

        df.to_csv(
            HISTORY_FILE,
            index=False
        )


def save_history(
    analysis_type,
    sector,
    role,
    score
):

    create_history_file()

    df = pd.read_csv(
        HISTORY_FILE
    )

    new_row = {

        "Type":
        analysis_type,

        "Sector":
        sector,

        "Role":
        role,

        "Score":
        score
    }

    df.loc[
        len(df)
    ] = new_row

    df.to_csv(
        HISTORY_FILE,
        index=False
    )


def load_history():

    create_history_file()

    return pd.read_csv(
        HISTORY_FILE
    )