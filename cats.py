def get_cats_info(path: str) -> list:
    """
    Reads a file with information about cats and returns a list of dictionaries.

    Input:
    :param path: string     Path to text file.

    Output:
    :return: list: List of dictionaries with information about cats.
    """
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_data = line.strip().split(',')
                if len(cat_data) == 3:
                    cat_dict = {
                        "id": cat_data[0],
                        "name": cat_data[1],
                        "age": cat_data[2]
                    }
                    cats_info.append(cat_dict)
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return cats_info

# Example of using the function
cats_info: list = get_cats_info("cats_file.txt")
print(cats_info)