#include<stdio.h>
#include<unistd.h>
char player = 'X';
char a[3][3];
int over=0;
int p=0,c=0;
void grid()
{

	printf("_________________________________________________\n");
	printf("|	%c	|	%c	|	%c	|\n",a[0][0],a[0][1],a[0][2]);
	printf("|_______________|_______________|_______________|\n");
	printf("|	%c	|	%c	|	%c	|\n",a[1][0],a[1][1],a[1][2]);
	printf("|_______________|_______________|_______________|\n");
	printf("|	%c	|	%c	|	%c	|\n",a[2][0],a[2][1],a[2][2]);
	printf("-------------------------------------------------\n");
}
int win()
{
	for(int i=0;i<3;i++)
	{
		if(a[i][0]==a[i][1] && a[i][1]==a[i][2] && a[i][0]!=' ')
		{
			return 1;
		}
	}

	for(int j=0;j<3;j++)
	{
		if(a[0][j]==a[1][j] && a[1][j]==a[2][j] && a[0][j]!=' ')
		{
			return 1;
		}
	}
	if(a[0][0]==a[1][1] && a[1][1]==a[2][2] && a[0][0]!=' ')
	{
		return 1;
	}
	if(a[0][2]==a[1][1] && a[1][1]==a[2][0] && a[0][2]!=' ')
	{
		return 1;
	}
	return 0;

}

int draw()
{
	for(int i=0;i<3;i++)
	{
		for(int j=0;j<3;j++)
			{
				if(a[i][j]== ' ')
				{
					return 0;
				}
			}

	}
	return 2;
}

void main()
{
	printf("HELLO PLAYERS!!\nthis game was made by : - DHRUV ROHILLA.\n\n\n");
	sleep(1);
	printf("the game is....tic-tac-toe!!\nthe rules are simple,there are 2 players\n");
		printf("one is 'X' and other is 'O'\n");
		printf("the first player is 'X'\n");
		printf("the player needs to make either the row,column or diagonal same as their symbol.\n");
		printf("the index starts from zero '0',you have to press enter key after entering the first number and then enter\n " );
		printf("the second number.");
		printf("the first one to fill any one of the three mentioned,wins!\n");
		printf("if none of the player's symbol matches,its a draw.\n");
		printf("enjoy!\n\n");
		sleep(3);
	for(int i=0;i<3;i++)
	{
		for(int j=0;j<3;j++)
		{
			a[i][j]=' ';
		}
	}
	while(!over)
	{
		
		grid();

	int row,col;
	printf("%c enter the row and column",player);
	scanf("%d%d",&row,&col);
	if(row<0 || row>=3 || col<0 || col>=3 || a[row][col]!=' ')
	{
		printf("enter valid input(0,1,2) or chose empty space\n");
		continue;
	}
	a[row][col]= player;
	if(win())
	{
		grid();
		printf("player %c won!",player);
		over=1;
	}
	else if(draw())
	{
		grid();
		printf("its a draw!");
		over=2;
	}
	player=(player== 'X')? 'O': 'X';
	}

}

