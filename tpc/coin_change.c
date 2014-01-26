#include<stdio.h>
int den[]={1,2,5,10,20,50,100,500,1000};

int calc(int x, int pos)
{
	int i, ans = 0;
	ans = x/2 + 1;
	for(i=2;i<9;i++)
	{
		if(i>pos)break;
		if(x>=den[i])
		{
			ans += calc(x-den[i], i);
		}
		else
			break;
	}
	return ans;
}

int main()
{
	int a;
	while(1)
	{
		printf("Enter a number: ");
		scanf("%d", &a);
		printf("%d\n", calc(a, 9));
	}
}
