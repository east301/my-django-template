#!/bin/sh

# ==================================================
# useful functions and variables
# ==================================================

function usage_exit() {
    echo "Usage: $0 [-d]" 1>&2
    exit 1
}

function run() {
    echo "$(tput bold)[RUN] $@ $(tput sgr0)"
    eval "$@"
}

BASE_DIR=$(cd $(dirname $0); cd ..; pwd)
MODE="production"

while getopts d OPT; do
    case $OPT in
        d) MODE="development" ;;
        *) usage_exit ;;
    esac
done


# ==================================================
# creates virtualenv and installs dependencies
# ==================================================

run cd $BASE_DIR

[ ! -d venv ] && run virtualenv venv
run source venv/bin/activate
run pip install -r requirements.txt


# ==================================================
# creates local_settings.py
# ==================================================

run cd $BASE_DIR/{{ project_name }}

if [ ! -f settings_local.py ]; then
    if [ $MODE == "development" ]; then
        run ln -s settings_development.py settings_local.py
    else
        run ln -s settings_production.py settings_local.py
    fi
fi


# ==================================================
# runs bower
# ==================================================

run cd $BASE_DIR

run bower install


# ==================================================
# runs manage.py
# ==================================================

run cd $BASE_DIR

if [ $MODE == "development" ]; then
    python manage.py syncdb
else
    run python manage.py syncdb --noinput
    run python manage.py collectstatic --noinput
fi
