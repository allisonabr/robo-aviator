import os
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def iniciar_navegador():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    chrome_options.binary_location = "/usr/bin/google-chrome"
    return webdriver.Chrome(options=chrome_options)

def vigiar_aviator():
    driver = iniciar_navegador()
    url_base = "https://estrelabet.bet.br"
    url_jogo = "https://estrelabet.bet.br/gameplay/aviator"
    
    print("[Vigiando Fluxo]: Acessando a página inicial para injetar credenciais...")
    driver.get(url_base)
    time.sleep(5)
    
    try:
        with open("cookies.txt", "r") as f:
            cookies = json.load(f)
            for cookie in cookies:
                if 'sameSite' in cookie:
                    if cookie['sameSite'] not in ["Strict", "Lax", "None"]:
                        cookie['sameSite'] = "Lax"
                driver.add_cookie(cookie)
        print("[Vigiando Fluxo]: Cookies injetados com sucesso!")
    except Exception as e:
        print(f"[Erro]: Falha ao carregar o arquivo de cookies: {e}")
        return

    print("[Vigiando Fluxo]: Direcionando para a tela do Aviator...")
    driver.get(url_jogo)
    time.sleep(12)
    
    ultimo_resultado = None
    
    while True:
        try:
            elemento_historico = driver.find_element(By.CSS_SELECTOR, ".stats-block .bubble-item, .payouts-block .bubble")
            resultado_atual = elemento_historico.text.strip()
            
            if resultado_atual and resultado_atual != ultimo_resultado:
                ultimo_resultado = resultado_atual
                print(f"[Vigiando Fluxo]: Nova decolagem detectada! Multiplicador: {resultado_atual}")
                
        except Exception:
            print("[Vigiando Fluxo]: Aguardando próxima decolagem do avião...")
            
        time.sleep(4)

if __name__ == "__main__":
    vigiar_aviator()
