from result import Result, Ok, Err


def inc(x) -> Result:
    return Ok(x + 1)


print(Ok(1).and_then(inc))  # Ok(2)
print(Err(None).and_then(inc))  # Err(None)

x = ZeroDivisionError("5 was divided by 0")
print(Err(x))


def verbose_error_print(err: Err):
    match err:
        case Err(KeyError(message)):
            print("There was a key error", err.value)  # or some fancy message
        case Err(ZeroDivisionError()):
            print("There was division error", err.value)  # or some fancy message
        case _:
            print(err)  # or some fancy message


def print_result(r: Result):
    match r:
        case Ok(content):
            print("The result is ok:", content)
        case Err(content):
            print("The result was not ok!")
            verbose_error_print(r)


print_result(Err(ZeroDivisionError("5 was divided by 0")))
