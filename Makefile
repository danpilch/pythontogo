PYCMD=python3
HTML_PATH=./html
BINARY_NAME=$(BINARY_PATH)/

all: clean build
clean: 
	rm -rf $(HTML_PATH)/*
build: 
	$(PYCMD) templating.py > $(HTML_PATH)/index.html
	ln -sf $(HTML_PATH)/index.html .
