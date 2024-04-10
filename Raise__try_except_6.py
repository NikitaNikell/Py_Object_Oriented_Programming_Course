def function_1():
    raise ValueError("Oops, something went wrong")


def function_2():
    try:
        function_1()
    except Exception as e:
        print("Exception caught:", e)


function_2()