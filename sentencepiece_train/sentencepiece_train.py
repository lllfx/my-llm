import sentencepiece as spm

spm.SentencePieceTrainer.train(
    input='data/corpus.txt',
    model_prefix='tokenizer',
    vocab_size=4000,
    character_coverage=0.9995,
    model_type="bpe",
)
