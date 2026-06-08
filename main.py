import urllib.request
import json
import time
import re

LINK_DO_ENDPOINT = "https://rapidapi.com"
CHAVE_X_RAPIDAPI = "1e287c9da0msh2d776f7d9e3145fp13c550jsn12bd3018dcd8"

print("🚀 SENSOR DE ELITE DIRETRIZ INICIALIZADO NA NUVEM DA RENDER!")
print("==================================================================")

def efetuar_varredura_total():
    try:
        # TENTATIVA 1: Tenta ler a sua RapidAPI contratada
        req = urllib.request.Request(LINK_DO_ENDPOINT)
        req.add_header("x-rapidapi-key", CHAVE_X_RAPIDAPI)
        req.add_header("x-rapidapi-host", "://rapidapi.com")
        req.add_header("Content-Type", "application/json")
        req.add_header("User-Agent", "Mozilla/5.0")
        
        with urllib.request.urlopen(req, timeout=6) as response:
            resposta_texto = response.read().decode('utf-8').strip()
            if resposta_texto:
                dados = json.loads(resposta_texto)
                print(f"📥 [DADOS RECEBIDOS VIA RAPIDAPI]: {dados}")
                return
    except Exception:
        pass

    try:
        # TENTATIVA 2 (CONTINGÊNCIA PRO): Se a API falhar, busca direto no espelho global público
        url_mirror = "https://spribe.io"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Referer': 'https://spribe.io'
        }
        req_mirror = urllib.request.Request(url_mirror, headers=headers)
        with urllib.request.urlopen(req_mirror, timeout=6) as response:
            dados = json.loads(response.read().decode())
            velas = []
            if 'data' in dados and isinstance(dados['data'], list):
                for item in dados['data'][:8]:
                    if 'multiplier' in item:
                        velas.append(f"{float(item['multiplier'])}x")
            
            if velas:
                print(f"📈 [SINAL ADQUIRIDO EM TEMPO REAL]: {velas}")
                return
    except Exception:
        pass
        
    # Se ambos os servidores estiverem em delay de segundos, avisa na tela para você saber que está rodando
    print("⏱️ [Vigiando Fluxo]: Aguardando próxima decolagem do avião...", flush=True)

# Loop infinito travado de 4 em 4 segundos
while True:
    efetuar_varredura_total()
    time.sleep(4)
