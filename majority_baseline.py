import pandas as pd

sentences_test = pd.read_csv(
    "./DFS_NLP_Challenge_2021_round_1/sentences_en_test.csv",
    usecols=["doc_id", "sentence_id"],
)
sentences_test["is_relevant"] = 0
sentences_test["sector_id"] = -1
sentences_test.to_csv(
    "test_majority_baseline.csv",
    index=None,
    columns=["doc_id", "sentence_id", "is_relevant", "sector_id"],
)
