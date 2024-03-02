# inp=int(input("What is your age?"))

# if inp < 15:
#     print("you are a kid")
# elif inp < 20:
#     prin("You are a teenager")
# elif inp < 50:
#     print("Youre an adult")
# else:
#     print("youre very old dude")

inp=int(input("What is your age?"))

if inp => 0 and inp <= 15:
    print("you are a kid")
elif inp <= 20 and inp > 15:
    print("You are a teenager")
elif inp <= 100 and inp > 20:
    print("Youre an adult")
else:
    print("youre very old dude")