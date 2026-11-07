import streamlit as st
import pandas as pd

st.set_page_config(page_title="TechYatch Lab: Martha's Bakery", page_icon="🕵️")

st.title("🕵️ Data Detective Case #1: Martha's Bakery")
st.write("Adjust the sales and profit numbers below to help Martha find her real money-maker!")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🍞 Bread")
    bread_sold = st.number_input("Units Sold (Bread)", min_value=0, value=500, step=50)
    bread_profit = st.number_input("Profit/Unit (£) - Bread", min_value=0.0, value=1.00, step=0.25)

with col2:
    st.subheader("🎂 Cakes")
    cake_sold = st.number_input("Units Sold (Cakes)", min_value=0, value=300, step=50)
    cake_profit = st.number_input("Profit/Unit (£) - Cakes", min_value=0.0, value=5.00, step=0.50)

with col3:
    st.subheader("🍩 Doughnuts")
    donut_sold = st.number_input("Units Sold (Doughnuts)", min_value=0, value=700, step=50)
    donut_profit = st.number_input("Profit/Unit (£) - Doughnuts", min_value=0.0, value=0.50, step=0.25)

data = pd.DataFrame({
    "Product": ["Bread", "Cakes", "Doughnuts"],
    "Units Sold": [bread_sold, cake_sold, donut_sold],
    "Total Profit (£)": [
        bread_sold * bread_profit,
        cake_sold * cake_profit,
        donut_sold * donut_profit
    ]
})

st.subheader("📊 Live Bakery Summary")
st.dataframe(data, use_container_width=True)

st.subheader("📈 Profit Comparison Chart")
st.bar_chart(data.set_index("Product")["Total Profit (£)"])

best_row = data.loc[data["Total Profit (£)"].idxmax()]
st.success(f"💡 Data Detective Insight: Focus on **{best_row['Product']}**! It generates the highest total profit (£{best_row['Total Profit (£)']:.2f}).")
