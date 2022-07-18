def howmuch(n, a, cost):
    cookies = 0
    cash = 0
    if n > a:
        while a != n:
            cookies = cookies + (a - 2) * 4
            a = a + 1
        accounts = cookies / 60
        cash = int(accounts) * cost
        if accounts % 1 != 0:
            cash = cash + cost
        print(f'You need {cash} rubles to get this lvl!')
    else:
        print('Type correct lvl')

def rolls(cash, cost):
    print(f'You will get {cash // cost * 60} cookies, {int(cash // cost * 60 / 5)} roulette rolls')

def whatlvl(cash, act, cost):
    cookies = cash / cost * 60
    print(f'You will get {int(cookies)} cookies')
    while cookies > 0:
        cookies = cookies - cost * (act - 2)
        act = act + 1
    print(f'And new, {act} lvl')


if __name__ == '__main__':
    print(f'Select Mode: "How much money do you need to get N lvl?" or "What level will I get for N money?" or "Money/Cookie converter"')
    print(f'Type "HM" or "WL" or "MC"')
    answer = input().lower()

    if answer == "hm":
        print('Whats your actual lvl?')
        hm_act_lvl = int(input())
        print('What level you want to get?')
        hm_n_lvl = int(input())
        print('Enter the cost of the account')
        acc_price = int(input())
        howmuch(hm_n_lvl, hm_act_lvl, acc_price)

    elif answer == "wl":
        print('Whats your cash amount?')
        wl_cash = int(input())
        print('Enter the cost of the account')
        acc_price = int(input())
        print('Whats your actual lvl?')
        wl_act_lvl = int(input())
        whatlvl(wl_cash, wl_act_lvl, acc_price)
    elif answer == "mc":
        print('What your cash amount?')
        mc_cash = int(input())
        print('Enter the cost of the account')
        acc_price = int(input())
        rolls(mc_cash, acc_price)
    else:
        print('Type correct key')