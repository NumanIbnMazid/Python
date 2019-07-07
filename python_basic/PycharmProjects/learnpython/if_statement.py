
is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a Male or Tall or both")
else:
    print("You are neither Male nor Tall")

print("\n")

is_male = False
is_tall = False

if is_male or is_tall:
    print("You are a Male or Tall or both")
else:
    print("You are neither Male nor Tall")

print("\n")

is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a Tall Male")
elif is_male and not(is_tall):
    print("You are a Short Male")
elif not(is_male) and is_tall:
    print("You are not a Male but is Tall")
else:
    print("You are not a Tall Male")