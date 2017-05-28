from random import randint # This is what helps me to create a random generator

class Die:

    def roll_die(self, number_of_rolls):
        number_of_sides = 6

        for number in range(number_of_rolls):

            random_number = randint(1, number_of_sides)

            if number <= number_of_rolls - 1:
                print("The first few choices were: " + str(random_number))
            else:
                print("The final choice is: " + str(random_number))

        final_string = "The random number is " + str(random_number)
        return final_string


roll_dice = Die().roll_die(100)

print(roll_dice)