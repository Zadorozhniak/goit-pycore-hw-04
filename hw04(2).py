def get_cats_info(path):
    cats = []  
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    cat_id, name, age = line.strip().split(",")
                    cats.append({
                        "id": cat_id,
                        "name": name,
                        "age": int(age) 
                    })
                except ValueError:
                    print(f"Error in line: {line.strip()}")

    except FileNotFoundError:
        print(f"File '{path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return cats  

cats_data = """60b90c1c13067a15887e1ae1,Gabby,1
60b90c2413067a15887e1ae2,Star,2
60b90c2e13067a15887e1ae3,Peper,7
60b90c3b13067a15887e1ae4,Cobby,8
60b90c4613067a15887e1ae5,Cake,2
"""

with open("cats_file.txt", "w", encoding="utf-8") as file:
    file.write(cats_data)

cats_info = get_cats_info("cats_file.txt")
print(cats_info)
