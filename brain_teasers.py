#===============================================================================================
# Scripts for brain teasers and fun projects
# Date: 15.12.2022
# Author: Tobias Fritz
#===============================================================================================


# For a sum of results, return the minimum amount of euro coins 
def automat(cash, wallet = []):
  ''' Take an amount of cash in cent (int) and return the minimal amount of coins as a list
  param:  
          cash:   int:  the amount to be payed in cent
          wallet: list: coins that are used
  '''
    
    #coin dict
    coins = [200,100,50,20,10,5,2,1]
    
    # iterate from highest to lowest
    for coin in coins: 
        
        # if the cash value - coin = 0 we're done and can return the set of coins
        if (cash-coin) == 0: 
            return wallet + [coin]
        
        # if the cash value - coin not 0 we call the function recursively and add the coin to our wallet
        elif (cash-coin) > 0 :
            wallet.append(coin)
            return (automat(cash-coin,wallet))
          
