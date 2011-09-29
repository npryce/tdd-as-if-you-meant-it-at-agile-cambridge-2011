
Nobody = ""
X = "X"
Middle = 1

def who_wins(moves):
    return Nobody


def test_nobody_has_won_when_nobody_has_moved():
    winner = who_wins([])
    assert winner == Nobody

def test_nobody_has_won_when_player_x_plays_in_the_middle():
    winner = who_wins([(X, Middle, Middle)])
    assert winner == Nobody
