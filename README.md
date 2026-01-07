## dq_wordcloud

Generate a word cloud from the `game_title` column of a Steam Discovery Queue CSV, visualizing frequency of individual **nouns** and **adjectives** using NLTK POS tagging.

The project is intentionally small, explicit, and reproducible. No notebooks, no hidden state.

This project was fully vibe-coded with **ChatGPT 5.2**.

---

### Requirements

- Python 3.11+
- Linux / WSL (tested on Ubuntu via WSL)
- VSCode (Remote – WSL recommended)

Python dependencies are listed in `requirements.txt`.

---

### Project Structure

```
dq_wordcloud/
  discovery_queue_log.csv
  requirements.txt
  README.md
  .gitignore
  nltk_data/
  src/
    wordcloud_titles.py
```

---

### Setup (WSL / Bash)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Install required NLTK data locally to the project:

```bash
mkdir -p nltk_data
python -c "import nltk; nltk.download('punkt', download_dir='nltk_data')"
python -c "import nltk; nltk.download('punkt_tab', download_dir='nltk_data')"
python -c "import nltk; nltk.download('averaged_perceptron_tagger_eng', download_dir='nltk_data')"
```

---

### Run

```bash
python src/wordcloud_titles.py
```

By default, the script:
- reads `discovery_queue_log.csv`
- extracts `game_title`
- tokenizes and POS-tags titles
- keeps only NN* and JJ* tokens
- generates a word cloud

If GUI display is unreliable under WSL, the script can be configured to write `wordcloud.png` to disk.

---

### Notes

- Virtual environments have no effect on git behavior.
- `.venv/`, `nltk_data/`, and generated images are ignored by default.
- POS tagging on short titles is approximate by nature; expect some noise.
- Stopwords and lemmatization are intentionally omitted to keep the pipeline transparent and editable.
