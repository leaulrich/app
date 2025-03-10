import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import random
import time


# Load dataset
tips = sns.load_dataset("tips")

# Create the scatter plot
fig1, ax = plt.subplots()
sns.regplot(data=tips, x="total_bill", y="tip", ax=ax)
ax.set_title("Tips vs Total Bill")
question1="Are the tip and total bill correlated?"
pair1=(question1, fig1)

fig2, ax = plt.subplots()
sns.barplot(data=tips, x="day", y="total_bill", ax=ax)
ax.set_title("Average revenue by day")
question2="Which days generate the highest revenue?"
pair2=(question2, fig2)


# Initialize session state variables
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "show_answer_button" not in st.session_state:
    st.session_state.show_answer_button = False  # Control visibility of the answer button

# Start button logic
if st.button("Click to Start"):
    st.session_state.start_time = time.time()
    st.session_state.show_answer_button = True  # Show answer button when you click start

    # Display a random chart
    chosen = random.choice((pair1, pair2))
    question, chart = chosen
    st.title(question)
    st.pyplot(chart)

# Button to Record Response Time
if st.session_state.show_answer_button:
    if st.button("I answered your question"):
        elapsed_time = round(time.time() - st.session_state.start_time, 2)
        st.write(f"You took {elapsed_time} seconds to answer.")
        st.session_state.show_answer_button = False  # Hide the answer button after clicking it