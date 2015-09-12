.PHONY: clean-pyc ext-test test tox-test test-with-mem upload-docs docs audit

all: clean-pyc test

test:
	python tests/runtests.py

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

docs:
	$(MAKE) -C docs html
