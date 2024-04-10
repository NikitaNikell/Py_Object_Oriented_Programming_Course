try:
    assert 1 == 2, "Что-то пошло не так"
except AssertionError as err:
    print("Отловили AssertionError:", err)
finally:
    print("Досвидули")