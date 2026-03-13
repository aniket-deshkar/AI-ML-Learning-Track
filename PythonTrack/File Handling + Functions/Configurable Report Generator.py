import json

in_file_path = "/home/aniket-deshkar/PycharmProjects/Path2AI/PythonTrack/File Handling + Functions/employees.csv"
out_file_path = "/home/aniket-deshkar/PycharmProjects/Path2AI/PythonTrack/File Handling + Functions/employees_data_export.txt"


def generate_report(file_name, *metrics,**options):
    employees = []
    with open(file_name, "r") as input_file:
        lines = input_file.readlines()

        if len(lines) == 0:
            return
        headers = lines[0].strip().split(',')

        i = 1
        while i < len(lines):
            line = lines[i].strip()
            if line == "":
                i += 1
                continue

            emp_values = line.split(",")
            employee = {}
            a = 0
            while a < len(headers):
                employee[headers[a]] = emp_values[a]
                a += 1

            employees.append(employee)
            i += 1

        report = []
        #metrics
        for metric in metrics:
            if metric == "avg_salary":
                total_sum = 0
                count = 0
                for emp in employees:
                    total_sum += float(emp["salary"])
                    count += 1
                value = total_sum / count
                label = "Average Salary"

            elif metric == "max_salary":
                max_val = 0
                for emp in employees:
                    current_salary = float(emp["salary"])
                    if current_salary > max_val:
                        max_val = current_salary
                value = max_val
                label = "Max Salary"

            else:
                continue

            if options.get("rounding"):
                value = round(value)

            currency = options.get("currency", "")
            line = f"{label}: {currency} {value}".strip()

            if options.get("uppercase"):
                line = line.upper()

            report.append(line)

    # write report to a file
    with open(out_file_path, "w") as out_file:
        for line in report:
            out_file.write(line + "\n")

#Calling generate_report function
generate_report(in_file_path,"avg_salary","max_salary",uppercase=True,currency="INR")


