import sentencepiece as spm

sp = spm.SentencePieceProcessor()

text = "这贾雨村原系胡州人氏，也是诗书仕宦之族，因他生于末世，父母祖宗根基已尽，人口衰丧，只剩得他一身一口，在家乡无益，因进京求取功名，再整基业。"

sp.Load("tokenizer.model")
print(sp.EncodeAsPieces(text))