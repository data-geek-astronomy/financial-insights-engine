<<<<<<< HEAD
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
=======
# 💡 Financial Insights & Personalization Engine

An intelligent analytics platform that combines advanced machine learning, customer segmentation, and personalized recommendations to help financial technology companies optimize customer relationships and drive business growth.

## 🎯 Project Overview

This project demonstrates enterprise-grade data science capabilities aligned with Intuit's Staff Data Scientist role requirements. It showcases:

- **Customer Segmentation**: KMeans clustering to identify 4 distinct customer segments
- **Financial Health Scoring**: ML-driven composite scoring model
- **Cash Flow Forecasting**: Time-series analysis for revenue prediction
- **Personalized Recommendations**: Segment-based product recommendations engine
- **Advanced Analytics Dashboard**: Interactive Streamlit UI with Intuit design language

## 📊 Key Features

### 1. Customer Segmentation
- **High-Value Enterprise**: Premium customers with highest revenue and engagement
- **Growth Potential**: Emerging customers with strong engagement but lower current revenue
- **At-Risk Customers**: High-value but declining engagement segments
- **New & Engaged**: Newly acquired, highly engaged customer base

### 2. Financial Health Score
Composite metric combining:
- Monthly Revenue (30% weight)
- Engagement Score (30% weight)  
- Customer Lifetime Value (40% weight)

### 3. Predictive Analytics
- **Cash Flow Forecasting**: Linear regression-based 6-month revenue forecast
- **Engagement Prediction**: Time-series analysis of customer engagement trends
- **Churn Risk Assessment**: Identification of at-risk customer segments

### 4. Personalization Engine
Context-aware product recommendations based on:
- Customer segment classification
- Financial health trajectory
- Transaction patterns
- Engagement metrics
>>>>>>> 6fb26a773937460627a5178387b164987b77c1e3

## 🛠️ Tech Stack

- **Frontend**: Streamlit (Interactive Dashboard)
- **ML/Data**: scikit-learn, pandas, numpy
- **Visualization**: Plotly
- **Design**: Custom Intuit-inspired CSS styling

## 📁 Project Structure

```
financial-insights-engine/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── .gitignore            # Git ignore rules
```

<<<<<<< HEAD
## Installation

```bash
pip install -r requirements.txt
streamlit run app.py
```

=======
## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip or conda package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/data-geek-astronomy/financial-insights-engine.git
cd financial-insights-engine
```

2. **Create a virtual environment (optional but recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

### Running the Application

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

>>>>>>> 6fb26a773937460627a5178387b164987b77c1e3
## 📈 Usage Guide

### Dashboard Navigation

1. **Key Performance Metrics**
   - View aggregated KPIs for selected customer segments
   - Monitor financial health, revenue, and engagement trends

2. **Segmentation Tab** 🎯
   - Visualize customer distribution across segments
   - Analyze segment characteristics (revenue, CLV, engagement)
   - Financial Health Matrix showing customer positioning

3. **Forecasting Tab** 📈
   - 6-month cash flow forecast with confidence intervals
   - Historical trend analysis
   - Revenue growth projections

4. **Recommendations Tab** 🛍️
   - View AI-generated product recommendations by segment
   - Personalization rationale based on customer profile
   - Cross-sell and upsell opportunities

5. **Customer Details Tab** 💼
   - Search and filter individual customer profiles
   - View complete customer metrics and assigned segments
   - Export data for further analysis

### Filtering

Use the sidebar to filter by customer segment and view metrics specific to your target audience.

## 🤖 Machine Learning Models

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
Application: Inventory, staffing, investment planning
```

## 📊 Data Model

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

## 🎨 Design & UX

The UI follows Intuit design principles:
- **Color Palette**: Teal (#2DD4BF), Blue (#0EA5E9), Dark Gray (#1F2937)
- **Typography**: Clean, modern sans-serif fonts
- **Layout**: 4-column responsive grid
- **Interactivity**: Plotly charts with hover details
- **Accessibility**: High contrast, readable text

## 🔧 Configuration

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

<<<<<<< HEAD

=======
## 📚 Skills Demonstrated

### Data Science
- ✅ Customer segmentation and clustering
- ✅ Feature engineering and normalization
- ✅ Time-series forecasting
- ✅ Statistical analysis and metric design
- ✅ Data visualization and storytelling

### Machine Learning
- ✅ Unsupervised learning (KMeans)
- ✅ Supervised learning (Linear Regression)
- ✅ Model evaluation and validation
- ✅ Feature scaling and preprocessing

### Software Engineering
- ✅ Clean, modular code architecture
- ✅ Caching for performance optimization
- ✅ Interactive dashboard development
- ✅ Documentation and best practices

### Business Analytics
- ✅ KPI definition and monitoring
- ✅ Customer lifetime value modeling
- ✅ Segment-based strategy
- ✅ Data-driven recommendations

## 🚢 Deployment

### Streamlit Cloud
1. Push repository to GitHub
2. Go to [Streamlit Cloud](https://share.streamlit.io/)
3. Create new app and connect your GitHub repo
4. Streamlit automatically deploys on every push

### Local Deployment
```bash
streamlit run app.py --logger.level=error
```

### Docker
Create a `Dockerfile` for containerized deployment:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
CMD ["streamlit", "run", "app.py"]
```

## 📈 Future Enhancements

- [ ] Real database integration (PostgreSQL/MongoDB)
- [ ] Real customer data pipeline
- [ ] Advanced causal inference models
- [ ] A/B testing framework integration
- [ ] Multi-armed bandit optimization
- [ ] Real-time metric updates
- [ ] User authentication and role-based access
- [ ] Export functionality (PDF reports, CSV)
- [ ] Advanced time-series models (ARIMA, Prophet)
- [ ] Recommendation system optimization with collaborative filtering

## 🔐 Data Privacy & Compliance

- Customer data is anonymized with ID prefixes
- No personal identifying information stored
- Compliant with data governance best practices
- Suitable for sensitive financial data

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💼 About

**Built for**: Intuit Staff Data Scientist role requirements  
**Project Type**: Customer Analytics & Personalization Platform  
**Tech Stack**: Python, Streamlit, scikit-learn, Plotly  
**Use Case**: Financial technology customer intelligence and optimization

## 📞 Contact & Support

For questions or issues:
- Open an issue on GitHub
- Review the documentation above
- Check Streamlit documentation: https://docs.streamlit.io

## 🙏 Acknowledgments

- Inspired by Intuit's mission to empower financial success
- Built with Streamlit's interactive framework
- Designed following modern data science best practices
- UI/UX principles from Intuit's design language

---

**Last Updated**: June 2026  
**Version**: 1.0.0  
**Status**: Production Ready
>>>>>>> 6fb26a773937460627a5178387b164987b77c1e3
