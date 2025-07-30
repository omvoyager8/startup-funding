import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(layout="wide", page_title="Startup Analysis")

df = pd.read_csv("startup_cleaneddd.csv")
df['date'] = pd.to_datetime(df['date'], dayfirst=True, errors='coerce')
df['month'] = df['date'].dt.month
df['Year'] = df['date'].dt.year

def load_overall_analysis():
    st.title('Overall Analysis')

    total = round(df['amount'].sum())
    max_funding = round(df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0])
    avg_funding = round(df.groupby('startup')['amount'].sum().mean())
    num_startups = df['startup'].nunique()

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric('Total', str(total) + ' Cr')
    with col2:
        st.metric('Max Funding', str(max_funding) + ' Cr')
    with col3:
        st.metric('Avg Funding', str(avg_funding) + ' Cr')
    with col4:
        st.metric('Num Startups', str(num_startups))

    st.header('MOM Graph')
    selected_option = st.selectbox('Select Type', ['Total', 'Count'])

    if selected_option == 'Total':
        temp_df = df.groupby(['Year', 'month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['Year', 'month'])['amount'].count().reset_index()

    temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['Year'].astype('str')

    fig5, ax5 = plt.subplots()
    ax5.plot(temp_df['x_axis'], temp_df['amount'])
    plt.xticks(rotation='vertical')
    st.pyplot(fig5)

def load_investor_details(investor):
    st.title(investor)
    last5_df = df[df['investors'].str.contains(investor, na=False)].head()[['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        big_series = df[df['investors'].str.contains(investor, na=False)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
        st.subheader('Biggest Investments')
        fig, ax = plt.subplots()
        ax.bar(big_series.index, big_series.values)
        st.pyplot(fig)

    with col2:
        vertical_series = df[df['investors'].str.contains(investor, na=False)].groupby('vertical')['amount'].sum()
        st.subheader('Sectors Invested In')
        fig1, ax1 = plt.subplots()
        ax1.pie(vertical_series, labels=vertical_series.index, autopct='%1.1f%%')
        st.pyplot(fig1)

    with col3:
        round_series = df[df['investors'].str.contains(investor, na=False)].groupby('round')['amount'].sum()
        st.subheader('Stages Invested In')
        fig2, ax2 = plt.subplots()
        ax2.pie(round_series, labels=round_series.index, autopct='%1.1f%%')
        st.pyplot(fig2)

    with col4:
        city_series = df[df['investors'].str.contains(investor, na=False)].groupby('city')['amount'].sum()
        st.subheader('Cities Invested In')
        fig3, ax3 = plt.subplots()
        ax3.pie(city_series, labels=city_series.index, autopct='%1.1f%%')
        st.pyplot(fig3)

    # Year-on-year investment chart
    year_series = df[df['investors'].str.contains(investor, na=False)].groupby('Year')['amount'].sum()
    st.subheader('YoY Investment')
    fig4, ax4 = plt.subplots()
    ax4.plot(year_series.index, year_series.values)
    st.pyplot(fig4)

# Sidebar Navigation
st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('Select One', ['Overall Analysis', 'Startup', 'Investor'])

if option == 'Overall Analysis':
    load_overall_analysis()

elif option == 'Startup':
    selected_startup = st.sidebar.selectbox('Select Startup', sorted(df['startup'].unique().tolist()))
    btn1 = st.sidebar.button('Find Startup Details')
    st.title('Startup Analysis')
    # You can add startup-related functions here

else:
    selected_investor = st.sidebar.selectbox('Select Investor', sorted(set(sum(df['investors'].dropna().str.split(','), []))))
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_details(selected_investor)
        st.title('Investor Analysis')
