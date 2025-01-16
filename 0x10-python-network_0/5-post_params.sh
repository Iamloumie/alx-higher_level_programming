#!/bin/bash
# Script takes in URL, send POST request, displays body's response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
