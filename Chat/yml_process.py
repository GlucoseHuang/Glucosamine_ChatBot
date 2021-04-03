import yaml
import xlsxwriter

files = [
    "workspace/corpus/ai.yml",
    "workspace/corpus/botprofile.yml",
    "workspace/corpus/conversations.yml",
    "workspace/corpus/emotion.yml",
    "workspace/corpus/food.yml",
    "workspace/corpus/gossip.yml",
    "workspace/corpus/greetings.yml",
    "workspace/corpus/history.yml",
    "workspace/corpus/humor.yml",
    "workspace/corpus/literature.yml",
    "workspace/corpus/money.yml",
    "workspace/corpus/movies.yml",
    "workspace/corpus/politics.yml",
    "workspace/corpus/psychology.yml",
    "workspace/corpus/science.yml",
    "workspace/corpus/sports.yml",
    "workspace/corpus/trivia.yml"
]

conversations = []
for file in files:
    with open(file, "r", encoding="utf-8") as fp:
        s = fp.read()

    conversations.extend(yaml.load(s, Loader=yaml.FullLoader)["conversations"])

book = xlsxwriter.Workbook('workspace/train.xlsx')
sheet = book.add_worksheet('record')

sheet.write(0, 0, "input")
sheet.write(0, 1, "output")
for i, con in enumerate(conversations):
    sheet.write(i + 1, 0, con[0])
    sheet.write(i + 1, 1, con[1])

book.close()
