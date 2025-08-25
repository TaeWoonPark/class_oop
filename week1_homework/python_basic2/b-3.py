def main():

    rows = int(input("9"))
    cols = int(input("9"))

    for J in range(1, rows + 1):
        for i in range(1, cols + 1):
             product = i * j

             print(f"{i} * {j} = {product:2} |", end="")
        print()

if __name__ == "__main__":
    main()

        


