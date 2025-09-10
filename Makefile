MAKEFLAGS += --silent

run:
	[ -d .venv ] || make venv
	cd src && ./main.py

venv:
	[ -d .venv ] || python3 -m venv .venv
	.venv/bin/pip3 install --upgrade pip
	.venv/bin/pip3 install -r requirements.txt

link:
	ln -sf $(shell realpath bin/run.sh) ~/.local/bin/template
