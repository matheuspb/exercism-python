#!/bin/sh

set -e
for test in ./*/*test.py; do
	python $test;
done;
