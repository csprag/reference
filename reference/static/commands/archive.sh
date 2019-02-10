#!/bin/bash
for file in `find basics scripting tools -type f | sort | awk 'NR % 2 == 0'`; do
  echo "Clearing" $file
  COMMAND=$(basename $file | sed 's/\.[^.]*$//')
  TEMPLATE=$(cat template.md)
  echo "${TEMPLATE/COMMAND/$COMMAND}" > $file
done
