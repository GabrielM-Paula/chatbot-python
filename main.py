from chatbot.engine import ChatbotEngine

COMANDOS_SAIR = {"sair", "exit", "quit", "tchau"}

def main():
    print("Carregando modelo de games...")
    bot = ChatbotEngine()
    
    print("\n" + "=" * 50)
    print("🎮 CHATBOT DE JOGOS INICIADO 🎮")
    print("=" * 50)
    print("Exemplos de perguntas que você pode fazer:")
    print(" • 'Olá, tudo bem?'")
    print(" • 'Me fale sobre God of War'")
    print(" • 'O que você sabe sobre The Last of Us?'")
    print(" • 'Me indique um jogo'")
    print(" • 'Conhece o Spider-Man?'")
    print("Digite 'sair' a qualquer momento para encerrar.")
    print("=" * 50 + "\n")
    
    while True:
        try:
            msg = input("Você: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Até logo e boa jogatina!")
            break
            
        if msg.lower() in COMANDOS_SAIR:
            print("Bot: Até logo e boa jogatina!")
            break
            
        if not msg:
            continue
            
        resposta = bot.responder(msg)
        print(f"Bot: {resposta}")
        print("-" * 40)

if __name__ == "__main__":
    main()