import os
import glob


assignment = "Assignment1"
file_names = glob.glob(f"{os.path.join(os.getcwd(),assignment)}/ex*")
# Now you can process each file
output = open(f"{assignment}/FlückigerManuel_PalapurackalDeepak_{assignment}.py","w")
for file_name in file_names:
    with open(file_name, "r") as file:
        # Read the contents of the file or perform any other actions
        content = file.read()
        output.write("# ")
        output.write(os.path.basename(file_name))
        output.write("\n")
        output.write(content)
        output.write("\n")
