import json
import random
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from chatbot.preprocess import preprocessar

CAMINHO_INTENTS = os.path.join(
    os.path.dirname(__file__), "..", "data", "intents.json"
)

class ChatbotEngine:
    def __init__(self):
        self.intents = self._carregar_intents()
        self.vectorizer = TfidfVectorizer()
        self.modelo = LogisticRegression(max_iter=1000)
        self.tags = []
        self.respostas_por_tag = {}
        self._treinar()

    def _carregar_intents(self) -> dict:
        with open(CAMINHO_INTENTS, "r", encoding="utf-8") as f:
            return json.load(f)

    def _treinar(self):
        frases = []
        labels = []
        for intent in self.intents["intents"]:
            tag = intent["tag"]
            self.respostas_por_tag[tag] = intent["responses"]
            for padrao in intent["patterns"]:
                frases.append(preprocessar(padrao))
                labels.append(tag)
        
        X = self.vectorizer.fit_transform(frases)
        self.modelo.fit(X, labels)
        self.tags = list(set(labels))
        print(f"[engine] Modelo treinado com {len(frases)} frases sobre jogos e {len(self.tags)} intenções.")

    def prever_intent(self, mensagem: str) -> tuple[str, float]:
        texto = preprocessar(mensagem)
        X = self.vectorizer.transform([texto])
        probs = self.modelo.predict_proba(X)[0]
        idx = probs.argmax()
        tag = self.modelo.classes_[idx]
        confianca = float(probs[idx])
        return tag, confianca

    def responder(self, mensagem: str, limiar: float = 0.20) -> str:
        tag, confianca = self.prever_intent(mensagem)
        if confianca < limiar:
            return "Desculpe, ainda não conheço esse jogo ou assunto. Tente perguntar sobre God of War, The Last of Us ou pedir uma recomendação!"
        return random.choice(self.respostas_por_tag[tag])