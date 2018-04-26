import subprocess

# values = (("A", "B"), ("C", "D"), ("E", "F"))

# command = "python test_input.py"
# for first, second in values: 
#     # lazy use of universal_newlines to prevent the need for encoding/decoding
#     p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, universal_newlines=True)  
#     output, err = p.communicate(input="{}\n{}\n".format(first, second))
#     # stderr is not connected to a pipe, so err is None
#     print(first, second, "->", end="")
#     # we just want the result of the command
#     print(output[output.rfind(" "):-1])

subprocess.call("python cli.py is-prime 8")
subprocess.call("python cli.py kv-record Leeeeeeroyyy Jennnnnkinnnnns")
subprocess.call("python cli.py kv-retrieve Leeeeeeroyyy ")

subprocess.call("python cli.py md5 test")
subprocess.call("python cli.py factorial 5")
subprocess.call("python cli.py fibonacci 8")


subprocess.call("python cli.py is-prime 1")
subprocess.call("python cli.py slack-alert test")
print()
print("Output should match below:")
print()
print("False")
print("False")
print("Jennnnnkinnnnns")
print("098f6bcd4621d373cade4e832627b4f6")
print("120")
print("[0, 1, 1, 2, 3, 5, 8]")
print("False")
print("True")



#subprocess.call(["/path/to/command", "arg1", "-arg2"])