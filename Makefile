all: test

test:
	for f in data/*.in; do \
		echo "- Procesando '$$f'... " ; \
		python ./src/main.py "$$f" "$${f%.in}.out" && echo "Done." || true; \
	done
