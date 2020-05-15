cube = 27
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low) / 2.0
num_guesses = 0
while abs(guess ** 3 - cube) >= epsilon:
    if (guess ** 3 >= cube):
        high = guess
    else:
        low = guess
    guess = (high + low) / 2.0
    num_guesses += 1
print(guess)
print('num_guesses=', num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print('Failed on cube root of', cube)
else:
    print(guess, 'is close to the cube root of', cube)
