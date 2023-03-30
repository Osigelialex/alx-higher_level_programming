#!/bin/bash
# displays size of the body of a response
echo curl --silent $1 | wc -c
