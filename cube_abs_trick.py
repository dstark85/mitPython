

def cube_fault(cube):
    for guess in range(abs(cube) + 1):  # got tripped up here. 
        if guess ** 3 >= abs(cube):
            break
    if guess ** 3 != abs(cube):
        print(cube, 'is not a perfect cube')
    else:
        if cube < 0:
            guess = -guess
        print('Cube root of ' + str(cube) + ' is ' + str(guess))

def test(num):
    print('Now testing number: ', num)
    cube_fault(num)


def main():
    test(8)
    test(9)
    test(-8)
    test(-9)


if __name__ == '__main__':
    main()
