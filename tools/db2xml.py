#!/usr/bin/env python3


import sys
import gzip
import argparse
from xml.sax.saxutils import XMLGenerator
from sqlitedict import SqliteDict

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--database", type=str, help="database file", required=True)
args = parser.parse_args()


db = SqliteDict(args.database)
writer = XMLGenerator(sys.stdout, 'utf-8')
writer.startDocument()
writer.startElement('document', {})
writer.characters("\n")
    
for key,val in db.items():
    writer.startElement('s', { 'id': str(val) })
    writer.characters(key.strip())
    writer.endElement('s')
    writer.characters("\n")

writer.endElement('document')
writer.characters("\n")
writer.endDocument()
