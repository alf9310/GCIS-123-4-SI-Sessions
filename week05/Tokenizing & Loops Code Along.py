"""
Bring cookies to class and have the students make the following functions.
@author Audrey Fuller
@author Zoe Bingham (cookie code)
"""
def give_cookie(name, number):
    print("Giving " + str(number) + " cookies to " + name)

def loop_example(cookies_given):
    cookies_total = 42
    for cookies_eaten in range(0, cookies_total, cookies_given):
        name = input("Input person recieving cookie's name: ")
        if( cookies_total - cookies_eaten < cookies_given):
            cookies_given = cookies_total - cookies_eaten
            give_cookie(name, cookies_total - cookies_eaten)
        else:
            give_cookie(name, cookies_given)
        print("Cookies left is " + str(cookies_total-cookies_eaten-cookies_given))
    """
    while( cookies_total > cookies_eaten):
        name = input("Input person recieving cookie's name: ")
        if( cookies_total - cookies_eaten < cookies_given):
            give_cookie(name, cookies_total - cookies_eaten)
            cookies_eaten += cookies_total - cookies_eaten
        else:
            give_cookie(name, cookies_given)
            cookies_eaten += cookies_given
        print("Cookies left is " + str(cookies_total-cookies_eaten))
        """

def main():
    loop_example(5)

if __name__ == '__main__':
    main()