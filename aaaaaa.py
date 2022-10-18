
tuition = 8000
for i in range(1, 6):
        tuition *= 1.03
        if i == 1:
            print("In 1 year, the tuition will be $" + str(tuition) + ".")
        else:
            print("In "+str(i)+" years, the tuition will be $" + str(tuition) + ".") 
