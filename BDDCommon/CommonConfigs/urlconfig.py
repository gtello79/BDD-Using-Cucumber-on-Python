import os

# validando variable de entorno
env = os.getenv("ENV")
base_url = None


# Definiendo url base
if env == "LOCAL":
    base_url = "http://localhost:10009"
elif env == "DEMO":
    base_url = "http://demostore.supersqa.com/"
else:
    raise Exception(f"No se ha encontrado el valor de la variable de entorno {env}")

# Configurando url a partir de la url base
URLCONFIGS = {
    "my account": f"{base_url}/my-account/",
    "home": f"{base_url}",
}
