from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_ENV: str = "development"
    APP_TITLE: str = "Portfolio API"
    APP_VERSION: str = "0.1.0"
    CORS_ORIGINS: list[str] = ["http://localhost:5173"]
    CALENDLY_URL: str = "https://calendly.com/henriquediasjr"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
