from django.shortcuts import render, redirect
from django.contrib import messages
import random

def home(request):
    options = ["Rock", "Paper", "Scissors"] 

    if request.method == "POST":
        player_choice = request.POST['user'].title() 
        computer_choice = random.choice(options).title()  

        if player_choice == computer_choice:
            messages.info(request, f"{computer_choice}, It's a Tie 😐")
        elif player_choice == "Rock" and computer_choice == "Scissors":
            messages.success(request, f"{computer_choice}, You Win ⭐")
        elif player_choice == "Paper" and computer_choice == "Rock":   
            messages.success(request, f"{computer_choice}, You Win ⭐")
        elif player_choice == "Scissors" and computer_choice == "Paper":
            messages.success(request, f"{computer_choice}, You Win ⭐")
        else:
             messages.success(request, f"{computer_choice}, 💻 Win")
        return redirect('home') 
    return render(request, 'index.html')
