import streamlit as st
import pandas as pd
import joblib
import random

# ====== CONFIG ==========
st.set_page_config(page_title="Abdul's Student Success Studio", page_icon="🎓", layout="wide")
st.sidebar.image("generated-image.png", width=120)
st.sidebar.title("Navigation 🚀")
tabs = ["Live Predictor", "Explore Data", "Champions Board", "Feedback"]
section = st.sidebar.radio("", tabs)

# ====== MOTIVATION QUOTES ==========
quotes = [
    "Success isn't overnight. Keep at it! 🚀",
    "Dream big, work hard, stay humble.",
    "Small progress is still progress.",
    "Code. Learn. Win!"
]
st.sidebar.markdown(f"##### 💬 Tip: {random.choice(quotes)}")

# ====== MODEL LOADING (update path if different) ==========
@st.cache_resource
def load_model():
    model = joblib.load(r"C:\Users\abdula\OneDrive\Desktop\StudentPerformancePredictionModel\Student_Performance_Data_Analysis_model.pkl")
    scaler = joblib.load(r"C:\Users\abdula\OneDrive\Desktop\StudentPerformancePredictionModel\Student_Performance_Data_Analysis_scaler.pkl")
    selector = joblib.load(r"C:\Users\abdula\OneDrive\Desktop\StudentPerformancePredictionModel\Student_Performance_Data_Analysis_selector.pkl")
    return model, scaler, selector

model, scaler, selector = load_model()

# ====== TABS ==========
if section == "Live Predictor":
    st.markdown("<h1 style='color:#009fe3'>🔮 Smart Score Predictor</h1>", unsafe_allow_html=True)
    st.info("Enter student details below. Instantly predict their final score! Try changing values and see the magic ✨.")

    with st.form("prediction_form"):
        col1, col2 = st.columns(2)
        with col1:
            features = {
                'Previous_Sem_Score': st.slider('Previous Sem Score', 0.0, 100.0, 62.0),
                'Study_Hours_per_Week': st.slider('Study Hours/week', 0.0, 40.0, 14.0),
                'Attendance_Percentage': st.slider('Attendance %', 0.0, 100.0, 80.0),
                'Parental_Education': st.selectbox('Parental Education', ['High School', 'Graduate', 'Postgraduate']),
                'Library_Usage_per_Week': st.slider('Library Usage/week', 0, 10, 3),
                'Sleep_Hours': st.slider('Sleep Hours', 2.0, 12.0, 6.0),
                'Internet_Access': st.selectbox('Internet Access', ['Yes', 'No']),
                'Gender': st.selectbox('Gender', ['Male', 'Female'])
            }
        with col2:
            features.update({
                'Family_Income': st.number_input('Family Income', 5000.0, 100000.0, 34000.0),
                'Tutoring_Classes': st.selectbox('Tutoring Classes', ['Yes', 'No']),
                'Sports_Activity': st.selectbox('Sports?', ['Yes', 'No']),
                'Extra_Curricular': st.selectbox('Extra Curricular?', ['Yes', 'No']),
                'School_Type': st.selectbox('School Type', ['Public', 'Private']),
                'Motivation_Level': st.slider('Motivation Level', 1.0, 10.0, 7.0),
                'Test_Anxiety_Level': st.slider('Test Anxiety', 1.0, 10.0, 4.0),
                'Teacher_Feedback': st.selectbox('Feedback', ['Poor', 'Average', 'Good', 'Excellent']),
                'Peer_Influence': st.slider('Peer Influence', 1.0, 10.0, 6.0)
            })
        submitted = st.form_submit_button("🎯 Predict Now")
    if submitted:
        df_input = pd.DataFrame([features])
        df_input = pd.get_dummies(df_input)
        expected_columns = scaler.feature_names_in_
        for col in expected_columns:
            if col not in df_input.columns:
                df_input[col] = 0
        df_input = df_input[expected_columns]
        scaled_input = scaler.transform(df_input)
        selected_input = selector.transform(scaled_input)
        pred = model.predict(selected_input)[0]
        color = "#00cb92" if pred > 60 else "#f2545b"
        st.markdown(
            f"<div style='padding:20px;border-radius:12px;background:{color};color:white;width:300px;text-align:center;'>"
            f"<h2>Predicted Final Score</h2><div style='font-size:40px;'>{pred:.2f}</div></div>",
            unsafe_allow_html=True
        )
        st.balloons()

elif section == "Explore Data":
    st.markdown("<h1 style='color:#ffaf3d;'>🧪 Data Explorer</h1>", unsafe_allow_html=True)
    st.info("Quickly visualize feature relationships and stats. Choose variable to plot!")
    # Load real data if available
    df = pd.read_excel(r"C:\Users\abdula\OneDrive\Desktop\StudentPerformancePredictionModel\Task____students_performance_dataset.xlsx")
    plot = st.selectbox("Show Analysis for:", ["Correlation Heatmap", "Feature Distribution"])
    import seaborn as sns
    import matplotlib.pyplot as plt
    if plot == "Correlation Heatmap":
    # Only numeric columns
        num_df = df.select_dtypes(include=['number'])
        fig, ax = plt.subplots()
        sns.heatmap(num_df.corr(), annot=True, ax=ax, cmap="mako")
        st.pyplot(fig)

    else:
        col = st.selectbox("Choose column:", [c for c in df.columns if df[c].dtype in ['int64','float64']])
        fig, ax = plt.subplots()
        sns.histplot(df[col], kde=True, color="#44bcd8", ax=ax)
        st.pyplot(fig)

elif section == "Champions Board":
    st.markdown("<h1 style='color:#00baad;'>🏅 Top Scorers Leaderboard</h1>", unsafe_allow_html=True)
    # Sample leaderboard (replace with real data if needed)
    leaderboard = pd.DataFrame({
        "Student": ["Arun", "Sanya", "Vijay", "Meera", "Karthik"],
        "Final_Score": [98, 91.5, 89, 87, 85.5]
    })
    st.table(leaderboard)
    st.success("Want to get featured? Score high & submit your story!")

elif section == "Feedback":
    st.markdown("<h1 style='color:#ff4181;'>✍️ Feedback & Feature Requests</h1>", unsafe_allow_html=True)
    with st.form("feedback_form"):
        name = st.text_input("Your Name")
        remark = st.text_area("Feedback to Abdul?")
        rating = st.slider("App rating", 1, 5, 3)
        submitted = st.form_submit_button("Send")
    if submitted:
        st.success(f"Thanks {name or 'Anonymous'}! Your feedback (⭐{rating}) is sent.")
        st.snow()

# ======= Personal Footer/Watermark =======
st.markdown("<hr style='border:1px solid #222;'>", unsafe_allow_html=True)
st.markdown(
    "<div style='text-align:right;font-size:11px;color:#aaa;'> Made by Abdul | Unique Analytics UI | 2025 </div>",
    unsafe_allow_html=True
)
