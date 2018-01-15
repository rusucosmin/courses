for file in `ls test`; do
  echo $file
  filename="${file%.*}"
  ./comp "./test/${file}"
  cp out.asm "test/${filename}.asm"
done
