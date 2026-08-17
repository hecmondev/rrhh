from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    def __init__(self):
        super().__init__()

    name: str

    model_config = SettingsConfigDict(env_file='.env')
