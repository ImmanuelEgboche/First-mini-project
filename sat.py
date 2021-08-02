try:
    with open("crash.txt","r") as f:
        file = f.read()
    print(file)
except Exception as e:
    print("Thats not right" + str(e))