# ==============================================================================
# Executive Command Interface: Master Streamlit Application Frontend
# Implementation: Highly Scalable SaaS UI & Multi-Threaded State Management
# ==============================================================================
import streamlit as st
import pandas as pd
from src.data_collector import collect_realtime_data
from src.chart_visualizer import draw_mood_donut_chart, draw_executive_gauge

# Initialize core viewport and environment states
st.set_page_config(page_title="Executive Twitter AI Dashboard", page_icon="⚡", layout="wide")

# Inject tailored enterprise-grade CSS wrappers for dynamic deep glowing DOM components
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

# Build application header
st.title("⚡ Real-Time Twitter/X Modular AI Sentiment Engine")
st.markdown("A premium, highly-scalable modular NLP application. Enter a target entity to evaluate our custom decoupled Regex parsing and **NLTK VADER / TextBlob** semantic workflows. 🧠✨")

# Instantiate global interactive configuration sidebar
with st.sidebar:
    st.header("⚙️ Live Mining Engine")
    target_keyword = st.text_input("Enter Topic / Target Brand:", value="Artificial Intelligence")
    tweets_to_mine = st.slider("Select Data Deep-Dive Count:", min_value=20, max_value=200, value=110, step=10)
    
    st.markdown("---")
    run_mining = st.button("🚀 Execute Modular Mining", type="primary", use_container_width=True)
    st.caption("⚡ System Status: Enterprise Simulation Engine Active ✅")

# Handle runtime asynchronous execution pipeline
if run_mining:
    with st.spinner(f"Initiating decoupled multi-threaded data scraping and NLP pipeline for '{target_keyword}'..."):
        # Dispatch execution to underlying modular data ingestion tier
        result_df = collect_realtime_data(keyword=target_keyword, total_count=tweets_to_mine)
        
    st.success(f"Successfully executed decoupled NLP pipeline across {len(result_df)} structured entities!")
    
    # Compute overarching analytical aggregations
    net_velocity = result_df["VADER Score"].mean()
    gross_interactions = result_df["Likes"].sum() + result_df["Retweets"].sum()
    
    # --------------------------------------------------------------------------
    # CYBER-SAAS EXECUTIVE ADVISORY BANNER (Strictly Non-Indented HTML Tier)
    # --------------------------------------------------------------------------
    if net_velocity >= 0.15:
        exec_status = "MARKET PERCEPTION: THRIVING 🟩"
        exec_sub = "Massive Public Positivity & High Organic Adoption Velocity"
        border_neon = "#10b981"      # Intense Neon Emerald
        bg_obsidian = "linear-gradient(135deg, #064e3b 0%, #022c22 100%)" 
        pill_bg = "#047857"
        text_accent = "#a7f3d0"
        shadow_glow = "rgba(16, 185, 129, 0.25)"
    elif net_velocity <= -0.15:
        exec_status = "MARKET PERCEPTION: CRITICAL 🟥"
        exec_sub = "Severe Public Outrage, System Bug Reports & PR Backlash"
        border_neon = "#ef4444"      # Intense Neon Ruby
        bg_obsidian = "linear-gradient(135deg, #7f1d1d 0%, #450a0a 100%)" 
        pill_bg = "#991b1b"
        text_accent = "#fecaca"
        shadow_glow = "rgba(239, 68, 68, 0.25)"
    else:
        exec_status = "MARKET PERCEPTION: NEUTRAL 🟨"
        exec_sub = "Balanced Consumer Sentiments & Stable Market Trajectory"
        border_neon = "#f59e0b"      # Intense Neon Amber
        bg_obsidian = "linear-gradient(135deg, #78350f 0%, #451a03 100%)" 
        pill_bg = "#b45309"
        text_accent = "#fde68a"
        shadow_glow = "rgba(245, 158, 11, 0.25)"

    # STRUCTURAL RATIONALE FOR ZERO INDENTATION BELOW: 
    # By ensuring our HTML string starts completely flush left without blank lines, 
    # Streamlit's Markdown engine parses it 100% as pristine DOM graphic containers!
    cyber_html_banner = f"""
<div style="background: {bg_obsidian}; border-left: 10px solid {border_neon}; border-right: 1px solid rgba(255,255,255,0.1); border-top: 1px solid rgba(255,255,255,0.1); border-bottom: 1px solid rgba(255,255,255,0.1); padding: 30px; border-radius: 14px; box-shadow: 0 12px 35px -5px {shadow_glow}; margin-bottom: 35px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
<div style="font-size: 13px; text-transform: uppercase; color: {text_accent}; font-weight: 800; letter-spacing: 2.5px; margin-bottom: 8px;">✦ Real-Time AI Executive Advisory Report</div>
<div style="font-size: 34px; font-weight: 900; color: #ffffff; letter-spacing: 0.5px; margin-bottom: 10px;">{exec_status}</div>
<div style="font-size: 18px; font-weight: 700; color: #f3f4f6; margin-bottom: 24px; padding-bottom: 16px; border-bottom: 1px solid rgba(255,255,255,0.15);">Strategic Overview: <span style="color: {text_accent};">{exec_sub}</span></div>
<div style="font-size: 13px; color: #d1d5db; margin-bottom: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px;">⚙️ Algorithmic Telemetry Rationale & Real-World Amplification:</div>
<div style="display: flex; flex-wrap: wrap; gap: 14px; margin-top: 6px;">
<div style="background: {pill_bg}; color: #ffffff; padding: 10px 20px; border-radius: 30px; font-weight: 700; font-size: 14px; border: 1px solid rgba(255,255,255,0.3); box-shadow: 0 4px 6px rgba(0,0,0,0.2);">📊 Entities Mined: {tweets_to_mine} Posts</div>
<div style="background: {pill_bg}; color: #ffffff; padding: 10px 20px; border-radius: 30px; font-weight: 700; font-size: 14px; border: 1px solid rgba(255,255,255,0.3); box-shadow: 0 4px 6px rgba(0,0,0,0.2);">🧠 Net VADER Coefficient: {net_velocity:+.2f}</div>
<div style="background: {pill_bg}; color: #ffffff; padding: 10px 20px; border-radius: 30px; font-weight: 700; font-size: 14px; border: 1px solid rgba(255,255,255,0.3); box-shadow: 0 4px 6px rgba(0,0,0,0.2);">🔥 Amplification Reach: {gross_interactions:,} Engagements</div>
</div>
</div>
"""
    st.markdown(cyber_html_banner, unsafe_allow_html=True)

    # --------------------------------------------------------------------------
    # Primary Executive KPI Displays
    # --------------------------------------------------------------------------
    col_metric1, col_metric2, col_metric3 = st.columns(3)
    
    with col_metric1:
        st.markdown(f'<div class="glow-card"><div class="glow-title">Net VADER Index</div><div class="glow-val">{net_velocity:.2f}</div></div>', unsafe_allow_html=True)
    with col_metric2:
        total_likes = result_df["Likes"].sum()
        st.markdown(f'<div class="glow-card"><div class="glow-title">Cumulative Tweet Likes</div><div class="glow-val">{total_likes:,}</div></div>', unsafe_allow_html=True)
    with col_metric3:
        total_rts = result_df["Retweets"].sum()
        st.markdown(f'<div class="glow-card"><div class="glow-title">Viral Amplification (Retweets)</div><div class="glow-val">{total_rts:,}</div></div>', unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)

    # --------------------------------------------------------------------------
    # Decoupled Enterprise Visualization Tier
    # --------------------------------------------------------------------------
    col_chart1, col_chart2 = st.columns(2)
    with col_chart1:
        st.plotly_chart(draw_mood_donut_chart(result_df), use_container_width=True)
    with col_chart2:
        st.plotly_chart(draw_executive_gauge(net_velocity), use_container_width=True)

    # --------------------------------------------------------------------------
    # In-Memory Database Deep-Dive & Pristine File Export
    # --------------------------------------------------------------------------
    st.markdown("### 📋 Structured NLP Database Records")
    st.dataframe(result_df, use_container_width=True, height=350)
    
    export_file = result_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="💾 Export Complete Structured NLP Schema as CSV",
        data=export_file,
        file_name=f"Executive_Twitter_Report_{target_keyword}.csv",
        mime="text/csv"
    )