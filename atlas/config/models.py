from pydantic import BaseModel, Field, HttpUrl


class BrowserSettings(BaseModel):
    name: str = "chromium"
    headless: bool = True
    timeout_ms: int = Field(default=10_000, gt=0)
    viewport_width: int = Field(default=1440, gt=0)
    viewport_height: int = Field(default=900, gt=0)


class ApiSettings(BaseModel):
    base_url: HttpUrl
    timeout_seconds: float = Field(default=10.0, gt=0)


class Settings(BaseModel):
    environment: str
    web_base_url: HttpUrl
    api: ApiSettings
    browser: BrowserSettings = BrowserSettings()
