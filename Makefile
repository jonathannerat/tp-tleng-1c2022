all: test

test:
	for f in data/*.in; do \
		python ./main.py "$$f" "$${f%.in}.out" ; \
	done
