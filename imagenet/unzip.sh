dir=/data/imageNet/train

for x in `ls $dir/*tar`
do
    filename=`basename $x .tar`
    echo $x
    mkdir $dir/$filename
    tar -xvf $x -C $dir/$filename
done