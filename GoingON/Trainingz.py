temperature = int(input('how is it? '))
is_sunny = input("Is it sunny? (yes/no): ")

is_sunny = is_sunny.lower() == "yes"

if temperature > 20:
  if is_sunny:
    print("Perfect beach weather!")
  else:
    print('bad day')