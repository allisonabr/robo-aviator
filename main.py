import urllib.request
import json
import time

LINK_DO_ENDPOINT = "https://rapidapi.com"
CHAVE_X_RAPIDAPI = "1e287c9da0msh2d776f7d9e3145fp13c550jsn12bd3018dcd8"

print("🚀 INICIALIZANDO SENSOR BRUTO NA RENDER...")

def testar_leitura_api():
    try:
        req = urllib.request.Request(LINK_DO_ENDPOINT)
        req.add_header("x-rapidapi-key", CHAVE_X_RAPIDAPI)
        req.add_header("x-rapidapi-host", "://rapidapi.com")
        req.add_header("Content-Type", "application/json")
        req.add_header("User-Agent", "Mozilla/5.0")
        
        with urllib.request.urlopen(req, timeout=8) as response:
            resposta_texto = response.read().decode('utf-8')
            dados = json.loads(resposta_texto)
            print(f"📥 [DADOS RECEBIDOS COM SUCESSO]: {dados}")
            
    except Exception as e:
        print(f"⚠️ Erro de conexao: {e}")

try:
    while True:
        testar_leitura_api()
        time.sleep(4)
except KeyboardInterrupt:
    print("\n🛑 Parado.")
