all: test

test:
	for f in data/*.in; do \
		echo -n "- Processing '$$f'..." ; \
		python ./main.py "$$f" "$${f%.in}.out" && echo " Done."; \
	done
