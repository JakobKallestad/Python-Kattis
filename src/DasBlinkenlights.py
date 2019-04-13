p,q, s = map(int, input().split())
p_set = {p*i for i in range(1, int(s/p)+1)}
q_set = {q*i for i in range(1, int(s/q)+1)}
print("yes" if len(p_set.intersection(q_set)) > 0 else "no")
