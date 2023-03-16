# def likes(names):
#     n = len(names)
#     return {
#         0: "no one likes this",
#         1: "{} likes this",
#         2: "{} and {} like this",
#         3: "{}, {} and {} like this",
#         4: "{}, {} and {others} others like this",
#     }[min(4, n)].format(*names[:3], others=n - 2)


def likes(names):
    match names:
        case []:
            return "no one likes this"
        case [a]:
            return f"{a} likes this"
        case [a, b]:
            return f"{a} and {b} like this"
        case [a, b, c]:
            return f"{a}, {b} and {c} like this"
        case [a, b, *rest]:
            return f"{a}, {b} and {len(rest)} others like this"


name_array = ["Kevin"]

print(likes(name_array))

name_array = ["Kevin", "Tim"]

print(likes(name_array))

name_array = ["Kevin", "Tim", "Bryce"]

print(likes(name_array))

name_array = ["Kevin", "Tim", "Bryce", "Paul", "Christine"]

print(likes(name_array))
