print("You sit awkwardly on the too small stool at the too tall bar. A single index finger traces up and down the sweating glass in front of you, catching the beads as they travel down the glass to join a growing puddle.")

print("")
print("The barkeep reluctantly addresses you by the blatantly embodied title, represented by the garrish crimson and black sigil on your shoulder, \"Meeting someone Regulator...?")

print("")

print("He trails off, waiting for you to fill in the rest.")

print("")
name = input("Choose your character name. ")
print("")

age = int(input("What is your age? ")) 
hp_value = age + 5
if age >= 60:
    hp_value = age + 10


print("")
if age >= 18:
    print(
        "At last, your time on this plane has reached it's ending! Prepare yourself.")

    print("")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
      print("")
      print("Regulator", name,"you are starting with", hp_value, "health.")
        
    
        
        
      print("")
      print("The barkeep is waiting for his answer.")
      print("")

      answer_or_ignore = input("You don't have time for this nonsense. Do you answer/ignore? ")

      if answer_or_ignore == "answer":
        print("")
        print("Bruskly, you give the man your name, \"", name,"\", and take a long swig from the now warm glass. You feel miminal loss of your faculties and lose 2 health.")
        hp_value -= 2
        print("Your heath is now", hp_value,".")

      else:
        print("")
        print(
                "The barkeep thinks better of his question and moves along to the next patron.")

        print("")
    else:
        print("The brave die young, but the coward's life never begins.")

else:
    print("It is not your time yet young one.")
