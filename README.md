
## 🚀 Employee Salary Predictor

**Machine Learning Project | AI/ML Internship**

### 📌 Project Overview

The **Employee Salary Predictor** is a machine learning–based classification system that predicts whether an employee earns **more than $50K or ≤ $50K annually**, based on demographic, educational, and employment-related attributes.

This project was developed as part of my **AI & Machine Learning internship**, with a strong focus on **data preprocessing, feature engineering, model comparison, and real-world prediction usability**.

---

## 🎯 Objective

To build an end-to-end machine learning pipeline that:

* Analyzes employee demographic and work-related data
* Trains and compares multiple ML classification models
* Predicts salary category accurately
* Allows **real-time prediction** using user inputs
* Saves and deploys the best-performing model

---

## 🧠 Dataset

* **Source:** Adult Census Income Dataset
* **Target Variable:** `income` (`<=50K` or `>50K`)
* **Features Include:**

  * Age
  * Workclass
  * Education level
  * Marital status
  * Occupation
  * Capital gain/loss
  * Hours per week
  * Gender, race, native country, etc.

---

## ⚙️ Technologies & Tools Used

* **Programming Language:** Python
* **Libraries:**

  * Pandas, NumPy
  * Scikit-learn
  * Matplotlib
  * Joblib
* **Platform:** Google Colab
* **Version Control:** Git & GitHub

---

## 🔍 Project Workflow

1. **Data Loading & Exploration**

   * Checked dataset dimensions, data types, and class distribution
   * Identified missing and inconsistent values

2. **Data Cleaning & Preprocessing**

   * Replaced missing categorical values (`?`) with meaningful labels
   * Removed irrelevant work classes and rare education categories
   * Removed outliers from the `age` feature
   * Dropped redundant features

3. **Feature Engineering**

   * Applied **Label Encoding** to categorical variables
   * Scaled numerical features using **MinMaxScaler**

4. **Model Training & Evaluation**
   Trained and evaluated multiple machine learning models:

   * K-Nearest Neighbors (KNN)
   * Logistic Regression
   * Multi-Layer Perceptron (Neural Network)
   * **Random Forest Classifier (Best Model)**

5. **Model Comparison**

   * Compared models using **accuracy score**
   * Selected Random Forest based on superior performance

6. **User Input Prediction**

   * Built a console-based prediction system
   * Accepts employee details and predicts salary category

7. **Model Saving**

   * Saved the trained Random Forest model using `joblib`
   * Ready for deployment or integration with a web app

---

## 📊 Model Performance

* **Best Model:** Random Forest Classifier
* **Evaluation Metrics:**

  * Accuracy
  * Precision
  * Recall
  * F1-Score
  * Confusion Matrix

The Random Forest model achieved **high classification accuracy** and balanced performance across both salary classes.

---

## 🧪 Sample Prediction Output

```text
🔎 Enter Employee Details to Predict Salary Group

✅ The predicted salary group is: >50K
```

---

## 📁 Repository Structure

```bash
EmployeeSalaryPredictor/
│
├── Employee_salary_predictor_IBM_Project.ipynb
├── best_model.pkl
├── README.md
└── dataset/
    └── adult.csv
```

---

## 🌟 Key Highlights

✔ End-to-end ML pipeline
✔ Real-world dataset handling
✔ Multiple model comparison
✔ Clean preprocessing & feature scaling
✔ Model persistence using joblib
✔ Recruiter-friendly project structure

---

## 🚀 Future Enhancements

* Deploy using **Streamlit** 
* Add **cross-validation** for robustness
* Hyperparameter tuning with GridSearchCV
* Improve interpretability using **feature importance**
* Integrate UI-based input instead of console

---

## 👨‍💻 About Me

I am a **B.Tech IT student** with hands-on experience in **Machine Learning, Data Analysis, and Model Deployment**, actively seeking opportunities to apply AI/ML solutions to real-world problems.

📌 *This project reflects my ability to build practical ML systems beyond theory.*

---

