# -*- coding: utf-8 -*-

import sys
from wikipedia2vec.dictionary import Dictionary
from wikipedia2vec.mention_db import MentionDB
from wikipedia2vec.utils.tokenizer.mecab_tokenizer import MeCabTokenizer

dic = Dictionary.load(sys.argv[2])
db = MentionDB.load(sys.argv[3], dic)
with open(sys.argv[1]) as f:
  text = f.read()

tokenizer = MeCabTokenizer()
tokens = tokenizer.tokenize(text)

for mention in db.detect_mentions(text, tokens):
  print(mention)
