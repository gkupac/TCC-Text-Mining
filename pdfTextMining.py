import os
import PyPDF2
import nltk
import re
from wordcloud import WordCloud
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
from PyPDF2 import PdfReader
import matplotlib.pyplot as plt

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def pdf_reader(folder_path):
    texts = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.pdf'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "rb") as file:
                pdf_reader = PdfReader(file)
                text = ""
                for page_number in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_number] 
                    text += page.extract_text()
            texts.append(text)
    return texts

def process_text(text_pdf):
    # Tokenização
    tokens = word_tokenize(text_pdf.lower())

    # Remove stop words em português e remove pontuações
    filtered_tokens = [token for token in tokens if token not in stopwords.words('portuguese') and not re.search(r'[.,;:!?()\[\]{}"\'’“”]', token)]

    # Lematização
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

    # Converte os tokens para string
    processed_text = ' '.join(lemmatized_tokens)

    return processed_text

def generate_wordcloud(texts):
    for text in texts:
        processed_text = process_text(text)
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(processed_text)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()


folder_path_pdf = "C:\\Users\\loren\\Documents\\Desenvolvimento\\Faculdade\\TCC\\TCC-Text-Mining\\pdfs"

texts = pdf_reader(folder_path_pdf)

generate_wordcloud(texts)
