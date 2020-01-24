__author__ = 'Alexandre Calil Martins Fonseca, Github: xandao6'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from typing import Callable, Union, Tuple


def fixed_system(
        gen_bet_result: Callable[[int], bool], 
        win_rate: int,
        payout_rate: int,
        bankroll: Union[int, float], 
        bet_count: int,
        bet_percentage: int
) -> Tuple[int, Union[int, float]]:
    '''
    Parameters
    ----------
    gen_bet_result -> Callable[[int], bool]
        A function that generate a random bet result, considering the win rate,
        and return True for win or False for lose.
    win_rate -> int
        The win rate is a rate that can range from 0 to 100, which means the 
        percentage you have of winning. 
        To know your win rate you must divide the total bets you won by the 
        total bet, the more bets the more 
        accurate that rate will be.
    payout_rate -> int
        The payout rate means how much you will win, for example an 80% payout
        rate means that for every $ 1 wagered you will win $1 * 80% = 0.80c. 
        Here the payout rate varies from less infinite to more infinite, but 
        this value generally ranges from 0 to 200.
    bankroll -> Union[int, float]
        The bankroll is the amount of money you have to bet.
    bet_count -> int
        The bet count is the amount of bets you will simulate.
    bet_percentage -> int
        The bet percentage is the amount you will risk on each bet.

    Returns
    -------
    Tuple[int, Union[int, float]]
        This function returns a tuple containing two lists, the first is the 
        X axis which is the amount of bets, the second is the Y axis which is 
        the bankroll history.

    '''
    
    bet_count_history_X = []
    bankroll_history_Y = []
    bet_size = bankroll*bet_percentage/100.0
    currentWager = 1
    
    while currentWager <= wager_count:
        if gen_bet_result(win_rate):
            bankroll += bet_size*payout/100.0
        else:
            bankroll -= bet_size
            if bankroll <= 0:
                print('Broke')
                break
        bet_count_history_X.append(currentWager)
        bankroll_history_Y.append(bankroll)
        currentWager += 1
        
    return bet_count_history_X, bankroll_history_Y