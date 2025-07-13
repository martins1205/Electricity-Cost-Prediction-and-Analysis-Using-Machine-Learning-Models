# Electricity-Cost-Prediction-and-Analysis-Using-Machine-Learning-Models
This Jupyter Notebook provides an end-to-end workflow for analyzing and predicting electricity costs based on various features such as site area, structure type, water consumption, recycling rate, utilization rate, air quality index, issue resolution time, and resident count.

## Key Steps in the Notebook:
1. **Data Loading and Exploration**:
   - Load the dataset and inspect its structure.
   - Perform exploratory data analysis (EDA) using visualizations and statistical summaries.

2. **Feature Engineering and Preprocessing**:
   - Handle categorical and numerical features using preprocessing techniques.

3. **Model Training and Evaluation**:
   - Train and evaluate three machine learning models: Linear Regression, Random Forest Regressor, and Support Vector Regressor (SVR).
   - Perform hyperparameter tuning to optimize the Random Forest model.

4. **Model Deployment**:
   - Save the best-performing model for deployment.

5. **Visualization**:
   - Generate various plots to understand feature importance, residuals, and model performance.

## Files Generated:
- `random_forest_best_model.pkl`: The saved Random Forest model.
- `electricity_cost_prediction_app.py`: A Streamlit app for predicting electricity costs interactively.
- ## Features:
- Interactive input fields for entering site details.
- Real-time prediction of electricity costs using a pre-trained Random Forest model.




## How to Run:
1.Open the notebook in Jupyter and run the cells sequentially.
2. Use the saved model in the Streamlit app for predictions.
