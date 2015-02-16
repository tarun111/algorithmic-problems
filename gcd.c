#include<stdio.h>
#include<assert.h>

int gcd(int a, int b)
{
    int t;
    while (b) {
        t = b;
        b = a % b;
        a = t;
    }
    return a;
}

int main()
{
    assert(gcd(6,9) == 3);
    assert(gcd(2,1) == 1);
    assert(gcd(3, 7) == 1);
    assert(gcd(7, 21) == 7);
    return 0;
}
