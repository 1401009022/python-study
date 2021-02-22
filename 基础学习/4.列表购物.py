
"""
列表循环
"""
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]



def showgoods(goods):
    print("======商品列表如下======")
    for i in range(0,len(goods)):
        print(i+1,goods[i].get('name'))

def showchart(chart):
    for i in range(0,len(chart)):
        print(chart[i])

def chargemoney(summoney):
    num  = int(input("请输入要充值的金额： "))
    summoney += num
    print("充值成功，剩余金额为：",summoney)
    return  summoney

def tochart(goods,num,chart):
    chart.append(goods[num-1])
    print("添加成功，目前购物车内商品为：")
    showchart(chart)
    return chart

def movechart(num,goodsbuy):
    goodsbuy.remove(num)
    return goodsbuy

def buy(goodsbuy,summoney):
    num = 0
    for i in range(0,len(goodsbuy)):
        num += goodsbuy[i]['price']
    if num > summoney:
        print("余额不足，购买失败")
        exit()
    else:
        num -= summoney
        goodsbuy.clear()

def main():
    chart = []
    summoney = int(input("请输入总资产: "))
    while True:
        print("======请选择需要的服务======")
        print("1.充值")
        print("2.购买商品")
        print("3.查看购物车")
        print("4.移除购物车商品")
        print("5.购买")
        print("6.退出")
        opt = int(input())

        if opt == 1:
            summoney = chargemoney(summoney)
        elif opt == 2:
            showgoods(goods)
            num = int(input("请输入您要加入购物车的商品的编号"))
            tochart(goods,num,chart)
        elif opt == 3:
            showchart(chart)
        elif opt ==4:
            showchart(chart)
            num = int(input("请输入您要移除的购物车商品的编号"))
        elif opt ==5:
            buy(chart,summoney)
        else:
            exit()



if __name__ == '__main__':
    main()

















