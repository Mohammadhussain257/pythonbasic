i = 0
while i <= 5:
    print(i)
    i += 1
print('*'*15)

secret_key = 'mysecret'
guess_count = 0
guess = ''
guess_limit = 3
out_of_guess = False

while guess != secret_key and not(out_of_guess):
    if guess_count < guess_limit:
        guess = input('Enter secret key : ')
        guess_count +=1
    else:
        out_of_guess = True

if out_of_guess:
    print('Out of guess your are blocked')
else:
    print('Key matched access granted')