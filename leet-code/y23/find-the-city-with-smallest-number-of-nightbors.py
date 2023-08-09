def find(n, edges, distanceThreshold):
    def warshall(_n, _edges, _distance):
        dist = [[(_distance + 1)] * _n for _ in range(_n)]
        for i in range(_n):
            dist[i][i] = 0
        for u, v, w in _edges:
            dist[u][v] = w
            dist[v][u] = w
        for k in range(_n):
            for i in range(_n):
                for j in range(_n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        return dist

    result = -1
    min_cities_cnt = n
    d = warshall(n, edges, distanceThreshold)
    for i in range(n):
        cities_cnt = sum(d[i][j] <= distanceThreshold for j in range(n))
        if cities_cnt <= min_cities_cnt:
            result = i
            min_cities_cnt = cities_cnt
    return result


assert find(4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4) == 3
assert find(5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2) == 0
