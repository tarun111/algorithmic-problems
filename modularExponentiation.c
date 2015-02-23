int modexp(int base, int exp, int M)
{
    long long res = 1;
    long long b = base;
    while(exp) {
        if(exp&1) {
            res = (res * b) % M;
        }
        b = (b * b) % M;
        exp >>= 1;
    }
    return (int)res;
}
