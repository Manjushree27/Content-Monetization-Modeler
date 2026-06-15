# Live Evaluation Preparation

## 5-Minute Presentation Script

Hello, my project is Content Monetization Modeler. The goal is to predict YouTube ad revenue using video performance metrics such as views, likes, comments, watch time, subscribers, category, device, and country. I started with data understanding, checked missing values and duplicates, cleaned the data, handled outliers using IQR capping, and created features like engagement rate, watch time efficiency, interaction score, and subscriber engagement score. I trained exactly five models: Linear Regression, Ridge, Lasso, Random Forest, and Gradient Boosting. Based on R2, RMSE, and MAE, the selected best model is Lasso Regression. Finally, I built a Streamlit application with prediction, EDA, model comparison, insights, and a revenue optimization advisor.

## 10-Minute Presentation Script

Start with the problem statement, then show the dataset columns. Explain data cleaning decisions, then open the EDA dashboard and discuss revenue distribution, category, device, country, engagement, and watch time charts. After that, explain each engineered feature and why it helps. Show the model comparison table and explain why Lasso Regression was selected. Demonstrate the prediction page and what-if simulator. End with business insights, limitations, and future scope.

## End-to-End Workflow

Dataset -> EDA -> Cleaning -> Feature Engineering -> Encoding and Scaling -> Train-Test Split -> Five Model Training -> Model Evaluation -> Best Model Saving -> Streamlit App -> Render Deployment.

## Architecture Explanation

The architecture is intentionally simple: CSV data is processed with Python scripts, the best scikit-learn pipeline is saved with joblib, and Streamlit loads the model for prediction. This matches a fresher-level data science project without unnecessary cloud or MLOps tools.

## Model Explanation

| index | Model | R2 Score | RMSE | MAE |
| --- | --- | --- | --- | --- |
| 0 | Lasso Regression | 0.9525879353893328 | 13.478061860355057 | 3.082985140191183 |
| 1 | Ridge Regression | 0.9525759169726782 | 13.479770019453706 | 3.1154705224978 |
| 2 | Linear Regression | 0.9525749233834394 | 13.479911227078883 | 3.1170486216061013 |
| 3 | Gradient Boosting Regressor | 0.9522862410874666 | 13.520875924230417 | 3.563864347299884 |
| 4 | Random Forest Regressor | 0.9514821310218172 | 13.634332164178184 | 3.509145028161436 |


## 50 Technical Questions and Answers

**Q1. What should you explain about Python list and dictionary usage?**

Answer: Explain Python list and dictionary usage in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q2. What should you explain about Pandas DataFrame operations?**

Answer: Explain Pandas DataFrame operations in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q3. What should you explain about NumPy arrays?**

Answer: Explain NumPy arrays in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q4. What should you explain about missing value handling?**

Answer: Explain missing value handling in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q5. What should you explain about duplicates?**

Answer: Explain duplicates in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q6. What should you explain about outliers?**

Answer: Explain outliers in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q7. What should you explain about EDA?**

Answer: Explain EDA in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q8. What should you explain about correlation?**

Answer: Explain correlation in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q9. What should you explain about regression?**

Answer: Explain regression in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q10. What should you explain about train-test split?**

Answer: Explain train-test split in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q11. What should you explain about R2 score?**

Answer: Explain R2 score in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q12. What should you explain about RMSE?**

Answer: Explain RMSE in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q13. What should you explain about MAE?**

Answer: Explain MAE in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q14. What should you explain about feature engineering?**

Answer: Explain feature engineering in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q15. What should you explain about one-hot encoding?**

Answer: Explain one-hot encoding in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q16. What should you explain about standard scaling?**

Answer: Explain standard scaling in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q17. What should you explain about linear regression?**

Answer: Explain linear regression in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q18. What should you explain about ridge regression?**

Answer: Explain ridge regression in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q19. What should you explain about lasso regression?**

Answer: Explain lasso regression in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q20. What should you explain about random forest?**

Answer: Explain random forest in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q21. What should you explain about gradient boosting?**

Answer: Explain gradient boosting in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q22. What should you explain about overfitting?**

Answer: Explain overfitting in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q23. What should you explain about underfitting?**

Answer: Explain underfitting in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q24. What should you explain about model comparison?**

Answer: Explain model comparison in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q25. What should you explain about pickle and joblib?**

Answer: Explain pickle and joblib in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q26. What should you explain about Streamlit widgets?**

Answer: Explain Streamlit widgets in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q27. What should you explain about Render deployment?**

Answer: Explain Render deployment in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q28. What should you explain about requirements.txt?**

Answer: Explain requirements.txt in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q29. What should you explain about Git commits?**

Answer: Explain Git commits in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q30. What should you explain about README writing?**

Answer: Explain README writing in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q31. What should you explain about business insights?**

Answer: Explain business insights in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q32. What should you explain about target variable?**

Answer: Explain target variable in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q33. What should you explain about categorical variables?**

Answer: Explain categorical variables in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q34. What should you explain about numeric variables?**

Answer: Explain numeric variables in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q35. What should you explain about data leakage?**

Answer: Explain data leakage in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q36. What should you explain about pipeline?**

Answer: Explain pipeline in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q37. What should you explain about train data?**

Answer: Explain train data in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q38. What should you explain about test data?**

Answer: Explain test data in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q39. What should you explain about feature importance?**

Answer: Explain feature importance in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q40. What should you explain about prediction workflow?**

Answer: Explain prediction workflow in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q41. What should you explain about model interpretability?**

Answer: Explain model interpretability in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q42. What should you explain about statistics basics?**

Answer: Explain statistics basics in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q43. What should you explain about median imputation?**

Answer: Explain median imputation in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q44. What should you explain about IQR method?**

Answer: Explain IQR method in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q45. What should you explain about revenue optimization?**

Answer: Explain revenue optimization in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q46. What should you explain about what-if simulator?**

Answer: Explain what-if simulator in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q47. What should you explain about app design?**

Answer: Explain app design in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q48. What should you explain about CSV data?**

Answer: Explain CSV data in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q49. What should you explain about data cleaning decisions?**

Answer: Explain data cleaning decisions in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q50. What should you explain about project limitations?**

Answer: Explain project limitations in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q51. What should you explain about future scope?**

Answer: Explain future scope in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

## 50 Project Questions and Answers

**Q1. What should you explain about why this project was chosen?**

Answer: Explain why this project was chosen in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q2. What should you explain about problem statement?**

Answer: Explain problem statement in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q3. What should you explain about dataset columns?**

Answer: Explain dataset columns in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q4. What should you explain about target variable meaning?**

Answer: Explain target variable meaning in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q5. What should you explain about EDA findings?**

Answer: Explain EDA findings in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q6. What should you explain about category revenue result?**

Answer: Explain category revenue result in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q7. What should you explain about device revenue result?**

Answer: Explain device revenue result in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q8. What should you explain about country revenue result?**

Answer: Explain country revenue result in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q9. What should you explain about engagement rate formula?**

Answer: Explain engagement rate formula in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q10. What should you explain about watch time efficiency formula?**

Answer: Explain watch time efficiency formula in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q11. What should you explain about interaction score formula?**

Answer: Explain interaction score formula in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q12. What should you explain about subscriber engagement formula?**

Answer: Explain subscriber engagement formula in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q13. What should you explain about model training process?**

Answer: Explain model training process in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q14. What should you explain about best model reason?**

Answer: Explain best model reason in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q15. What should you explain about linear model use?**

Answer: Explain linear model use in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q16. What should you explain about tree model use?**

Answer: Explain tree model use in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q17. What should you explain about comparison table?**

Answer: Explain comparison table in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q18. What should you explain about revenue advisor?**

Answer: Explain revenue advisor in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q19. What should you explain about performance score?**

Answer: Explain performance score in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q20. What should you explain about leaderboard?**

Answer: Explain leaderboard in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q21. What should you explain about feature importance?**

Answer: Explain feature importance in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q22. What should you explain about what-if simulator?**

Answer: Explain what-if simulator in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q23. What should you explain about Streamlit pages?**

Answer: Explain Streamlit pages in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q24. What should you explain about Render commands?**

Answer: Explain Render commands in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q25. What should you explain about folder structure?**

Answer: Explain folder structure in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q26. What should you explain about README content?**

Answer: Explain README content in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q27. What should you explain about business users?**

Answer: Explain business users in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q28. What should you explain about creator benefits?**

Answer: Explain creator benefits in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q29. What should you explain about data limitations?**

Answer: Explain data limitations in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q30. What should you explain about ethics?**

Answer: Explain ethics in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q31. What should you explain about manual testing?**

Answer: Explain manual testing in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q32. What should you explain about local run command?**

Answer: Explain local run command in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q33. What should you explain about deployment run command?**

Answer: Explain deployment run command in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q34. What should you explain about model saving?**

Answer: Explain model saving in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q35. What should you explain about prediction input?**

Answer: Explain prediction input in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q36. What should you explain about categorical encoding?**

Answer: Explain categorical encoding in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q37. What should you explain about scaling?**

Answer: Explain scaling in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q38. What should you explain about outlier treatment?**

Answer: Explain outlier treatment in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q39. What should you explain about missing values?**

Answer: Explain missing values in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q40. What should you explain about duplicates?**

Answer: Explain duplicates in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q41. What should you explain about evaluation metrics?**

Answer: Explain evaluation metrics in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q42. What should you explain about residual errors?**

Answer: Explain residual errors in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q43. What should you explain about model tradeoffs?**

Answer: Explain model tradeoffs in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q44. What should you explain about explainability?**

Answer: Explain explainability in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q45. What should you explain about improvements?**

Answer: Explain improvements in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q46. What should you explain about GitHub repository?**

Answer: Explain GitHub repository in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q47. What should you explain about commit message examples?**

Answer: Explain commit message examples in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q48. What should you explain about live demo flow?**

Answer: Explain live demo flow in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q49. What should you explain about presentation flow?**

Answer: Explain presentation flow in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q50. What should you explain about why no advanced MLOps?**

Answer: Explain why no advanced MLOps in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

**Q51. What should you explain about fresher-level design?**

Answer: Explain fresher-level design in simple words, connect it to this YouTube revenue project, and mention the decision used in the code.

## 50 Viva Questions and Answers

**Q1. How would you explain this project in viva question 1?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q2. How would you explain this project in viva question 2?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q3. How would you explain this project in viva question 3?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q4. How would you explain this project in viva question 4?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q5. How would you explain this project in viva question 5?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q6. How would you explain this project in viva question 6?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q7. How would you explain this project in viva question 7?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q8. How would you explain this project in viva question 8?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q9. How would you explain this project in viva question 9?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q10. How would you explain this project in viva question 10?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q11. How would you explain this project in viva question 11?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q12. How would you explain this project in viva question 12?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q13. How would you explain this project in viva question 13?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q14. How would you explain this project in viva question 14?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q15. How would you explain this project in viva question 15?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q16. How would you explain this project in viva question 16?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q17. How would you explain this project in viva question 17?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q18. How would you explain this project in viva question 18?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q19. How would you explain this project in viva question 19?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q20. How would you explain this project in viva question 20?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q21. How would you explain this project in viva question 21?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q22. How would you explain this project in viva question 22?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q23. How would you explain this project in viva question 23?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q24. How would you explain this project in viva question 24?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q25. How would you explain this project in viva question 25?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q26. How would you explain this project in viva question 26?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q27. How would you explain this project in viva question 27?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q28. How would you explain this project in viva question 28?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q29. How would you explain this project in viva question 29?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q30. How would you explain this project in viva question 30?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q31. How would you explain this project in viva question 31?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q32. How would you explain this project in viva question 32?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q33. How would you explain this project in viva question 33?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q34. How would you explain this project in viva question 34?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q35. How would you explain this project in viva question 35?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q36. How would you explain this project in viva question 36?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q37. How would you explain this project in viva question 37?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q38. How would you explain this project in viva question 38?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q39. How would you explain this project in viva question 39?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q40. How would you explain this project in viva question 40?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q41. How would you explain this project in viva question 41?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q42. How would you explain this project in viva question 42?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q43. How would you explain this project in viva question 43?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q44. How would you explain this project in viva question 44?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q45. How would you explain this project in viva question 45?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q46. How would you explain this project in viva question 46?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q47. How would you explain this project in viva question 47?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q48. How would you explain this project in viva question 48?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q49. How would you explain this project in viva question 49?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.

**Q50. How would you explain this project in viva question 50?**

Answer: I would say that I built a Streamlit-based ML regression project to predict YouTube ad revenue, cleaned the dataset, engineered understandable features, compared five models, selected Lasso Regression, and converted the result into creator-friendly insights.