// segment tree

const int MAX_N = (int)1e5 + 777;
ll TREE[2 * MAX_N];

void build() 
{ 
  loopR(i,n-1,1,1) TREE[i]=TREE[i<<1] + TREE[i<<1|1]; 
}

void update(ll x,ll p) 
{
	p--;
	p+=n;
	TREE[p]=x;
	for (;p > 0; p >>= 1) TREE[p>>1] = TREE[p] + TREE[p^1];
}

ll query(ll l, ll r)
{
	ll ans=0;
	--l,--r;
	l+=n,r+=n;
	r++;
	while(l < r) 
  {
	    if (l&1) ans+=TREE[l++];
		if (r&1) ans+=TREE[--r];
		l>>=1;
		r>>=1;
	}
	return ans;
}
