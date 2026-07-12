from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Aurora Media Server"
    database_url: str = "sqlite:///./aurora.db"
    secret_key: str = "dev-secret-key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
