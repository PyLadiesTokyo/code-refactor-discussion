import pytest
import calc


@pytest.mark.parametrize(
    [
        "test_input",
        "expected",
    ],
    [
        ([10, 5], (15, 5)),
        ([3, 10], (13, -7)),
    ]
)
def test_calc(test_input, expected):
    """
    足し算、引き算のテスト（元のコード）
    """
    assert calc.calc(*test_input) == expected

@pytest.mark.parametrize(
    [
        "test_input",
        "expected",
    ],
    [
        ([10, 5], 15),
        ([3, 10], 13),
    ]
)
def test_add(test_input, expected):
    """
    足し算のテスト
    """
    assert calc.add(*test_input) == expected


@pytest.mark.parametrize(
    [
        "test_input",
        "expected",
    ],
    [
        ([10, 5], 5),
        ([3, 10], -7),
    ]
)
def test_sub(test_input, expected):
    """
    引き算のテスト
    """
    assert calc.sub(*test_input) == expected
