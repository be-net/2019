CHAPS_TMP=$(wildcard chap-*.jinja)
CHAPS_CMP=$(patsubst chap-%.jinja, chap-%, $(CHAPS_TMP))

.PHONY: all clean abs

all: program.pdf prog.md boa.pdf

prog.tex: render_jinja.py prog.tex.jinja prog.yaml abs/*.yaml
	rm -f prog.tex
	python render_jinja.py prog.yaml prog.tex.jinja > prog.tex

$(CHAPS_CMP): render_jinja.py prog.yaml $(CHAPS_TMP) abs/*.yaml
	python render_jinja.py prog.yaml $@.jinja > $@

program.pdf: prog.tex program.tex $(CHAPS_CMP)
	latexmk -lualatex program.tex

boa.pdf: prog.tex $(CHAPS_CMP)
	latexmk -lualatex boa.tex


prog.md: render_jinja.py prog.yaml prog.md.jinja
	rm -f prog.md
	python render_jinja.py prog.yaml prog.md.jinja > prog.md
	cp -f prog.md ../content/page/prog.md

prog.html: render_jinja.py prog.html.jinja prog.yaml abs
	rm -f prog.html
	python render_jinja.py prog.html.jinja > prog.html

clean:
	latexmk -C
