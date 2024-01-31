#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
all_arguments="${@}"
doCloud=false
ha_mode={~~ha_mode~~}
# parse arguments
while [[ $# -gt 0 ]]
do
  key="$1"
  case $key in
    --cloud)
      if [ $ha_mode = false ]
      then
        doCloud=true
        csp=$2
        shift
      else
        echo "Cloud launch does not support NVFlare HA mode."
        exit 1
      fi
    ;;
  esac
  shift
done

if [ $doCloud = true ]
then
  case $csp in
    azure)
      $DIR/azure_start.sh ${all_arguments}
      ;;
    aws)
      $DIR/aws_start.sh ${all_arguments}
      ;;
    *)
      echo "Only on-prem or azure or aws is currently supported."
  esac
else
  $DIR/sub_start.sh &
fi
  
