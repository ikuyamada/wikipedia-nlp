# -*- coding: utf-8 -*-

import logging
import sys
from gensim.models.word2vec import Word2Vec, LineSentence

logging.basicConfig(level=logging.INFO)

model = Word2Vec(LineSentence(sys.argv[1]), sg=1)
model.save(sys.argv[2])
