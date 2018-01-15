echo "Copying grammar .txt ..."
cp cminusgrammar.txt grammar.txt
echo "Starting parsing $1"
python gcc.py $1
x=$1
name=${x%.cpp}_pif.txt
input=`cat $name`
python SLRParser.py "$input"
