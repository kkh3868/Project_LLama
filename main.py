import streamlit as st
from langchain_community.llms import CTransformers
#hello
llm = CTransformers( 
    model="llama-2-7b-chat.ggmlv3.q5_0.bin",
    model_type="llama"
)

st.title("SC 알고리즘 Task Llama2 인공지능")

# Function to generate code
def generate_code(content):
    result = llm.predict("write the C# code exmaple about" + content + ": ")
    return result

# Create or load conversation history
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []

# Function to display conversation history
def display_history():
    st.write("## Conversation History")
    for idx, (query, response) in enumerate(st.session_state.conversation_history, 1):
        st.write(f"**Query {idx}:** {query}")
        st.write(f"**Response {idx}:** {response}")
        st.write("---")

content = st.text_input('코드 작성 요청하기')

if st.button('코드 요청'):
    with st.spinner('코드 작성중...'):
        result = generate_code(content)
        st.write(result)
        # Append the current query and response to conversation history
        st.session_state.conversation_history.append((content, result))

# Display conversation history if requested
if st.checkbox('Show Conversation History'):
    display_history()
