import argparse
import pandas as pd
from sklearn.metrics import f1_score


def hamming_score(y_true, y_pred):
    # https://link.springer.com/chapter/10.1007/978-3-540-24775-3_5
    score = 0
    for yt, yp in zip(y_true, y_pred):
        yt, yp = set(yt), set(yp)
        score += len(yt & yp) / len(yt | yp)
    return score / len(y_true)


example_text = """example:

python eval.py --gold-file ./DFS_NLP_Challenge_2021/sentences_val.csv --pred-file preds_val.csv"""

parser = argparse.ArgumentParser(
    description="Calculate the evaluation metrics.",
    epilog=example_text,
    formatter_class=argparse.RawDescriptionHelpFormatter,
)
parser.add_argument(
    "-g", "--gold-file", help="The ground truth csv file.", type=str, required=True
)
parser.add_argument(
    "-p", "--pred-file", help="The prediction csv file.", type=str, required=True
)

args = parser.parse_args()

df_true = pd.read_csv(
    args.gold_file, usecols=["doc_id", "sentence_id", "is_relevant", "sector_ids"],
)
df_pred = pd.read_csv(
    args.pred_file, usecols=["doc_id", "sentence_id", "is_relevant", "sector_ids"],
)

if len(df_pred) != len(df_true):
    print("Both files must have same number of instances")
    exit()

df_eval = pd.merge(
    df_true,
    df_pred,
    on=["doc_id", "sentence_id"],
    how="left",
    suffixes=("_true", "_pred"),
)
y_true_relevance, y_pred_relevance = (
    df_eval["is_relevant_true"].tolist(),
    df_eval["is_relevant_pred"].tolist(),
)
y_pred_relevance = list(map(lambda x: -1 if pd.isna(x) else x, y_pred_relevance))
f1_score_relevance = f1_score(y_true_relevance, y_pred_relevance, average="macro")

print(f"Macro-averaged F1 score for is_relevant variable is: {f1_score_relevance*100:.2f}")


y_true_sectorids, y_pred_sectorids = (
    df_eval["sector_ids_true"].tolist(),
    df_eval["sector_ids_pred"].tolist(),
)
# y_pred_sectorids = list(map(lambda x: [] if pd.isna(x) else x, y_pred_sectorids))
hamming_score_sectorids = hamming_score(y_true_sectorids, y_pred_sectorids)
print(f"Accuracy for sector_ids variable is: {hamming_score_sectorids*100:.2f}")
