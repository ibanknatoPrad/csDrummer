# remove trailing spaces
s/^ \+//g
s/ \+$//g

# replace two or more space with \n
s/ \{2,\}/\n/g

# start table
s/\(Options:\)/\1\n@table @option\n/

# end table
$s/\(.*\)/\1\n\n@end table/

# find options
s/^\(-.*\)/@item \1/

# handle values
s/'\([^']*\)'/@samp{\1}/g

