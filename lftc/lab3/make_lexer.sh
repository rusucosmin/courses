flex lab3.lx
gcc lex.yy.c -o lexer

if [[ $* == *--test* ]];
then
  cat too_long.cpp
  ./lexer too_long.cpp
  echo "verified syntax of too_long.cpp"
  read -p "Press enter to continue..."
  cat syntax_error.cpp
  ./lexer syntax_error.cpp
  echo "verified syntax of syntax_error.cpp"
  read -p "Press enter to continue..."
  cat circle_perim_area.cpp
  ./lexer circle_perim_area.cpp
  echo "verified syntax of circle_perim_area.cpp"
  read -p "Press enter to continue..."
  cat cmmdc.cpp
  ./lexer cmmdc.cpp
  echo "verified syntax of cmmdc.cpp"
  read -p "Press enter to continue..."
  cat main.cpp
  ./lexer main.cpp
  echo "verified syntax of main.cpp"
  read -p "Press enter to continue..."
  cat sum.cpp
  ./lexer sum.cpp
  echo "verified syntax of sum.cpp"
  read -p "Press enter to continue..."
fi

