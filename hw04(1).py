
with open("salary_file.txt", "w", encoding="utf-8") as file:
    file.write("Gabby Thomson,6800\n")
    file.write("Matthew Crauford,8150\n")
    file.write("Clark Gillory,5050\n")

print("File created!")

def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            salaries = []
            
            for line in file:
                try:
                    name, salary = line.strip().split(",")
                    salaries.append(int(salary))
                except ValueError:
                    print(f"Error in line: {line.strip()}")  

        if not salaries:
            return 0, 0  

        total = sum(salaries)
        average = total / len(salaries)
        
        return total, average

    except FileNotFoundError:
        print(f"File '{path}' not found.")
        return None, None
    except Exception as e:
        print(f"An error occured: {e}")
        return None, None


total, average = total_salary("salary_file.txt")

if total is not None:
    print(f"Total salary: {total}, avarage salary: {average}")
