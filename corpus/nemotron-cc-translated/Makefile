# -*-makefile-*-
#
# use project_2005815 for allas storage
# --> HPLT project (100TiB storage available)
#

include Makefile.def
include ../Makefile.def


.PHONY: all
all:
	${MAKE} xml/Makefile
	${MAKE} -C xml create-align-files
	${MAKE} release

#	${MAKE} delete-empty-bitexts


xml-consolidate:
	${MAKE} -C xml create-align-files



## test and compare some counts

TRANSLATE_DIR = /users/tiedeman/research/translate-fineweb/maxidl/nemotron-cc-english-run1/translated
OPUS_RELEASE_DIR = /users/tiedeman/synOPUS-ingest/releases/nemotron-cc-translated

count-de:
	pigz -cd ${TRANSLATE_DIR}/txt/deu/*.txt.gz | wc -w > $@
	pigz -cd ${TRANSLATE_DIR}/jsonl/deu/*.jsonl.gz | jq -r '.text' | grep --text . | wc -w >> $@
	unzip -p ${OPUS_RELEASE_DIR}/v1syn/raw/de.zip '*.xml' | sed 's/<[^>]*>//g' |  grep --text . | wc -w >> $@

count-en:
	pigz -cd ${TRANSLATE_DIR}/txt/eng/*.txt.gz | wc -w > $@
	pigz -cd ${TRANSLATE_DIR}/jsonl/eng/*.jsonl.gz | jq -r '.text' | grep --text . | wc -w >> $@
	unzip -p ${OPUS_RELEASE_DIR}/v1syn/raw/en.zip '*.xml' | sed 's/<[^>]*>//g' |  grep --text . | wc -w >> $@





## standard procedures are specified in the following makefiles
##
##   Makefile.submit ....... submit a job to our cluster
##   Makefile.process ...... standard corpus processing tasks
##   Makfile.release ....... download packages and website
##   Makefile.cwb .......... indexing with CWB
##   Makfile.udparse ....... dependency parsing

include ../Makefile.submit
include ../Makefile.process
include ../Makefile.release
# include ../Makefile.cwb
# include ../Makefile.udparse



## small fix to remove strings from opus_read messages

# ALG_SAMPLE_FIX= $(patsubst %.html,%.html.backup,${ALG_SAMPLES})
# fix-alg-samples: ${ALG_SAMPLE_FIX}
# ${ALG_SAMPLE_FIX}: %.html.backup: %.html
# 	mv $< $@
# 	sed -e "s/Measuring file.*\r//" < $@ > $<
# 	touch $@




## select one of the following to set the annotation level in xml/
##
##   Makefile.tokenize ..... tokenization only
##   Makefile.tag .......... tokenization and PoS tagging (if available)
##   Makefile.annotate ..... all annotation in Uplug


include ../Makefile.tokenize-polyglot
# include ../Makefile.tokenize-fast
# include ../Makefile.tokenize-moses
# include ../Makefile.tokenize
# include ../Makefile.tag
# include ../Makefile.annotate


XMLNEW = $(patsubst xml/%,xml-new/%,$(wildcard xml/*.xml.gz))

fixxml: ${XMLNEW}

${XMLNEW}: xml-new/%: xml/%
	mkdir -p $(dir $@)
	zcat $< | sed 's/\.gz//g' | gzip -c > $@
