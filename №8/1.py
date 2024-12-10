# coding=windows-1251
def calculate_score(word):
    english_scores = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }

    russian_scores = {
        '�': 1, '�': 1, '�': 1, '�': 1, '�': 1, '�': 1, '�': 1, '�': 1, '�': 1,
        '�': 2, '�': 2, '�': 2, '�': 2, '�': 2, '�': 2,
        '�': 3, '�': 3, '�': 3, '�': 3, '�': 3,
        '�': 4, '�': 4,
        '�': 5, '�': 5, '�': 5, '�': 5, '�': 5,
        '�': 8, '�': 8, '�': 8,
        '�': 10, '�': 10, '�': 10
    }

    if all(char in english_scores for char in word.upper()):
        score = sum(english_scores[char] for char in word.upper())
    elif all(char in russian_scores for char in word.upper()):
        score = sum(russian_scores[char] for char in word.upper())
    else:
        return "����� �������� ������������ �������."

    return score

word_input = input("������� �����: ")
score = calculate_score(word_input)

print(f"��������� ����� '{word_input}': {score} �����.")