
class Cycle:
    def hamiltonianCycle(self, node):
        count = 1
        i = node - 1
        while (i > 0):
            count = count * i
            i -= 1
        print("\n Numarul nodului : ", node, end="")
        print("\n Ciclul Hamiltonian : ", (int(count / 2)), end="")


def main():
    task = Cycle()
    #  Test
    n=input("Introduceti numarul de noduri al grafului")
    task.hamiltonianCycle(int(n))


if __name__ == "__main__": main()