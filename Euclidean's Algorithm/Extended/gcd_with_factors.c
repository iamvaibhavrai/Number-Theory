#include <stdio.h>
#include <conio.h>

int findGcdAndFactors(int a,int b,int *x,int *y){
  if (a == 0) {
    *x = 0;
    *y = 1;
    return b;
  }
  int x1,y1;
  int gcd = findGcdAndFactors(b%a,b,&x1,&y1);
  *x = y1 - (b/a) * x1;
  *y = x1;
  return gcd;
}

int main() {
  int x,y,a,b,gcd;
  printf("Enter numbers\n");
  scanf("%d%d",&a,&b);
  if(a > b) {
    gcd = findGcdAndFactors(a,b,&x,&y);
  } else {
    gcd = findGcdAndFactors(b,a,&y,&x);
  }
  printf("%d\n%d\n%d",gcd,x,y);
  return 0;
}
