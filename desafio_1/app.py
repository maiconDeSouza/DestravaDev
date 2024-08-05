from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

site = "https://www.tempo.com/sao-paulo.htm"

# Configure o WebDriver para usar o ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navegue até o site do Google
driver.get(site)

try:
    # Aguarde até que o elemento da temperatura esteja visível
    temperatura_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "/html/body/main/div[2]/section/section[1]/div[1]/div[1]/span/span[2]/span[1]/span/span/span[1]"))
    )
    print("Temperatura:", temperatura_element.text)

    # Se necessário, mude para o iframe e encontre o elemento do céu
    # iframe = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.TAG_NAME, "iframe"))
    # )
    # driver.switch_to.frame(iframe)

    ceu_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "/html/body/main/div[2]/section/section[1]/div[1]/div[2]/a/span[2]/span[2]"))
    )
    print("Céu:", ceu_element.text)
except Exception as e:
    print(e)
finally:
    # Feche o navegador
    driver.quit()
