# BDD - Using Cucumber on Python

## Instalación
- Por preferencia, decidí utilizar chromeDrive en vez de geckodrive (firefox) debido al origen en que instalé mi Firefox. De todos modos, dejo antecedentes desde donde obtener las instalaciones para ambos drivers:

### WebDriver
* Elegir Drive de acuerdo a navegador de preferencia
    * Descarga de ChromeDriver (https://chromedriver.chromium.org/)
    * Descarga de geckoDriver (https://github.com/mozilla/geckodriver/releases)
* Verificar la version compatible
* Descargar compatible
* Descomprimir archivo tar.gz
* Mover archivo chromedriver a /usr/local/bin/
* Crear ejecutable utilizando chmod +x chromedrive (o geckodriver)

* Ejecutar el comando
`python3 driver_test.py`

* Esperar que la linea de comando solo arroje dos mensaje
    1. Pasaron 5 segundos
    2. Cierre de sesión


