def input_array(prompt):
    while True:
        array = input(prompt).split()
        if all(x.isdigit() and 0 <= int(x) <= 9 for x in array):
            return list(map(int, array))
        else:
            print("Array harus berisi bilangan bulat dari 0 sampai 9.")

def main():
    A = input_array("Masukkan elemen array A : ")
    B = input_array("Masukkan elemen array B : ")

    C = list(set(A)- set(B))
    D = list(set(B)- set(A))
    E = list(set(A) & set(B))

    print("Array yang hanya ada di A:", C)
    print("Array yang hanya ada di B:", D)
    print("Array yang ada di A dan B:", E)

if __name__ == "__main__":
    main()
    