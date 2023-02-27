with open('./input', 'r', encoding='utf-8') as input_data:
    data = input_data.read().splitlines()
    N = len(data[0])
    gamma = 0
    eps = 0
    for n in range(N):
        count1 = sum(1 for r in data if r[n] == '0')
        count2 = len(data) - count1
        gamma *= 2
        eps *= 2
        if count1 < count2:
            gamma += 1
        else:
            eps += 1
    print(gamma * eps)
