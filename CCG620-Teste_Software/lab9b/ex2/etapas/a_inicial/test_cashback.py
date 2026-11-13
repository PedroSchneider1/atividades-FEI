from cashback import cashback


def test_cashback_positivo():
    assert cashback([50, 100, 200]) > 0
