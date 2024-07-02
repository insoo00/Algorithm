import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
distance = [int(1e9)] * (N + 1)
for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))
start, end = map(int, input().split())


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start)) # (우선순위=비용, 값=엣지 번호)
    distance[start] = 0
    while heap:
        curCost, curEdge = heapq.heappop(heap)
        if distance[curEdge] < curCost:
            if curEdge == end:
                break
            else:
                continue
        for i in graph[curEdge]:
            cost = curCost + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))

dijkstra(start)
print(distance[end])