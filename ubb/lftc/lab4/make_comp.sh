flex lab4.lx
yacc -d grammar.y
gcc lex.yy.c y.tab.c -o comp

if [[ $* == *--test* ]];
then
  cat too_long.cpp
  ./comp too_long.cpp
  echo "verified syntax of too_long.cpp"
  read -p "Press enter to continue..."
  cat circle_perim_area.cpp
  ./comp circle_perim_area.cpp
  echo "verified syntax of circle_perim_area.cpp"
  read -p "Press enter to continue..."
  cat cmmdc.cpp
  ./comp cmmdc.cpp
  echo "verified syntax of cmmdc.cpp"
  read -p "Press enter to continue..."
  cat main.cpp
  ./comp main.cpp
  echo "verified syntax of main.cpp"
  read -p "Press enter to continue..."
  cat sum.cpp
  ./comp sum.cpp
  echo "verified syntax of sum.cpp"
  read -p "Press enter to continue..."
  cat syntax_error.cpp
  ./comp syntax_error.cpp
  echo "verified syntax of syntax_error.cpp"
  read -p "Press enter to continue..."

fi

