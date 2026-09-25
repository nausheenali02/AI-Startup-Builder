import sys
import os
from importlib.metadata import version
from dotenv import load_dotenv

load_dotenv()

def test_environment():
    print(f"[OK] Python Version: {sys.version.split()[0]}")
    
    import langchain_core
    import langgraph
    import pydantic
    
    langgraph_ver = getattr(langgraph, "__version__", None) or version("langgraph")
    
    print(f"[OK] LangChain Core Version: {langchain_core.__version__}")
    print(f"[OK] LangGraph Version: {langgraph_ver}")
    print(f"[OK] Pydantic Version: {pydantic.__version__}")

    # Check for keys
    gemini_key = os.getenv("GOOGLE_API_KEY")
    openai_key = os.getenv("OPENAI_API_KEY")
    tavily_key = os.getenv("TAVILY_API_KEY")

    has_llm = bool(gemini_key or openai_key)
    print(f"[{'OK' if has_llm else 'WARN'}] LLM Key detected: {'Yes' if has_llm else 'Missing GOOGLE_API_KEY or OPENAI_API_KEY'}")
    print(f"[{'OK' if tavily_key else 'WARN'}] Tavily Key detected: {'Yes' if tavily_key else 'Missing TAVILY_API_KEY'}")

if __name__ == "__main__":
    test_environment()