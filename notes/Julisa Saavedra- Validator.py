import csv


def validate(num: str):
    if len(num) == 16:
        list_form = list(num)
        last_num = list_form.pop(15)
        reverse_form = reverse(list_form)

        for index in range(len(reverse_form)):
            reverse_form[index] = int(reverse_form[index])

            if index % 2 == 0:
                reverse_form[index] *= 2

            if reverse_form[index] >= 9:
                reverse_form[index] -= 9

        total = sum(reverse_form) % 10

        if total == int(last_num):
            return True

        else:
            return False


def reverse(num: list):
    return num[::-1]


with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")
        for row in reader:
            old_number = row[0]
            if validate(old_number):
                writer.writerow(row)
        print("OK")
