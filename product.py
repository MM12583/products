buy_list = []
while True :
    product = input('請輸入商品名稱: ')
    if product == 'q' :
        break
    price = int(input('請輸入商品價格: '))
    # 二(多)維清單,將小清單裝進大清單
    p_p = []
    p_p.append(product)  
    p_p.append(price)
    # 簡寫 p_p = [product, price]
    buy_list.append(p_p)
# ** 下面重要
n = 0
c = 0
sum_c = 0
with open ('products.csv', 'w', encoding = 'utf-8') as f :  # csv為資料常用檔，請愛用(可用excel開)，utf-8 解決亂碼
    f.write('商品,價格\n') # 都要寫在字串內，','為分隔號
    for x in buy_list : # 利用迴圈逐項印出    
        name = buy_list[n][0]     # 選取資料
        cost = int(buy_list[c][1])
        print('您了買商品', name, '價格為', cost, '元')
        f.write(str(name) + ',' + str(cost) + '\n') # write 一定要用字串，加逗號在excel可以分格
        n += 1
        c += 1
        sum_c += cost
print('總共', len(buy_list), '件', sum_c, '元')