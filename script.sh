#!/usr/bin/env bash

for file in *.js; do
	echo '#!/usr/bin/node' | cat - "$file" >temp && mv temp "$file"
done
