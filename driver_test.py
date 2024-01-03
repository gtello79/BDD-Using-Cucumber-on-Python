from selenium import webdriver
from selenium.webdriver.common.by import By

# Configura el driver de Chrome con ChromeDriver
# Al no pasar el parametro Service, está utilizando la version definida en el path
driver = webdriver.Chrome()

# En caso que se quisiera utilizar otra version, deberá ser del tipo
# Especifica la ruta al ejecutable de ChromeDriver
# from selenium.webdriver.chrome.service import Service
# chrome_driver_path = '/path/chromedriver'
# service = Service(chrome_driver_path)
# driver = webdriver.Chrome(service=service)

# Navega a una página web, por ejemplo, Google
driver.get("https://www.google.com")

# Realiza alguna acción, como buscar una palabra clave
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium WebDriver")
search_box.submit()

# Espera unos segundos para ver los resultados
import time
time.sleep(5)

print(f'Pasaron 5 segundos')

# Cierra el navegador
driver.quit()
print(f'Cierre de sesion')