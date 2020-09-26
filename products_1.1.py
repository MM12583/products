# 讀取檔案
def read_file(filename) : # 設定參數為函式內使用資料
    buy_list = []
    with open (filename, 'r', encoding = 'utf-8') as t :
        for line in t :
            if '商品' in line :
                continue 
            name, price = line.strip().split(',') 
            buy_list.append([name, price]) 
    return buy_list # 回傳結果 

#讓使用者輸入
def user_input(buy_list) :
    while True :
        product = input('請輸入商品名稱: ')
        if product == 'q' :
            break
        price = int(input('請輸入商品價格: '))
        buy_list.append([product, price])
    return buy_list

# 寫入檔案
def write_file(filename, buy_list) :
    with open (filename, 'w', encoding = 'utf-8') as f :  
        f.write('商品名,價格\n')
        for x in buy_list :    
            f.write(x[0] + ',' + str(x[1]) + '\n')

# 印出所購買商品
def print_products(buy_list) :
    for p in buy_list :
        print('您買了', p[0], p[1], '元')

# 算出總價
def print_sum(buy_list) :
    sum_t = 0
    for c in buy_list :
        cost = int(c[1])
        sum_t += cost
    print('總共', len(buy_list), '件', '是', sum_t, '元')


import os
def main() :
    filename = 'products_f.csv'
    if os.path.isfile(filename) :
        print('找到檔案')
        buy_list = read_file(filename) # 檔名用字串
    else :
        print('找不到檔案')

    buy_list = user_input(buy_list)
    print_products(buy_list)
    print_sum(buy_list)
    write_file('products_f.csv', buy_list)
main()
