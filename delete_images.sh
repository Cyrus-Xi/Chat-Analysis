#!/usr/bin/env bash

# Delete all non-html files one level down.
find . -depth 2 -type f -not -name '*.html' -delete
