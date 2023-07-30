# opens a file called my_file.txt and prints the contents
with open("C:/Users/huand/OneDrive/Desktop/100-Days-Of-Code-Python/100DayCourse/Day24/my_file.txt") as file:
    contents = file.read()
    print(contents)


# # Append to my_file.txt using mode="a"
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")


# # Create a new file called hello_world.txt, because it doesn't exist yet, it will create it.
# with open("hello_world.txt", mode="w") as file:
#     file.write("Hello World.")