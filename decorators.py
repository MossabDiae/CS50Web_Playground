# Original script: https://cs50.harvard.edu/web/2020/notes/2/#decorators
# Edited by Mossab Diae (github : @mossaybo)
# Instead of using the Syntactic sugar for decorators, hello function
# will be generated "manually" by calling the announce function and 
# passing lambda function to it.
# more about lambda functions : https://cs50.harvard.edu/web/2020/notes/2/#lambda-functions

def announce(f):
    def wrapper():
        print("about to run the function...")
        f()
        print("Done running function")
    return wrapper

hello = announce(lambda : print("hello mossab"))

#@announce
#def hello():
#    print("hello world")

hello()