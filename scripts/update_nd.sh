#!/usr/bin/env bash

REMOTEDIR='\/Volumes\/~cforstal\/www\/cdt-30020-sp17'

cp templates/base_nd.tmpl templates/base.tmpl

for LOCALFILE in $(ls pages/*.yaml)
do
  REMOTEFILE=$(echo $LOCALFILE | sed -e 's/\.yaml/\.html/' -e "s/pages/$REMOTEDIR/")
  echo $LOCALFILE '->' $REMOTEFILE
  scripts/yasb.py $LOCALFILE > $REMOTEFILE
done

cp templates/base_localhost.tmpl templates/base.tmpl

echo "rysnc static files"
rsync -rv --progress static /Volumes/~cforstal/www/cdt-30020-sp17
