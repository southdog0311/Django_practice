import pytest
from cards.cards import compare_cards

def test_compare_cards():
    assert compare_cards('A', 'K') == 'A'
    assert compare_cards('5', '10') == '10'
    assert compare_cards('J', 'Q') == 'Q'
    assert compare_cards('2', '2') == 'Equal'

    with pytest.raises(ValueError):
        compare_cards('1', 'A')

    with pytest.raises(ValueError):
        compare_cards('A', 'B')
        
    # 更多測試用例
    assert compare_cards('10', '10') == 'Equal'
    assert compare_cards('3', '4') == '4'
    assert compare_cards('J', '10') == 'J'
