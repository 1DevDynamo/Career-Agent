from langchain_google_genai import ChatGoogleGenerativeAI
from app.configure import GOOGLE_API_KEY

def get_gemini_llm(model="gemini-1.5-pro"):
    try:
        return ChatGoogleGenerativeAI(
            google_api_key=GOOGLE_API_KEY,
            model=model,
            temperature=0.3
        )
    except Exception as e:
        print(f"⚠ Gemini error: {e}, using mock model instead.")
        return lambda x: "Mock response for testing"


