import random
import time

random_number = random.randint(1,10)

while True:
  guess = input("Skriv in en gissning: ")
  guess = int(guess)

  if guess > random_number:
    print("Fel! Gissa lägre!")
  elif guess < random_number:
    print("Fel! Gissa högre!")
  else:
    break

print("Du har klarat dig! Grattis du har gått vidare till nivå 2")
time.sleep(2)
while True:
  guess = input("Skriv in en gissning: ")
  guess = int(guess)

  if guess > random_number:
    print("Fel! Gissa lägre!")
  elif guess < random_number:
    print("Fel! Gissa högre!")
  else:
    break

print("Du har klarat nivå 2.")