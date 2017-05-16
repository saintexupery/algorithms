def chooseCity(n,city):
    min_cost = 0
    locate = city[0][0]

    for i in range(0, n):
        total_cost = 0

        for j in range(0, n):
            if i != j:
                distance = abs(city[i][0] - city[j][0])
                population = city[j][1]

                total_cost += distance * population

        if min_cost > total_cost:
            min_cost = total_cost
            locate = city[i][0]

        elif min_cost == total_cost:
            locate = min(locate[i][0], locate[j][0])

    return locate

#아래 코드는 출력을 위한 테스트 코드입니다.

print(chooseCity(3,[[1,5],[2,2],[3,3]]))
