SOURCE = main.xsm
BIN = main.bin
CAS = main.cas
WAV = main.wav

subdirs := font text

FONT_DATA = font/font_data.xsm
TEXT_DATA = text/text_data.xsm

XSM_JAR_PATH = "../xsm/xsm/xsm.jar"
XSM_LIB_PATH = "../xsm/xsm/library"
OPEN_EMU= open -a PC6001VX
COPY_TO_EMU	= cp $(CAS) ~/.pc6001vx/tape

.PHONY: all $(subdirs)
all: $(CAS) $(subdirs)

$(BIN): $(SOURCE) $(subdirs)
	java -jar $(XSM_JAR_PATH) $(SOURCE) -library $(XSM_LIB_PATH) -addressmap -optimize off -optimizejump on $(BIN)

$(CAS): $(BIN)
	z88dk-appmake +nec -b $(BIN) --org 0x8437 --mode 1 --audio

$(subdirs):
	$(MAKE) -C $@

clean:
	rm -rf $(CAS) $(BIN) *.wav
	rm -rf font/*.xsm
	rm -rf text/*.xsm

run:
	$(COPY_TO_EMU)
	$(OPEN_EMU)

dump:
	od -tx1 $(BIN)

dis:
	z88dk-dis $(BIN)

