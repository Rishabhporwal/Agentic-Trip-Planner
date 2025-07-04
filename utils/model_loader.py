import os
from dotenv import load_dotenv
from typing import Literal, Optional, Any
from pydantic import BaseModel, Field
from utils.config_loader import load_config

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI


class ConfigLoader:
    def __init__(self):
        print("Loading configuration...")
        self.config = load_config()

    def __getitem__(self, key: str) -> Any:
        return self.config[key]

class ModelLoader(BaseModel):
    
    model_provider: Literal['openai', 'groq'] = "groq"
    config: Optional[ConfigLoader] = Field(default=None, exclude=True)

    def model_post_init(self, __context: Any) -> None:
        self.config = ConfigLoader()

    class Config:
        arbitrary_types_allowed = True

    def load_llm(self):
        print(f"LLM is loading from {self.model_provider} provider...")

        if self.model_provider == 'groq':
            print(f"Using Groq model...")
            groq_api_key = os.getenv("GROQ_API_KEY")
            model_name = self.config['llm']['groq']['model_name']
            llm = ChatGroq(model=model_name, api_key=groq_api_key)
        elif self.model_provider == 'openai':
            print(f"Using OpenAI Model...")
            openai_api_key = os.getenv("OPENAI_API_KEY")
            model_name = self.config['llm']['openai']['model_name']
            llm = ChatOpenAI(model_name=model_name, openai_api_key=openai_api_key)

        return llm