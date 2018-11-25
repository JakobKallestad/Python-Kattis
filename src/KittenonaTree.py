

def bfs(adj, placement):
    while placement != -1:
        print(placement, end=' ')
        placement = adj[placement]




if __name__ == "__main__":
    kitten = int(input())
    adj = [-1 for _ in range(101)]
    #print(adj)
    while True:
        line_list = list(map(int, input().split()))
        if line_list[0] == -1:
            break
        src = line_list[0]
        for i in range(1, len(line_list)):
            adj[line_list[i]] = src

    #print(adj)
    bfs(adj, kitten)

