from result import Result, Ok, Err


def inc(x) -> Result:
    return Ok(x + 1)


print(Ok(1).and_then(inc))  # Ok(2)
print(Err(None).and_then(inc))  # Err(None)
