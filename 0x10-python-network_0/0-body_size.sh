#!/bin/bash
# script that takes in URL, send request to dt URL, displays size response's body
curl -s "$1" | wc -c
