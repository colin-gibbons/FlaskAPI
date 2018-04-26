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

prime = subprocess.call("python cli.py is-prime 8")
subprocess.call("python cli.py kv-record Leeeeeeroyyy Jennnnnkinnnnns")
subprocess.call("python cli.py kv-retrieve Leeeeeeroyyy ")

subprocess.call("python cli.py md5 test")
subprocess.call("python cli.py factorial 5")
subprocess.call("python cli.py fibonacci 8")

print("hahahahaha, %r" %(prime))

subprocess.call("python cli.py is-prime 1")
subprocess.call("python cli.py slack-alert test")

#subprocess.call(["/path/to/command", "arg1", "-arg2"])