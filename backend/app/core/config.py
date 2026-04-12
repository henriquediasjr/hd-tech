from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_ENV: str = "development"
    APP_TITLE: str = "Portfolio API"
    APP_VERSION: str = "0.1.0"
    CORS_ORIGINS: list[str] = ["http://localhost:5173"]
    CALENDLY_URL: str = "https://calendly.com/henriquediasjr"

    # Email — Gmail SMTP (use an App Password, not your account password)
    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USER: str = ""       # Gmail address used to send (e.g. you@gmail.com)
    SMTP_PASSWORD: str = ""   # Gmail App Password (16-char)
    CONTACT_EMAIL: str = "henriquediasjr@gmail.com"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
