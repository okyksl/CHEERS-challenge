from ast import literal_eval
from collections import defaultdict, Counter

import numpy as np
import pandas as pd

sentences_train = pd.read_csv("./DFS_NLP_Challenge_2021_round_1/sentences_en_train.csv")
sentences_test = pd.read_csv(
    "./DFS_NLP_Challenge_2021_round_1/sentences_en_test.csv",
    usecols=["doc_id", "sentence_id"],
)
# Calculate class counts for `is_relevant`
is_relevant_coutns = sentences_train["is_relevant"].value_counts().to_dict()
is_relevant_coutns = Counter(is_relevant_coutns)
# Calculate class probabilities for `is_relevant`
is_relevant_coutns_zero_prob = is_relevant_coutns[0] / (
    is_relevant_coutns[0] + is_relevant_coutns[1]
)
is_relevant_coutns_one_prob = is_relevant_coutns[1] / (
    is_relevant_coutns[0] + is_relevant_coutns[1]
)
# Generate random samples according to the training data probabilities
sentences_test["is_relevant"] = np.random.choice(
    [0, 1],
    size=len(sentences_test),
    p=[is_relevant_coutns_zero_prob, is_relevant_coutns_one_prob],
)

# convert `sector_ids` from string to python list
sentences_train["sector_ids"] = sentences_train["sector_ids"].apply(literal_eval)
# Calculate class counts for `sector_ids`
sector_id_freqs = defaultdict(int)
for sids in sentences_train["sector_ids"].tolist():
    for sid in sids:
        sector_id_freqs[sid] += 1
sector_id_freqs = Counter(sector_id_freqs)
# Calculate class probabilities for `sector_ids`
all_counts = sum(sector_id_freqs.values())
sector_id_probs = {
    cls_id: sector_id_freqs[cls_id] / all_counts for cls_id in sector_id_freqs.keys()
}
# Generate random samples according to the training data probabilities
choices = list(sector_id_probs.keys())
probs = list(sector_id_probs.values())
num_samples = sentences_test["is_relevant"].eq(1).sum()
sentences_test["sector_id"] = -1
sentences_test.loc[sentences_test["is_relevant"].eq(1), "sector_id"] = np.random.choice(
    choices, size=num_samples, p=probs
)


sentences_test.to_csv(
    "test_biased_random_baseline.csv",
    index=None,
    columns=["doc_id", "sentence_id", "is_relevant", "sector_id"],
)
