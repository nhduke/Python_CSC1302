# lab12.py  — Pandas Mini-Practice 
# pip or pip3 install pandas if you have not installed pandas
# Run:  python lab12.py

import pandas as pd

# ----------------------------
# Fixed mini datasets (given)
# ----------------------------

df_people = pd.DataFrame(
    {
        "id":   [101, 102, 103, 104],
        "name": ["Ana", "Bo", "Chen", "Dee"],
        "age":  [20,   22,   21,    20],
    }
)

df_scores = pd.DataFrame(
    {
        "id":    [101, 102, 104, 105],
        "score": [88,   72,   59,  91],
    }
)

# ----------------------------
# Functions to implement
# ----------------------------
def sort_by_age(df):
    """
    Return df sorted by 'age' ascending.

    Hint: df.sort_values(by="age", ascending=True, ignore_index=True)
    """
    return df.sort_values(by="age", ascending=True, ignore_index=True)


def sort_by_age_then_name(df):
    """
    Return df sorted by age asc, then name desc.

    Hint: df.sort_values(by=["age","name"], ascending=[True, False], ignore_index=True)
    """
    return df.sort_values(by=["age","name"], ascending=[True, False], ignore_index=True)


def select_name_age_21_plus(df):
    """
    Keep columns ["name","age"] and rows where age >= 21.

    Hint: df.loc[df["age"] >= 21, ["name","age"]].reset_index(drop=True)
    """
    return df.loc[df["age"] >= 21, ["name","age"]].reset_index(drop=True)


def resize_people(df):
    """
    Resize df_people:
      - Add one new row (e.g., id=106, name='Eli', age=23)
      - Add a new column 'age_plus_1' = age + 1
      - Drop the original 'age' column and return

    Hints:
      - pd.concat([df, pd.DataFrame([row_dict])], ignore_index=True)
      - df["age_plus_1"] = df["age"] + 1
      - df.drop(columns=["age"])
    """
    row_dict = {"id": 106, "name": "Eli", "age": 23}
    df_new = pd.concat([df, pd.DataFrame([row_dict])], ignore_index=True)
    df_new["age_plus_1"] = df_new["age"] + 1
    df_new = df_new.drop(columns=["age"])
    return df_new


def merge_people_scores_left(df_ppl, df_scr):
    """
    Left-merge df_people with df_scores on 'id' (keep all people).

    Hint: pd.merge(df_ppl, df_scr, how="left", on="id")
    """
    return pd.merge(df_ppl, df_scr, how="left", on="id")


def concat_rows(df):
    """
    Row-wise: split df_people into two parts and concat back together.

    Hints:
      - mid = len(df)//2; top = df.iloc[:mid]; bottom = df.iloc[mid:]
      - pd.concat([top, bottom], ignore_index=True)
    """
    mid = len(df) // 2
    top = df.iloc[:mid]
    bottom = df.iloc[mid:]
    return pd.concat([top, bottom], ignore_index=True)


def concat_cols(df_ppl, df_scr):
    """
    Column-wise: concat df_people[["id"]] and df_scores[["score"]].
    (Indices may differ; use reset_index to align row counts for display.)

    Hint: pd.concat([A.reset_index(drop=True), B.reset_index(drop=True)], axis=1)
    """
    A = df_ppl[["id"]].reset_index(drop=True)
    B = df_scr[["score"]].reset_index(drop=True)
    return pd.concat([A, B], axis=1)


# ==========================
# Tiny PASS/FAIL test suite. DO NOT EDIT CONTENT BELOW.
# ==========================
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def check(name, cond):
    print(f"{name}: " + (f"{GREEN}PASS{RESET}" if cond else f"{RED}FAIL{RESET}"))

def main():
    print("=== Lab 12: Pandas Mini-Practice ===\n")

    # 1) Sorts
    s1 = sort_by_age(df_people)
    check("Sort by age asc (is_monotonic_increasing)",
          s1["age"].is_monotonic_increasing)

    s2 = sort_by_age_then_name(df_people)
    # verify first by age; within equal ages (20), names should be desc: 'Dee' before 'Ana'
    ok_age = s2["age"].is_monotonic_increasing
    # find equal-age blocks and ensure names are descending within those blocks
    ok_ties = True
    for age_val, group in s2.groupby("age"):
        names = list(group["name"])
        if names != sorted(names, reverse=True):
            ok_ties = False
            break
    check("Sort by age asc, then name desc (ties handled)", ok_age and ok_ties)

    # 2) Select
    sel = select_name_age_21_plus(df_people)
    check("Select columns ['name','age']",
          list(sel.columns) == ["name", "age"])
    check("Select rows age >= 21",
          (sel["age"].min() >= 21) if not sel.empty else True)

    # 3) Resize
    rz = resize_people(df_people)
    check("Resize: +1 row",
          rz.shape[0] == df_people.shape[0] + 1)
    check("Resize: has 'age_plus_1' and dropped 'age'",
          ("age_plus_1" in rz.columns) and ("age" not in rz.columns))

    # 4) Merge (left)
    mg = merge_people_scores_left(df_people, df_scores)
    # All people retained:
    check("Merge-left keeps all people",
          mg.shape[0] == df_people.shape[0])
    # At least one NaN score (id=103 has no score; should be NaN)
    check("Merge-left produces NaN for missing scores",
          mg["score"].isna().any())

    # 5) Concat
    rcat = concat_rows(df_people)
    # Should equal original after split+stitch:
    check("Concat rows reconstructs df_people",
          rcat.reset_index(drop=True).equals(df_people.reset_index(drop=True)))

    ccat = concat_cols(df_people, df_scores)
    check("Concat cols has both 'id' and 'score'",
          set(ccat.columns) == {"id", "score"})

    print("\nDone.")

if __name__ == "__main__":
    main()
