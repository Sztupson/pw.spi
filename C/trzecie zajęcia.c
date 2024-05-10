// #include <stdio.h>
// #include <stdlib.h>
// #include <time.h>
// #include <stdbool.h>
// #include <string.h>

// #define TAB_SIZE 10
// #define MENU_SIZE 2


// enum optionCode {UNDEFINED, SET_SELECTED, SET_FREE, RESET, PRINT_STAT, QUIT};


// struct skladowe {
//   int x;
//   int y;
// };

// struct option {
//   enum optionCode code;
//   char letter[2];
//   char text[32];
// };

// struct option options[] = {
//   {PRINT_ALL, "a", "Wypisz wszystkie\n"},
//   {SET_SELECTED, "s", "Ustaw wybrany\n"}
// };

// void wypisz(struct skladowe s){
//   printf("%d %d\n", s.x, s.y);
// }



// void init(struct skladowe tab[], int index){
//   tab[index].x = 0;
//   tab[index].y = 0;
// }

// enum optionCode menu() {
//   char buffer[32];
//   int i;
//   for(i=0;i<MENU_SIZE;i++){
//     printf("[%s] %s\n", options[i].letter, options[i].text);
// }
//   /*
//   printf("[a] Wypisz wszystkie\n");
//   printf("[s] Ustaw wybrany\n");
//   printf("[f] Ustaw pierwszy wolny\n");
//   printf("[r] Resetuj wybrany\n");
//   printf("[c] Statystyka\n");
//   printf("[q] Wyjście\n");
//   */

//   printf("Podaj opcję: ");

//   //scanf("%s", buffer);
//   fgets(buffer, 4, stdin);
//   buffer[strlen(buffer)-1] = '\0';

//   printf("Dokonany wybór: %s\n", buffer);
//   /*
//   if (strcmp(buffer, "a") == 0) {
//   return PRINT_ALL;
//   } else if (strcmp(buffer,"s") == 0) {
//   return SET_SELECTED;
//   } else if (strcmp(buffer, "f") == 0) {
//   return SET_FREE;
//   } else if (strcmp(buffer, "r") == 0) {
//   return RESET;
//   } else if (strcmp(buffer, "c") == 0) {
//   return PRINT_STAT;
//   } else if (strcmp(buffer, "q") == 0) {
//   return QUIT;
//   }
//   */

//   for (i=0; i<MENU_SIZE; i++)
//     if (strcmp(buffer, options[i].letter) == 0) {
//       return options[i].code;
//     }


//   return UNDEFINED;
// }

// void executeAction(enum optionCode choice){
// }




// int main() {
//   srand(time(NULL));

//   struct skladowe tab[10];
//   int i;
//   enum optionCode choice = PRINT_ALL
//   if (wybor == "a"){
//     for(i = 0; i<TAB_SIZE; i++){
//       init(tab, i);
//       wypisz(tab[i]);
//     }
//   } else if (wybor == "s"){
//       printf("Wybierz indeks tablicy, ktory chcesz zmienic: \n");
//       scanf("%d", index);
//       printf("Wybierz liczbe pierwsza ktora ma byc pod wybranym indeksem: \n");
//       scanf("%d", liczba1);
//       tab[index].x = liczba1;
//       printf("Wybierz liczbe druga ktora ma byc pod wybranym indeksem: \n");
//       scanf("%d", liczba2);
//       tab[index].y = liczba2;
//   }



//   while(choice != QUIT){
//     choice = menu();
//     executeAction(choice)
//   }


//   return 0;
// }
