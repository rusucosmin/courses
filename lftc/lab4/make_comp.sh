flex lab4.lx
yacc -d --verbose --debug grammar.y
gcc lex.yy.c y.tab.c -o comp

if [[ $* == *--test* ]];
then
  ./comp too_long.cpp
  echo "verified syntax of too_long.cpp"
  read -p "Press enter to continue..."
  ./comp circle_perim_area.cpp
  echo "verified syntax of circle_perim_area.cpp"
  read -p "Press enter to continue..."
  ./comp cmmdc.cpp
  echo "verified syntax of cmmdc.cpp"
  read -p "Press enter to continue..."
  ./comp main.cpp
  echo "verified syntax of main.cpp"
  read -p "Press enter to continue..."
  ./comp sum.cpp
  echo "verified syntax of sum.cpp"
  read -p "Press enter to continue..."
fi

