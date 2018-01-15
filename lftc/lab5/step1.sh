echo "Copying grammar .txt ..."
cp simple_grammar.txt grammar.txt
echo "Starting parsing $1"
python SLRParser.py "$1"
