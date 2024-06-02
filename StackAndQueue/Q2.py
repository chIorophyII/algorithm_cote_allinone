def whenWillBeWarm(temperature):
    restDay = [0] * len(temperature)
    stack = []

    for t in range(len(temperature)):
        while stack and temperature[t] > stack[-1][0]:
                restDay[stack[-1][1]] = (t - stack[-1][1])
                stack.pop()
        stack.append([temperature[t], t])

    return restDay


def dailyTemperatures(temperatures):
    ans = [0] * len(temperatures)
    stack = []
    for cur_day, cur_temp in enumerate(temperatures):
        while stack and stack[-1][1] < cur_temp:
            prev_day, _ = stack.pop()
            ans[prev_day] = cur_day - prev_day
        stack.append((cur_day, cur_temp))
    return ans


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(whenWillBeWarm([73, 74, 75, 71, 69, 72, 76, 73]))
