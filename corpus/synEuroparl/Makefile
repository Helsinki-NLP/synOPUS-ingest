

SCRIPT_DIR    := $(CURDIR)/scripts
ALIGNED_DIR   := $(CURDIR)/../aligned
EUROPARL_DIR  := /projappl/nlpl/data/OPUS/Europarl/v8

LANGPAIRS     := $(sort $(notdir $(wildcard $(ALIGNED_DIR)/*-*)))
ALIGN_XML     := $(addsuffix .xml.gz,${LANGPAIRS})
LANG_ZIP      := $(addsuffix .zip,$(wildcard ??))
TRG_LANGS     := $(patsubst en-%,%,${LANGPAIRS})


## non-English languages in Europarl (that are aligned to English)

EP_ENXX_LANGS := $(patsubst en-%.xml.gz,%,$(notdir $(wildcard ${EUROPARL_DIR}/xml/en-*.xml.gz))) \
		 $(patsubst %-en.xml.gz,%,$(notdir $(wildcard ${EUROPARL_DIR}/xml/*-en.xml.gz)))


## alignments between the new target languages (pivoted through English)

TRG_ALIGN_XML := $(shell for s in ${TRG_LANGS}; do \
	  		     for t in ${TRG_LANGS}; do \
	    		        if [ $$s \< $$t ]; then \
			          echo "xml/$$s-$$t.xml.gz"; \
			        fi \
			     done \
			   done )

## alignments between the new target languages and non-English Europarl languages
## (pivoted through English)

ENXX_ALIGN_XML := $(shell for s in ${TRG_LANGS}; do \
	  		     for t in ${EP_ENXX_LANGS}; do \
	    		        if [ $$s \< $$t ]; then \
			          echo "xml/$$s-$$t.xml.gz"; \
			        else \
			          echo "xml/$$t-$$s.xml.gz"; \
			        fi \
			     done \
			   done )



.PHONY: all
all: ${ALIGN_XML}
	${MAKE} zipfiles multi multiparallel
	find Europarl -delete
	find . -type l -name '*.xml.gz' -delete
	${MAKE} move-files


.PHONY: move-files
move-files:
	mkdir -p xml raw
	mv *.zip raw/
	mv *.xml.gz xml/
	cp /projappl/nlpl/data/OPUS/Europarl/v8/raw/*.zip raw/





## multi-parallel corpus (consistent sentence alignments across all language pairs)

multiparallel: ${ALIGN_XML}
	mkdir -p $@
	cd $@ && opus2multi .. en $(patsubst en-%,%,${LANGPAIRS})
	gzip $@/*.xml



## pivoting through english

multi: ${TRG_ALIGN_XML} ${ENXX_ALIGN_XML}

${TRG_ALIGN_XML}:
	mkdir -p $(dir $@)
	( s=$(firstword $(subst -, ,$(notdir $(@:.xml.gz=)))); \
	  t=$(lastword $(subst -, ,$(notdir $(@:.xml.gz=)))); \
	  cd $(dir $@); \
	  $(SCRIPT_DIR)/opus2multi $(CURDIR) en $$s $$t; \
	  $(SCRIPT_DIR)/opus-pivoting en-$$s.xml en-$$t.xml | gzip -c > $(notdir $@); \
	  rm -f en-$$s.xml en-$$t.xml; )

${ENXX_ALIGN_XML}:
	mkdir -p $(dir $@)
	( s=$(firstword $(subst -, ,$(notdir $(@:.xml.gz=)))); \
	  t=$(lastword $(subst -, ,$(notdir $(@:.xml.gz=)))); \
	  if [ -e ${EUROPARL_DIR}/xml/$$s-en.xml.gz ]; then \
	    ln -s ${EUROPARL_DIR}/xml/$$s-en.xml.gz .; \
	  fi; \
	  if [ -e ${EUROPARL_DIR}/xml/en-$$t.xml.gz ]; then \
	    ln -s ${EUROPARL_DIR}/xml/en-$$t.xml.gz .; \
	  fi; \
	  cd $(dir $@); \
	  $(SCRIPT_DIR)/opus2multi $(CURDIR) en $$s $$t; \
	  $(SCRIPT_DIR)/opus-pivoting en-$$s.xml en-$$t.xml | gzip -c > $(notdir $@); \
	  rm -f en-$$s.xml en-$$t.xml; )
	if [ `zgrep xtargets $@ | head -1 | wc -l` -eq 0 ]; then \
	  echo "alignment file for $@ is empty --> delete"; \
	  rm -f $@; \
	fi

.PHONY: delete-empty-multi
delete-empty-multi:
	for f in `ls xml/*.xml.gz`; do \
	  if [ `zgrep xtargets $$f | head -1 | wc -l` -eq 0 ]; then \
	    echo "alignment file for $$f is empty --> delete"; \
	    rm -f $$f; \
	  fi \
	done



## convert jsonl files to OPUS XML files

${ALIGN_XML}:
	${SCRIPT_DIR}/jsonl_to_opus.py \
		-s $(firstword $(subst -, ,$(@:.xml.gz=))) \
		-t $(lastword $(subst -, ,$(@:.xml.gz=))) \
	< $(ALIGNED_DIR)/$(@:.xml.gz=)/$(@:.xml.gz=)-aligned-output-fixed.jsonl \
	| sed 's/><\/link>/\/>/' | gzip -c > $@


## pack all corpus files into OPUS compatible zipfiles

.PHONY: zipfiles
zipfiles: ${LANG_ZIP}

${LANG_ZIP}:
	mkdir -p Europarl/raw
	mv $(@:.zip=) Europarl/raw/
	zip -q -r $@ Europarl/raw/$(@:.zip=)
	echo 'Europarl/raw/$(@:.zip=)' > Europarl/raw/$(@:.zip=)/INFO
	echo 'Europarl'               >> Europarl/raw/$(@:.zip=)/INFO
	echo 'vGPT4-2025'             >> Europarl/raw/$(@:.zip=)/INFO
	zip -j $@ Europarl/raw/$(@:.zip=)/INFO
	find Europarl/raw/$(@:.zip=) -delete
