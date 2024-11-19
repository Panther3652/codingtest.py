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
풀이 2. DFS
소요시간: 188ms
'''

import sys
input = sys.stdin.readline

# start 노드부터 시작하여 DFS를 끝까지 돌고 사이클 존재 여부를 리턴하는 함수
def findCycle(start):
    for adjustNode in graph[start]:
        # 인접 노드가 자신의 부모 노드인 경우 패스
        if parent[start] == adjustNode:
            continue

        # 인접 노드가 부모 노드가 아닌데 방문 이력이 있다는 것은 곧 사이클을 의미
        if visited[adjustNode]:
            return True
        
        parent[adjustNode] = start
        visited[adjustNode] = 1

        '''
        인접 노드를 루트 노드로 하는 서브 트리에
        사이클이 존재하면 곧 전체 트리에 사이클이 존재하는 것과 같음
        '''

        if findCycle(adjustNode):
            return True
        
    return False

n, m = map(int, input().split())
case = 1

while n != 0 or m != 0:
    graph = [[] for _ in range(n + 1)]
    parent = [-1] * (n + 1)
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
            parent[node] = node
            visited[node] = 1
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