#!/bin/bash

cd ..
git rm -rf .
git commit -m "removing everything"
git checkout master -- doc/s_build/html/
git add doc/s_build/html/*
git mv doc/s_build/html/* .

# create nojekyll

touch .nojekyll
git add .nojekyll
# finally commit

git commit -m "deploying"

