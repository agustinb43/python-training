
def fibonacci(n):
    a, b = 0, 1
    result = [0]
    while len(result) < n:
        a, b = b, a + b
        result.append(a)
    return result

if __name__ == '__main__':
    assert fibonacci(0) == [0]
    assert fibonacci(3) == [0, 1, 1]
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(20) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
    assert fibonacci(1000)[-1] == 26863810024485359386146727202142923967616609318986952340123175997617981700247881689338369654483356564191827856161443356312976673642210350324634850410377680367334151172899169723197082763985615764450078474174626
    print('Passed!')