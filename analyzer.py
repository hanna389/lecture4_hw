import nltk
import os
from collections import Counter

nltk.download('punkt')
nltk.download('punkt_tab')

file_path = "./text.txt"

def analyze_text(file_path):

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл за шляхом '{file_path}' не знайдено.")
    
    with open(file_path, mode="r", encoding="utf-8") as file:
        text = file.read()

    if not text.strip():
        raise ValueError("Текст у файлі є порожнім.")

    tokens = nltk.word_tokenize(text.lower())

    words = [token for token in tokens if token.isalpha()]

    words_count = len(words)
    frequency = dict(Counter(words))

    return words_count, frequency