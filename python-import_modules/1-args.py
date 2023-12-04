from sys import argv

num_args = len(argv) - 1  # Subtract 1 to exclude the script name
args_list = argv[1:]

if num_args == 0:
    print("0 arguments.")
else:
    print("{} {}:".format(num_args, "argument" if num_args == 1 else "arguments"))
    for i, arg in enumerate(args_list, start=1):
        print("{}: {}".format(i, arg))