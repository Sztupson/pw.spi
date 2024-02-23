#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/*int
main ()
{
  srand(time (NULL));
  int v;
  int m[7][7];
  for (int i = 0; i < 7; i++)
	{
	  for (int j = 0; j < 7; j++)
		{
		    v = rand ();
		  if (v % 2 == 0)
			{
			  m[i][j] = 1;
			}
		  else;
		  {
			if (v % 2 != 0)
			  {
				m[i][j] = 0;
			  }
		  }
		}
	}

  for (int i = 0; i < 7; i++)
	{
	  for (int j = 0; j < 7; j++)
		{
		  printf ("%d ", m[i][j]);
		}
	  printf ("\n");
	}
}
*/

//gra w statki

int
main ()
{
  srand (time (NULL));
  int plansza[8][8];
  int statki;
  for (int i = 0; i < 8; i++)
	{
	  for (int j = 0; j < 8; j++)
		{
		  statki = rand ();
		  plansza[i][j] = statki % 2;

		}
	}
  for (int i = 0; i < 8; i++)
	{
	  for (int j = 0; j < 8; j++)
		{
		  printf ("%d ", plansza[i][j]);
		}
	  printf ("\n");
	}
  printf ("Podaj wspolrzedne strzalu (np:1,1): ");
  int strzal[1][1];
  scanf ("%d", strzal);
  if (strzal  plansza == 1)
	{
	  printf ("Trafiles");
	}
  else
	{
	  printf ("Nie trafiles");
	}
}
