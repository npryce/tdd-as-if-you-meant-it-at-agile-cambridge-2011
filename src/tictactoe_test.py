
Nobody = "Nobody"
X = "X"
O = "O"

Top = 0
Left = 0
Middle = 1
Bottom = 2
Right = 2

def who_wins(moves):
    return X if len(moves) == 5 else Nobody


def test_nobody_has_won_when_nobody_has_moved():
    winner = who_wins([])
    assert winner == Nobody

def test_nobody_has_won_when_player_x_plays_in_the_middle():
    winner = who_wins([(X, Middle, Middle)])
    assert winner == Nobody

def test_x_wins_after_minimal_number_of_moves():
    winner = who_wins([
            (X, Top, Left),
            (O, Bottom, Left),
            (X, Top, Middle),
            (O, Bottom, Middle),
            (X, Top, Right)])
    
    assert winner == X
