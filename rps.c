#include<stdio.h>
#include<unistd.h>
#include <stdlib.h>
#include <time.h>

void main()
{
	int round,c=0,k=0;
	char input[20];
	printf("Welcome player!\nThis game was made by Dhruv Rohilla.\n\n\n");
	sleep(1);
	printf("\nRules:-\n");
	sleep(1);
	printf("This is the basic game of rock,paper and scissors\nfirst you choose how many rounds you want to play\nthen choose from rock(r),paper(p),scissors(s)\nyou will be playing against the computer\nfor each time you win,you will earn a point\nfor each time you loose,the pc gets a point\nthe one with most points wins!!\nNOTE:Entering wronf input during game will reduce your score!\n\n");
	sleep(3);
	printf("READY?\n");
	sleep(1);
	printf("GET SET...\n");
	sleep(1);
	printf("GO!!!\n\n");
	sleep(1);
	printf("How many rounds you want to play? : ");
	scanf("%d",&round);
    while(round!=0)
    {
        printf("invalid input!\n");
        printf("How many rounds you want to play? : ");
        scanf("%d",&round);
    }


	
	
	for(int i=0;i<round;i++)
	{
		printf("choose from rock(r),paper(p)or scissors(s) : ");
		scanf("%s",&input[i]);
		srand(time(NULL));

   
    char options[] = {'r', 'p', 's'};

    
    int length = sizeof(options) / sizeof(options[0]);

    int randomIndex = rand() % length;

    char randomLetter = options[randomIndex];

    printf("computer's response : %c\n",randomLetter);

    if(input[i]==randomLetter)
    {
    	printf("Draw!\nyour ponits:%d\ncomputer's points:%d\n",c,k);
    }
    else if(input[i]== 'r' && randomLetter=='s')
    {
    	printf("you won!\n");
    	c++;
    	printf("your ponits:%d\ncomputer's points:%d\n",c,k);
    }
    else if(input[i]== 'r' && randomLetter=='p')
    {
    	printf("you lost!\n");
    	k++;
    	printf("your ponits:%d\ncomputer's points:%d\n",c,k);
    }
    else if(input[i]== 'p' && randomLetter=='r')
    {
    	printf("you won!\n");
    	c++;
    	printf("your ponits:%d\ncomputer's points:%d\n",c,k);
    }
    else if(input[i]== 'p' && randomLetter=='s')
	 {
    	printf("you lost!\n");
    	k++;
    	printf("your ponits:%d\ncomputer's points:%d\n",c,k);
    }
    else if(input[i]== 's' && randomLetter=='r')
	 {
    	printf("you lost!\n");
    	k++;
    	printf("your ponits:%d\ncomputer's points:%d\n",c,k);
    }
    else if(input[i]== 's' && randomLetter=='p')
    {
    	printf("you won!\n");
    	c++;
    	printf("your ponits:%d\ncomputer's points:%d\n",c,k);
    }
    else
    {
    	printf("wrong input!!\n");

    	c--;
		printf("your ponits:%d\ncomputer's points:%d\n",c,k);

	}
    }
    sleep(1);
    printf("FINAL SCORES:-\nyours : %d\ncomputer : %d\n\n",c,k);
    sleep(1);
    if(c>k)
    {
    	printf("YOU WON!!!");
    }
    else if(c==k)
    {
    	printf("DRAW!!!");
    }
    else
    {
    	printf("YOU LOST! BETTER LUCK NEXT TIME :)");
    }


}