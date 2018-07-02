f=`find . -type f`
d=`find . -type d`

for x in $f; do
  for y in $d; do
    if [ $x = $y ]; then
      echo $x;
      echo $y;
      echo "OK"
    fi
  done
done

