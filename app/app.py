"""Streamlit application for YouTube ad revenue prediction."""

from pathlib import Path
import sys

import joblib
import pandas as pd
import plotly.express as px
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "src"))

from prediction import advisor_messages, performance_score, predict_revenue


DATA_PATH = ROOT / "data" / "processed" / "cleaned_youtube_revenue.csv"
RAW_DATA_PATH = ROOT / "data" / "raw" / "youtube_ad_revenue_dataset.csv"
MODEL_PATH = ROOT / "models" / "best_model.pkl"
COMPARISON_PATH = ROOT / "reports" / "results" / "model_comparison.csv"
IMPORTANCE_PATH = ROOT / "reports" / "results" / "feature_importance.csv"


st.set_page_config(page_title="Content Monetization Modeler", layout="wide")


@st.cache_data
def load_data():
    path = DATA_PATH if DATA_PATH.exists() else RAW_DATA_PATH
    return pd.read_csv(path)


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


def metric_cards(df):
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Videos", f"{len(df):,}")
    c2.metric("Avg Revenue", f"${df['ad_revenue_usd'].mean():,.2f}")
    c3.metric("Avg Views", f"{df['views'].mean():,.0f}")
    c4.metric("Categories", df["category"].nunique())


def collect_prediction_inputs(df):
    col1, col2, col3 = st.columns(3)
    with col1:
        views = st.number_input("Views", 1, 10_000_000, int(df["views"].median()), step=100)
        likes = st.number_input("Likes", 0, 1_000_000, int(df["likes"].median()), step=10)
        comments = st.number_input("Comments", 0, 500_000, int(df["comments"].median()), step=5)
    with col2:
        watch_time = st.number_input(
            "Watch Time Minutes", 1.0, 10_000_000.0, float(df["watch_time_minutes"].median()), step=100.0
        )
        video_length = st.number_input(
            "Video Length Minutes", 0.5, 300.0, float(df["video_length_minutes"].median()), step=0.5
        )
        subscribers = st.number_input(
            "Subscribers", 1, 50_000_000, int(df["subscribers"].median()), step=1000
        )
    with col3:
        category = st.selectbox("Category", sorted(df["category"].unique()))
        device = st.selectbox("Device", sorted(df["device"].unique()))
        country = st.selectbox("Country", sorted(df["country"].unique()))

    return {
        "video_id": "user_input",
        "date": pd.Timestamp.today(),
        "views": views,
        "likes": likes,
        "comments": comments,
        "watch_time_minutes": watch_time,
        "video_length_minutes": video_length,
        "subscribers": subscribers,
        "category": category,
        "device": device,
        "country": country,
        "ad_revenue_usd": 0,
    }


def page_overview(df):
    st.title("Content Monetization Modeler")
    metric_cards(df)
    st.subheader("Project Workflow")
    st.write(
        "Dataset -> EDA -> Cleaning -> Feature Engineering -> Model Training -> Model Comparison -> Streamlit Prediction -> Render Deployment"
    )
    st.dataframe(df.head(10), width="stretch")


def page_prediction(df):
    st.title("Revenue Prediction")
    model = load_model()
    input_data = collect_prediction_inputs(df)
    predicted = predict_revenue(model, input_data)
    score = performance_score(predicted, df["ad_revenue_usd"].quantile(0.90))
    c1, c2 = st.columns(2)
    c1.metric("Predicted Revenue", f"${predicted:,.2f}")
    c2.metric("Revenue Performance Score", f"{score}/100")
    st.progress(score / 100)


def page_eda(df):
    st.title("EDA Dashboard")
    metric_cards(df)
    c1, c2 = st.columns(2)
    c1.plotly_chart(px.histogram(df, x="ad_revenue_usd", nbins=50, title="Revenue Distribution"), width="stretch")
    c2.plotly_chart(px.scatter(df.sample(min(4000, len(df)), random_state=42), x="engagement_rate", y="ad_revenue_usd", color="category", title="Engagement vs Revenue"), width="stretch")
    c3, c4, c5 = st.columns(3)
    c3.plotly_chart(px.bar(df.groupby("category", as_index=False)["ad_revenue_usd"].mean(), x="category", y="ad_revenue_usd", title="Category Analysis"), width="stretch")
    c4.plotly_chart(px.bar(df.groupby("device", as_index=False)["ad_revenue_usd"].mean(), x="device", y="ad_revenue_usd", title="Device Analysis"), width="stretch")
    c5.plotly_chart(px.bar(df.groupby("country", as_index=False)["ad_revenue_usd"].mean(), x="country", y="ad_revenue_usd", title="Country Analysis"), width="stretch")


def page_model_comparison():
    st.title("Model Comparison")
    comparison = pd.read_csv(COMPARISON_PATH)
    st.dataframe(comparison, width="stretch")
    st.plotly_chart(px.bar(comparison, x="Model", y="R2 Score", title="R2 Score Ranking"), width="stretch")
    if IMPORTANCE_PATH.exists():
        importance = pd.read_csv(IMPORTANCE_PATH).head(15)
        st.plotly_chart(px.bar(importance, x="importance", y="feature", orientation="h", title="Top Revenue Drivers"), width="stretch")


def page_insights(df):
    st.title("Business Insights")
    top_category = df.groupby("category")["ad_revenue_usd"].mean().sort_values(ascending=False)
    top_device = df.groupby("device")["ad_revenue_usd"].mean().sort_values(ascending=False)
    top_country = df.groupby("country")["ad_revenue_usd"].mean().sort_values(ascending=False)
    insights = [
        f"{top_category.index[0]} is the highest earning category on average.",
        f"{top_device.index[0]} is the highest earning device segment.",
        f"{top_country.index[0]} is the strongest country segment.",
        "Engagement rate combines likes and comments, so it is better than looking at likes alone.",
        "Watch time supports revenue because more attention usually gives more monetization opportunity.",
        "Subscriber engagement is useful because a large subscriber count is not enough without activity.",
        "The what-if simulator can guide creators before publishing or promoting a video.",
        "Category leaderboard helps plan future content topics.",
    ]
    for item in insights:
        st.write(f"- {item}")


def page_advisor(df):
    st.title("Revenue Optimization Advisor")
    model = load_model()
    input_data = collect_prediction_inputs(df)
    predicted = predict_revenue(model, input_data)
    st.metric("Current Prediction", f"${predicted:,.2f}")
    st.subheader("Recommendations")
    for message in advisor_messages(input_data, predicted):
        st.info(message)


def main():
    df = load_data()
    page = st.sidebar.radio(
        "Pages",
        [
            "Revenue Prediction",
            "EDA Dashboard",
            "Model Comparison",
            "Revenue Optimization Advisor",
        ],
    )

    if page == "Revenue Prediction":
        page_prediction(df)
    elif page == "EDA Dashboard":
        page_eda(df)
    elif page == "Model Comparison":
        page_model_comparison()
    elif page == "Revenue Optimization Advisor":
        page_advisor(df)


if __name__ == "__main__":
    main()
