import sys
from collections import defaultdict
input = sys.stdin.readline
from queue import PriorityQueue

V, E = map(int, input().split())            # 노드 개수, 에지 개수
start, final = map(int, input().split())    # 출발지, 목적지
myList = [[] for _ in range(V+1)]           # 인접리스트
distance = [sys.maxsize] * (V + 1)          # 초기값 무한대
parents = defaultdict()                     # 경로 추적을 위한 딕셔너리

for c in range(1, V+1):
    if c != start:
        parents[c] = None

for _ in range(E):
    u, v, w = map(int, input().split())     # 가중치가 있는 인접 리스트 저장
    myList[u].append((v,w))


def dijkstra(graph, start):

    visited = [False] * (V + 1)
    q = PriorityQueue()

    q.put((0, start))       # start를 시작점으로 설정
    distance[start] = 0

    while q.qsize() > 0:
        current = q.get()
        c_w = current[0]    # current_weight
        c_v = current[1]    # current_vertex

        if visited[c_v]:
            continue

        visited[c_v] = True
        for next in graph[c_v]: # 인접 노드(next) 탐색
            next_node = next[0]
            next_value = next[1]

            if distance[next_node] > distance[c_v] + next_value:  # 최소 거리로 업데이트
                distance[next_node] = distance[c_v] + next_value
                parents[next_node] = c_v                          # parents에 부모 노드를 삽입
                q.put((distance[next_node], next_node))

    for i in range(1, V + 1):   # 출력
        if visited[i]:
            print("노드", i, ":", distance[i])
        else:
            print("INF")



print("노드1부터 각 노드까지의 거리")
dijkstra(myList, start)

path = []
current = final

# 경로 추적을 위한 코드
while current != start:     # 목적지부터 출발지까지 부모 노드를 찾음
    path.append(current)
    if current in parents:
        current = parents[current]
    else:
        break;
path.append(start)
path.reverse()

print("\n", final, "까지의 경로: ", end="")
print(path)
print(final, "까지의 거리 : ", end="")
print(distance[final])

