import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

from src.pipeline.prediction_pipeline import (
    CustomData,
    PredictionPipeline
)

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Student Performance AI Dashboard",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* MAIN BACKGROUND */

[data-testid="stAppViewContainer"] {
    background: linear-gradient(to right, #020617, #0f172a);
    color: white;
}

/* SIDEBAR */

[data-testid="stSidebar"] {
    background: #020617;
    border-right: 1px solid #1e293b;
}

/* REMOVE WHITE SPACE */

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 1rem;
}

/* TEXT */

h1, h2, h3, h4, h5, h6 {
    color: white !important;
}

p, label, div {
    color: #e2e8f0;
}

/* METRIC CARDS */

.metric-card {
    background: linear-gradient(145deg, #0f172a, #111827);
    padding: 22px;
    border-radius: 20px;
    border: 1px solid #1e293b;
    box-shadow: 0px 0px 15px rgba(0,0,0,0.3);
}

/* SECTION CARDS */

.section-card {
    background: linear-gradient(145deg, #0f172a, #111827);
    padding: 25px;
    border-radius: 24px;
    border: 1px solid #1e293b;
    margin-top: 20px;
}

/* PREDICTION CARD */

.prediction-card {
    background: linear-gradient(to right, #2563eb, #7c3aed);
    padding: 30px;
    border-radius: 24px;
    text-align: center;
    box-shadow: 0px 0px 25px rgba(37,99,235,0.3);
}

/* RECOMMENDATION CARD */

.recommendation-card {
    background: rgba(15,23,42,0.8);
    padding: 25px;
    border-radius: 20px;
    border-left: 5px solid #3b82f6;
}

/* BUTTON */

div.stButton > button {
    width: 100%;
    height: 58px;
    background: linear-gradient(to right, #ec4899, #8b5cf6);
    color: white;
    border: none;
    border-radius: 14px;
    font-size: 18px;
    font-weight: 600;
}

div.stButton > button:hover {
    background: linear-gradient(to right, #db2777, #7c3aed);
    color: white;
}

/* SLIDER */

.stSlider > div > div > div > div {
    background-color: #f43f5e !important;
}

/* SELECTBOX */

div[data-baseweb="select"] > div {
    background-color: #0f172a;
    border: 1px solid #1e293b;
    border-radius: 12px;
}

/* HIDE STREAMLIT MENU */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

st.title("🎓 AI-Powered Student Performance Dashboard")

st.markdown("""
Predict academic performance using Machine Learning,
real-time analytics, and AI-powered recommendations.
""")

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown("## 📘 Student Information")

st.sidebar.write("Enter student details below")

age = st.sidebar.slider(
    "Age",
    15,
    22,
    18
)

studytime = st.sidebar.slider(
    "Study Time (1-4)",
    1,
    4,
    2
)

failures = st.sidebar.slider(
    "Past Failures",
    0,
    4,
    0
)

absences = st.sidebar.slider(
    "Absences",
    0,
    50,
    5
)

sex = st.sidebar.selectbox(
    "Gender",
    ["F", "M"]
)

internet = st.sidebar.selectbox(
    "Internet Access",
    ["yes", "no"]
)

st.sidebar.markdown("<br>", unsafe_allow_html=True)

predict_button = st.sidebar.button(
    "🚀 Predict Performance"
)

# =========================================================
# TOP METRICS
# =========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <h4>🤖 Model</h4>
        <h2>Random Forest</h2>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <h4>📊 Dataset</h4>
        <h2>UCI Student</h2>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <h4>⚡ Status</h4>
        <h2>Active</h2>
    </div>
    """, unsafe_allow_html=True)

with col4:

    current_time = datetime.now().strftime("%H:%M:%S")

    st.markdown(f"""
    <div class="metric-card">
        <h4>🕒 Updated</h4>
        <h2>{current_time}</h2>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# MAIN DASHBOARD
# =========================================================

if predict_button:

    # PREDICTION

    data = CustomData(
        age=age,
        studytime=studytime,
        failures=failures,
        absences=absences,
        sex=sex,
        internet=internet
    )

    pred_df = data.get_data_as_dataframe()

    predict_pipeline = PredictionPipeline()

    results = predict_pipeline.predict(pred_df)

    prediction = results[0]

    # =====================================================
    # PREDICTION SECTION
    # =====================================================

    st.markdown('<div class="section-card">', unsafe_allow_html=True)

    left_col, right_col = st.columns([1.2, 1])

    # -----------------------------------------------------

    with left_col:

        st.subheader("🎯 Prediction Result")

        gauge_chart = go.Figure(go.Indicator(
            mode="gauge+number",
            value=prediction,
            number={'suffix': "/20"},
            gauge={
                'axis': {'range': [0, 20]},
                'bar': {'color': "#38bdf8"},
                'bgcolor': "#111827",
                'steps': [
                    {'range': [0, 8], 'color': "#7f1d1d"},
                    {'range': [8, 14], 'color': "#78350f"},
                    {'range': [14, 20], 'color': "#14532d"}
                ]
            }
        ))

        gauge_chart.update_layout(
            paper_bgcolor="#111827",
            font_color="white",
            height=350
        )

        st.plotly_chart(
            gauge_chart,
            width="stretch"
        )

    # -----------------------------------------------------

    with right_col:

        if prediction < 8:

            performance_text = "⚠ High Academic Risk"

            recommendation = """
            ✅ Increase daily study hours  
            ✅ Reduce absenteeism  
            ✅ Focus on weak subjects  
            ✅ Practice consistent revision  
            """

        elif prediction < 14:

            performance_text = "📘 Average Performance"

            recommendation = """
            ✅ Improve assignment consistency  
            ✅ Spend more time on practice  
            ✅ Build better study routines  
            """

        else:

            performance_text = "🏆 Excellent Performance"

            recommendation = """
            ✅ Maintain current performance  
            ✅ Continue advanced preparation  
            ✅ Practice higher-level problems  
            """

        st.markdown(f"""
        <div class="prediction-card">
            <h1>{performance_text}</h1>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(f"""
        <div class="recommendation-card">
            <h2>💡 AI Recommendations</h2>
            <p>{recommendation}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # =====================================================
    # DONUT CHART SECTION
    # =====================================================

    st.markdown('<div class="section-card">', unsafe_allow_html=True)

    st.subheader("📊 Performance Contribution Analysis")

    chart_col1, chart_col2 = st.columns([1.2, 1])

    with chart_col1:

        contribution_df = pd.DataFrame({

            "Category": [
                "Study Impact",
                "Absence Impact",
                "Failure Impact"
            ],

            "Value": [
                max(studytime * 10, 1),
                max(absences, 1),
                max(failures * 5, 1)
            ]
        })

        donut_chart = px.pie(
            contribution_df,
            names="Category",
            values="Value",
            hole=0.55,
            color="Category",
            color_discrete_map={
                "Study Impact": "#3b82f6",
                "Absence Impact": "#fbbf24",
                "Failure Impact": "#ef4444"
            }
        )

        donut_chart.update_traces(
            textinfo="percent",
            textfont_size=18
        )

        donut_chart.update_layout(
            paper_bgcolor="#111827",
            plot_bgcolor="#111827",
            font_color="white",
            showlegend=False,
            height=450
        )

        st.plotly_chart(
            donut_chart,
            width="stretch"
        )

    # -----------------------------------------------------

    with chart_col2:

        st.markdown("""
        <br><br>
        """, unsafe_allow_html=True)

        st.markdown("""
        ### 🔵 Study Impact
        
        Positive impact from study time and consistency.
        """)

        st.markdown("""
        ### 🟡 Absence Impact
        
        Academic impact caused by absences.
        """)

        st.markdown("""
        ### 🔴 Failure Impact
        
        Impact due to previous academic failures.
        """)

    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.caption("""
Developed using Python, Streamlit, Plotly, Scikit-learn, Pandas, and Machine Learning Pipelines
""")