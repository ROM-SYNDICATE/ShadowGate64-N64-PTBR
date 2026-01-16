import os

def busca_avancada(rom_nome, palavra):
    if not os.path.exists(rom_nome):
        print(f"Erro: Arquivo {rom_nome} não encontrado.")
        return

    with open(rom_nome, "rb") as f:
        data = f.read()

    # Vamos testar 3 variações da palavra
    variacoes = [palavra.upper(), palavra.lower(), palavra.capitalize()]
    
    print(f"--- Iniciando busca avançada para: {palavra} ---")
    
    for v in variacoes:
        print(f"Testando variação: {v}")
        # Calcula distâncias
        distancias = [ord(v[i+1]) - ord(v[i]) for i in range(len(v)-1)]
        
        for i in range(len(data) - len(v)):
            match = True
            for j in range(len(distancias)):
                # Mudança técnica: usamos (abs) para lidar com variações de sinal
                if (data[i+j+1] - data[i+j]) != distancias[j]:
                    match = False
                    break
            
            if match:
                print(f"\n[!] ACHOU! Variação: {v}")
                print(f"Endereço (Offset): {hex(i).upper()}")
                print(f"Bytes na ROM: {data[i:i+len(v)].hex(' ').upper()}")
                # Mostra o que tem em volta para contexto
                contexto = data[i:i+20].hex(' ')
                print(f"Contexto (próximos 20 bytes): {contexto}")

# --- CONFIGURAÇÃO ---
arquivo_rom = "Shadowgate 64 - Trials of the Four Towers (USA) (En,Es).n64" 
busca_avancada(arquivo_rom, "Well done, Del! It is good") # Tente palavras curtas e comuns