#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Error: Please provide a branch name from which documentation will be built";
  exit 1
fi

BRANCH_NAME=$1

echo "Building documentation from $BRANCH_NAME"
echo "checking out gh-pages"
if ! git checkout gh-pages
then
  echo >&2 "checkout of gh-pages branch failed; please ensure you have local changes committed prior to running this script "
  echo "exiting"
  exit 1
fi

pwd
echo "removing current files"
rm -rf ./*.egg-info
git pull origin gh-pages
rm -r ./*.html ./*.js ./_modules ./_sources ./_static *.inv
touch .nojekyll
git checkout $BRANCH_NAME docs examples Makefile
# need to do this step because the readme will be overwritten
# mv docs/* .
make clean
make jupyter
make html
mv -fv docs/build/html/* ./
rm -r docs notebooks build Makefile source README.* __pycache__/ dist/

echo "--------------------------------------------------------------------"
echo " docs built; please review these changes and then run the following:"
echo "--------------------------------------------------------------------"
echo git add -A
echo git commit -m \"Generated gh-pages for `git log master -1 --pretty=short --abbrev-commit | grep commit`\"
echo git push origin gh-pages
echo git checkout $BRANCH_NAME
