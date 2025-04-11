1. we will basically read the Excel file in order to compute our game. As there will be more tables for the game, will randomly get the file to read 
2. We will store in a dictionary and based on the game, we will compute the interface.
3. If we have X, then it will be a disabled entry point 
4. If we have an operation than this will be an entry with the respective operation and with a grey entry
5. For the numbers we will proceed as follows:
   5a. There will be a label list to show the user what numbers he can enter
   5b. A dictionary of entries with the index of the entry and the entry
   5c. A list of the labels where we store the labels which we present what numbers are available
6. In case another number is used or a wrong number is used we give a message that the number is not correct or not supposed to be in another entry
7. In case the number is correct, we complete the entry and make the number on the labelframe green.
8. Number will be added with a check button which needs to be pressed by the user after the entry. In order to enter just a single square , when something is entered, we have a condition to check just a single entry.
8. We will introduce the value entered in a list of used numbers and also delete it from the list of numbers which needs to be used. Also, we will destroy that label, so that it will not appear anymore in the label of numbers
9. If everything is completed, we print a message that the game is finished and also update the frame label with a success message
