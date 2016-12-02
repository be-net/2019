
#!/usr/bin/env bash

class=$1

OLD_IFS=$IFS
IFS=$'\n'

for line in `cat $class`;
do
  regname=`echo $line | cut -d$'\t' -f 1`
  regsurn=`echo $line | cut -d$'\t' -f 2`
  regmail=`echo $line | cut -d$'\t' -f 3`
  regaffs=`echo $line | cut -d$'\t' -f 4`
  regwebp=`echo $line | cut -d$'\t' -f 5`
  echo "-"
  echo "  name: ${regname} ${regsurn}"
  echo "  email: ${regmail}"
  echo "  affiliation:"
  for af in `echo ${regaffs} | sed "s/,/\n/g"`;
  do
    echo "    - ${af}"
  done
  # add the user
done

IFS=$OLD_IFS
