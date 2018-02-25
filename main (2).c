#include<stdio.h>

int main()
{
  int a,b,c,s=0;// declare integers
  printf("Enter a number for a:\t"); // taking vertical lines
  scanf("%d",&a);
  c = a;
  
  while(a>0) //condition
  {
    b = a%10;
    s = (s*10)+b;
    a = a/10;
  }
  if(s==c) //loop inside loop
  {
    printf("The number  is palindrome");
  }
  else 
  {
    printf("The number is not palindrome");
  }
  return 0; //return value
}