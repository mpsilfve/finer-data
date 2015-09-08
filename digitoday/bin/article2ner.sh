#! /bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd)"

recode html |
python2.7 $DIR/get_digitoday_text.py |
sed 's//—/g'
