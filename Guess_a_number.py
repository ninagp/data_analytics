import numpy as np


def game_core_v2(number):
    """Set a random number, then lower or increase the number based on whether the random number is higher or
      lower than the guessed number"""
    count = 1
    n1 = 1
    n2 = 101
    while n1 != n2 - 1:  # Set cycle limits
        count += 1
        mid = n1 + (
                n2 - n1) // 2
        """Divide the given number field into two even subfields and look for the guessed number in one of the 
        subfields """
        if n1 == n2 - 1:
            return count
        elif number in range(n1,
                             mid):
            """The subfield gets further divided into two subfields and the above mentioned algorithm is repeated"""
            n2 = mid
        else:
            n1 = mid
    return (count + 1)  # exit the cycle if the number is guessed


def score_game(game_core):
    '''Run the function 1000 times to determine how fast the algorithm guesses the number'''
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f" Your algorithm guesses a number in {score} attempts")
    return (score)


score_game(game_core_v2)

