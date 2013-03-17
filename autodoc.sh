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
