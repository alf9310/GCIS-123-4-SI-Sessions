"""
Bring cookies to class and have the students make the following functions.
@author Audrey Fuller
@author Zoe Bingham (cookie code)
"""
def give_cookie(name, number):
    print("Giving " + name + " " + str(number) + " cookie(s)...\n")


def loop_example():
    cookies = 32
    cookies_eaten = 0
    while cookies_eaten < cookies:
        give_cookie(input("Who wants a cookie?\n"), 2)
        cookies_eaten += 2


def tokenize(string):
    tokens = string.split(" ")
    print(tokens[1])
    for token in tokens:
        print(token) 


def main():
    loop_example()
    #tokenize("Hi There! How Are You?")

if __name__ == '__main__':
        main()