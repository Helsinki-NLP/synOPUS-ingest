#!/usr/bin/env python3


import sys
import gzip
import argparse
import pycld2 as cld2
from sqlitedict import SqliteDict
from heliport import Identifier
from langcodes import *

parser = argparse.ArgumentParser()
parser.add_argument("-sf", "--source-file", type=str, help="source language file (gzip format)", required=True)
parser.add_argument("-tf", "--target-file", type=str, help="target language file (gzip format)", required=True)
parser.add_argument("-s",  "--source-language", type=str, help="Language to be tokenized (BCP 47)")
parser.add_argument("-t",  "--target-language", type=str, help="Language to be tokenized (BCP 47)")
parser.add_argument("-sdb", "--source-db", type=str, default="source.db", help="Source Language DB")
parser.add_argument("-tdb", "--target-db", type=str, default="target.db", help="Target Language DB")

args = parser.parse_args()

lid = Identifier()

sdb = SqliteDict(args.source_db)
tdb = SqliteDict(args.target_db)

srclang = args.source_language
trglang = args.target_language

srcfile = args.source_file
trgfile = args.target_file

if '___LASTID___' in sdb: lastsrcid = sdb['___LASTID___']
else: lastsrcid = 0

if '___LASTID___' in tdb: lasttrgid = tdb['___LASTID___']
else: lasttrgid = 0

wrongsrc = 0
wrongtrg = 0

with gzip.open(srcfile,'rt') as sf:
    with gzip.open(trgfile,'rt') as tf:
        for srcline in sf:
            trgline = tf.readline()

            if srclang and srclang=='uz':
                isReliable, textBytesFound, details = cld2.detect(srcline)
                if not isReliable: continue
                if details[0][1] != 'uz': continue
                    
            elif srclang:
                
                srcdetect3 = lid.identify(srcline)
                srcdetect = standardize_tag(srcdetect3)
                
                ## some tricks and heuristics to fix misatches in langids
                ## (is it OK to support nds detected as Dutch?)
                if srcdetect == 'cmn' and srclang.startswith('zh'): srcdetect = srclang
                elif srcdetect3 == 'msa' and srclang == 'id': srcdetect = srclang
                elif srcdetect3 == 'nld' and srclang == 'nds': srcdetect = srclang
                elif srcdetect3 == 'tgl' and srclang == 'tl': srcdetect = srclang
                elif srcdetect3 == 'hbs':
                    if srclang.startswith('bs'): srcdetect = srclang
                    elif srclang.startswith('sr'): srcdetect = srclang
                    elif srclang.startswith('hr'): srcdetect = srclang
                if srcdetect.replace('-','_') != srclang:
                    # sys.stderr.write(f"srcline {srcdetect} != {srclang}\n")
                    # sys.stderr.write('*')
                    # sys.stderr.flush()
                    wrongsrc += 1
                    continue

            if trglang and trglang=='uz':
                isReliable, textBytesFound, details = cld2.detect(trgline)
                if not isReliable: continue
                if details[0][1] != 'uz': continue

            elif trglang:
                trgdetect3 = lid.identify(trgline)
                trgdetect = standardize_tag(trgdetect3)
                if trgdetect == 'cmn' and trglang.startswith('zh'): trgdetect = trglang
                elif trgdetect3 == 'msa' and trglang == 'id': trgdetect = trglang
                elif trgdetect3 == 'nld' and trglang == 'nds': trgdetect = trglang
                elif trgdetect3 == 'tgl' and trglang == 'tl': trgdetect = trglang
                elif trgdetect3 == 'hbs':
                    if trglang.startswith('bs'): trgdetect = trglang
                    elif trglang.startswith('sr'): trgdetect = trglang
                    elif trglang.startswith('hr'): trgdetect = trglang

                if trgdetect.replace('-','_') != trglang:
                    # sys.stderr.write(f"trgline {trgdetect} != {trglang}\n")
                    # sys.stderr.write('+')
                    # sys.stderr.flush()
                    wrongtrg += 1
                    continue
                

            if srcline in sdb:
                srcid = sdb[srcline]
            else:
                lastsrcid += 1
                srcid = lastsrcid
                sdb[srcline] = srcid

            if trgline in tdb:
                trgid = tdb[trgline]
            else:
                lasttrgid += 1
                trgid = lasttrgid
                tdb[trgline] = trgid

            print(f"  <link xtargets='{srcid};{trgid}' />")

            if not srcid % 1000:
                sys.stderr.write('.')
                if not srcid % 10000:
                    sys.stderr.write(f" commit sdb {srcid}\n")
                    sdb.commit()
                sys.stderr.flush()

            if not trgid % 1000:
                sys.stderr.write('.')
                if not trgid % 10000:
                    sys.stderr.write(f" commit tdb {trgid}\n")
                    tdb.commit()
                sys.stderr.flush()


if wrongsrc: sys.stderr.write(f"wrong source language detected in {srcfile}: {wrongsrc}\n")
if wrongtrg: sys.stderr.write(f"wrong target language detected in {trgfile}: {wrongtrg}\n")

sdb['___LASTID___'] = lastsrcid
tdb['___LASTID___'] = lasttrgid

sdb.commit()
tdb.commit()
sdb.close()
tdb.close()

