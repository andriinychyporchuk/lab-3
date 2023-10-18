field = [
    ['.'] * 12,
    ['.', 'X', '.', 'X', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', 'X', '.', 'X', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
]

def display_field(field):
    for row in field:
        print(' '.join(row))

display_field(field)

while True:
    try:
        user_input = input("Вертикальне переміщення (R - скинути, q - вихід): ")
        if user_input.lower() == 'q':
            break
        elif user_input.upper() == 'R':
            field = [
                ['.'] * 12,
                ['.', 'X', '.', 'X', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', 'X', '.', 'X', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
            ]
            display_field(field)
        else:
            vertical_shift = int(user_input)
            horizontal_shift = int(input("Горизонтальне переміщення (R - скинути, q - вихід): "))

            for _ in range(abs(vertical_shift)):
                if vertical_shift > 0:
                    field.pop(0)
                    field.append(['.'] * 12)
                elif vertical_shift < 0:
                    field.pop()
                    field.insert(0, ['.'] * 12)

            for _ in range(abs(horizontal_shift)):
                if horizontal_shift > 0:
                    for row in field:
                        row.insert(0, '.')
                        row.pop()
                elif horizontal_shift < 0:
                    for row in field:
                        row.append('.')
                        row.pop(0)

            display_field(field)

    except ValueError:
        print("Невідома команда.")