# Financial Insights & Personalization Engine

A customer analytics platform for financial technology companies that combines machine learning, customer segmentation, and personalized recommendations to optimize customer relationships and business growth.

## Features

- **Customer Segmentation**: Identifies 4 distinct customer groups using clustering
- **Financial Health Scoring**: Composite scoring model based on revenue, engagement, and lifetime value
- **Cash Flow Forecasting**: 6-month revenue predictions
- **Personalized Recommendations**: Product recommendations by customer segment
- **Analytics Dashboard**: Interactive dashboard with key metrics and visualizations

## Core Components

### Customer Segments
- High-Value Enterprise: Premium customers with highest revenue and engagement
- Growth Potential: Emerging customers with strong engagement
- At-Risk Customers: High-value customers with declining engagement
- New & Engaged: Newly acquired, highly engaged customers

### Metrics
- Financial Health Score (0-100): Composite of revenue, engagement, and lifetime value
- Cash Flow Forecast: 6-month revenue predictions
- Customer Lifetime Value: Predicted total customer value
- Engagement Score: Customer activity metric

## Tech Stack

- **Frontend**: Streamlit (Interactive Dashboard)
- **ML/Data**: scikit-learn, pandas, numpy
- **Visualization**: Plotly
- **Design**: Custom Intuit-inspired CSS styling

## Project Structure

```
financial-insights-engine/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── .gitignore            # Git ignore rules
```

## Installation

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Usage Guide

### Dashboard Navigation

1. **Key Performance Metrics**
   - View aggregated KPIs for selected customer segments
   - Monitor financial health, revenue, and engagement trends

2. **Segmentation Tab**
   - Visualize customer distribution across segments
   - Analyze segment characteristics (revenue, CLV, engagement)
   - Financial Health Matrix showing customer positioning

3. **Forecasting Tab**
   - 6-month cash flow forecast
   - Historical trend analysis
   - Revenue growth projections

4. **Recommendations Tab**
   - View product recommendations by segment
   - Personalization rationale based on customer profile
   - Cross-sell and upsell opportunities

5. **Customer Details Tab**
   - Search and filter individual customer profiles
   - View complete customer metrics and assigned segments

### Filtering

Use the sidebar to filter by customer segment and view metrics specific to your target audience.

## Machine Learning Models

### Customer Segmentation (KMeans Clustering)
```
Features: Revenue, Transaction Frequency, Account Age, Avg Transaction Value, Engagement
Output: 4 distinct customer segments
Performance: Silhouette Score optimization
```

### Financial Health Scoring
```
Formula: (Revenue_norm × 0.3) + (Engagement_norm × 0.3) + (CLV_norm × 0.4)
Range: 0-100
Use Case: Customer prioritization and targeting
```

### Cash Flow Forecasting (Linear Regression)
```
Model: Linear Regression on historical revenue data
Horizon: 6 months forward
Features: Time index
Application: Revenue projection and planning
```

## Data Model

### Customer Attributes
- `customer_id`: Unique customer identifier
- `monthly_revenue`: Current monthly revenue
- `transaction_frequency`: Transactions per month
- `account_age_months`: Customer tenure
- `product_count`: Number of products used
- `avg_transaction_value`: Average transaction amount
- `customer_lifetime_value`: Predicted total lifetime value
- `engagement_score`: 0-100 engagement metric
- `financial_health_score`: Computed health metric
- `segment_name`: Assigned customer segment
- `recommended_products`: Personalized recommendations

## Design

The UI follows Intuit design principles:
- **Color Palette**: Teal (#2DD4BF), Blue (#0EA5E9), Dark Gray (#1F2937)
- **Typography**: Clean, modern sans-serif fonts
- **Layout**: 4-column responsive grid
- **Interactivity**: Plotly charts with hover details
- **Accessibility**: High contrast, readable text

## Configuration

### Adjusting Segmentation
Edit the `n_clusters` parameter in `perform_segmentation()`:
```python
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
```

### Modifying Weights in Health Score
Update the weights in the financial_health_score calculation:
```python
df['financial_health_score'] = (
    (df['monthly_revenue'] / df['monthly_revenue'].max() * 0.3) +
    (df['engagement_score'] / 100 * 0.3) +
    (df['customer_lifetime_value'] / df['customer_lifetime_value'].max() * 0.4)
) * 100
```
