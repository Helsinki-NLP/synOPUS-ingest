

include ../Makefile.def
include ../../Makefile.def



TATOEBA_GITRAW     := https://raw.githubusercontent.com/Helsinki-NLP/Tatoeba-Challenge/refs/heads/master
TATOEBA_BT_INFO    := ${TATOEBA_GITRAW}/data/Backtranslations.md
TATOEBA_BT_STORAGE := https://object.pouta.csc.fi/Tatoeba-MT-bt


WIKI_SOURCES  := $(sort $(shell wget -qq -O - ${TATOEBA_BT_INFO} | grep '${WIKITYPE}\.' | cut -f2 -d'[' | cut -f1 -d']' | cut -f1-3 -d.))
MONOXML_FILES := $(patsubst ../db/%.db,../raw/%.xml.gz,$(wildcard ../db/*/*.db))


## file-locking for exclusive access to certain DBs

LOCKFILE_DIR  := lock
FILELOCK_ARGS := -w 36000
FILELOCK      := flock ${FILELOCK_ARGS}

.PHONY: all
all: ${WIKI_SOURCES}
	${MAKE} db2xml

test:
	echo ${firstword ${WIKI_SOURCES}}

info:
	@echo "$(words ${WIKI_SOURCES}) language pairs to be converted"
	@echo "$(words $(filter $(wildcard ${WIKITYPE}\.*),${WIKI_SOURCES})) language pairs are done"


.PHONY: db2xml
db2xml: ${MONOXML_FILES}

${MONOXML_FILES}: ../raw/%.xml.gz: ../db/%.db
	mkdir -p $(dir $@)
	${OPUSTOOLS}/db2xml.py -d $< | gzip -c > $@


XCESALG_DOCTYPE = <!DOCTYPE cesAlign PUBLIC "-//CES//DTD XML cesAlign//EN" "">

${WIKI_SOURCES}:
	mkdir -p ${LOCKFILE_DIR}
	( ${FILELOCK} 9 || exit 1; \
	  b=$(word 1,$(subst ., ,$@)).$(word 2,$(subst ., ,$@)); \
	  p=$(word 3,$(subst ., ,$@)); \
	  s=$(word 1,$(subst -, ,$(word 3,$(subst ., ,$@)))); \
	  t=$(word 2,$(subst -, ,$(word 3,$(subst ., ,$@)))); \
	  S=$(shell iso639 -2 -k -n $(word 1,$(subst -, ,$(word 3,$(subst ., ,$@))))); \
	  T=$(shell iso639 -2 -k -n $(word 2,$(subst -, ,$(word 3,$(subst ., ,$@))))); \
	  if [ $$S == bs_Latn ]; then S='bs'; fi; \
	  if [ $$T == bs_Latn ]; then T='bs'; fi; \
	  if [ $$S == ms_Latn ]; then S='ms'; fi; \
	  if [ $$T == ms_Latn ]; then T='ms'; fi; \
	  if [ $$S == uz_Latn ]; then S='uz'; fi; \
	  if [ $$T == uz_Latn ]; then T='uz'; fi; \
	  if [ ! -e ../xml/$$S-$$T/$$b.xml.gz ]; then \
	    wget -qq -O $$b.$$p.$$S.gz ${TATOEBA_BT_STORAGE}/$$p/latest/$$b.$$p.$$s.gz; \
	    wget -qq -O $$b.$$p.$$T.gz ${TATOEBA_BT_STORAGE}/$$p/latest/$$b.$$p.$$t.gz; \
	    mkdir -p ../xml/$$S-$$T ../db/$$S ../db/$$T; \
	    echo '<?xml version="1.0" encoding="UTF-8"?>' > ../xml/$$S-$$T/$$b.xml; \
	    echo '${XCESALG_DOCTYPE}'                    >> ../xml/$$S-$$T/$$b.xml; \
	    echo '<cesAlign version="1.0">'              >> ../xml/$$S-$$T/$$b.xml; \
	    echo "<linkGrp targType=\"s\" fromDoc=\"$$S/$$b.src.xml.gz\" toDoc=\"$$T/$$b.trg.xml.gz\">"         >> ../xml/$$S-$$T/$$b.xml; \
	    mkdir -p ${TMPDIR}/$@.$$S ${TMPDIR}/$@.$$T; \
	    if [ -e ../db/$$S/$$b.src.db ]; then rsync ../db/$$S/$$b.src.db ${TMPDIR}/$@.$$S/; fi; \
	    if [ -e ../db/$$T/$$b.trg.db ]; then rsync ../db/$$T/$$b.trg.db ${TMPDIR}/$@.$$T/; fi; \
	    ${OPUSTOOLS}/moses2db.py -t $$T \
				-sf $$b.$$p.$$S.gz \
				-tf $$b.$$p.$$T.gz \
				-sdb ${TMPDIR}/$@.$$S/$$b.src.db \
				-tdb ${TMPDIR}/$@.$$T/$$b.trg.db \
		>> ../xml/$$S-$$T/$$b.xml; \
	    rsync ${TMPDIR}/$@.$$S/$$b.src.db ../db/$$S/; \
	    rsync ${TMPDIR}/$@.$$T/$$b.trg.db ../db/$$T/; \
	    find ${TMPDIR}/$@.$$S -delete; \
	    find ${TMPDIR}/$@.$$T -delete; \
	    echo '</linkGrp>'  >> ../xml/$$S-$$T/$$b.xml; \
	    echo '</cesAlign>' >> ../xml/$$S-$$T/$$b.xml; \
	    gzip -f ../xml/$$S-$$T/$$b.xml; \
	    rm -f $$b.$$p.$$S.gz $$b.$$p.$$T.gz; \
	  fi; \
	  wget -qq -O $@ ${TATOEBA_BT_STORAGE}/$$p/latest/README.md; \
	) 9> ${LOCKFILE_DIR}/$(word 1,$(subst ., ,$@)).$(word 2,$(subst ., ,$@)).lock

