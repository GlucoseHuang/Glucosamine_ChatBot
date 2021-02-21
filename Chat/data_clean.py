import pandas as pd
import re

df = pd.read_excel(r"record.xlsx")
df = df.astype("str")
df2 = df[~df[1].str.contains("^((\[表情\])|(\[图片\])|(@全体成员)|(@全体成员 )|(@.{1,16} )|( @.{1,16})|(nan)|())$")]
df2[1] = df2[1].str.replace(r"((\[表情\])|(\[图片\])|(@全体成员)|(@全体成员 )|(@.{1,16} )|( @.{1,16}))", "")

df2.index= range(len(df2.index))
df2["label"] = pd.Series(list(map(lambda x: int(x) % 2 + 1, df2.index.tolist())))
df2.to_excel("1.xlsx")