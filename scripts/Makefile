
# Create a list of existing txt files.
space := $(subst ,, )

ORG_TXT_FILES:= $(shell find /test -type f -name "*.txt" ! -name '*.N1.txt' -printf '%p*')
ORG_TXT_FILES:= $(subst $(space),\$(space),$(ORG_TXT_FILES))
ORG_TXT_FILES:= $(subst *,$(space),$(ORG_TXT_FILES))

N1_TXT_FILES = $(patsubst %.txt,%.N1.txt,$(ORG_TXT_FILES))

MANY_ORG_JPG_FILES:= $(patsubst %.txt,%.jpg,$(ORG_TXT_FILES))
ORG_JPG_FILES:= $(filter $(wildcard $(MANY_ORG_JPG_FILES)),$(MANY_ORG_JPG_FILES))
N1_JPG_FILES:= $(patsubst %.jpg,%.N1.jpg,$(ORG_JPG_FILES))

.PHONY: all

all: $(N1_TXT_FILES) $(N1_JPG_FILES)
	echo $(ORG_JPG_FILES)

$(N1_JPG_FILES) : %.N1.jpg : %.jpg
	 convert $< +noise Impulse $@

$(N1_TXT_FILES) : %.N1.txt : %.txt
	cp $< $@


.PHONY: clean

clean:
	rm $(N1_TXT_FILES) $(N1_JPG_FILES)



