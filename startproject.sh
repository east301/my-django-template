#!/bin/sh

#
function run() {
    echo "$(tput bold)[RUN] $@ $(tput sgr0)"
    eval "$@"
}

# checks command line arguments
if [ $# -ne 1 ]; then
    echo "Usage: $0 [project-name]" 1>&2
    exit 1
fi

# creates a django project
MY_DIR=$(cd $(dirname $0); pwd)
PROJ_NAME=$1
PROJ_DIR=$(pwd)/$PROJ_NAME

run django-admin.py startproject $PROJ_NAME --template=$MY_DIR -e html,json,sh

# remove unnecessary files
run cd $PROJ_DIR

[ -f README.md ] && rm README.md
[ -f startproject.sh ] && rm startproject.sh

# fix git-related stuffs
run cd $PROJ_DIR

[ -d .git ] && run rm -rf .git
[ -f src/.gitignore ] && run sed -i -e s/project_name/$PROJ_NAME/ src/.gitignore

# fix permission of files
run cd $PROJ_DIR

[ -f src/manage.py ] && run chmod +x src/manage.py
[ -f src/scripts/deploy.sh ] && run chmod +x src/scripts/deploy.sh
