from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from BDDCommon.CommonConfigs.urlconfig import URLCONFIGS
from BDDCommon.CommonFuncs.ActionsCommon import ActionsCommon
import os


class WebCommon(ActionsCommon):
    possible_locators = [
        By.ID,
        By.XPATH,
        By.LINK_TEXT,
        By.PARTIAL_LINK_TEXT,
        By.NAME,
        By.TAG_NAME,
        By.CLASS_NAME,
        By.CSS_SELECTOR,
    ]

    debug_flag = (os.getenv("DEBUG").lower() in ["1", "true", "on", "yes"]) or False

    @classmethod
    def get_webelement_from_locators(
        cls,
        context: WebDriver,
        locators: dict,
        searched_element: str,
    ) -> WebElement:
        try:
            searched_attr = locators[searched_element]
            searched_attr_type = searched_attr["type"]
            searched_attr_locator = searched_attr["locator"]
        except KeyError:
            raise KeyError(
                f"No se ha encontrado la llave {searched_element} en los locators {locators}"
            )

        searched_webElement = WebCommon.get_web_element_from_context(
            context, searched_attr_type, searched_attr_locator
        )

        return searched_webElement

    @classmethod
    def get_web_element_from_context(
        cls,
        context_or_web_element,
        locators_attr: str = None,
        locators_text: str = None,
    ) -> WebElement:
        if isinstance(context_or_web_element, WebElement):
            web_element = context_or_web_element

        else:
            if not all([locators_attr, locators_text]):
                raise AssertionError(
                    f"Revisar los parametros de locators_attr {locators_attr}, locators_text {locators_text}"
                    f"context_or_web_element: {type(context_or_web_element)}"
                )

            web_element: WebElement = cls.find_element(
                context_or_web_element, locators_attr, locators_text
            )

        return web_element

    @classmethod
    def go_to_url(cls, context, site=str, **kwargs):
        if not site.startswith("http"):
            try:
                url = URLCONFIGS[site]
            except KeyError:
                raise Exception(
                    f"El sitio {site} no existe dentro del archivo URL CONFIGS"
                )

        browser_type = context.config.userdata.get("browser")

        if isinstance(browser_type, str):
            browser_type = browser_type.lower()

        # Create instance of Firefox driver the browser type is not specified
        if not browser_type or browser_type.lower() == "chrome":

            if cls.debug_flag:
                options = webdriver.ChromeOptions()
                options.add_argument("--headless")

                context.driver = webdriver.Chrome(
                    service=ChromeService(ChromeDriverManager().install()),
                    options=options,
                )

            else:
                context.driver = webdriver.Chrome(
                    service=ChromeService(ChromeDriverManager().install())
                )
        elif browser_type.lower() == "firefox":
            context.driver = webdriver.Firefox()
        else:
            raise Exception(f"The browser type {browser_type} is not supported")

        # adding implicit wait
        wait = kwargs.get("implicitly_wait", 10000)

        context.driver.implicitly_wait(wait)
        # Clean the url and go to them
        url = url.strip()
        context.driver.get(url)

    # funcion creada para buscar webElements
    @classmethod
    def find_element(cls, context, locator_attribute, locator_text) -> WebElement:
        """
        Finds an element and returns the element object
        ::param context
        ::param locator_attribute: what to use to locate (example, id, class, xpath, etc)
        ::param locator_text: the locator text (example: the id, the class, the name, etc)
        """

        if locator_attribute not in cls.possible_locators:
            raise Exception(
                "The locator attribute provided is not in the approved attributes."
                f"The approves atributes are: {cls.possible_locators}"
            )

        try:
            web_element = context.driver.find_element(locator_attribute, locator_text)
        except Exception as e:
            raise Exception(e)

        return web_element

    # funcion creada para buscar webElements
    @classmethod
    def find_elements(cls, context, locator_attribute, locator_text) -> list:
        """
        Finds an elements and returns the element object list
        ::param context
        ::param locator_attribute: what to use to locate (example, id, class, xpath, etc)
        ::param locator_text: the locator text (example: the id, the class, the name, etc)
        """

        if locator_attribute not in cls.possible_locators:
            raise Exception(
                "The locator attribute provided is not in the approved attributes."
                f"The approves atributes are: {cls.possible_locators}"
            )

        try:
            web_element = context.driver.find_elements(locator_attribute, locator_text)
        except Exception as e:
            raise Exception(e)

        return web_element

    @classmethod
    def is_element_visible(cls, context_or_webelement):
        """
        Checks if element is visible and returns True and false
        """

        element = cls.get_web_element_from_context(context_or_webelement)

        is_displayed = element.is_displayed()
        return is_displayed and isinstance(is_displayed, bool)

    @classmethod
    def type_element(
        cls,
        context_or_web_element,
        input_string,
        locators_attr=None,
        locators_text=None,
    ):
        """
        Permite "escribir" dentro de un web_element, obtenido directamente desde el, o consultando por
        las características del web_element dentro de contexto
        """
        input_file: WebElement = cls.get_web_element_from_context(
            context_or_web_element, locators_attr, locators_text
        )

        input_file.send_keys(input_string)

    @classmethod
    def click_element(
        cls,
        context_or_web_element,
        locators_attr: str = None,
        locators_text: str = None,
    ):
        """
        Permite "hacer click" dentro de un web_element, obtenido directamente desde el,
        o consultando por las características del web_element dentro de contexto
        """

        input_file: WebElement = cls.get_web_element_from_context(
            context_or_web_element, locators_attr, locators_text
        )

        input_file.click()

    # ------------- ASSERT VALIDATION METHODS------------------------------------------
    @classmethod
    def assert_validate_text(
        cls,
        context_or_web_element,
        expected_text: str,
        locators_attr: str = None,
        locators_text: str = None,
    ):
        content_box: WebElement = cls.get_web_element_from_context(
            context_or_web_element, locators_attr, locators_text
        )

        try:
            element_text = content_box.text
        except AttributeError as e:
            raise AssertionError(
                f"El campo del web_element está vacío. {e.__traceback__}"
            )
        assert element_text == expected_text, (
            "El texto obtenido en la plataforma no es el esperado. "
            f"Obtenido: {element_text} "
            f"Esperado: {expected_text}"
            f"Locators: {locators_attr} {locators_text}"
        )

    @classmethod
    def assert_element_visible(cls, element: WebElement):
        """
        Function to check if the passed element is visble.
        Raises and excepction if it is not excepcion
        """

        if not cls.is_element_visible(element):
            raise AssertionError(f"The element {element} is nos displayed")

    @classmethod
    def assert_page_title(cls, context, expected_title: str):
        """
        Verifies the home page title is expected
        """

        # Obtiene el titulo actual del driver
        actual_title = context.driver.title

        assert actual_title == expected_title, (
            "The title is not as expected "
            f"Expected {expected_title}, Actual {actual_title}"
        )

    @classmethod
    def assert_current_url(cls, context, expected_url: str):
        # Get the current_url
        current_url = context.driver.current_url

        # Validate structure of expected_url
        if not expected_url.startswith("http") or not expected_url.startswith("https"):
            expected_url = f"https://{expected_url}"

        assert current_url == expected_url, (
            "The current url is not as expected"
            f"Actual {current_url} Expected {expected_url}"
        )

    @classmethod
    def assert_include_text_into_url(cls, context, expected_url: str):
        # Get the current_url
        current_url = context.driver.current_url

        # Validate structure of expected_url
        assert expected_url in current_url, (
            "The current url is not as expected"
            f"Actual {current_url} Expected {expected_url}"
        )

    @classmethod
    def assert_radio_button_is_selected(
        cls,
        context_or_web_element,
        locators_attr: str = None,
        locators_text: str = None,
    ):
        web_element = cls.get_web_element_from_context(
            context_or_web_element, locators_attr, locators_text
        )

        assert web_element.is_selected(), (
            "El elemento no está seleccionado. "
            f"WebElement {web_element.get_attribute('name')}"
        )

    @classmethod
    def get_element_text(cls,
        context_or_web_element,
        locators_attr: str = None,
        locators_text: str = None,
    ) -> str:
        web_element = cls.get_web_element_from_context(
            context_or_web_element, locators_attr, locators_text
        )
        web_element = cls.get_web_element_from_context(
            context_or_web_element, locators_attr, locators_text
        )

        return web_element.text