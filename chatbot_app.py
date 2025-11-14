import streamlit as st
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader 
from langchain_text_splitters import RecursiveCharacterTextSplitter 


load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
 
    st.error("GEMINI_API_KEY ortam değişkeni bulunamadı. Lütfen .env dosyanızı veya Streamlit Secrets ayarlarınızı kontrol edin.")
    st.stop()


@st.cache_resource(show_spinner=True)
def setup_rag_pipeline():
    
    EMBEDDING_MODEL_NAME = "text-embedding-004"
    
    
    try:

        loader = TextLoader("yatirim_verileri.txt", encoding="utf-8")
        documents = loader.load()
        

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, 
            chunk_overlap=100,
            separators=["\n\n", "\n", " ", ""]
        )
        texts = text_splitter.split_documents(documents)


        embedding_model = GoogleGenerativeAIEmbeddings(
            model=EMBEDDING_MODEL_NAME, 
            google_api_key=API_KEY
        )
 
        vectorstore = Chroma.from_documents(
            documents=texts,  
            embedding=embedding_model, 
    
        )
       
        
    except FileNotFoundError:
        st.error("HATA: 'yatirim_verileri.txt' dosyası bulunamadı. Lütfen GitHub deponuza eklediğinizden emin olun.")
 
        return None, None
    except Exception as e:
        st.error(f"RAG kurulumunda beklenmeyen bir hata oluştu: {e}")
        return None, None


    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash", 
        google_api_key=API_KEY,
        temperature=0.1
    )
    
    prompt = ChatPromptTemplate.from_template("""
    Sen, Akıllı Yatırım Asistanısın. Görevin, SADECE sağlanan bağlam bilgisine (Context) dayanarak 
    kullanıcının yatırım ve finansal konularla ilgili sorularını yanıtlamaktır. 
    Eğer bağlamda soruya dair net bir bilgi yoksa, "Üzgünüm, bu konuda elimdeki veri setinde yeterli bilgi bulunmamaktadır." 
    diye yanıt ver. Fikir yürütme veya genel bilgi verme.

    Bağlam (Context):
    {context}

    Soru: {question}
    """)

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    rag_chain = (
        {"context": retriever | RunnableLambda(format_docs), "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    return rag_chain, retriever

rag_chain, retriever = setup_rag_pipeline()

st.set_page_config(page_title="Akıllı Yatırım Asistanı RAG Chatbot")

st.title("💰 Akıllı Yatırım Asistanı")
st.caption("Veri setine dayalı RAG Chatbot (Gemini + LangChain + ChromaDB)")

if rag_chain is None:
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Yatırım veya finans ile ilgili bir soru sorunuz..."):

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Asistan yanıt oluşturuyor..."):
            
            response = rag_chain.invoke(prompt)
            st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

