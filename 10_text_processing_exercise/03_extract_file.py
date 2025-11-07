path_file = input().split("\\")

file_name, extension_name = path_file[-1].split(".")

print(f"File name: {file_name}")
print(f"File extension: {extension_name}")
