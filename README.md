# Statistical Predictive Text Models

This is one of the first projects that I ever did as a Computer Science student, and it remains one of my favorites. The project implements a model for a body of text, that can read text from the contents of a file, and can write its own contents to a new file in its directory. It also has a predictive classification feature, where you can take two texts from named authors and a third from an unnamed author, and it will predict which of the two names authors it was more likely to come from. Included in this repo is the code for both the text models as well as a driver for usage without a shell, and a bunch of test files that I used to test the program. Specifically, as an example, I tested the program with texts from Harry Potter and from Romeo and Juliet, which are stored in the files "rowlingtest.txt' and "shakespearetest.txt." The file "rowlingsample.txt" contains a different excerpt from Harry Potter, and the program is able to correctly classify the third file as being from JK Rowling and not Shakespeare. A demonstration of the program's execution using these files from the commandline is copied and pasted below. Other texts used in testing are included in this repo, containing texts from CNN and Fox News and from "Friends" and "The Office."

## Example Usage:

(base) matthew@Matthews-MacBook-Air FINALPROJECT copy % python3 driver.py

First file author name: jkr

Would you like to read this text from a file or from a previous model? [1] for file, [2] for model: 1

First file: rowlingtest.txt

Second file author name: ws

Would you like to read this text from a file or from a previous model? [1] for file, [2] for model: 1

Second file: shakespearetest.txt

Would you like to read your test text from a file or from a previous model? [1] for file, [2] for model: 1

Test file name: sample.txt

scores for jkr : [-1300.183, -416.442, -1276.082, -46.931, -8.987]



scores for ws : [-1326.248, -422.103, -1299.216, -53.377, -43.526] 



This test file is more likely to have come from jkr

Would you like to save any of these models? Select any of 1, 2, 3, or 0 for none: 1 2

(base) matthew@Matthews-MacBook-Air FINALPROJECT copy % python3 driver.py

First file author name: jkr

Would you like to read this text from a file or from a previous model? [1] for file, [2] for model: 2

Second file author name: ws

Would you like to read this text from a file or from a previous model? [1] for file, [2] for model: 2

Would you like to read your test text from a file or from a previous model? [1] for file, [2] for model: 1

Test file name: sample.txt

scores for jkr : [-1300.183, -416.442, -1276.082, -46.931, -8.987] 



scores for ws : [-1326.248, -422.103, -1299.216, -53.377, -43.526] 



This test file is more likely to have come from jkr

Would you like to save any of these models? Select any of 1, 2, 3, or 0 for none: 0

