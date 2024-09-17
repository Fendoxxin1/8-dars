# lst = ["olma", "anor", "gilos", True, 12, 10, "olma", "gilos", 1]
lst = ["olma", "anor", "gilos", True, 12, 10, "banan",9]
set1 = set(lst)

if len(set1) == len(lst):
    print("Dublikatlar yo'q")
else:
    print("Dublikatlar bor")