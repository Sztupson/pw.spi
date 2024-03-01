#include <stdio.h>

#define _3D 3
#define _2D 2

void addV(int x[], int y[], int v[], int size) { // czy *x czy x[] <- to jest to samo
    int s;
    for (s = 0; s < size; s++) {
        v[s] = x[s] + y[s];
    }
}


int main() {
    int v1_3d[_3D] = {1,2,3};
    int v2_3d[_3D] = {4,5,6};
    int v_3d[_3D];

    
    int v1_2d[_2D] = {1,2};
    int v2_2d[_2D] = {4,5};
    int v_2d[_2D];
    
    int i;
    
    addV(v1_3d, v2_3d, v_3d, _3D);
    
    for (i = 0; i<_3D; i++){
        printf("%d\n", v_3d[i]);
    }
    
    printf("=============\n");
    
    addV(v1_2d, v2_2d, v_2d, _2D);
    
    for (i = 0; i<_2D; i++){
        printf("%d\n", v_2d[i]);
    }
    
    printf("=============\n");
    
    addV(v1_3d, v2_2d, v_3d, _3D);
    
    for (i = 0; i<_3D; i++){
        printf("%d\n", v_3d[i]);
    }
    
    return 0;
}