import random
def miller(n):
	s=0
	#a,y,d,x
	if(n==2):
		return 1
	if(n%2==0):
		return 0
	x=n-1
	while(x%2==0):
		s = s + 1
		x = x/2
	d=x
	#a=rand()%(n-1)
	if(n<4):
            a = 2
        else:
        	a = random.randint(2, n-2)
	if(a<2):
		a=2
	y=pow(a,d,n)
	if(y!=1 and y!=n-1):
		r=1
		while(r<s and y!=n-1):
			y=pow(y,2,n)
			if(y==1):
				return 0
			r = r + 1
		if(y!=n-1):
			return 0
	return 1

def gcd(x, y):
	if(y==0):
		return x
	return gcd(y,x%y)

def rho(n):
	#divisor,c,x,xx,temp
        print "rho calculation for %", n
	if(n%2==0):
		return 2
	x=2
	c=1
	divisor=1
	xx=x
	counter = 0
	while(divisor==1):
		x=(pow(x,2,n)+c)%n;
		xx=(pow(xx,2,n)+c)%n;
		xx=(pow(xx,2,n)+c)%n;
		temp=x-xx;
		if(temp<0):
			temp = -temp
		if(temp==0):
			c = c + 1
		else:
                    divisor=gcd(temp,n)
                    counter = counter + 1
                    if(counter%10000==0):
                        print "checked  nums", counter
	return divisor


def factor(n):
	i=1
	if(n==1):
		return
	f=0
	while(i<10):
		f=miller(n)
		print "is prime ", f, n
		if(f==0):
			break
		i = i + 1
	
	if(f==1):
		#already prime
                print "prime: ", n
                if(n in map):
                    map[n] = map[n] + 1
                else:
        		map[n] = 1
		return
	
	fact2=rho(n)
	factor(fact2)
	factor(n/fact2)

#int main()
#{
#	int t,i,j;
#	long long inp,temp;
#	long double ldtemp,ans;
#	scanf("%d",&t);
#	while(t--)
#	{
#		scanf("%lld",&inp);
#		top=-1;
#		factor(inp);
#		ans=1;
#		for(i=0;i<=top;i++)
#		{
#			ldtemp=1;
#			for(j=0;j<=freq[i];j++)
#			{
#				ldtemp*=storeprimes[i];
#			}
#			ldtemp--;
#			ldtemp/=(storeprimes[i]-1);
#			ans*=ldtemp;
#		}
#		ans-=inp;
#		printf("%.0llf\n",ans);
#	}
#	return 0;
#}
map = {}
#factor(2639085015233392202740949386309743259521517793886143240989)
factor(833211727961546299775962002589)
print map
