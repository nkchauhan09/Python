#include<stdio.h>
int main()
{
	int n;
	int A[n];
	printf("Enter number of elements to be entered : ");
	scanf("%d", &n);
	printf("Enter elements one by one : ");
	for(int i = 1; i <= n; i++)
	{
		scanf("%d" &A[i]);
	}
	for(int i = 1; i <= n; i++)
    {		
		printf("%d", A[i])
	}
}