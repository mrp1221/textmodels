from finalproject import TextModel

# Get inputs from user
auth1 = input("First file author name: ")
check1 = int(input("Would you like to read this text from a file or from a previous model? [1] for file, [2] for model: "))
if check1 == 1:
    file1 = input("First file: ")
    source1 = TextModel(auth1)
    source1.add_file(file1)
else:
    source1 = TextModel(auth1)
    source1.read_model()
auth2 = input("Second file author name: ")
check2 = int(input("Would you like to read this text from a file or from a previous model? [1] for file, [2] for model: "))
if check2 == 1:
    file2 = input("Second file: ")
    source2 = TextModel(auth2)
    source2.add_file(file2)
else:
    source2 = TextModel(auth2)
    source2.read_model()

check3 = int(input("Would you like to read your test text from a file or from a previous model? [1] for file, [2] for model: "))
if check3 == 1:
    file3 = input("Test file name: ")
    source3 = TextModel("This test file")
    source3.add_file(file3)
else:
    name = input("Model name: ")
    source3 - TextModel(name)
    source3.read_model()

models = [source1, source2, source3]

# Classify
source3.classify(source1, source2)
saves = input("Would you like to save any of these models? Select any of 1, 2, 3, or 0 for none: ")
if "0" not in saves:
    for save in saves.split():
        models[int(save) - 1].save_model()