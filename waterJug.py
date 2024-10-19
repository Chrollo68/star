from collections import deque
def water_jug_fill_any_jug(m, n, d):
    queue = deque()
    queue.append((0, 0, []))
    visited = set()
    visited.add((0,0))
    while queue:

        a, b, path = queue.popleft()
        if a == d or b == d:
            path.append((a, b))
            return path
        possible_states=[(m,b,path +[(m,b)]),
                         (a,n,path +[(a,n)]),
                         (0,b,path +[(0,b)]),
                         (a,0,path +[(a,0)]),
                         (min(a+b,m),b-(min(a+b,m)-a),path+[(min(a+b,m),b-(min(a+b,m)-a))]),
                         (a-(min(a+b,n)-b),min(a+b,n),path+[(a-(min(a+b,n)-b),min(a+b,n))])]
        for state in possible_states:
            state_ab=(state[0],state[1])
            if state_ab not in visited:
                visited.add(state_ab)
                queue.append(state)
    return  None

m=4
n=3
d=2
steps=water_jug_fill_any_jug(m,n,d)
if steps:
    print(f"It is possible to measure exactly {d} liters in one of the jugs Steps:")
    for i,step in enumerate(steps):
        print(f"Step {i+1}: Jug 1={step[0]} liters , Jug 2={step[1]} liters")

else:
    print(f"It is possible to measure exactly {d} liters in one of the jugs Steps:")
