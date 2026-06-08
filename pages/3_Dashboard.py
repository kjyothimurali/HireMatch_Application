import streamlit as st
import pandas as pd

from utils.history import (
    load_history
)

st.title(
    "📊 Dashboard"
)

df = load_history()

if df.empty:

    st.warning(
        "No analysis history available"
    )

else:

    st.subheader(
        "Analysis History"
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    st.subheader(
        "Average Match Score"
    )

    avg_score = round(
        df["Score"].mean(),
        2
    )

    st.metric(
        "Average Score",
        f"{avg_score}%"
    )

    st.subheader(
        "Score Distribution"
    )

    chart_df = pd.DataFrame(
        {
            "Score":
            df["Score"]
        }
    )

    st.bar_chart(
        chart_df
    )

    st.subheader(
        "Sector Distribution"
    )

    sector_counts = (
        df["Sector"]
        .value_counts()
    )

    st.bar_chart(
        sector_counts
    )