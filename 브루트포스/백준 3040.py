dwarfs = [int(input()) for _ in range(9)]

def get_real(dwarfs):
    dwarfs_sum = sum(dwarfs)
    for i in range(9):
        dwarf_1 = dwarfs[i]
        for j in range(i+1, 9):
            dwarf_2 = dwarfs[j]
            temp = dwarfs_sum - dwarf_1 - dwarf_2
            if temp == 100:
                dwarfs.remove(dwarf_1)
                dwarfs.remove(dwarf_2)
                return dwarfs
            
print(*get_real(dwarfs), sep = '\n')