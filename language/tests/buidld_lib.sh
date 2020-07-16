#!/bin/bash

gcc -shared -fPIC -o libtest.so -std=c99 test.c
