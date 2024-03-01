// #include <stdio.h>

// #define _3D 3
// #define _2D 2

// void addV(int x[], int y[], int v[], int size) { // czy *x czy x[] <- to jest to samo
//     int s;
//     for (s = 0; s < size; s++) {
//         v[s] = x[s] + y[s];
//     }
// }


// int main() {
//     int v1_3d[_3D] = {1,2,3};
//     int v2_3d[_3D] = {4,5,6};
//     int v_3d[_3D];

    
//     int v1_2d[_2D] = {1,2};
//     int v2_2d[_2D] = {4,5};
//     int v_2d[_2D];
    
//     int i;
    
//     addV(v1_3d, v2_3d, v_3d, _3D);
    
//     for (i = 0; i<_3D; i++){
//         printf("%d\n", v_3d[i]);
//     }
    
//     printf("=============\n");
    
//     addV(v1_2d, v2_2d, v_2d, _2D);
    
//     for (i = 0; i<_2D; i++){
//         printf("%d\n", v_2d[i]);
//     }
    
//     printf("=============\n");
    
//     addV(v1_3d, v2_2d, v_3d, _3D);
    
//     for (i = 0; i<_3D; i++){
//         printf("%d\n", v_3d[i]);
//     }
    
//     return 0;
// }



// //==========================================
//                // STRUKTURY //
// //==========================================



#include <stdio.h>

struct vector3D {
    int components[3];
    int size;
};

struct vector3D initV3D(struct vector3D v){
    v.size = 3;
    for(int i=0;i<v.size;i++){
        v.components[i]=1;
    }
    return v;
}

struct vector3D addV3D(struct vector3D x,struct vector3D y){
    int s;
    struct vector3D z;
    z.size = x.size;

    for (s = 0; s < z.size; s++){
        z.components[s] = x.components[s] + y.components[s];
    }
    return z;
}

void printV3D(struct vector3D v){ // mozna tez zapisac jako:   struct vector3D printV3D(struct vector3D v){ 
    for(int i=0;i<v.size;i++){
        printf("%d ", v.components[i]);
    }
    printf("\n");
}

int main(){
    struct vector3D v1, v2={{4,5,6},3}, v;
    
    v1.size = 3;
    v1.components[0] = 1;
    v1.components[1] = 2;
    v1.components[2] = 3;
    
    printV3D(v1);
    printV3D(v2);
    
    v = addV3D(v1,v2);
    
    printV3D(v);
    
    return 0;
}
