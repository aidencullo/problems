# def chooseFleets(wheels):
#     def calculate_fleets(wheel, i):
#         if wheel % 2 != 0:
#             return 0
#         if i == len(num_wheels):
#             return 0
#         if wheel == num_wheels[i]:
#             return 1
#         if wheel < 2:
#             return 0
#         if (wheel, i) not in memo:
#             memo[(wheel, i)] = (calculate_fleets(wheel - num_wheels[i], i) +
#                                 calculate_fleets(wheel, i + 1))
#         return memo[(wheel, i)]

#     memo = {}
#     num_wheels = [2, 4]
#     return [calculate_fleets(wheel, 0) for wheel in wheels]


def chooseFleets(wheels):
    def calculate_fleets(wheel):
        if wheel % 2 != 0:
            return 0
        return (wheel // 4) + 1
        

    memo = {}
    num_wheels = [2, 4]
    return [calculate_fleets(wheel) for wheel in wheels]

