import prettytable

table = prettytable.PrettyTable([" ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"])

base_number = 32
line_size = 16
for i in range(2, 8):
    line = [chr(j) for j in range(base_number, base_number + line_size)]
    line.insert(0, hex(i).split("x")[1].upper())
    table.add_row(line)
    base_number += line_size

base_number = 128 + 2 * 16
for i in range(10, 16):
    line = [chr(j) for j in range(base_number, base_number + line_size)]
    line.insert(0, hex(i).split("x")[1].upper())
    table.add_row(line)
    base_number += line_size

print(table)
