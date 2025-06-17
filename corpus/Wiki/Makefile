# -*-makefile-*-
#


include Makefile.def
include ../Makefile.def


.PHONY: all
all:
	${MAKE} -C src all
	${MAKE} xml/Makefile
	${MAKE} -C xml create-align-files
	${MAKE} delete-empty-bitexts
	${MAKE} release


fix:
	zgrep '<linkGrp' xml/*.xml.gz | grep -v fromDoc | cut -f1 -d: | sort -u | xargs rm
	${MAKE} all

fix-xmlalg:
	@for l in $(wildcard xml/*.xml.gz); do \
	  mv $$l $$l.tmp; \
	  zcat $$l.tmp | tidy -w -xml -i | gzip -c > $$l; \
	done
#	  if [ `zcat $$l | grep '</linkGrp>' | wc -l` -gt 1 ]; then \
#	    echo "$$l"; \
#	    mv $$l $$l.tmp.gz; \
#	    zcat $$l.tmp.gz | sed 's|</linkGrp>||' | sed 's|</cesAlign>|</linkGrp></cesAlign>|' \
#	    | gzip -c > $$l; \
#	  fi \
#	done

# fix-db:
# 	for d in $(patsubst %.db,%,$(notdir $(wildcard raw/*/*.db))); do \
# 	  l=`echo $$d | cut -f3 -d.`; \
# 	  b=`echo $$d | cut -f1,2 -d.`; \
# 	  mkdir -p db/$$l; \
# 	  mv raw/$$l/$$d.db db/$$l/$$b.db; \
# 	done


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

