"""
    Functions to unzip file and subsample data.
"""

from pathlib import Path
import zipfile

import numpy as np
import pandas as pd


def untar_news_file(raw_data_path, zip_folder):
    """
        Unzip the news zip file.
    """
    unzipped_file = Path(raw_data_path, f"{zip_folder}.csv")
    if not unzipped_file.is_file():
        tgz_path = Path(raw_data_path, f"{zip_folder}.zip")
        with zipfile.ZipFile(tgz_path, 'r') as zip_ref:
            zip_ref.extractall(path=raw_data_path)


def sample_articles(sample_file_name, n_samples=0, nrows=1000, low_memory=False):
    """
        Select a random subsample of articles.

        nrows: only get samples from top k rows
        n_samples: number of sampled rows to return

        n_samples needs to be <= nrows
    """

    raw_path = Path("data/data_raw")
    sample_path = Path("data/subsamples")
    sample_path.mkdir(exist_ok=True)

    dtypes = {
        "Unnamed: 0": int,
        "author":str,
        "title": str,
        "article": str,
        "url": str,
        "section":str,
        "publication":str}

    read_cols = [
        'Unnamed: 0',
        'date',
        'author',
        'title',
        'article',
        'url',
        'section',
        'publication']

    df = pd.read_csv(raw_path / "all-the-news-2-1.csv",
        usecols=read_cols,
        parse_dates=["date"],
        dtype=dtypes,
        nrows=nrows,
        low_memory=low_memory)

    df = df.dropna(subset=['article'])

    if n_samples > 0:
        rng = np.random.default_rng(42)
        df = df.iloc[rng.choice(df.shape[0], n_samples, replace=False)]
    else:
        df = df.copy()

    df = df.rename(columns={"Unnamed: 0": "article_id"})
    df.to_csv(sample_path / f"{sample_file_name}.csv", index=False)


def sample_by_topic(sample_file_name, topic_list, n_samples=0, nrows=None):
    """
        By default reads in all 2.7 million articles.

        Available topics:
            ['art', 'business', 'finance', 'technology', 'climate', 'health',
            'other', 'sport', 'entertain', 'food', 'mix', 'politics',
            'fashion', 'health/science', 'law', 'realestate', 'science',
            'science/technology', 'travel', 'worldnews']
    """
    raw_path = Path("../data/data_raw") # using .. for quick fix
    sample_path = Path("../data/subsamples")
    # sample_path.mkdir(exist_ok=True)

    # dtypes = {
    #     "Unnamed: 0": int,
    #     "author":str,
    #     "title": object,
    #     "article": object,
    #     "url": str,
    #     "section":str,
    #     "publication":str}

    read_cols = [
        'Unnamed: 0',
        'date',
        'author',
        'title',
        'article',
        'url',
        'section',
        'publication']

    df = pd.read_csv(raw_path / "all-the-news-2-1.csv",
        usecols=read_cols,
        parse_dates=["date"],
        # dtype=dtypes,
        nrows=nrows)

    df = df.dropna(subset=['article'])

    # subsample topics
    topics = pd.read_csv(raw_path/'labelled_topics_by_pub_sec.csv')
    topics = topics[topics["topic"].isin(topic_list)]
    df = df.merge(topics, left_on=["section", "publication"], right_on=["section", "publication"])

    if n_samples > 0 and not df.empty:
        rng = np.random.default_rng(42)
        df = df.iloc[rng.choice(df.shape[0], min(df.shape[0], n_samples), replace=False)]
    else:
        df = df.copy()

    df = df.rename(columns={"Unnamed: 0": "article_id"})
    df.to_csv(f"{sample_path}/{sample_file_name}.csv", index=False)



if __name__ == '__main__':
    untar_news_file("data/data_raw", "all-the-news-2-1")
    sample_articles("test_sample", n_samples=1)
