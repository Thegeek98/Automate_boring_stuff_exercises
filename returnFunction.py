def foo():
    print("hello from inside of foo")
    return 1
if __name__ == '__main__':
    print("going to call foo")
    x = foo()
    print("called foo")
    print("foo returned " + str(x))q