from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from functools import lru_cache

class Settings(BaseSettings):
    LITELLM_MODEL: str = "gpt-3.5-turbo"
    GITHUB_TOKEN: str = Field(..., env="GITHUB_TOKEN")
    GITHUB_REPOSITORY: str = Field(..., env="GITHUB_REPOSITORY")
    ISSUE_NUMBER: int = Field(0, env="ISSUE_NUMBER")
    # GEMINI_API_KEY: str = Field("", env="GEMINI_API_KEY")
    OPENAI_API_KEY: str = Field("", env="OPENAI_API_KEY")    
    YOUR_PERSONAL_ACCESS_TOKEN: str = Field("", env="YOUR_PERSONAL_ACCESS_TOKEN")
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')
    # ALLOWED_USERS = ["github-actions[bot]", "Sunwood-ai-labs", "user2"]

@lru_cache()
def get_settings():
    return Settings()
