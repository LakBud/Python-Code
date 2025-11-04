print()
def christmas_tree(size: str) -> None:
    if size == "small":
        for i in range(0,12):
            if i % 3 == 0:
                print(i * "*")
                print()
                
christmas_tree("small")
