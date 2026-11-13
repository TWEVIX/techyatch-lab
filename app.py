import streamlit as st
import pandas as pd

st.set_page_config(page_title="TechYatch Lab | Virtual Internship Sandbox", page_icon="🕵️", layout="wide")

st.sidebar.title("🕵️ TechYatch Lab™")
st.sidebar.caption("A Twevix™ Innovation | Virtual Data Internship")

case_study = st.sidebar.radio(
    "Choose Your Data Detective Case:",
    [
        "Case 1: Martha's Bakery (Profit vs. Volume)",
        "Case 2: FitLife Gym (Retention & Churn)",
        "Case 3: The Smart Clinic Queue (Peak Flow)"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **The Golden Rule:** Data is information. Analysis turns it into action.")

# ==========================================
# CASE 1: MARTHA'S BAKERY
# ==========================================
if case_study == "Case 1: Martha's Bakery (Profit vs. Volume)":
    st.title("🧁 Case 1: Martha's Bakery (Profit vs. Volume)")
    st.write("Adjust the sales and profit numbers below to help Martha find her real money-maker!")
    ...
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

# ==========================================
# CASE 2: FITLIFE GYM
elif case_study == "Case 2: FitLife Gym (Retention & Churn)":
    st.header("💪 Case 2: FitLife Gym Member Churn")
    st.write("Analyze membership check-ins and reduce cancellation spikes.")
    ...
    # 1. The Interactive Dial
    churn_rate = st.slider("Simulated Churn Rate (%):", 1, 50, 12)
    
    # 2. The Cleaned Data Table (Linked to dynamic slider)
    gym_data = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
        "Cancellations": [5, 7, 6, 8, churn_rate, churn_rate + 4, churn_rate + 9],
        "Competitor Open": ["No", "No", "No", "No", "Yes", "Yes", "Yes"]
    })
    
    # 3. Displaying Content Layout Columns
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📋 Monthly Membership Log")
        st.dataframe(gym_data, use_container_width=True)
    with col2:
        st.subheader("📊 Churn Acceleration Metric")
        st.metric("Active Members Impacted", f"{churn_rate}%")

    with col1:
        st.subheader("📋 Monthly Membership Log")
        st.dataframe(gym_data, use_container_width=True)



    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("📋 Monthly Membership Log")
        st.dataframe(gym_data, use_container_width=True)

    with col2:
            st.subheader("📊 Churn Acceleration Metric")
            st.metric("Active Members Impacted", f"{churn_rate}%")

    st.subheader("🕵️ Detective Verification Check")
    suspect = st.radio(
        "Based on the data and customer feedback ('Equipment is old', 'Machines break often'), what is the best next action?",
        [
            "Blame the economy and do nothing",
            "Upgrade broken equipment and launch a member retention campaign",
            "Double membership prices immediately"
        ]
    )

    if st.button("Submit Investigation"):
        if "Upgrade broken equipment" in suspect:
            st.success("✅ Spot on, Detective! A new competitor opened in May, and equipment complaints accelerated cancellations.")
        else:
            st.warning("⚠️ Look closer at the clues—competitor entry in May plus equipment complaints explain the drop.")

# ==========================================
# CASE 3: THE SMART CLINIC QUEUE
# ==========================================
elif case_study == "Case 3: The Smart Clinic Queue (Peak Flow)":
    st.title("🏥 Case 3: The Smart Clinic Queue (Forecasting Patient Surges)")
    st.write("Imagine a clinic waiting room is a playground slide. Adjust nurse staffing to prevent long wait times during peak hours!")

    hours = ["08:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00"]
    expected_patients = [15, 28, 35, 30, 45, 60, 25]

    nurses_on_duty = st.slider("Select Nurses Scheduled for Peak Evening Shift (16:00 - 20:00):", min_value=1, max_value=10, value=3)
    patients_per_nurse_hr = 10

    clinic_df = pd.DataFrame({
        "Time": hours,
        "Predicted Patients": expected_patients,
        "Max Capacity": [nurses_on_duty * patients_per_nurse_hr] * len(hours)
    })

    st.subheader("📈 Patient Surge vs. Clinic Capacity")
    st.line_chart(clinic_df.set_index("Time"))

    peak_patients = max(expected_patients)
    capacity = nurses_on_duty * patients_per_nurse_hr

    if capacity >= peak_patients:
        st.success(f"✅ Smooth Flow! With {nurses_on_duty} nurses (capacity: {capacity} patients/hr), the clinic handles the 18:00 surge ({peak_patients} patients) with zero bottlenecks.")
    else:
        overflow = peak_patients - capacity
        st.error(f"🚨 Bottleneck Alert! At 18:00, {overflow} patients will face long delays. Increase nurses to at least {peak_patients // patients_per_nurse_hr}!")
