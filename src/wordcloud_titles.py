"""
Generate a word cloud from `game_title` in discovery_queue_log.csv,
filtering to nouns/adjectives (NN* and JJ*).

NLTK data is stored locally at ../nltk_data
"""

from __future__ import annotations

from pathlib import Path
import re

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

import nltk
from nltk import pos_tag, word_tokenize


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    csv_path = project_root / "discovery_queue_log.csv"
    nltk_data_dir = project_root / "nltk_data"

    # Ensure NLTK uses the project-local data dir first
    nltk.data.path.insert(0, str(nltk_data_dir))

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found: {csv_path}")

    df = pd.read_csv(csv_path)

    if "game_title" not in df.columns:
        raise KeyError("CSV must contain a 'game_title' column")

    titles = df["game_title"].dropna().astype(str)

    alpha_re = re.compile(r"^[a-z]+$")
    tokens: list[str] = []

    for title in titles:
        words = word_tokenize(title.lower())
        for word, tag in pos_tag(words):
            if (tag.startswith("NN") or tag.startswith("JJ")) and alpha_re.match(word):
                tokens.append(word)

    text = " ".join(tokens)

    wc = WordCloud(
        width=1600,
        height=900,
        background_color="white",
        collocations=False,
    ).generate(text)

    plt.figure(figsize=(12, 7))
    plt.imshow(wc)
    plt.axis("off")
    plt.tight_layout()
    out_path = project_root / "wordcloud.png"
    plt.savefig(out_path, dpi=200)
    print(f"Wrote: {out_path}")



if __name__ == "__main__":
    main()
