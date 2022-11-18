def higher(fnc, *argv):
    print(f"Calling function {fnc}")
    fnc(*argv)

def one_arg(only):
    print(f"Here is the only arg {only}")

def two_arg(first, second):
    print(f"Here is the first {first} And here is the second {second}")

higher(one_arg, "Only one")
higher(two_arg, "Here's one", "and Another one")
