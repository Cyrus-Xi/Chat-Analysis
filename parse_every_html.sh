#!/usr/bin/env bash

for f in ./\[multi-way\]/*.html; do
    ./parse_transcript.py "$f"
done
