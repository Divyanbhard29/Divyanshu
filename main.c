#include<stdio.h>

void checkprimenumber();

int main()
{
  checkprimenumber();
  return 0;
}
void checkprimenumber()
{
  int i,n,flag;
  printf("Enter a value of n");
  scanf("%d",&n);
  
  for(i=2;i<=n/2;++i)
  {
    if(n%i == 0)
    {
      flag = 1;
    }
  }
  if(flag == 1)
  {
    printf("Number is not prime number");
  }
  else
  {
    printf("Number is prime number");
  }
}