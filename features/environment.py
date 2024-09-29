import logging
import os

# features/environment.py
def before_all(context):
    # Configurar logging
    logging.basicConfig(
        filename="test_log.log",    # Archivo de logs
        level=logging.INFO,         # Nivel de log
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    logging.info("Iniciando las pruebas...")

def after_all(context):
    context.driver.quit()
    logging.info("Pruebas finalizadas.")

def after_step(context, step):
    if step.status == "failed":
        # Crear carpeta para guardar capturas si no existe
        screenshots_dir = "screenshots"
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)

        # Guardar la captura de pantalla
        screenshot_name = f"{screenshots_dir}/screenshot_{step.name}.png"
        context.driver.save_screenshot(screenshot_name)
        logging.error(f"El paso falló: {step.name}. Captura de pantalla guardada en {screenshot_name}")