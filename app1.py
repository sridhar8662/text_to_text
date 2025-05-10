import streamlit as st
import cohere

# Streamlit app layout
st.set_page_config(page_title="Text-to-Text using Cohere", page_icon="📝")
st.title("📝 Text-to-Text using Cohere")
st.markdown("Generate text using the Cohere API.")

# Input API key directly in the app
api_key = st.text_input("Enter your Cohere API Key", type="password")

# Show a warning if the API key is not provided
if not api_key:
    st.warning("⚠️ Please enter your Cohere API key to proceed.")

# Input field for the prompt to generate text
prompt = st.text_area("Enter the prompt for text generation", height=200)

# Button to trigger text generation
if st.button("Generate Text"):
    if api_key and prompt.strip():
        try:
            # Initialize the Cohere client
            co = cohere.Client(api_key)

            # Generate text using the Cohere Chat API
            response = co.chat(
                model='command-xlarge-nightly',
                message=prompt,
                temperature=0.7
            )

            # Display the generated text
            generated_text = response.text.strip()
            st.text_area("Generated Text", value=generated_text, height=200)
            st.success("✅ Text generation successful!")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
    else:
        st.warning("⚠️ Please provide both the API key and the prompt for text generation.")

# Footer
st.markdown("---")
st.caption("Powered by Cohere | Built with ❤️ using Streamlit")
