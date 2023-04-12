find . -name "*.py" ! -name '*main*' -type f -exec sh -c 'cp -v {} tests/' \;

find . -name "*.py" -type f -exec sh -c 'echo -e "#!/usr/bin/python3$(cat {})" > {}' \;

cd tests/

echo ""

for file in *.py; do mv "$file" "${file%.py}.txt"; done

exa -la
