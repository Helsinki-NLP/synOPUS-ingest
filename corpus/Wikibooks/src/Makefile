

include ../Makefile.def
include ../../Makefile.def


TATOEBA_GITRAW     := https://raw.githubusercontent.com/Helsinki-NLP/Tatoeba-Challenge/refs/heads/master
TATOEBA_BT_INFO    := ${TATOEBA_GITRAW}/data/Backtranslations.md
TATOEBA_BT_STORAGE := https://object.pouta.csc.fi/Tatoeba-MT-bt


WIKI_SOURCES  := $(sort $(shell wget -qq -O - ${TATOEBA_BT_INFO} | grep '${WIKITYPE}\.' | cut -f2 -d'[' | cut -f1 -d']' | cut -f1-3 -d.))
MONOXML_FILES := $(patsubst %.db,%.xml.gz,$(wildcard ../raw/*/*.db))


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

${MONOXML_FILES}: ../raw/%.xml.gz: ../raw/%.db
	${OPUSTOOLS}/db2xml.py -d $< | gzip -c > $@

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
	  wget -qq -O $$b.$$p.$$S.gz ${TATOEBA_BT_STORAGE}/$$p/latest/$$b.$$p.$$s.gz; \
	  wget -qq -O $$b.$$p.$$T.gz ${TATOEBA_BT_STORAGE}/$$p/latest/$$b.$$p.$$t.gz; \
	  wget -qq -O $@ ${TATOEBA_BT_STORAGE}/$$p/latest/README.md; \
	  mkdir -p ../xml/$$S-$$T ../raw/$$S ../raw/$$T; \
	  echo '<?xml version="1.0" encoding="UTF-8"?>'                        > ../xml/$$S-$$T/$$b.xml; \
	  echo '<!DOCTYPE cesAlign PUBLIC "-//CES//DTD XML cesAlign//EN" "">' >> ../xml/$$S-$$T/$$b.xml; \
	  echo '<cesAlign version="1.0">'                                     >> ../xml/$$S-$$T/$$b.xml; \
	  echo "<linkGrp targType=\"s\" fromDoc=\"$$S/$$b.xml.gz\" toDoc=\"$$T/$$b.xml.gz\">" >> ../xml/$$S-$$T/$$b.xml; \
	  mkdir -p ${TMPDIR}/WIKICONVERT; \
	  if [ -e ../raw/$$S/$$b.$$S.db ]; then rsync ../raw/$$S/$$b.$$S.db ${TMPDIR}/WIKICONVERT/; fi; \
	  if [ -e ../raw/$$T/$$b.$$T.db ]; then rsync ../raw/$$T/$$b.$$T.db ${TMPDIR}/WIKICONVERT/; fi; \
	  ${OPUSTOOLS}/moses2db.py -t $$T \
				-sf $$b.$$p.$$S.gz \
				-tf $$b.$$p.$$T.gz \
				-sdb ${TMPDIR}/WIKICONVERT/$$b.$$S.db \
				-tdb ${TMPDIR}/WIKICONVERT/$$b.$$T.db \
		>> ../xml/$$S-$$T/$$b.xml; \
	  rsync ${TMPDIR}/WIKICONVERT/$$b.$$S.db ../raw/$$S/; \
	  rsync ${TMPDIR}/WIKICONVERT/$$b.$$T.db ../raw/$$T/; \
	  echo '</linkGrp>'  >> ../xml/$$S-$$T/$$b.xml; \
	  echo '</cesAlign>' >> ../xml/$$S-$$T/$$b.xml; \
	  gzip -f ../xml/$$S-$$T/$$b.xml; \
	  rm -f $$b.$$p.$$S.gz $$b.$$p.$$T.gz; \
	) 9> ${LOCKFILE_DIR}/$(word 1,$(subst ., ,$@)).$(word 2,$(subst ., ,$@)).lock


#	  cd ../raw; \
#	  moses2opus -z -s $$S -t $$T -b $$b.$$p ../src/$$b.$$p.$$S.gz ../src/$$b.$$p.$$T.gz \
#	  | gzip -c > ../xml/$$S-$$T/$$b.$$p.xml.gz )
