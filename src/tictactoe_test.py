
Nobody = "Nobody"
FirstPlayer = "FirstPlayer"
SecondPlayer = "SecondPlayer"

Top = 0
Left = 0
Middle = 1
Bottom = 2
Right = 2

def there_is_a_line(a_players_moves):
    return a_players_moves in [
        [(Top, Left), (Top, Middle), (Top, Right)],
        [(Middle, Left), (Middle, Middle), (Middle, Right)],
        [(Bottom, Left), (Bottom, Middle), (Bottom, Right)]]


def test_there_is_a_horizontal_line_at_the_top():
    assert there_is_a_line([(Top, Left), (Top, Middle), (Top, Right)])

def test_there_is_a_horizontal_line_in_the_middle():
    assert there_is_a_line([(Middle, Left), (Middle, Middle), (Middle, Right)])

def test_there_is_a_horizontal_line_at_the_bottom():
    assert there_is_a_line([(Bottom, Left), (Bottom, Middle), (Bottom, Right)])

def test_something_that_is_not_a_line():
    assert not there_is_a_line([(Top, Left), (Top, Middle), (Bottom, Right)])


def who_wins(moves):
    first_player_moves = moves[::2]
    second_player_moves = moves[1::2]
    
    if there_is_a_line(first_player_moves):
        return FirstPlayer
    elif there_is_a_line(second_player_moves):
        return SecondPlayer
    else:
        return Nobody
    

def test_nobody_has_won_when_nobody_has_moved():
    winner = who_wins([])
    assert winner == Nobody

def test_nobody_has_won_when_player_x_plays_in_the_middle():
    winner = who_wins([(Middle, Middle)])
    assert winner == Nobody

def test_first_player_wins_after_minimal_number_of_moves():
    winner = who_wins([
            (Top, Left),
            (Bottom, Left),
            (Top, Middle),
            (Bottom, Middle),
            (Top, Right)])
    
    assert winner == FirstPlayer

def test_nobody_wins_after_five_inconclusive_moves():
    winner = who_wins([
            (Top, Left),
            (Bottom, Left),
            (Top, Middle),
            (Bottom, Middle),
            (Middle, Left)])
    
    assert winner == Nobody

def test_second_player_wins_after_minimal_number_of_moves():
    winner = who_wins([
            (Top, Left),
            (Bottom, Left),
            (Top, Middle),
            (Bottom, Middle),
            (Middle, Right),
            (Bottom, Right)])
    
    assert winner == SecondPlayer
