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

max_weight = int(input("������� ������������ ��� (��): "))

items = [
    ("�������", 5),
    ("�������� �����", 2),
    ("������", 1),
    ("������", 1),
    ("��������", 0.1),
    ("������", 0.05)
]

packed_items = pack_backpack(max_weight, items)

print("����, ������� ���������� � ������:")
for item in packed_items:
    print(item)
