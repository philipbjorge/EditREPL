# Markdown --> Restructured Text (for pypi)
# Using pandoc
pandoc -f markdown -t rst -o README_pypi.rst README.md
echo "Generated rst of readme at README_pypi.rst"

# Literate Documentation Generator
# Using pycco
rm -rf ./docs

echo '"""' > doc.docpy
cat README.md >> doc.docpy
echo '' >> doc.docpy
echo '"""' >> doc.docpy
echo '' >> doc.docpy
echo '' >> doc.docpy
cat editrepl/*.py >> doc.docpy

mv doc.docpy doc.py
pycco doc.py
rm doc.py
