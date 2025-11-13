# Student Performance Prediction

Predicts student academic performance using **machine learning** models! 🚀  
Includes Python data analysis in Jupyter Notebook and an interactive Streamlit web app for quick predictions and visualizations.  
This all-in-one project gives students, teachers, and parents quick insights into final scores using easy-to-use forms and sleek dashboards.

---

## Features

- Predicts a student's final score from academic and demographic inputs
- Simple, interactive Streamlit web app for live predictions  
- Data analysis and model training in Jupyter Notebook  
- Trained machine learning model for instant feedback  
- Visual leaderboard showcasing top scorers!  
- User feedback and app rating system built-in

---

## Prerequisites

Make sure you have:

- Python 3.8 or higher
- `pip` Python package manager

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/MohammedAbdulKadarS/Student_Performance_Prediction.git
cd Student_Performance_Prediction
```


### 2. Install Dependencies

```python
pip install -r requirements.txt
```


### 3. (Optional) Retrain the Model

The model files (`*_model.pkl`, `*_scaler.pkl`, `*_selector.pkl`) are already included. To retrain the model, edit and run:

```text
Open and modify Student_Performance_Data_Analysis.ipynb as needed
Save/export your own model if you wish
```


---

## Running the Application

### Streamlit Web App

```python
streamlit run student_performance_streamlit.py
```


Now open your browser and go to:

```text
http://localhost:8501
```


### Jupyter Notebook

Open and explore:

```text
Student_Performance_Data_Analysis.ipynb
```


---

## How It Works

- The app uses a machine learning model trained on historical student performance data (`Task___students_performance_dataset.xlsx`).
- Input details like previous semester scores, attendance, study hours, extracurriculars, etc.
- The model predicts the **final score**, displayed instantly on the app.
- Top scorers are shown on a leaderboard.
- You can submit feedback and rate the app directly.

---

## File Structure

```bash
Student_Performance_Prediction/
├── Student_Performance_Data_Analysis.ipynb           # Data analysis notebook
├── Student_Performance_Data_Analysis_model.pkl       # Trained ML model
├── Student_Performance_Data_Analysis_scaler.pkl      # Model scaler
├── Student_Performance_Data_Analysis_selector.pkl    # Feature selector
├── Task___students_performance_dataset.xlsx          # Sample training data
├── student_performance_streamlit.py                  # Streamlit web application
├── requirements.txt                                  # Python dependencies
├── generated-image.png                               # Project/app logo
├── README.md                                         # Project documentation
```


---

## Screenshots

### 1. Predictor Web App

<img width="1889" height="901" alt="Screenshot 2025-11-12 235945" src="https://github.com/user-attachments/assets/ce32b035-4b94-46aa-ac73-5cd922dac732" />


### 2. Prediction Output

<img width="1887" height="894" alt="Screenshot 2025-11-13 000035" src="https://github.com/user-attachments/assets/9c2d1813-3950-4b04-845f-9a6ae2535e97" />


### 3. Champions Leaderboard

<img width="1907" height="891" alt="Screenshot 2025-11-13 000145" src="https://github.com/user-attachments/assets/f2f705d6-b3b6-4ebf-8500-bb380e37272e" />


### 4. Feedback Section

<img width="1905" height="910" alt="Screenshot 2025-11-13 000206" src="https://github.com/user-attachments/assets/8b9db072-c886-4310-ba83-a9e986174e32" />


---

## Future Improvements

- Add separate login for students/teachers/parents  
- More detailed analytics and visualization features  
- Translation/localization for wider reach  
- Export reports and leaderboard to PDF/CSV  
- Enhanced model performance with extra features

---

## Step-by-Step Guide: How to Use the Student Performance Predictor

**Step 1:** Go to the "Live Predictor" tab.  
**Step 2:** Enter student details and click "Predict Now."  
**Step 3:** View the **Predicted Final Score**.  
**Step 4:** Check the "Champions" tab for the top scorers.  
**Step 5:** Click "Feedback" to rate the app or suggest new features!

---

## Credits

Special thanks to my faculty, mentors, and friends for their support and feedback.  
Open-source libraries and the data science community inspired this project.  
If you found this project useful, give it a ⭐ on GitHub!

---

## Contact

If you have questions, ideas, or want to connect, reach out to me at  
**mohammedabdulkadars@gmail.com** or [LinkedIn](https://www.linkedin.com/in/mohammedabdulkadars/).

---

**Thanks for visiting! All the best for your learning journey.**

---
