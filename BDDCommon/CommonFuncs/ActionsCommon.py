from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement


class ActionsCommon:
    @classmethod
    def make_hover_on_a_element(
        cls,
        context,
        objective_WebElement: WebElement = None,
        locators_attr: str = None,
        locators_text: str = None,
    ):
        # Initialize the action
        web_driver = context.driver
        action_chains = ActionChains(web_driver)

        # Obtiene el webElement desde el locator
        if not isinstance(objective_WebElement, WebElement):
            objective_WebElement: WebElement = cls.get_web_element_from_context(
                context, locators_attr, locators_text
            )

        # Mover el cursor sobre el elemento
        action_chains.move_to_element(objective_WebElement).perform()
