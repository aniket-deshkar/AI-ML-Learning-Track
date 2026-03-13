def csv_parser(filename):
    students_data = []
    try:
        with open(filename, 'r') as file:
            csv_data = file.readlines()
            header_row = csv_data[0]
            if "id" not in header_row or "name" not in header_row or "marks" not in header_row:
                raise KeyError(f"Missing {header_row} column")
            for rows in csv_data[1:]:
                try:
                    values = rows.strip().split(',')
                    students_data.append({'id': values[0], 'name': values[1], 'marks': int(values[2])})
                except ValueError:
                    print('Invalid marks:', values[2])
    except FileNotFoundError as error:
        print(error)
    except KeyError as key_error:
        print(key_error)
    return students_data

students = csv_parser("/home/aniket-deshkar/PycharmProjects/Path2AI/PythonTrack/Exceptions + Modules/students.csv")
print(students)

