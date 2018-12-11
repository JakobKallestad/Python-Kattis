def union(p, q, uf_id, size):
    idp = find(p, uf_id)
    idq = find(q, uf_id)
    if size[idp] > size[idq]:
        uf_id[idq] = idp
        size[idp] += size[idq]
    else:
        uf_id[idp] = idq
        size[idq] += size[idp]


def find(p, uf_id):
    while p != uf_id[p]:
        uf_id[p] = uf_id[uf_id[p]]
        p = uf_id[p]
    return p


def connected(p, q, uf_id):
    return find(p, uf_id) == find(q, uf_id)


if __name__ == "__main__":
    n_cities = int(input())
    for _ in range(n_cities):
        n_vertexes = int(input())
        n_start_edges = int(input())
        uf_id = [i for i in range(n_vertexes)]
        size = [1 for i in range(n_vertexes)]
        n_groups = n_vertexes

        for _ in range(n_start_edges):
            a, b = map(int, input().split())
            if not connected(a, b, uf_id):
                union(a, b, uf_id, size)
                n_groups -= 1
        print(n_groups-1)

