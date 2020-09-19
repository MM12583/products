# 讓使用者輸入
buy_list = []
while True :
    product = input('請輸入商品名稱: ')
    if product == 'q' :
        break
    price = int(input('請輸入商品價格: '))
    buy_list.append([product, price])

# 寫入檔案
with open ('products.csv', 'w', encoding = 'utf-8') as f :  
    f.write('商品名,價格\n')
    for x in buy_list :    
        f.write(x[0] + ',' + str(x[1]) + '\n')

# 檢查檔案,並讀取
import os
products = []
if os.path.isfile('products.csv') :
    with open ('products.csv', 'r', encoding = 'utf-8') as t :
        for line in t :
            if '商品' in line :
                continue 
        name, price = line.strip().split(',') 
        products.append([name, price]) 
else :
    print('找不到檔案')

# 印出所購買商品
for p in buy_list :
    print('您買了', p[0], p[1], '元')

# 算出總價
sum_t = 0
for c in buy_list :
    cost = int(c[1])
    sum_t += cost
print('總共', len(buy_list), '件', '是', sum_t, '元')

