NPROCESSORS := $(shell getconf _NPROCESSORS_ONLN)
MAKEFLAGS += -j$(NPROCESSORS)

# Create a list of existing txt files.

ORG_TXT_FILES:= \
	$(shell find /test -type f -name "*.txt" ! -name '*.N1.txt' ! -name '*.S1.txt') \
	$(shell find /data -type f -name "*.txt" ! -name '*.N1.txt' ! -name '*.S1.txt') \

N1_TXT_FILES = $(patsubst %.txt,%.N1.txt,$(ORG_TXT_FILES))
S1_TXT_FILES = $(patsubst %.txt,%.S1.txt,$(ORG_TXT_FILES))

MANY_ORG_JPG_FILES:= $(patsubst %.txt,%.jpg,$(ORG_TXT_FILES))
ORG_JPG_FILES:= $(filter $(wildcard $(MANY_ORG_JPG_FILES)),$(MANY_ORG_JPG_FILES))
N1_JPG_FILES:= $(patsubst %.jpg,%.N1.jpg,$(ORG_JPG_FILES))
S1_JPG_FILES:= $(patsubst %.jpg,%.S1.jpg,$(ORG_JPG_FILES))

.PHONY: all

all: \
	$(N1_TXT_FILES) \
	$(N1_JPG_FILES) \
	$(S1_TXT_FILES) \
	$(S1_JPG_FILES)

#	echo $(ORG_JPG_FILES)

$(N1_JPG_FILES) : %.N1.jpg : %.jpg
	 convert $< +noise Impulse $@

$(N1_TXT_FILES) : %.N1.txt : %.txt
	cp $< $@

$(S1_JPG_FILES) : %.S1.jpg : %.jpg
	 convert $< -unsharp 0x3+2.0 $@

$(S1_TXT_FILES) : %.S1.txt : %.txt
	cp $< $@


.PHONY: clean

clean:
	-rm \
		$(N1_TXT_FILES) \
		$(N1_JPG_FILES) \
		$(S1_TXT_FILES) \
		$(S1_JPG_FILES) \
		2>/dev/null



