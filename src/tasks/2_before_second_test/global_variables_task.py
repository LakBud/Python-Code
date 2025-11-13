print()
def christmas_tree(size: str) -> None:
    total_rows = 0
    
    if size == "large":
        total_rows = 7
    elif size == "medium":
        total_rows = 5
    elif size == "small":
        total_rows = 3
    else:
        print("Write either small, medium or large to generate your christmas tree")
        return
        
    for i in range(total_rows):
        print(f"{"*" * (2*i+1):^20}")
    print()


size_variable = str(input("Write small, medium or large to create your christmas tree: "))
print()

christmas_tree(size_variable)
