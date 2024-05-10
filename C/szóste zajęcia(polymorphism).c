// #include <stdio.h>
// #include <stdlib.h>

// int getMaxInt(int * tab, unsigned int size);
// double getMaxDoubles(double * tab, unsigned int size);

// int main(void) {
//     int tabOfInts[] = {3, 2, 1, 5, 6, 4};
//     double tabOfDoubles[] = {3.3, 2.2, 1.1, 5.5, 6.6, 4.4};
    
//     printf("max = %d\n", getMaxInt(tabOfInts, 6));
//     printf("max = %f\n", getMaxDoubles(tabOfDoubles, 6));
    
//     return EXIT_SUCCESS;
// }


// int getMaxInt(int *tab, unsigned int size) {
//     int i;
//     int max = tab[0];
    
//     for(i=0; i<size; i++) {
//         if(tab[i] > max) {
//             max = tab[i];
//         }
//     }
//     return max;
// }

// double getMaxDoubles(double *tab, unsigned int size) {
//     int i;
//     double max = tab[0];
    
//     for(i=0; i<size; i++) {
//         if(tab[i] > max) {
//             max = tab[i];
//         }
//     }
//     return max;
// }




//       V2V2V2V2V2



// #include <stdio.h>
// #include <stdlib.h>

// enum argumentType {INT, DOUBLE};

// void getMax(void * tabPoly, unsigned int size, enum argumentType type);

// int getMaxInt(int * tab, unsigned int size);
// double getMaxDoubles(double * tab, unsigned int size);

// int main(void) {
//     int tabOfInts[] = {3, 2, 1, 5, 6, 4};
//     double tabOfDoubles[] = {3.3, 2.2, 1.1, 5.5, 6.6, 4.4};
    
//     getMax(tabOfInts, 6, INT);
//     getMax(tabOfDoubles, 6, DOUBLE);
    
//     return EXIT_SUCCESS;
// }


// void getMax(void * tabPoly, unsigned int size, enum argumentType type) {
//     int i;
    
//     if(type == INT) {
//         int max;
//         int *tab = (int *)tabPoly;

//         max = tab[0];
//         for(i=0; i<size; i++) {
//             if(tab[i] > max) {
//                 max = tab[i];
//             }
//         }
//     printf("max = %d\n", max);
//     } else if (type == DOUBLE){
//         double max;
//         double *tab = (double *)tabPoly;

//         max = tab[0];
//         for(i=0; i<size; i++) {
//             if(tab[i] > max) {
//                 max = tab[i];
//             }
//         }
//     printf("max = %f\n", max);
//     }
// }



// V3V3V3V33VV3V33VV3V3V3

// #include <stdio.h>
// #include <stdlib.h>

// #define FOO(x) (7*x*x)


// #define maxLoop(_max) \
//     typeof(_max) max; \
//     typeof(_max) *tab = (typeof(_max) *)tabPoly; \
//     max = tab[0]; \
//     for(i=1; i<size; i++) { \
//         if(tab[i] > max) { \
//             max = tab[i]; \
//         } \
//     }


// enum argumentType {INT, DOUBLE};

// union polyType {
//     int i;
//     double d;
// };

// union polyType getMax(void * tabPoly, unsigned int size, enum argumentType type);
// int getMaxInt(int * tab, unsigned int size);
// double getMaxDoubles(double * tab, unsigned int size);



// int main(void) {
//     int tabOfInts[] = {3, 2, 1, 5, 6, 4};
//     double tabOfDoubles[] = {3.3, 2.2, 1.1, 5.5, 6.6, 4.4};
//     union polyType result1, result2;
    
//     printf("%d\n", FOO(5));
    
//     result1 = getMax(tabOfInts, 6, INT);
//     result2 = getMax(tabOfDoubles, 6, DOUBLE);
    
//     printf("Max = %d\n", result1.i);
//     printf("Max = %f\n", result2.d);
  
//     return EXIT_SUCCESS;
// }



// union polyType getMax(void * tabPoly, unsigned int size, enum argumentType type) {
//     int i;
//     union polyType result;
//     int maxI;
//     double maxD;
    
//     if(type == INT) {
//         maxLoop(maxI)
//         result.i = max;
//     } else if (type == DOUBLE) {
//         maxLoop(maxD)
//         result.d = max;
//     }
//     return result;
// }



// NOWE ZADANIE 

// #include <stdio.h>
// #include <stdlib.h>
// #include <string.h>
// #include <ctype.h>


// int findMin(int arr[], int size) {
//     int min = arr[0];
//     for (int i = 1; i < size; i++) {
//         if (arr[i] < min) {
//             min = arr[i];
//         }
//     }
//     return min;
// }


// void printInRange(int arr[], int size, int minIndex, int maxIndex, int includeMin, int includeMax) {
//     if (minIndex < 0 || maxIndex >= size || minIndex > maxIndex) {
//         printf("Niepoprawny zakres.\n");
//         return;
//     }
//     for (int i = minIndex + includeMin; i <= maxIndex - includeMax; i++) {
//         printf("%d ", arr[i]);
//     }
//     printf("\n");
// }

// int dgjdgmain(int argc, char *argv[]) {
//     int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
//     int size = sizeof(arr) / sizeof(arr[0]);

//     if (argc < 2) {
//         printf("Podaj komendę (np. inRange 1 5 T T lub min).\n");
//         return 1;
//     }

//     char *command = argv[1];

//     for (int i = 0; command[i]; i++) {
//         command[i] = tolower(command[i]);
//     }


//     if (strcmp(command, "inrange") == 0 && argc == 6) {
//         int minIndex = atoi(argv[2]);
//         int maxIndex = atoi(argv[3]);
//         char includeMinChar = argv[4][0];
//         char includeMaxChar = argv[5][0];

//         int includeMin = (includeMinChar == 'F' || includeMinChar == 'f') ? 1 : 0;
//         int includeMax = (includeMaxChar == 'F' || includeMaxChar == 'f') ? 1 : 0;

//         printf("Elementy w podanym zakresie: ");
//         printInRange(arr, size, minIndex, maxIndex, includeMin, includeMax);
//     } else if (strcmp(command, "min") == 0 && argc == 2) {
//         printf("Minimalna wartość: %d\n", findMin(arr, size));
//     } else {
//         printf("Niepoprawna komenda lub błędna liczba argumentów.\n");
//         return 1;
//     }

//     return 0;
// }