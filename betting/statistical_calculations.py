import betting.strategies as strategies 


def calculate_expected_rate_of_return(user_input):
    '''
    The expected return is the profit or loss an investor anticipates on an 
    investment that has known or anticipated rates of return (RoR). It is 
    calculated by multiplying potential outcomes by the chances of them 
    occurring and then totaling these results. 
    For example, if an investment has a 55% chance of gaining 87% and a 45% 
    chance of losing 100%, the expected return is 2.85% 
    (55% x 87% + 45% x -100% = 2.85%).

    A 'ror' of 3% means that you tend to win 3% of your stake in the long run.
    '''
    rate_of_return = user_input['win_rate']*user_input['payout_rate'] - \
        user_input['lose_rate']*1
    return round(rate_of_return*100, 2)


# FIXME: I think this formula is wrong because of payout.
def calcule_risk_of_ruin(current_strategy, user_input):
    '''
    Risk of ruin is a concept in gambling, insurance, and finance relating to 
    the likelihood of losing all one's investment capital[1] or extinguishing 
    one's bankroll below the minimum for further play. For instance, if someone 
    bets all their money on a simple coin toss, the risk of ruin is 50%. In a 
    multiple-bet scenario, risk of ruin accumulates with the number of bets: 
    each repeated play increases the risk, and persistent play ultimately 
    yields the stochastic certainty of gambler's ruin.

    Formula: Risk of Ruin = ((1 - (W*R - L)) / (1 + (W*R - L)))^U
        Where:
            W = the probability of a desirable outcome, or a win
            L = the probability of an undesirable outcome, or a loss
            R = Payout Rate, 0 <= R <= 1
            U = the maximum number of risks that can be taken before the 
                individual reaches their threshold for ruin
    '''

    units = 0
    if current_strategy == strategies.strategies_list[0]:
        if user_input['stoploss'] is None:
            user_input['stoploss'] = 0
        units = (user_input['initial_bankroll'] -
                 user_input['stoploss'])/user_input['bet_value']

    risk_of_ruin = (
        (1 - (user_input['win_rate']*user_input['payout_rate'] - user_input['lose_rate'])) /
        (1 + (user_input['win_rate']*user_input['payout_rate'] - user_input['lose_rate'])))**units
    return round(risk_of_ruin*100, 2)


def calculate_broke_percentage(user_input, broke_count):
    return round((broke_count / user_input['samples']) * 100, 2)


def calculate_profited_percentage(user_input, profitors_count):
    return round((profitors_count / user_input['samples']) * 100, 2)


def calculate_survived_profited_percentage(
        user_input, broke_count, profitors_count):
    try:
        survive_profit_percent = round(
            (profitors_count / (user_input['samples'] - broke_count)) * 100, 2)
    except ZeroDivisionError:
        survive_profit_percent = 0
    return survive_profit_percent


def calculate_final_bankroll_average(user_input, bankroll_histories):
    final_bankroll_sum = 0
    for bankroll_history in bankroll_histories:
        final_bankroll_sum += bankroll_history[-1]
    final_bankroll_average = round(final_bankroll_sum/user_input['samples'], 2)
    return final_bankroll_average


def calculate_average_profit(profits):
    try:
        average_profit = round(sum(profits) / len(profits), 2)
    except ZeroDivisionError:
        average_profit = 0
    return average_profit


def calculate_average_loses(loses):
    try:
        average_loses = round(sum(loses) / len(loses), 2)
    except ZeroDivisionError:
        average_loses = 0
    return average_loses


def calculate_expected_profit(average_profit, profited_percentage):
    return round(average_profit * (profited_percentage/ 100), 2)


def calculate_expected_loss(average_loses, profited_percentage):
    return round(average_loses * (1 - (profited_percentage / 100)), 2)