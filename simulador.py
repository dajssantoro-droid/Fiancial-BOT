import yfinance as yf

print("--- ALGORITMO DE ANÁLISE DE MERCADO ---")

codigo = input("Digite o código da ação (ex: AAPL, GOOGL): ")

try:
    # 1. Busca os dados dos últimos 5 dias na bolsa
    acao = yf.Ticker(codigo)
    dados_historicos = acao.history(period="5d")
    
    # 2. Guarda a coluna de preços de fechamento
    precos_fechamento = dados_historicos['Close']
    
    print("\n--- PREÇOS DOS ÚLTIMOS 5 DIAS ---")
    print(precos_fechamento)
    
    # 3. Pega o preço de hoje (última linha da tabela)
    preco_hoje = precos_fechamento.iloc[-1]
    
    # 4. APRENDENDO SOZINHA: O Python calcula a média dos 5 dias com '.mean()'
    preco_medio = precos_fechamento.mean()
    
    print("\n--- ANÁLISE ESTATÍSTICA ---")
    print(f"Preço de hoje: ${preco_hoje:.2f}")
    print(f"Média dos últimos 5 dias: ${preco_medio:.2f}")
   
    if preco_hoje < preco_medio:
        print("Alerta: preço abaixo da média")
        print("Recomendação: comprar")

    else:
        print("Alerta: preço acima da média")
        print("Recomendação: Vender ou aguardar")

except Exception as erro:
    # Se der erro, o Python vai nos dizer exatamente o motivo real do erro
    print(f"\n[ERRO] Ocorreu o seguinte problema: {erro}")


