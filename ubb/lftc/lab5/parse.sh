python gcc.py $1
x=$1
name=${x%.cpp}_pif.txt
input=`cat $name`
python SLRParser.py "$input"
