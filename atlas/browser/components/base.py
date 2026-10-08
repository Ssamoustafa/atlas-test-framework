from playwright.sync_api import Locator, Page


class Component:
    def __init__(self, page: Page, selector: str) -> None:
        self.page = page
        self.root: Locator = page.locator(selector)

    def is_visible(self) -> bool:
        return self.root.is_visible()
