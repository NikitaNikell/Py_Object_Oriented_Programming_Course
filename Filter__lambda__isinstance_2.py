def get_add(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and type(a) != bool and type(b) != bool:
        return a + b
    elif isinstance(a, (str)) and isinstance(b, (str)):
        return a + b
    return None

print(get_add(1, 4))
print(get_add(1, 4.5))
print(get_add("Nikita", "Nikell"))
print(get_add(1,"4"))
print(get_add(True, 1))