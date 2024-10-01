default: keyboard-stickers.pdf

keyboard-stickers.svg: gen-sheet.py
	python $^ $@

keyboard-stickers.pdf: keyboard-stickers.svg
	magick $^ -resize 2480x3507 -units PixelsPerInch -density 300x300 $@

.PHONY: clean
clean:
	rm -f keyboard-stickers.svg keyboard-stickers.pdf 
