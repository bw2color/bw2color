#include <cstdio>
#include <iostream>
using namespace std;

int main()
{
    freopen("rename.sh", "w", stdout);
    for (int i=0; i<115; i++) {
        cout << "cp lab_images_" << i << ".tfrecord "
             << "val_lab_images_" << i << ".tfrecord"
             << endl;
    } 
    return 0; 
} 
