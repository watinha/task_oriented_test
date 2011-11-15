#! /usr/bin/make

PYTHON=/usr/bin/python
RM=/bin/rm

tests-unit:
	@$(PYTHON) bin/run_unit_tests.py

help:
	@echo "\n"
	@echo "****************************************************"
	@echo "***** \033[1;34mUnit tests for Accessibility test help\033[0;0m *****"
	@echo "****************************************************"
	@echo "    \033[32mtests-unit:\033[0m   unit test the python written action classes"
	@echo "\n"

.PHONY: tests-unit
