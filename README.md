# NLP Basics — Code & Notebooks

<p align="right">
  <img src="https://hilpisch.com/tpq_logo_bic.png" alt="The Python Quants" width="25%">
</p>

This repository contains the Jupyter notebooks, Python scripts, and generated artifacts that accompany the *NLP Basics* class in the CPF Program. The material progresses from fundamental string operations to modern transformer models and LLM-driven code and LaTeX generation.

## Class

The material follows the structure of the *NLP Basics* class by Dr. Yves J. Hilpisch.

<p align="center">
  <img src="https://hilpisch.com/cpf_logo.png" alt="CPF Program" width="35%">
</p>

## Notebooks

- `nlp_basics_01/01_nlp_basics.ipynb` — `str` objects
- `nlp_basics_02/02_nlp_basics.ipynb` — working with `str` objects
- `nlp_basics_03/03_nlp_basics.ipynb` — working with larger `str` objects
- `nlp_basics_04/04_nlp_basics.ipynb` — `nltk` package
- `nlp_basics_05/05_nlp_basics.ipynb` — `nltk` & `lxml` packages
- `nlp_basics_06/06_nlp_basics.ipynb` — PDF documents, key words, key sentences
- `nlp_basics_07/07_nlp_basics.ipynb` — regular expressions and the `re` module
- `nlp_basics_08/08_nlp_basics.ipynb` — regular expressions and the `re` module (cont.)
- `nlp_basics_09/09_nlp_basics.ipynb` — regular expressions and the `re` module (cont.)
- `nlp_basics_10/10_nlp_basics.ipynb` — prediction of sequences of numbers
- `nlp_basics_11/11_nlp_basics.ipynb` — prediction of sequences of numbers (cont.)
- `nlp_basics_12/12_nlp_basics.ipynb` — prediction of sequences of numbers (RNNs)
- `nlp_basics_13/13_nlp_basics.ipynb` — prediction of sequences of characters
- `nlp_basics_14/14_nlp_basics.ipynb` — prediction of text
- `nlp_basics_15/15_nlp_basics_a.ipynb` — prediction of text (character-based)
- `nlp_basics_15/15_nlp_basics_b.ipynb` — prediction of text (word-based)
- `nlp_basics_16/16_nlp_basics.ipynb` — word embeddings
- `nlp_basics_17/17_nlp_basics.ipynb` — word embeddings (cont.)
- `nlp_basics_18/18_nlp_basics.ipynb` — word embeddings (cont.)
- `nlp_basics_19/19_nlp_basics.ipynb` — word embeddings (cont.)
- `nlp_basics_20/20_nlp_basics.ipynb` — transformers
- `nlp_basics_21/21_nlp_basics.ipynb` — transformers (cont.)
- `nlp_basics_22/22_nlp_basics_a.ipynb` — transformers (cont.)
- `nlp_basics_22/22_nlp_basics_b.ipynb` — transformers (cont.)
- `nlp_basics_23/23_nlp_basics.ipynb` — transformers (cont.)
- `nlp_basics_24/24_nlp_basics.ipynb` — transformers (cont.)
- `nlp_basics_25/25_nlp_basics_a.ipynb` — deploying a small DeepSeek model locally on macOS
- `nlp_basics_25/25_nlp_basics_b.ipynb` — deploying a small DeepSeek model on Ubuntu with GPU
- `nlp_basics_26/26_nlp_basics.ipynb` — deploying and chatting with multiple LLMs
- `nlp_basics_27/27_nlp_basics_a.ipynb` — AI tool usage & career impact
- `nlp_basics_27/27_nlp_basics_b.ipynb` — LSM programming challenge
- `nlp_basics_28/28_nlp_basics.ipynb` — LSM programming challenge (web app)
- `nlp_basics_29/29_nlp_basics.ipynb` — LSM programming challenge (visual web app)
- `nlp_basics_30/` — LaTeX generation by LLMs (intro to LaTeX)
- `nlp_basics_31/` — LaTeX generation by LLMs (BSM model)
- `nlp_basics_32/` — LaTeX generation by LLMs (LSM algorithm)

## Structure

Each sub-folder corresponds to one session and contains the notebook(s) and any accompanying files (data, scripts, generated HTML/PDF artifacts). The later sessions (25-32) also include `.tex`/`.pdf` outputs produced by different LLMs (GPT, Claude, Gemini, DeepSeek, o4-mini) to illustrate comparative code and LaTeX generation capabilities.

## Usage

The notebooks are designed to run in a standard scientific Python environment (or in Google Colab) with the following stack:

- Python 3.11+
- `nltk`, `lxml` (NLP fundamentals)
- `re` (regular expressions)
- `numpy`, `pandas`, `matplotlib` (data and visualization)
- `torch` (RNNs and sequence prediction)
- `gensim` or `fasttext` (word embeddings)
- `transformers` (BERT, GPT and related models)
- `llama-cpp-python` (local LLM deployment)
- `gradio` or `streamlit` (web app demos)

To get started, open a notebook in your preferred Jupyter environment or in Google Colab, run the cells from top to bottom, and follow along with the class sessions.

It is often convenient to install the "Open in Colab" Chrome extension which lets you open notebooks in Colab directly from the GitHub repository.

## Disclaimer

This repository and its contents are provided for educational and illustrative purposes only and come without any warranty or guarantees of any kind — express or implied. Use at your own risk. The authors and The Python Quants GmbH are not responsible for any direct or indirect damages, losses, or issues arising from the use of this code. Do not use the provided examples for critical decision‑making, financial transactions, medical advice, or production deployments without rigorous review, testing, and validation.

Some examples may reference third‑party libraries, datasets, services, or application programming interfaces that are subject to their own licenses and terms; you are responsible for ensuring compliance.

## Contact

- Email: [team@tpq.io](mailto:team@tpq.io)
- Linktree: [linktr.ee/dyjh](https://linktr.ee/dyjh)
- CPF Program: [python-for-finance.com](https://python-for-finance.com)
- The AI Engineer: [theaiengineer.dev](https://theaiengineer.dev)
- The Crypto Engineer: [thecryptoengineer.dev](https://thecryptoengineer.dev)
