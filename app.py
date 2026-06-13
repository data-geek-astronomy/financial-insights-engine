import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings('ignore')

# Set page config with Intuit-style colors
st.set_page_config(
    page_title="Financial Insights & Personalization",
    page_icon="💡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Intuit-style color scheme
INTUIT_TEAL = "#2DD4BF"
INTUIT_BLUE = "#0EA5E9"
INTUIT_DARK = "#1F2937"
INTUIT_LIGHT = "#F3F4F6"
INTUIT_GREEN = "#10B981"
INTUIT_RED = "#EF4444"

# Custom CSS for Intuit-style UI
st.markdown(f"""
    <style>
        /* Main container styling */
        .main {{
            background-color: #FFFFFF;
        }}

        /* Header styling */
        .header-title {{
            color: {INTUIT_DARK};
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }}

        .header-subtitle {{
            color: #6B7280;
            font-size: 1.1rem;
            margin-bottom: 2rem;
        }}

        /* Metric card styling */
        .metric-card {{
            background: linear-gradient(135deg, {INTUIT_BLUE}15, {INTUIT_TEAL}15);
            border-left: 4px solid {INTUIT_BLUE};
            padding: 1.5rem;
            border-radius: 8px;
            margin-bottom: 1rem;
        }}

        /* Section header */
        .section-header {{
            color: {INTUIT_DARK};
            font-size: 1.5rem;
            font-weight: 600;
            margin: 2rem 0 1rem 0;
            border-bottom: 2px solid {INTUIT_TEAL};
            padding-bottom: 0.5rem;
        }}

        /* Tab styling */
        .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {{
            font-size: 1rem;
            font-weight: 500;
        }}

        /* Sidebar styling */
        .sidebar .sidebar-content {{
            background-color: {INTUIT_LIGHT};
        }}
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Generate synthetic customer financial data"""
    np.random.seed(42)
    n_customers = 500

    data = {
        'customer_id': [f'CUST_{i:05d}' for i in range(1, n_customers + 1)],
        'monthly_revenue': np.random.exponential(2000, n_customers),
        'transaction_frequency': np.random.poisson(15, n_customers),
        'account_age_months': np.random.exponential(30, n_customers),
        'product_count': np.random.poisson(2, n_customers),
        'avg_transaction_value': np.random.gamma(2, 500, n_customers),
        'customer_lifetime_value': np.random.exponential(50000, n_customers),
        'engagement_score': np.random.uniform(0, 100, n_customers),
    }

    df = pd.DataFrame(data)
    df['financial_health_score'] = (
        (df['monthly_revenue'] / df['monthly_revenue'].max() * 0.3) +
        (df['engagement_score'] / 100 * 0.3) +
        (df['customer_lifetime_value'] / df['customer_lifetime_value'].max() * 0.4)
    ) * 100

    return df

@st.cache_data
def perform_segmentation(df):
    """Perform customer segmentation using KMeans"""
    features = ['monthly_revenue', 'transaction_frequency', 'account_age_months',
                'avg_transaction_value', 'engagement_score']

    scaler = StandardScaler()
    X = scaler.fit_transform(df[features])

    kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
    df['segment'] = kmeans.fit_predict(X)

    segment_names = {
        0: 'High-Value Enterprise',
        1: 'Growth Potential',
        2: 'At-Risk Customers',
        3: 'New & Engaged'
    }
    df['segment_name'] = df['segment'].map(segment_names)

    return df

@st.cache_data
def predict_cash_flow(df):
    """Time-series forecasting for cash flow"""
    model = LinearRegression()
    X = np.arange(len(df)).reshape(-1, 1)
    y = df['monthly_revenue'].values
    model.fit(X, y)

    future_months = 6
    future_X = np.arange(len(df), len(df) + future_months).reshape(-1, 1)
    forecast = model.predict(future_X)

    return forecast

@st.cache_data
def generate_recommendations(df):
    """Generate personalized product recommendations"""
    recommendations = {
        'High-Value Enterprise': ['Advanced Analytics Suite', 'Custom Integration Tools', 'Dedicated Support'],
        'Growth Potential': ['Time Tracking Software', 'Invoice Management', 'Cash Flow Analytics'],
        'At-Risk Customers': ['Financial Planning Tools', 'Cost Optimization Guide', 'Premium Support'],
        'New & Engaged': ['Expense Tracking', 'Business Dashboard', 'Mobile App Access']
    }

    df['recommended_products'] = df['segment_name'].map(
        lambda x: ', '.join(recommendations.get(x, []))
    )

    return df

# Load and process data
df = load_data()
df = perform_segmentation(df)
df = generate_recommendations(df)

# Header
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown('<div class="header-title">💡 Financial Insights & Personalization</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="header-subtitle">AI-Powered Customer Analytics & Smart Recommendations</div>',
                unsafe_allow_html=True)
with col2:
    st.metric("Total Customers", f"{len(df):,}")

st.divider()

# Sidebar filters
st.sidebar.markdown("### 🎯 Filters")
selected_segment = st.sidebar.multiselect(
    "Customer Segment",
    options=df['segment_name'].unique(),
    default=df['segment_name'].unique(),
    key="segment_filter"
)

filtered_df = df[df['segment_name'].isin(selected_segment)]

# Key Metrics Row
st.markdown('<div class="section-header">📊 Key Performance Metrics</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    avg_health = filtered_df['financial_health_score'].mean()
    st.metric(
        "Avg Health Score",
        f"{avg_health:.1f}%",
        delta=f"{avg_health - df['financial_health_score'].mean():.1f}%",
        delta_color="inverse"
    )

with col2:
    total_revenue = filtered_df['monthly_revenue'].sum()
    st.metric(
        "Total Monthly Revenue",
        f"${total_revenue:,.0f}",
        delta=f"+{total_revenue/df['monthly_revenue'].sum()*100:.1f}%"
    )

with col3:
    avg_clv = filtered_df['customer_lifetime_value'].mean()
    st.metric(
        "Avg Customer Lifetime Value",
        f"${avg_clv:,.0f}",
        delta=f"+${avg_clv - df['customer_lifetime_value'].mean():,.0f}"
    )

with col4:
    engagement = filtered_df['engagement_score'].mean()
    st.metric(
        "Engagement Score",
        f"{engagement:.1f}",
        delta=f"+{engagement - df['engagement_score'].mean():.1f}"
    )

st.divider()

# Main content tabs
tab1, tab2, tab3, tab4 = st.tabs(["🎯 Segmentation", "📈 Forecasting", "🛍️ Recommendations", "💼 Customer Details"])

# Tab 1: Segmentation
with tab1:
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Customer Segments Distribution")
        segment_counts = filtered_df['segment_name'].value_counts()
        colors = [INTUIT_BLUE, INTUIT_TEAL, INTUIT_RED, INTUIT_GREEN]

        fig = go.Figure(data=[
            go.Pie(
                labels=segment_counts.index,
                values=segment_counts.values,
                marker=dict(colors=colors),
                textposition='inside',
                textinfo='label+percent',
                hovertemplate='<b>%{label}</b><br>Count: %{value}<br>Percentage: %{percent}<extra></extra>'
            )
        ])
        fig.update_layout(height=400, showlegend=True, margin=dict(l=0, r=0, t=0, b=0))
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("### Segment Characteristics")
        segment_stats = filtered_df.groupby('segment_name').agg({
            'monthly_revenue': 'mean',
            'customer_lifetime_value': 'mean',
            'engagement_score': 'mean',
            'customer_id': 'count'
        }).round(0)
        segment_stats.columns = ['Avg Revenue', 'Avg CLV', 'Engagement', 'Count']

        st.dataframe(segment_stats, use_container_width=True)

    # Scatter plot: Revenue vs Engagement
    st.markdown("### Financial Health Matrix")
    fig = px.scatter(
        filtered_df,
        x='engagement_score',
        y='monthly_revenue',
        color='segment_name',
        size='customer_lifetime_value',
        hover_data=['customer_id', 'financial_health_score'],
        color_discrete_map={
            'High-Value Enterprise': INTUIT_BLUE,
            'Growth Potential': INTUIT_TEAL,
            'At-Risk Customers': INTUIT_RED,
            'New & Engaged': INTUIT_GREEN
        },
        title='Customer Position: Engagement vs Revenue'
    )
    fig.update_layout(height=400, hovermode='closest')
    st.plotly_chart(fig, use_container_width=True)

# Tab 2: Forecasting
with tab2:
    st.markdown("### Cash Flow Forecast (Next 6 Months)")

    forecast = predict_cash_flow(filtered_df)
    months = ['Month +1', 'Month +2', 'Month +3', 'Month +4', 'Month +5', 'Month +6']

    fig = go.Figure()

    # Historical data
    historical = filtered_df['monthly_revenue'].tail(12)
    fig.add_trace(go.Scatter(
        y=historical.values,
        name='Historical',
        mode='lines',
        line=dict(color=INTUIT_BLUE, width=3),
        fill='tozeroy',
        fillcolor=f'{INTUIT_BLUE}20'
    ))

    # Forecast
    fig.add_trace(go.Scatter(
        y=forecast,
        name='Forecast',
        mode='lines+markers',
        line=dict(color=INTUIT_TEAL, width=3, dash='dash'),
        marker=dict(size=8)
    ))

    fig.update_layout(
        title='Revenue Forecast Analysis',
        xaxis_title='Time Period',
        yaxis_title='Revenue ($)',
        height=400,
        hovermode='x unified'
    )
    st.plotly_chart(fig, use_container_width=True)

    # Forecast metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Current Avg Revenue", f"${filtered_df['monthly_revenue'].mean():,.0f}")
    with col2:
        st.metric("Forecasted Avg (6M)", f"${forecast.mean():,.0f}",
                 delta=f"{((forecast.mean()/filtered_df['monthly_revenue'].mean() - 1)*100):.1f}%")
    with col3:
        st.metric("Trend", "📈 Upward" if forecast[-1] > forecast[0] else "📉 Downward")

# Tab 3: Recommendations
with tab3:
    st.markdown("### Personalized Product Recommendations")

    # Recommendation engine
    col1, col2 = st.columns([2, 1])

    with col1:
        st.info("🤖 **AI-Powered Recommendations**: Each customer receives tailored product suggestions based on their segment, financial health, and engagement patterns.")

    with col2:
        show_recommendations = st.checkbox("Show Top Recommendations", value=True)

    if show_recommendations:
        # Group by segment and show recommendations
        for segment in filtered_df['segment_name'].unique():
            segment_data = filtered_df[filtered_df['segment_name'] == segment]

            col1, col2, col3 = st.columns([2, 1, 1])
            with col1:
                st.markdown(f"**{segment}**")
                if len(segment_data) > 0:
                    recommendation = segment_data.iloc[0]['recommended_products']
                    st.markdown(f"💡 {recommendation}")
            with col2:
                st.metric("Segment Size", len(segment_data))
            with col3:
                avg_score = segment_data['financial_health_score'].mean()
                st.metric("Avg Score", f"{avg_score:.0f}%")

            st.divider()

# Tab 4: Customer Details
with tab4:
    st.markdown("### Customer Database")

    # Search/filter
    search = st.text_input("Search by Customer ID", "")

    display_df = filtered_df.copy()
    if search:
        display_df = display_df[display_df['customer_id'].str.contains(search, case=False)]

    # Display columns
    display_cols = ['customer_id', 'segment_name', 'monthly_revenue', 'financial_health_score',
                    'customer_lifetime_value', 'engagement_score', 'recommended_products']

    st.dataframe(
        display_df[display_cols].sort_values('financial_health_score', ascending=False),
        use_container_width=True,
        height=400
    )

    st.caption(f"Showing {len(display_df)} of {len(filtered_df)} customers")

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #6B7280; padding: 2rem 0;'>
    <p><strong>Financial Insights & Personalization Engine</strong></p>
    <p>Powered by Advanced ML & Data Science | Built with Streamlit & Intuit Design Principles</p>
</div>
""", unsafe_allow_html=True)
