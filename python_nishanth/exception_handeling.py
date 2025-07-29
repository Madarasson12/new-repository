list =["one","two","three","four"]
print(list[0])
try:
    print(list[6])
except Exception as e:
        print("An error occurred:", e)
print("this is the last line")