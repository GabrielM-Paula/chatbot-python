import re
import nltk
from nltk.stem import PorterStemmer

try:
    nltk.data.find("tokenizers/punkt_tab")
except LookupError:
    nltk.download("punkt_tab", quiet=True)

stemmer = PorterStemmer()

def tokenizar(texto: str) -> list[str]:
    return nltk.word_tokenize(texto)

def normalizar(texto: str) -> str:
    texto = texto.lower()
    texto = re.sub(r"[^\w\sáàâãéèêíïóôõúçñ]", "", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto

def stem_palavra(palavra: str) -> str:
    return stemmer.stem(palavra)

def preprocessar(texto: str) -> str:
    texto = normalizar(texto)
    tokens = tokenizar(texto)
    stems = [stem_palavra(t) for t in tokens if t.strip()]
    return " ".join(stems)