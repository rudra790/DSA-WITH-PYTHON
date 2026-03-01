seat=input("enter seat type sleeper/ac/general/luxury").lower()
match seat:
    case "sleeper":
        print(" from s1 to s4")
    case "ac":
        print("from h1 to h4")
    case "general":
        print("d1 to d5")
    case "luxury":
        print("a1 to a3")
    case _:
        print("invalid input")