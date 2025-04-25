# IATA Topic Evolution Analyzer

This project analyzes the evolution of aviation industry topics from [IATA Annual Review reports](https://www.iata.org/en/publications/annual-review/) (PDFs) using NLP, topic modeling techniques and Retrieval Augmented Generation. The project aims at providing insights for new entrepreneurs in the aviation sector.

First, it builds semantic clusters (meta-topics) across two decades of reports, identifies key trends, and supports strategic recommendations for entrepreneurs entering the aviation space. Secondly, it provides natural language question answering using semantic search across IATA reports.

---

## Features
- PDF parsing and sentence-level chunking
- Sentence embedding with `SentenceTransformer`
- Per-year topic modeling using `BERTopic`
- Meta-topic clustering using optimized `KMeans`
- Visual timeline of topic frequency and trend shifts
- Emerging/declining trend detection
- Strategic insights for aviation entrepreneurs
- RAG-style semantic search in IATA reports using FAISS + local LLMs via `ollama`

---

## Tech Stack

- Python 3.12+
- Poetry (dependency manager)
- `pdfplumber` for PDF text extraction
- `nltk` for sentence tokenization
- `sentence-transformers` for embeddings
- `BERTopic` for unsupervised topic modeling
- `scikit-learn` for clustering
- `faiss` for vector similarity search
- `ollama` for LLM-based answering
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
2. Run the notebooks:
  - `01_topic_evolution.ipynb` for topic modeling and trend analysis
  - `02_semantic_query_rag.ipynb`for natural language question answering using semantic search

### 4. Example of use RAG
```bash
query = "What are the major sustainability initiatives?"
```

```bash
Generated Answer:
1. Aviation Industry's Commitment to Carbon Neutral Growth (CNG): The aviation industry has committed to achieve carbon neutral growth from 2020, and already has a plan in place to achieve this goal by 2050. 
2. Development of Sustainable Biofuels: Aviation is actively working towards the development of sustainable biofuels as an alternative to traditional fossil fuels. The industry is exploring three possible synthetic fuels derived from coal, natural gas, and biomass, with biomass offering the best emissions reductions. 
3. Four-Pillar Emissions Strategy: This strategy, adopted by the entire aviation industry in 2008, focuses on reducing emissions through four key pillars: operational efficiency, infrastructure, market-based measures, and alternative jet fuels. The strategy is estimated to save $5 billion in fuel costs. 
4. Infrastructure Improvements: Governments are urged to support essential infrastructure improvements that could help reduce aviation emissions. These improvements may lead to cost savings for the industry. 
5. Joint Action: Truly effective solutions require joint action from all stakeholders in the aviation sector, including airlines, manufacturers, and fuel suppliers. 
6. Dealing with Punitive Economic Measures: The aviation industry is dealing with often punitive economic measures levied by governments on airlines as they strive to reduce emissions.

```


