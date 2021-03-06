'''
1보다 큰 N개의 도시 중 한 곳에 공항을 지을 예정입니다.
사람들의 편의를 위해 공항으로부터 각 사람들까지의 도시간 이동 거리가 최소가 되는 도시에 짓기로 하였습니다.
편의상 도시는 일직선상에 놓여있다고 가정하며 좌표의 범위는 음수가 포함됩니다.
또한 좌표는 정렬되어 있지 않습니다.
직선상의 위치와 그 도시에 사는 사람들의 수가 주어질 때,
공항을 지을 도시의 위치를 반환해주는 함수 chooseCity 함수를 완성하세요.
거리가 같은 도시가 2개 이상일 경우 위치가 더 작은 쪽의 도시를 선택하면 됩니다.
예를 들어 다음과 같은 정보의 도시가 있다고 가정해 봅시다.

[[1,5],[2,2],[3,3]]
이 살 경우, 각각의 도시에 공항을 지었을 때의 사람들의 이동 거리는 8, 8, 12 이므로 1번 또는 2번에 지을 수 있지만,
1의 위치가 더 작으므로 1을 반환해주면 됩니다.
'''

from operator import itemgetter

def chooseCity(n,city):
    city = sorted(city, key=lambda x: x[0])

    min_cost = 0
    locate = city[0][0]

    population_left = 0
    population_right = 0

    for i in range(0, n):
        population_right += city[i][1]
        min_cost += abs(city[0][0] - city[i][0]) * city[i][1]

    population_right -= city[0][1]
    total_cost = min_cost
    for i in range(1, n):
        population_left += city[i-1][1]
        total_cost = total_cost + population_left - population_right
        population_right -= city[i][1]

        if min_cost > total_cost:
            min_cost = total_cost
            locate = city[i][0]

    return locate

    # for i in range(0, n):
    #     total_cost = 0
    #
    #     for j in range(0, n):
    #         if i != j:
    #             distance = abs(city[i][0] - city[j][0])
    #             population = city[j][1]
    #
    #             total_cost += distance * population
    #
    #     if min_cost > total_cost:
    #         min_cost = total_cost
    #         locate = city[i][0]
    #
    #     elif min_cost == total_cost:
    #         locate = min(locate[i][0], locate[j][0])

    # return locate

#아래 코드는 출력을 위한 테스트 코드입니다.

print(chooseCity(3,[[1,5],[2,2],[3,3]]))
print(chooseCity(3,[[0,1000],[1,1],[10000000,1]]))
