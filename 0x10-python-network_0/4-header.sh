#!/bin/bash
# Script takes in URL, send GET request, and displays response's body
curl -sH "X-School-User-Id: 98" "$1"
