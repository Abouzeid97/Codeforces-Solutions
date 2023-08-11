n = int(input())
ct = 0
for q in range (0,n):
    s = input()
    if s == 'Icosahedron':
        ct += 20
    if s == 'Tetrahedron':
        ct += 4
    if s == 'Cube':
        ct += 6
    if s == 'Octahedron':
        ct += 8
    if s == 'Dodecahedron':
        ct += 12
print(ct)
