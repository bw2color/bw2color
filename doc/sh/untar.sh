dir=./
for x in `ls *.tar`
do
    filename=`basename $x .tar`
    mkdir $filename
    tar -xf $x -C ./$filename
done