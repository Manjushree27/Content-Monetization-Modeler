# Content Monetization Modeler - Final Project Report

Machine Learning Based YouTube Advertisement Revenue Prediction System

This Markdown file is a source companion for the generated DOCX report.

Dataset rows: 122,400
Dataset columns: 12
Best model: Lasso Regression
R2: 0.9526
RMSE: 13.4781
MAE: 3.0830

## Model Comparison

| Model | R2 Score | RMSE | MAE |
|---|---:|---:|---:|
| Lasso Regression | 0.9526 | 13.4781 | 3.0830 |
| Ridge Regression | 0.9526 | 13.4798 | 3.1155 |
| Linear Regression | 0.9526 | 13.4799 | 3.1170 |
| Gradient Boosting Regressor | 0.9523 | 13.5209 | 3.5639 |
| Random Forest Regressor | 0.9515 | 13.6343 | 3.5091 |

## Business Insights

- Tech has the highest average revenue among categories.
- Mobile traffic gives the highest average revenue by device.
- Us is the strongest country by average revenue.
- `watch_time_minutes` is the strongest numerical revenue driver after the target itself.
- Videos with stronger watch time usually create better monetization potential.
- Higher likes and comments improve engagement quality and can support higher revenue.
- Subscriber base matters, but subscriber engagement is more useful than raw subscribers alone.
- Very low video length can limit watch-time opportunity even when views are good.
- Very long videos still need retention; length alone does not guarantee revenue.
- Country mix should be tracked because CPM can vary by market.
- Device mix is useful for planning thumbnails and viewing experience.
- The model can support creators before publishing by testing expected performance scenarios.
- Content categories with high average revenue can guide future content calendars.
- Improving comment activity can lift the interaction score and revenue score.
- The what-if simulator helps convert model output into practical creator actions.

## Report Note

The full report with all chapters, placeholders, tables, and academic front matter is available as a DOCX file in reports/final_report.