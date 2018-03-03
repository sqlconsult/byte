#!/bin/sh
MYVAR=sometext
echo "double quotes gives you $MYVAR"
echo 'single quotes gives you $MYVAR'
#will give this:
#
#double quotes gives you sometext
#single quotes gives you $MYVAR
