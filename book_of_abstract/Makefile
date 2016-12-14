CHAPS_TMP=$(wildcard chap-*.jinja)
CHAPS_CMP=$(patsubst chap-%.jinja, chap-%, $(CHAPS_TMP))
POSTDEST=../content

ALLABS=$(wildcard abs/*.yaml)
NOABS=abs/affs.yaml abs/registr.yaml
ABS=$(filter-out $(NOABS),$(ALLABS))
WEBABS=$(patsubst %.yaml,$(POSTDEST)/%.md,$(ABS))

PROG=$(POSTDEST)/page/prog.md

.PHONY: all clean abs

all: program.pdf $(PROG) boa.pdf $(WEBABS)

prog.tex: render_jinja.py prog.tex.jinja prog.yaml abs/*.yaml
	rm -f prog.tex
	python render_jinja.py prog.yaml prog.tex.jinja > prog.tex

$(CHAPS_CMP): render_jinja.py prog.yaml $(CHAPS_TMP) abs/*.yaml
	python render_jinja.py prog.yaml $@.jinja > $@

program.pdf: prog.tex program.tex $(CHAPS_CMP)
	latexmk -lualatex program.tex

boa.pdf: prog.tex $(CHAPS_CMP) boa.tex
	latexmk -lualatex boa.tex
	mkdir -p ../static/files
	cp boa.pdf ../static/files/boa-benet-2016.pdf


# abs/registr.yaml: abs/registr.sh abs/registr.txt
# 	bash abs/registr.sh abs/registr.txt > abs/registr.yaml


$(PROG): render_jinja.py prog.yaml prog.md.jinja
	python render_jinja.py prog.yaml prog.md.jinja > $@

prog.html: render_jinja.py prog.html.jinja prog.yaml abs
	rm -f prog.html
	python render_jinja.py prog.html.jinja > prog.html

clean:
	latexmk -C
	rm -r $(POSTDEST)/abs
	rm -r $(PROG)

$(POSTDEST)/abs/%.md: abs/%.yaml render_jinja.py post.md.jinja
	mkdir -p $(POSTDEST)/abs
	python render_jinja.py $< post.md.jinja > $@
