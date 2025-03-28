# Sleep-Based Workout Recommendation App

This Streamlit app provides personalized workout recommendations based on a user's sleep data using a trained machine learning model.

---

## 🚀 Overview

The app takes the following inputs:

- Total Sleep Hours  
- Sleep Quality (%)  
- Deep Sleep (%)  
- Wake-Up Time  
- Date (for record keeping)

It uses a **Decision Tree Classifier**, trained on synthetic sleep pattern data, to recommend one of the following workout types:

- **Rest**
- **Stretching**
- **Light Cardio**
- **Cardio**
- **Strength**
- **HIIT**

Each recommendation includes estimated workout **duration** and **calories burned**.

---

## 📁 Project Structure

```
├── train_model.py             # Script to generate and save ML model
├── workout_model.pkl          # Trained model (auto-generated)
├── sleep_workout_app.py       # Streamlit app script
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Zuraiz270/Sleep-Based-Workout-Recommendation.git
cd folder_name
```

### 2. Create a Conda Environment

```bash
conda create -n sleepfit python=3.10 -y
conda activate sleepfit
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Train the Model (Run Once)

```bash
python train_model.py
```

This generates `workout_model.pkl`.

### 5. Launch the Streamlit App

```bash
streamlit run sleep_workout_app.py
```

---

## 🧠 Model Info

- **Type**: Decision Tree Classifier  
- **Training Data**: Simulated based on rule-based logic  
- **Framework**: scikit-learn  
- **Features**: Sleep Hours, Sleep Quality, Deep Sleep %

---

## ✅ Features

- Clean, responsive UI (Streamlit)
- Integrated machine learning prediction
- Rule-based logic transformed into a predictive model
- Estimation of workout duration and calorie burn
- Minimal local resource usage

---

## 📦 Dependencies

- Python 3.10
- Streamlit
- scikit-learn
- pandas
- joblib

See `requirements.txt` for full versions.

---

## 🧪 Future Enhancements

- Real-time data from Apple Health or Google Fit APIs  
- Support for CSV/batch uploads  
- User session storage and history  
- Deploy on Streamlit Cloud or Hugging Face Spaces  
- Add user feedback loop for model improvement

---