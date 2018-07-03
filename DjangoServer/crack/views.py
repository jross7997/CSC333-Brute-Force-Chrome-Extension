#Brute Force Cracker
#Authors: Justin Ross and Emma Brunell
#This program is a simple brute force password cracker. It was made for
#purely educational purposes. The program can take in alphanumeric strings of length 9 or less
#(including capitals, lowercase and these symbols !@#$%^&*()-_=+~`:;<>., )
#It will crack the password and return the password and the number of attempts
#at cracking it were made. This was intended to run on a Django Server.
#The program takes in the password as a query parameter and produces JSON.
from django.shortcuts import render
from django.http import JsonResponse
import itertools
import string

def index(request):
    #The query parameter is "pass"
    real = request.GET["pass"]
    #Check if the password is 9 characters or less
    if len(real) < 10:
        #Define the accepted characters and initialize a count
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits +'!@#$%^&*()-_=+~`:;<>.,'
        attempts = 0
        #Brute force crack.
        #Checks if the string in question matches the original password,
        #if not, increment and check with the next character in line
        for password_length in range(1, 9):
            for guess in itertools.product(chars, repeat=password_length):
                attempts += 1
                guess = ''.join(guess)
                if guess == real:
                    return JsonResponse({"password": guess,"attempts":attempts})
    else:
        return JsonResponse({"password": "Password too Long","attempts":"0"})
