def rzeczy(*args):
    for arg in args:
        print(arg)

rzeczy('lampa','krzeslo','stol','pusia','pancio');


def rzeczy("pierwsza_rzecz", args):
    print(pierwsza_rzecz)
    print(args[0])
    for arg in args:
        print(arg)

rzeczy('lampa','krzeslo','stol','pusia','pancio')
