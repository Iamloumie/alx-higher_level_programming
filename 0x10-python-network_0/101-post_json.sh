#!/bin/bash
# Script that sends a JSON POST request to a URL passed as the first argument and displays the response's body
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
