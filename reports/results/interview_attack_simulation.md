# Interview Attack Simulation

These are likely evaluator questions with direct answers a fresher can explain confidently.

| No. | Question | Difficulty | Can Project Answer? | Suggested Answer |
|---:|---|---|---|---|
| 1 | What is the target variable? | Easy | YES | The target variable is `ad_revenue_usd`, which represents YouTube ad revenue in USD. |
| 2 | Is this regression or classification? | Easy | YES | It is regression because the model predicts a continuous numeric revenue value. |
| 3 | Why did you handle missing values with median? | Medium | YES | Median is less affected by extreme values, so it is suitable for skewed video metrics like likes and watch time. |
| 4 | How many duplicate rows were present? | Easy | YES | The raw data had 2,400 duplicate rows, and they were removed before training. |
| 5 | How did you detect outliers? | Medium | YES | I used the IQR method with lower bound Q1 - 1.5*IQR and upper bound Q3 + 1.5*IQR. |
| 6 | Why did you cap outliers instead of deleting them? | Medium | YES | Capping keeps useful rows while reducing the effect of extreme values on training. |
| 7 | What is engagement rate? | Easy | YES | Engagement rate is `(likes + comments) / views`; it measures viewer interaction relative to reach. |
| 8 | Why did you create watch time efficiency? | Medium | YES | It compares total watch time with video length, helping understand how efficiently a video holds attention. |
| 9 | How did you encode category, device, and country? | Medium | YES | I used one-hot encoding inside a scikit-learn `ColumnTransformer`. |
| 10 | Why did you scale numeric features? | Medium | YES | Linear, Ridge, and Lasso models are sensitive to feature scale, so scaling makes numeric features comparable. |
| 11 | Which five models did you compare? | Easy | YES | Linear Regression, Ridge Regression, Lasso Regression, Random Forest Regressor, and Gradient Boosting Regressor. |
| 12 | Which model performed best? | Easy | YES | Lasso Regression performed best with R2 around 0.9526, RMSE around 13.48, and MAE around 3.08. |
| 13 | Why did Lasso win over Random Forest? | Hard | YES | The dataset appears to have mostly linear relationships, especially watch time with revenue, so a regularized linear model generalized slightly better. |
| 14 | What does R2 score mean? | Medium | YES | R2 explains how much variance in revenue the model can explain. A value near 0.95 means the model explains most of the variation. |
| 15 | What does RMSE mean? | Medium | YES | RMSE is the square root of average squared error. It penalizes larger errors more than MAE. |
| 16 | What does MAE mean? | Easy | YES | MAE is the average absolute difference between actual and predicted revenue. |
| 17 | What are the top revenue drivers? | Medium | YES | The saved feature importance file shows watch time as the strongest driver, followed by engagement-related features. |
| 18 | How does the Streamlit app use the model? | Medium | YES | The app loads `models/best_model.pkl`, collects user inputs, creates engineered features, and returns a revenue prediction. |
| 19 | What is the Revenue Performance Score? | Medium | YES | It is a simple 0-100 score comparing predicted revenue against a high-revenue benchmark from the dataset. |
| 20 | What are the project limitations? | Hard | YES | The dataset is synthetic, no external YouTube API data is used, and online deployment depends on Render setup. More features like upload time and traffic source could improve realism. |

## Risk Questions

1. **Why is the notebook shorter than the scripts?**  
   The project uses modular scripts for reproducibility, while the notebook explains the analysis flow. The generated reports and figures contain the detailed outputs.

2. **Is the model overfitted?**  
   The test results are close across all five models, and simpler linear models perform best, which suggests the model is not relying on overly complex patterns.

3. **Why use Lasso if the PDF says Linear Regression?**  
   The PDF asks for a regression model and comparison of five models. Linear Regression was included, but Lasso was selected because it gave slightly better evaluation metrics.

4. **Can this predict real YouTube revenue?**  
   It can demonstrate the ML workflow and estimate revenue patterns from this dataset, but real-world deployment would need real historical channel data and CPM information.
