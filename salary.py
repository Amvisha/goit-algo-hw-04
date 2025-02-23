def total_salary(path):
    """
    Parses a file with developer salaries and returns the total and average salary amount.

    Input:
    :param path: string     Path to text file.

    Output:
    :return: tuple   A tuple of two numbers: total salaries and average salary
    """

    total_salary = 0
    developer_count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                developer, salary = line.strip().split(',')
                total_salary += float(salary)
                developer_count += 1

        if developer_count == 0:
            print(f"The file '{path}' is empty.")
            return 0, 0  # Returning 0, 0, if file is empty

        average_salary = total_salary / developer_count
        return total_salary, average_salary

    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return 0, 0  # Returning 0, 0 in case of file error

    except ValueError:
        print(f"Error: Invalid data in file '{path}'. Check file format.")
        return 0, 0  # Returning 0, 0 in case of data error

# Example of using the function:
total, average = total_salary("salary_file.txt")
print(f"Total salary: {total}, Average salary: {average}")