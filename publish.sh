#!/bin/bash

MESSAGE="${1:-Update books}"

git add .
git commit -m "$MESSAGE"
git push