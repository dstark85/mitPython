# this file shows how to create exceptions

try:
    raise Exception('test', 'debug')  # creates an exception
except Exception as myException:  # defines the exception as var
    print(type(myException))
    print(myException.args) # way to access arguments of exception
    print(myException)


try:
    '8' / 2
except:
    print("something went awry")
    raise   # this condensed form just raises the exception
