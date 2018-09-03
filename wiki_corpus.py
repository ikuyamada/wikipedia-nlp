# -*- coding: utf-8 -*-

import bz2
import sys
from rdflib import Graph

def read_ttl(f):
  lines = []
  for line in f:
    lines.append(line.decode('utf-8').rstrip())
    if len(lines) == 1000: #1000行をまとめて処理
      for triple in parse_lines(lines):
        yield triple
      lines = []
  if lines:
    for triple in parse_lines(lines):
      yield triple

def parse_lines(lines):
  g = Graph()
  g.parse(data=u'\n'.join(lines), format='n3')
  return g

with bz2.BZ2File(sys.argv[1]) as in_file:
  for (_, p, o) in read_ttl(in_file):
    if p.toPython() == 'http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#isString':
      print(o.toPython())
