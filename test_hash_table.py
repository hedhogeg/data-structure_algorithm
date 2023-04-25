from hash_table import HashTable

h = HashTable()

h.setData(1, '이운재')
h.setData(4, '최진철')
h.setData(20, '홍명보')
h.setData(6, '유상철')
h.setData(22, '송종국')
h.setData(21, '박지성')
h.setData(5, '김남일')
h.setData(10, '이영표')
h.setData(8, '최태욱')
h.setData(9, '설기현')
h.setData(14, '이천수')

print(f'1 : {h.getData(1)}')
h.removeData(1)
print(f'1 : {h.getData(1)}')
print(f'21 : {h.getData(21)}')
