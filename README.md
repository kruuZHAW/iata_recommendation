# IATA Topic Evolution Analyzer

This project analyzes the evolution of aviation industry topics from [IATA Annual Review reports](https://www.iata.org/en/publications/annual-review/) (PDFs) using NLP and topic modeling techniques.

It builds semantic clusters (meta-topics) across two decades of reports, identifies key trends, and supports strategic recommendations for entrepreneurs entering the aviation space.

---

## Features

- PDF parsing and sentence-level chunking
- Sentence embedding with `SentenceTransformer`
- Per-year topic modeling using `BERTopic`
- Meta-topic clustering using optimized `KMeans`
- Visual timeline of topic frequency and trend shifts
- Emerging/declining trend detection
- Strategic insights for aviation entrepreneurs

---

## Tech Stack

- Python 3.12+
- Poetry (dependency manager)
- `pdfplumber` for PDF text extraction
- `nltk` for sentence tokenization
- `sentence-transformers` for embeddings
- `BERTopic` for unsupervised topic modeling
- `scikit-learn` for clustering
- `matplotlib` & `seaborn` for visualization

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/iata-topic-evolution.git
cd iata-topic-evolution
```

### 2. Install dependencies with Poetry
```sh
poetry config virtualenvs.in-project true
poetry install
```

### 3. How to use
1. Place all IATA annual review PDFs in the `data/` folder.
2. Run the `01_topic_evolution.ipynb` notebook.
