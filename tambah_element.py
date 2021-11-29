a=[1,2,3,4,5]
b=[6,7,8,9,10]

print('2 bagian dari list pertama (A) dan kedua (B)')
b.append(a[0:2])
print(b)
print()

print('tambah list (B) dengan nilai string')
b.append("11")
print(b)
print()

print('tambah list (B) dengan 3 nilai')
print(b+[12+13+14])
print()

print('gabungkang lis (B) dengan list (A)')
print(a+b)
print()
