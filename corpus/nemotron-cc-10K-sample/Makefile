# -*-makefile-*-
#


include Makefile.def
include ../Makefile.def


.PHONY: all
all:
	${MAKE} xml/Makefile
	${MAKE} -C xml create-align-files
	${MAKE} delete-empty-bitexts
	${MAKE} release


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
