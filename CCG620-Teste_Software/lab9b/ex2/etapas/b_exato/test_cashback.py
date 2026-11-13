from cashback import cashback


def test_cashback_valor_exato():
    # 50 nao entra (< 100); 100 -> 5.0; 200 -> 10.0; total = 15.0
    assert cashback([50, 100, 200]) == 15.0
