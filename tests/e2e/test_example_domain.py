import pytest
from playwright.sync_api import Page, expect

from atlas.browser import BasePage
from atlas.config import Settings


class ExamplePage(BasePage):
    path = "/"

    @property
    def heading(self):
        return self.page.get_by_role("heading", name="Example Domain")


@pytest.mark.e2e
@pytest.mark.smoke
def test_example_domain_is_reachable(page: Page, settings: Settings) -> None:
    example = ExamplePage(page, str(settings.web_base_url))
    example.open()
    expect(example.heading).to_be_visible()
