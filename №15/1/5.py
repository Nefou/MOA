mrr = [1,3,4,5,6,7,8]
vaule = int(input(f"Введите число которое хотите удалить из данного массива:\n{mrr} \n"))
end = 0
i = -1
mrr = [num for num in mrr if num != vaule]
print(mrr)
