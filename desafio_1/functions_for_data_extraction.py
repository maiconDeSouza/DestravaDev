from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def navigate_to_the_website(url):
    try:
        driver.get(url)
    except Exception as e:
        print(e)
        print("Algo de errado ocorreu ao acessar o navegador!")

def extract_data(data_label, xpath):
    try:
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        return {data_label: element.text}
    except Exception as e:
        print(e)
        print("Algum erro ao pegar o valor dos elementos!")

def quit_website():
    try:
        driver.quit()
    except Exception as e:
        print(e)
        print("Erro ao tentar fechar o navegador!")
