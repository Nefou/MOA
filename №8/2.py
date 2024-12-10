# coding=windows-1251
def pack_backpack(max_weight, items):
    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)

    total_weight = 0
    packed_items = []

    for item, weight in sorted_items:
        if total_weight + weight <= max_weight:
            packed_items.append(item)
            total_weight += weight

    return packed_items

max_weight = int(input("Введите максимальный вес (кг): "))

items = [
    ("палатка", 5),
    ("спальный мешок", 2),
    ("удочка", 1),
    ("термос", 1),
    ("салфетки", 0.1),
    ("жвачка", 0.05)
]

packed_items = pack_backpack(max_weight, items)

print("Вещи, которые помещаются в рюкзак:")
for item in packed_items:
    print(item)
