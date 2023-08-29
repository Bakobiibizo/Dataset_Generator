import streamlit as st

st.title("Dataset Generator")

main_container = st.container()

main_container.selectbox("Select an API:" , ["OpenAI","Open Assistant"] , index=0)
main_container.selectbox("Select the Datatype You Want to Use:" , ["Option 1","Option 2","Option 3"] , index=0)
main_container.file_uploader("Upload Your Dataset:")
main_container.button("Generate Dataset")

st.divider()
feedback_container = st.container()

feedback_container.subheader("Feedback")
feedback_container.selectbox("Please rate your experience with the dataset generator:", [1, 2, 3, 4, 5], index=0)
feedback_container.text_area("Provide any additional feedback on your experience:")
feedback_container.button("Submit")

st.sidebar.title("API Settings")
st.sidebar.text_input("Enter your API Key:")
st.sidebar.selectbox("Select the API:", ["OpenAI","Open Assistant"], index=0)
st.sidebar.button("Save")
