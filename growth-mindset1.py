import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Growth Mindset Challenge",
    page_icon="🌱",
    layout="centered",
)

# Title and Introduction
st.title("🌱 Growth Mindset Challenge")
st.write("""
Welcome to the **Growth Mindset Challenge** web app!
This app will help you understand what a growth mindset is and how you can adopt it in your life.
""")

# Section: What is Growth Mindset?
st.header("What is a Growth Mindset?")
st.write("""
A growth mindset is the belief that your abilities and intelligence can be developed through hard work, perseverance, and learning from mistakes.
This concept was popularized by psychologist **Carol Dweck**.
""")

# Section: Why Adopt a Growth Mindset?
st.header("Why Adopt a Growth Mindset?")
reasons = [
    "✅ Embrace Challenges",
    "✅ Learn from Mistakes",
    "✅ Persist Through Difficulties",
    "✅ Celebrate Effort",
    "✅ Keep an Open Mind"
]
for reason in reasons:
    st.write(reason)

# Section: How to Practice It?
st.header("How Can You Practice a Growth Mindset?")
tips = [
    "🎯 Set Learning Goals",
    "🔍 Reflect on Your Learning",
    "💬 Seek Feedback",
    "😊 Stay Positive"
]
for tip in tips:
    st.write(tip)

# Interactive Section: Reflection
st.subheader("Your Growth Reflection")
reflection = st.text_area("Write about a time you turned a mistake into a learning opportunity:")

if st.button("Submit Reflection"):
    if reflection.strip():
        st.success("Thank you for sharing your experience! Keep growing!")
    else:
        st.warning("Please write something before submitting.")

# Final Message
st.markdown("---")
st.info("Remember: Every step, forward or backward, is part of your learning process. Keep going!")

# Footer
st.markdown("Made with ❤️ **Najma Ibrahim** using Streamlit")