from src.data_selection import sample_articles, sample_by_topic



# sample_articles("10k_random", n_samples=10000, nrows=50000)

sample_by_topic("sample50k_topic4",
    ["health", "technology", "politics", "entertain"],
    n_samples=50000
    )
