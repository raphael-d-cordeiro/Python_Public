headers = ['CID', 'Name', 'Points.', 'Enrollment.', 'Average.']
compulsory_course = ['CO11', 'CO12', 'CO13']
elective_course = ['CO14']
count = 0
with open('c.txt', 'r') as file_c:
    file_c.seek(0, 0)
    file_string = file_c.read().replace('\n', ' ')
    fields = file_string.split(' ')

with open('cr.txt', 'w') as file_cr:
    for field in headers:
        file_cr.write(f'{field}    ')
    file_cr.write('\n')
    for v in fields:
        if count == 4:
            file_cr.write('\n')
            count = 0
        count += 1
        if v in compulsory_course:
            file_cr.write(f'{v} *    ')
            continue
        elif v in elective_course:
            file_cr.write(f'{v} -    ')
            continue
        elif count == 3:
            file_cr.write(f' ')
            continue
        file_cr.write(f'{v}    ')

