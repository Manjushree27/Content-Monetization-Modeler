# EDA and Cleaning Report

## Dataset Overview

- Rows: 122,400
- Columns: 12
- Target variable: `ad_revenue_usd`
- Duplicate rows found: 2,400
- Cleaned rows after processing: 120,000

## Data Types

| index | dtype |
| --- | --- |
| video_id | str |
| date | str |
| views | int64 |
| likes | float64 |
| comments | float64 |
| watch_time_minutes | float64 |
| video_length_minutes | float64 |
| subscribers | int64 |
| category | str |
| device | str |
| country | str |
| ad_revenue_usd | float64 |

## Missing Values

| index | missing_count |
| --- | --- |
| video_id | 0 |
| date | 0 |
| views | 0 |
| likes | 6117 |
| comments | 6112 |
| watch_time_minutes | 6105 |
| video_length_minutes | 0 |
| subscribers | 0 |
| category | 0 |
| device | 0 |
| country | 0 |
| ad_revenue_usd | 0 |

## Outlier Detection

IQR method was used because it is simple to explain and suitable for a fresher-level project.

| Column | Lower Bound | Upper Bound | Outlier Count |
|---|---:|---:|---:|
| views | 9,732.00 | 10,268.00 | 878 |
| likes | -601.00 | 2,799.00 | 0 |
| comments | -151.50 | 700.50 | 0 |
| watch_time_minutes | -4,922.45 | 80,087.52 | 0 |
| video_length_minutes | -12.02 | 44.05 | 0 |
| subscribers | -497,019.25 | 1,501,718.75 | 0 |
| ad_revenue_usd | 41.36 | 464.14 | 0 |

## Visualization Findings

1. Revenue distribution shows most videos earn in a middle band, with fewer very high earning videos.
2. Category analysis helps identify content themes with better revenue potential.
3. Device analysis shows how viewing behavior changes revenue opportunities.
4. Country-level analysis is useful because ad rates differ by market.
5. Engagement rate has a positive business meaning because likes and comments show viewer interest.
6. Watch time is important because longer attention gives more ad-serving opportunity.
7. Correlation analysis confirms which numerical variables move most closely with revenue.

## Cleaning Decisions

- Missing numerical values were filled with median values to avoid distortion from high values.
- Missing categorical values were filled as `Unknown`.
- Duplicate rows were removed because they can bias training.
- Outliers were capped using IQR bounds instead of deleted, so useful rows were retained.
- Text categories were stripped and title-cased for consistency.
