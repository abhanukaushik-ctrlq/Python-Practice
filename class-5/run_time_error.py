x = 5
print("x is", x)
y = 7
print("y is", y)
x = "hello"
print("now x is", x)
print(x + 10)                 #first x was re-declated as a string called "hello" and now you can't add 10 to a string
print("This line never runs") # the syntax is correct, hence the program is converted to bytecode
                              # but never runs because the running is stopped at the printing of the weird logic.


# this is another run time error, where the score is not defined. so run time.
print("Starting...")
print(score)
print("This never runs")
