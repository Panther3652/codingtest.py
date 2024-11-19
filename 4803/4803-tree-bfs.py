'''
No. 4083 - 트리 (골드 4)
https://www.acmicpc.net/problem/4803

문제
그래프는 정점과 간선으로 이루어져 있다. 두 정점 사이에 경로가 있다면, 두 정점은 연결되어 있다고 한다. 연결 요소는 모든 정점이 서로 연결되어 있는 정점의 부분집합이다. 그래프는 하나 또는 그 이상의 연결 요소로 이루어져 있다.

트리는 사이클이 없는 연결 요소이다. 트리에는 여러 성질이 있다. 예를 들어, 트리는 정점이 n개, 간선이 n-1개 있다. 또, 임의의 두 정점에 대해서 경로가 유일하다.

그래프가 주어졌을 때, 트리의 개수를 세는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 n ≤ 500과 m ≤ n(n-1)/2을 만족하는 정점의 개수 n과 간선의 개수 m이 주어진다. 다음 m개의 줄에는 간선을 나타내는 두 개의 정수가 주어진다. 같은 간선은 여러 번 주어지지 않는다. 정점은 1번부터 n번까지 번호가 매겨져 있다. 입력의 마지막 줄에는 0이 두 개 주어진다.

출력
입력으로 주어진 그래프에 트리가 없다면 "No trees."를, 한 개라면 "There is one tree."를, T개(T > 1)라면 "A forest of T trees."를 테스트 케이스 번호와 함께 출력한다.
'''

'''
풀이 1. BFS
소요시간: 2036ms
'''

import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

# start 노드부터 시작하여 BFS를 끝까지 돌고 사이클 존재 여부를 리턴하는 함수
def findCycle(start):
    isCycle = False
    q = deque()
    q.append(start)

    while q:
        currentNode = q.popleft()

        '''
        노드를 큐에서 뽑았을 때 visited를 갱신
        이 때, 뽑은 노드의 visited가 이미 1인 경우는 사이클이 존재한다는 것을 의미
        예를 들어 1-2, 2-3, 3-1인 사이클이 있다고 가정하면
        1에서 2와 3을 큐에 넣고 1의 visited는 1이 됨
        그 다음 2를 큐에서 뽑고 visited를 1로 한 다음
        3을 큐에 넣는다 (1에서 넣은 3이 뽑기 전이므로 visited가 0)
        그 다음 1에서 넣은 3을 큐에서 뽑고 visited에 1을 넣음
        이제 큐에는 2에서 넣은 3이 아직 남아있고 이 것을 뽑았을 때
        visited[3]이 이미 1이므로 사이클로 판정
        '''
        if visited[currentNode]:
            isCycle = True
        
        visited[currentNode] = 1

        for adjustNode in graph[currentNode]:
            if visited[adjustNode] == 0:
                q.append(adjustNode)
    
    return isCycle

n, m = map(int, input().split())
case = 1

while n != 0 or m != 0:
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    count = 0

    # 양 방향 매핑
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # visited가 0인 모든 노드를 돌면서
    # 가능한 모든 연결 요소 (연결 그래프)를 순회
    for node in range(1, n + 1):
        if visited[node] == 0:
            if not findCycle(node):
                count += 1

    if count == 0:
        print(f'Case {case}: No trees.')
    elif count == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: A forest of {count} trees.')

    case += 1
    n, m = map(int, input().split())

