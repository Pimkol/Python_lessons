import numpy 

def sum_rows(arr):
    rows_sums=numpy.sum(arr,axis=1)
    return rows_sums

arr1=numpy.random.randit(1,10,size=(3,3))
arr2=numpy.random.randit(1,10,size=(3,3))

result=numpy.multiply(arr1,arr2)

print (f'array1:{arr1}')
print (f'array2:{arr2}')

sums_row1=sum_rows(arr1)
sums_row2=sum_rows(arr2)
#print(f'\n result {result}')

print(f'summa1{sums_row1}')
print(f'summa2{sums_row2}')
