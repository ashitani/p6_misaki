TARGET= text_data.xsm

all: $(TARGET)

.SUFFIXES: .xsm .txt

.txt.xsm:
	python dump_text_data.py $< > $@

clean:
	rm -rf *.xsm
