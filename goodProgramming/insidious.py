# This program illustrates how a program can lock a user in


def get_fav_num(mercy):
    count = 0
    while True:
        count += 7
        try:
            num = int(input('give me a num '))
            if num == 42: 
                print("That's it!")
                break
        except KeyboardInterrupt:
            print("Ah ah ah, not so fast")
        except:
            print("Numbers only, eh?")
        if count > mercy:
            print("Ok, enough being cruel")
            break


get_fav_num(41)
