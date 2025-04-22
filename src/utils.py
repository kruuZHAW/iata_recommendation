import re
import pdfplumber
import nltk
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction import text

nltk.download("punkt")
nltk.download("stopwords")

class IATAProcessor:
    def __init__(self, custom_stopwords=None):
        base_stopwords = text.ENGLISH_STOP_WORDS
        if custom_stopwords:
            base_stopwords = base_stopwords.union(custom_stopwords)
        self.stopwords = base_stopwords

    def extract_text_from_pdf(self, pdf_path):
        """Extracts text from all pages in a PDF file."""
        full_text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    full_text += page_text + "\n"
        return full_text

    def chunk_text(self, text, chunk_size=5):
        """Tokenizes text into sentences and chunks them into groups of N sentences."""
        sentences = sent_tokenize(text)
        return [" ".join(sentences[i:i + chunk_size]) for i in range(0, len(sentences), chunk_size)]

    def clean_chunk(self, text):
        """Lowercases and removes punctuation and stopwords from a chunk."""
        text = text.lower()
        text = re.sub(r"[^a-zA-Z\s]", "", text)
        words = text.split()
        words = [w for w in words if w not in self.stopwords]
        return " ".join(words)

    def preprocess_pdf(self, pdf_path, chunk_size=5):
        """End-to-end processing of a PDF file"""
        raw_text = self.extract_text_from_pdf(pdf_path)
        chunks = self.chunk_text(raw_text, chunk_size=chunk_size)
        cleaned_chunks = [self.clean_chunk(chunk) for chunk in chunks]
        return cleaned_chunks
