# -*- coding: utf-8 -*-

import sys
from wikipedia2vec.dictionary import Dictionary
from wikipedia2vec.mention_db import MentionDB

dic = Dictionary.load(sys.argv[1])
db = MentionDB.load(sys.argv[2], dic)
words = set()

for mention in db:
  if mention.link_prob >= 0.1:
    if mention.text not in words:
      words.add(mention.text)
      print(mention.text)
