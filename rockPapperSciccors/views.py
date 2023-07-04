from django.shortcuts import render, redirect
from django.contrib import messages
import random

def home(request):
    options = ["Rock", "Paper", "Scissors"]  # Renamed 'option' to 'options'

    if request.method == "POST":
        player_choice = request.POST['user'].title()  # Renamed 'playerChoice' to 'player_choice'
        computer_choice = random.choice(options).title()  # Renamed 'computerChoice' to 'computer_choice'

        if player_choice == computer_choice:
            messages.success(request, f"Computer also choose {computer_choice}, So it's a tie")  # Removed 'return' as messages are not returned directly

        elif player_choice == "Rock":
            if computer_choice == "Scissors":
                messages.success(request, f"Computer choose {computer_choice}, Rock smashes the scissors. You win!")
            else:
                messages.success(request, f"Computer choose {computer_choice}, Paper covers the rock. You lose!")

        elif player_choice == "Paper":
            if computer_choice == "Scissors":
                messages.success(request,f"Computer choose {computer_choice}, Scissors cut the paper. You lose!")
            else:
                messages.success(request, f"Computer choose {computer_choice}, Paper covers the rock. You win!")

        elif player_choice == "Scissors":
            if computer_choice == "Rock":
                messages.success(request, f"Computer choose {computer_choice}, Rock smashes the scissors. You lose!")
            else:
                messages.success(request, f"Computer choose {computer_choice}, Scissors cut the paper. You win!")

        return redirect('home')  # Redirect after processing the POST request

    return render(request, 'index.html')
