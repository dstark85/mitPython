iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count)
    iteration += 1

# Output: Iteration 0; count is 12. Iteration 1; count is 24
count = 0
for iteration in range(5):
    letter = 0
    end = len("hello, world")
    while letter < end:
        count += 1    
    print("Iteration " + str(iteration) + "; count is: " + str(count)
      
