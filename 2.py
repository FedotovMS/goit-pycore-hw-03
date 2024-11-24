import random

def get_numbers_ticket(min, max, quantity):
   
   if not (1 <= min <= max <= 1000):
         raise ValueError("Параметри min і max мають бути в межах [1, 1000], і min <= max.")
   
   if not (1 <= quantity <= (max - min + 1)):
        raise ValueError("Кількість чисел має бути не меншою за 1 і не більшою за кількість чисел у діапазоні.")
    
   numbers = random.sample(range(min, max + 1), quantity)
   return sorted(numbers)


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

# # lottery_numbers = get_numbers_ticket(49, 1, 6)
# # print("Ваші лотерейні числа:", lottery_numbers)


# lottery_numbers = get_numbers_ticket(1, 49, 100)
# print("Ваші лотерейні числа:", lottery_numbers)