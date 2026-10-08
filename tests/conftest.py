from collections.abc import Generator

import pytest
from playwright.sync_api import Browser, BrowserContext, Page, Playwright, sync_playwright

from atlas.api import ApiClient
from atlas.config import Settings, load_settings
from atlas.reporting import artifact_path


@pytest.fixture(scope="session")
def settings() -> Settings:
    return load_settings()


@pytest.fixture
def api_client(settings: Settings) -> Generator[ApiClient, None, None]:
    with ApiClient(str(settings.api.base_url), settings.api.timeout_seconds) as client:
        yield client


@pytest.fixture(scope="session")
def playwright_instance() -> Generator[Playwright, None, None]:
    with sync_playwright() as instance:
        yield instance


@pytest.fixture(scope="session")
def browser(playwright_instance: Playwright, settings: Settings) -> Generator[Browser, None, None]:
    browser_type = getattr(playwright_instance, settings.browser.name)
    instance = browser_type.launch(headless=settings.browser.headless)
    yield instance
    instance.close()


@pytest.fixture
def page(browser: Browser, settings: Settings, request: pytest.FixtureRequest) -> Generator[Page, None, None]:
    context: BrowserContext = browser.new_context(
        viewport={
            "width": settings.browser.viewport_width,
            "height": settings.browser.viewport_height,
        }
    )
    page = context.new_page()
    page.set_default_timeout(settings.browser.timeout_ms)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield page

    report = getattr(request.node, "rep_call", None)
    if report and report.failed:
        page.screenshot(path=artifact_path(request.node.nodeid, "png"), full_page=True)
        context.tracing.stop(path=artifact_path(request.node.nodeid, "zip"))
    else:
        context.tracing.stop()
    context.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo[object]):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)
