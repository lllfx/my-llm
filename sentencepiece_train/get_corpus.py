with open("data/红楼梦.txt", "r", encoding="utf-8") as fp:
    data = fp.read().strip().split("\n")

with open("data/corpus.txt", "w", encoding="utf-8") as fp:
    for d in data:
        d = d.strip()
        if "===" in d or len(d) == 0 or d == "《斗破苍穹》来自:":
            continue
        print(d,file=fp)


