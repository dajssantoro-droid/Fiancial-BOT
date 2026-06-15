import yfinance as yf

print("--- ALGORITMO DE ANÁLISE DE MERCADO ---")

codigo = input("Digite o código da ação (ex: AAPL, GOOGL): ")

try:
    
    acao = yf.Ticker(codigo)
    dados_historicos = acao.history(period="5d")
    
    
    precos_fechamento = dados_historicos['Close']
    
    print("\n--- PREÇOS DOS ÚLTIMOS 5 DIAS ---")
    print(precos_fechamento)
    
    
    preco_hoje = precos_fechamento.iloc[-1]
    
    
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
    
    print(f"\n[ERRO] Ocorreu o seguinte problema: {erro}")


