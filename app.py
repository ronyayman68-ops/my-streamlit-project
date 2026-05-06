import streamlit as st
st.set_page_config(page_title="Rawan's Budget Tracker", layout="wide")

ICON_MAP = {
    "Food": "https://openmoji.org/data/color/svg/1F355.svg",        
    "Transport": "https://openmoji.org/data/color/svg/1F697.svg",   
    "Tech": "https://openmoji.org/data/color/svg/1F4BB.svg",        
    "Entertainment": "https://openmoji.org/data/color/svg/1F3AC.svg", 
    "Other": "https://openmoji.org/data/color/svg/1F4B0.svg"         
}

st.title("💸 Smart Budget & Expense Visualizer")


if 'expenses' not in st.session_state:
    st.session_state.expenses = []

st.sidebar.header("Configuration")
monthly_budget = st.sidebar.number_input("Set Monthly Budget ($):", min_value=10.0, value=500.0, step=50.0)

if st.sidebar.button("Reset All Data"):
    st.session_state.expenses = []
    st.rerun()


with st.container():
    st.subheader("Add New Expense")
    col1, col2, col3 = st.columns([3, 2, 2])

    with col1:
        item_name = st.text_input("What did you buy?", placeholder="e.g., Freelance Software License")
    with col2:
        amount = st.number_input("Amount ($):", min_value=0.0, step=1.0)
    with col3:
        category = st.selectbox("Category:", list(ICON_MAP.keys()))

    if st.button("Add to Tracker", use_container_width=True):
        if item_name and amount > 0:
            st.session_state.expenses.append({
                "Name": item_name, 
                "Amount": amount, 
                "Category": category
            })
            st.success(f"Successfully added {item_name}!")
        else:
            st.error("Please enter both a name and a valid amount.")


if st.session_state.expenses:
    total_spent = sum(item["Amount"] for item in st.session_state.expenses)
    remaining = monthly_budget - total_spent
    utilization = (total_spent / monthly_budget) * 100

    st.write("---")
    st.subheader("Financial Overview")
    

    m1, m2, m3 = st.columns(3)
    m1.metric("Total Spent", f"${total_spent:,.2f}")
    m2.metric("Remaining Budget", f"${remaining:,.2f}", delta=f"{remaining:,.2f}", delta_color="normal")
    m3.metric("Budget Used", f"{utilization:.1f}%")

    progress_color = min(total_spent / monthly_budget, 1.0)
    if total_spent > monthly_budget:
        st.error(f"You are ${abs(remaining):,.2f} over budget!")
    
    st.progress(progress_color)

    st.write("Expense History")
    for item in st.session_state.expenses:
        with st.expander(f"{item['Name']} - ${item['Amount']}", expanded=True):
            c1, c2, c3 = st.columns([1, 5, 2])
            with c1:
                st.image(ICON_MAP.get(item["Category"]), width=50)
            with c2:
                st.write(f"**Description:** {item['Name']}")
                st.write(f"**Category:** {item['Category']}")
            with c3:
                st.write(f"### ${item['Amount']:,.2f}")

else:
    st.info("No expenses tracked yet. Enter your first purchase above to see the dashboard!")