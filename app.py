# ==============================================================================
# Executive Command Interface: Fully Integrated Master Cloud SaaS Application
# Implementation: Decoupled Logic Workflow, Cyberspace UX & Telemetry Serialization
# ==============================================================================
import sys
import os
import re
import random
from datetime import datetime, timedelta
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import nltk
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from tweetclaw_import import build_dashboard_rows, load_tweetclaw_records

# Inject Absolute Workspace Path Booster to guarantee Cloud Module Resolution
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# ------------------------------------------------------------------------------
# ENTERPRISE NLP ENGINE TIER (Safely Encapsulated Runtime)
# ------------------------------------------------------------------------------
# Safely resolve NLTK emotional lexical vocabularies during cloud container boot
try:
    sia = SentimentIntensityAnalyzer()
except LookupError:
    nltk.download('vader_lexicon', quiet=True)
    sia = SentimentIntensityAnalyzer()

def execute_text_sanitization(raw_text: str) -> str:
    """Purges broken URLs, metadata (@), and network noise while preserving emojis."""
    cleaned = re.sub(r"http\S+|www\S+|https\S+", "", raw_text, flags=re.MULTILINE)
    cleaned = re.sub(r"\@\w+", "", cleaned)
    cleaned = re.sub(r"^RT[\s]+", "", cleaned)
    cleaned = re.sub(r"[^\w\s\d\.\,\!\?]", "", cleaned)
    return cleaned.strip()

def evaluate_semantic_polarity(raw_tweet: str) -> dict:
    """Executes multi-lexicon evaluation (NLTK VADER & TextBlob)."""
    clean_text = execute_text_sanitization(raw_tweet)
    if not clean_text:
        return {"Cleaned Tweet": raw_tweet, "Mood": "Neutral 😐", "Score": 0.0, "Polarity": 0.0}
        
    scores = sia.polarity_scores(clean_text)
    compound = scores['compound']
    
    if compound >= 0.05:
        category = "Positive 😃"
    elif compound <= -0.05:
        category = "Negative 😡"
    else:
        category = "Neutral 😐"

    blob = TextBlob(clean_text)
    return {
        "Cleaned Tweet": clean_text,
        "Mood": category,
        "Score": compound,
        "Polarity": blob.sentiment.polarity
    }

def collect_synthetic_telemetry(keyword: str, total_count: int) -> pd.DataFrame:
    """Synthesizes high-velocity client telemetry analyzing any entity."""
    happy_phrases = [
        f"Absolutely blown away by the incredible features of {keyword}! It is brilliant. 🔥",
        f"I highly recommend {keyword} to every developer out there. Huge success! 🚀",
        f"The performance and security of {keyword} in 2026 is top tier. 10/10!",
        f"Loving the beautiful design updates in {keyword}. Amazing customer support! 🌟",
        f"My team just migrated all our infrastructure to {keyword}. Extremely happy!"
    ]
    angry_phrases = [
        f"Terrible production bugs in {keyword} today. Horrible experience overall. 😡",
        f"Why is {keyword} so overpriced and constantly crashing? Very frustrated.",
        f"Complete waste of time. Do not install the latest update of {keyword}! 📉",
        f"Extremely disappointed with {keyword}'s performance. Horrible lag.",
        f"{keyword} completely deleted my saved settings. Completely unacceptable! 🤦‍♂️"
    ]
    plain_phrases = [
        f"Here is a technical documentation overview discussing the architecture of {keyword}.",
        f"Anybody else currently building a complete portfolio analyzing {keyword}?",
        f"Live tech news: {keyword} officially rolled out security patch v3.2 this morning.",
        f"An unbiased technical review exploring the explicit pros and cons of {keyword}.",
        f"Comparing the market share benchmarks of {keyword} against its competitors."
    ]

    raw_dataset = []
    now = datetime.now()
    for _ in range(total_count):
        post_time = now - timedelta(minutes=random.randint(1, 180))
        prob = random.random()
        if prob < 0.44:
            text = random.choice(happy_phrases)
        elif prob < 0.74:
            text = random.choice(angry_phrases)
        else:
            text = random.choice(plain_phrases)
            
        ai_output = evaluate_semantic_polarity(text)
        raw_dataset.append({
            "Timestamp": post_time.strftime("%Y-%m-%d %H:%M:%S"),
            "Raw Tweet": text,
            "Cleaned Tweet": ai_output["Cleaned Tweet"],
            "Sentiment Tag": ai_output["Mood"],
            "VADER Score": round(ai_output["Score"], 3),
            "TextBlob Polarity": round(ai_output["Polarity"], 3),
            "Likes": random.randint(15, 2500),
            "Retweets": random.randint(1, 350)
        })
        
    df = pd.DataFrame(raw_dataset)
    df = df.sort_values(by="Timestamp", ascending=False).reset_index(drop=True)
    return df

# ------------------------------------------------------------------------------
# CYBER-SAAS FRONTEND UI WORKSPACE
# ------------------------------------------------------------------------------
st.set_page_config(page_title="Executive Twitter AI Dashboard", page_icon="⚡", layout="wide")

st.markdown("""
<style>
    .glow-card {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        padding: 26px;
        border-radius: 14px;
        text-align: center;
        box-shadow: 0 8px 20px -4px rgba(0, 0, 0, 0.6);
        border: 1px solid #334155;
        color: white;
    }
    .glow-title { font-size: 13px; text-transform: uppercase; color: #94a3b8; font-weight: 800; letter-spacing: 1.5px; }
    .glow-val { font-size: 40px; font-weight: 900; margin-top: 10px; color: #38bdf8; }
</style>
""", unsafe_allow_html=True)

st.title("⚡ Real-Time Twitter/X Modular AI Sentiment Engine")
st.markdown("A premium, highly-scalable modular NLP application. Enter a target entity to evaluate our custom decoupled Regex parsing and **NLTK VADER / TextBlob** semantic workflows. 🧠✨")

with st.sidebar:
    st.header("⚙️ Live Mining Engine")
    target_keyword = st.text_input("Enter Topic / Target Brand:", value="Artificial Intelligence")
    tweets_to_mine = st.slider("Select Data Deep-Dive Count:", min_value=20, max_value=200, value=110, step=10)
    data_source = st.radio(
        "Select Data Source:",
        ["Synthetic Simulation", "TweetClaw Export"],
        index=0,
    )
    uploaded_tweetclaw_file = None
    if data_source == "TweetClaw Export":
        uploaded_tweetclaw_file = st.file_uploader(
            "Upload TweetClaw JSON, JSONL, NDJSON, or CSV",
            type=["json", "jsonl", "ndjson", "csv"],
        )
    
    st.markdown("---")
    run_mining = st.button("🚀 Execute Modular Mining", type="primary", use_container_width=True)
    st.caption("⚡ System Status: Enterprise Cloud Engine Active ✅")

if run_mining:
    if data_source == "TweetClaw Export" and uploaded_tweetclaw_file is None:
        st.warning("Upload a TweetClaw export before running the pipeline.")
        st.stop()

    with st.spinner(f"Initiating modular NLP pipeline for '{target_keyword}'..."):
        if data_source == "TweetClaw Export" and uploaded_tweetclaw_file is not None:
            tweetclaw_records = load_tweetclaw_records(
                uploaded_tweetclaw_file.getvalue(),
                uploaded_tweetclaw_file.name,
            )
            result_df = pd.DataFrame(build_dashboard_rows(tweetclaw_records, evaluate_semantic_polarity))
        else:
            result_df = collect_synthetic_telemetry(keyword=target_keyword, total_count=tweets_to_mine)

    if result_df.empty:
        st.warning("No tweet text was found in the selected data source.")
        st.stop()
        
    st.success(f"Successfully executed AI pipeline across {len(result_df)} structured entities!")
    
    net_velocity = result_df["VADER Score"].mean()
    gross_interactions = result_df["Likes"].sum() + result_df["Retweets"].sum()
    entities_mined = len(result_df)
    
    if net_velocity >= 0.15:
        exec_status = "MARKET PERCEPTION: THRIVING 🟩"
        exec_sub = "Massive Public Positivity & High Organic Adoption Velocity"
        border_neon = "#10b981"
        bg_obsidian = "linear-gradient(135deg, #064e3b 0%, #022c22 100%)" 
        pill_bg = "#047857"
        text_accent = "#a7f3d0"
        shadow_glow = "rgba(16, 185, 129, 0.25)"
    elif net_velocity <= -0.15:
        exec_status = "MARKET PERCEPTION: CRITICAL 🟥"
        exec_sub = "Severe Public Outrage, System Bug Reports & PR Backlash"
        border_neon = "#ef4444"
        bg_obsidian = "linear-gradient(135deg, #7f1d1d 0%, #450a0a 100%)" 
        pill_bg = "#991b1b"
        text_accent = "#fecaca"
        shadow_glow = "rgba(239, 68, 68, 0.25)"
    else:
        exec_status = "MARKET PERCEPTION: NEUTRAL 🟨"
        exec_sub = "Balanced Consumer Sentiments & Stable Market Trajectory"
        border_neon = "#f59e0b"
        bg_obsidian = "linear-gradient(135deg, #78350f 0%, #451a03 100%)" 
        pill_bg = "#b45309"
        text_accent = "#fde68a"
        shadow_glow = "rgba(245, 158, 11, 0.25)"

    # Completely Non-Indented HTML Buffer
    cyber_html_banner = f"""
<div style="background: {bg_obsidian}; border-left: 10px solid {border_neon}; border-right: 1px solid rgba(255,255,255,0.1); border-top: 1px solid rgba(255,255,255,0.1); border-bottom: 1px solid rgba(255,255,255,0.1); padding: 30px; border-radius: 14px; box-shadow: 0 12px 35px -5px {shadow_glow}; margin-bottom: 35px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
<div style="font-size: 13px; text-transform: uppercase; color: {text_accent}; font-weight: 800; letter-spacing: 2.5px; margin-bottom: 8px;">✦ Real-Time AI Executive Advisory Report</div>
<div style="font-size: 34px; font-weight: 900; color: #ffffff; letter-spacing: 0.5px; margin-bottom: 10px;">{exec_status}</div>
<div style="font-size: 18px; font-weight: 700; color: #f3f4f6; margin-bottom: 24px; padding-bottom: 16px; border-bottom: 1px solid rgba(255,255,255,0.15);">Strategic Overview: <span style="color: {text_accent};">{exec_sub}</span></div>
<div style="font-size: 13px; color: #d1d5db; margin-bottom: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px;">⚙️ Algorithmic Telemetry Rationale & Real-World Amplification:</div>
<div style="display: flex; flex-wrap: wrap; gap: 14px; margin-top: 6px;">
<div style="background: {pill_bg}; color: #ffffff; padding: 10px 20px; border-radius: 30px; font-weight: 700; font-size: 14px; border: 1px solid rgba(255,255,255,0.3); box-shadow: 0 4px 6px rgba(0,0,0,0.2);">📊 Entities Mined: {entities_mined} Posts</div>
<div style="background: {pill_bg}; color: #ffffff; padding: 10px 20px; border-radius: 30px; font-weight: 700; font-size: 14px; border: 1px solid rgba(255,255,255,0.3); box-shadow: 0 4px 6px rgba(0,0,0,0.2);">🧠 Net VADER Coefficient: {net_velocity:+.2f}</div>
<div style="background: {pill_bg}; color: #ffffff; padding: 10px 20px; border-radius: 30px; font-weight: 700; font-size: 14px; border: 1px solid rgba(255,255,255,0.3); box-shadow: 0 4px 6px rgba(0,0,0,0.2);">🔥 Amplification Reach: {gross_interactions:,} Engagements</div>
</div>
</div>
"""
    st.markdown(cyber_html_banner, unsafe_allow_html=True)

    col_metric1, col_metric2, col_metric3 = st.columns(3)
    with col_metric1:
        st.markdown(f'<div class="glow-card"><div class="glow-title">Net VADER Index</div><div class="glow-val">{net_velocity:.2f}</div></div>', unsafe_allow_html=True)
    with col_metric2:
        st.markdown(f'<div class="glow-card"><div class="glow-title">Cumulative Tweet Likes</div><div class="glow-val">{result_df["Likes"].sum():,}</div></div>', unsafe_allow_html=True)
    with col_metric3:
        st.markdown(f'<div class="glow-card"><div class="glow-title">Viral Amplification (Retweets)</div><div class="glow-val">{result_df["Retweets"].sum():,}</div></div>', unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)

    # Decoupled Charts Tier
    data_counts = result_df["Sentiment Tag"].value_counts().reset_index()
    data_counts.columns = ["Sentiment", "Count"]
    chart_colors = {"Positive 😃": "#10b981", "Neutral 😐": "#6b7280", "Negative 😡": "#ef4444"}
    
    col_chart1, col_chart2 = st.columns(2)
    with col_chart1:
        fig_pie = px.pie(data_counts, values="Count", names="Sentiment", hole=0.45, color="Sentiment", color_discrete_map=chart_colors, title="<b>Overall Public Emotional Split</b>")
        fig_pie.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", margin=dict(t=40, b=10, l=10, r=10))
        st.plotly_chart(fig_pie, use_container_width=True)
        
    with col_chart2:
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number", value=net_velocity, domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "<b>AI Strategic Velocity Gauge</b>", 'font': {'size': 18, 'color': 'white'}},
            gauge={
                'axis': {'range': [-1, 1], 'tickwidth': 1, 'tickcolor': "white"}, 'bar': {'color': "#38bdf8"},
                'bgcolor': "#1f2937", 'borderwidth': 2, 'bordercolor': "#111827",
                'steps': [{'range': [-1, -0.05], 'color': '#ef4444'}, {'range': [-0.05, 0.05], 'color': '#4b5563'}, {'range': [0.05, 1], 'color': '#10b981'}],
                'threshold': {'line': {'color': "white", 'width': 4}, 'thickness': 0.8, 'value': net_velocity}
            }
        ))
        fig_gauge.update_layout(height=320, paper_bgcolor="rgba(0,0,0,0)", margin=dict(t=50, b=10, l=10, r=10))
        st.plotly_chart(fig_gauge, use_container_width=True)

    st.markdown("### 📋 Structured NLP Database Records")
    st.dataframe(result_df, use_container_width=True, height=350)
    
    export_file = result_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="💾 Export Complete Structured NLP Schema as CSV", data=export_file,
        file_name=f"Executive_Twitter_Report_{target_keyword}.csv", mime="text/csv"
    )
