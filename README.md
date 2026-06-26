# 🏥 Patient Queue Wait Time Prediction System

A Machine Learning project that predicts the waiting time of patients in a hospital queue using historical queue and service data. The project includes data preprocessing, exploratory data analysis (EDA), machine learning model development, and a Streamlit web application for real-time wait time prediction.

---

## Project Overview

Long waiting times in hospitals can reduce patient satisfaction and increase operational inefficiencies. This project aims to predict patient waiting time using machine learning techniques, helping hospitals improve scheduling and queue management.

---

## Objectives

- Predict patient waiting time accurately.
- Analyze queue patterns and peak hospital hours.
- Compare multiple machine learning algorithms.
- Build a user-friendly Streamlit application for real-time predictions.

---

## Dataset

The dataset contains patient queue information, including:

- Arrival Time
- Start Time
- Finish Time
- Queue Length
- Waiting Time

### Features Engineered

- Arrival Hour
- Arrival Minute
- Arrival Day
- Arrival Month
- Weekend Indicator
- Service Time
- Total Time

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Joblib
- Streamlit

---

## Exploratory Data Analysis (EDA)

The following analyses were performed:

- Data Cleaning
- Missing Value Analysis
- Duplicate Record Removal
- Feature Engineering
- Distribution of Waiting Time
- Queue Length Analysis
- Service Time Analysis
- Total Time Analysis
- Outlier Detection
- Correlation Heatmap
- Peak Hour Analysis

---

## 🤖 Machine Learning Models

The following regression models were trained and evaluated:

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor

---

## 📈 Evaluation Metrics

The models were evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

The best-performing model was selected based on the evaluation results and saved using Joblib.

---

## Streamlit Application

The Streamlit application allows users to:

- Enter queue details
- Predict patient waiting time
- View patient input data
- Display scheduling recommendations
- Analyze queue information

Run the application using:

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
Patient-Queue-Wait-Time-Prediction
│
├── Patient_Queue_Wait_Time_Predictor.ipynb
├── app.py
├── requirements.txt
├── README.md
├── queue_data.csv
├── cleaned_queue_data.csv
├── patient_wait_time_model.pkl
└── screenshots
```

---

## ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/Rishika14104/Patient-Queue-Wait-Time-Prediction.git
```

Move into the project directory:

```bash
cd Patient-Queue-Wait-Time-Prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 📷 Project Screenshots

Add screenshots of:

- Exploratory Data Analysis
- Streamlit Dashboard
- Prediction Result
- Feature Importance Graph

Store them inside the **screenshots/** folder.

<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/2022dc17-cc19-4d9f-8cbf-955b176b3496" />

<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/8d972e07-7996-43db-b8e7-a9387b909a21" />


---

## Future Enhancements

- Deep Learning Models
- Real-time Hospital Database Integration
- Appointment Scheduling Optimization
- Multi-Hospital Queue Prediction
- Live Dashboard with Real-Time Updates

---

## Results

- Successfully cleaned and preprocessed the dataset.
- Built multiple regression models for wait time prediction.
- Compared model performance using standard evaluation metrics.
- Developed an interactive Streamlit application for predicting patient waiting times.

---

## 👩‍💻 Author

**Rishika Kosireddy**

GitHub: https://github.com/Rishika14104

---
