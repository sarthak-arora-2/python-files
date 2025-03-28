#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Input/Letters/starting_letter.txt", "r") as starting_letter:
    letter_line = starting_letter.readlines()

with open("Input/Names/invited_names.txt", "r") as invited_names:
    names = invited_names.readlines()

example = letter_line[0]
for name in names:
    mod = name.strip("\n")
    letter_line[0] = example.replace("[name]", f"{mod}")
    string = ""
    final_letter = string.join(letter_line)
    with open(f"Output/ReadyToSend/letter_for_{mod}.txt", "w") as output:
        output.write(f"{final_letter}")

