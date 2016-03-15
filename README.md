# -Pothi

The program takes 'keyword' as a input and stream tweets. After streaming it forms a cache of most recently used words and then according to the problem the score is updated in every 30 
seconds. I made a function named 'update_score' which execute in every 30 seconds and check if a word in cache is repeated again in the spam of 1 minute or not. If not then it reduces its
score by 1 and if yes then it continues checking other words. Also, it checks if the score of a word is 0 or not and if it is 0 then it deletes that word. After updatation I made a 
function 'print_score' which prints the word and its score in cache after every 1 minute.
To execute the code, we have to give an input i.e. keyword and the program will give output i.e most recently used words and its score.
