for s in[*open(0)][2::2]:
    a=sorted(map(int,s.split()))
print(a[-(a[0]>=0)])