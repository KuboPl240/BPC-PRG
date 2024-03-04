def return_coins(money, denominations):
    """
    Return any amount of money in coins of available denominations
    :param money: the amount of money to be returned
    :param list denominations: available denominations of coins
    :rtype list
    :return: the minimum number of coins that sum up to the value of money to be returned
    """
    returned_coins = []
    #sort denominations from coin with biggest value to coin with smallest value
    denominations.sort(reverse=True)
    if not(isinstance(money, int)):
        print("Nespravny vstup")
        return []
    index = 0
    while money>0:
        #if selected coin has less or same value as money, decrement money by value of that coin
        if(money>=denominations[index]):
            money-=denominations[index]
            returned_coins.append(denominations[index])
        #if selected coin has more value then money, switch to the coin with less value
        elif index<len(denominations)-1:
            index+=1
        #if there is no more coins with less or same value as money, end algorithm
        else: break


    return returned_coins


if __name__ == "__main__":
    money = int(input("Zadej castku k vraceni: "))
    denominations = [1, 2, 5, 10, 20, 50]
    coins = return_coins(money, denominations)
    print(f"Vracím mince o hodnotě {coins} Kč.")
