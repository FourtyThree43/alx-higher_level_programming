#!/usr/bin/env bash
fileType=('*.py')

for file in ${fileType}; do
	echo '#!/usr/bin/python3' | cat - "$file" >temp && mv temp "$file"
done
