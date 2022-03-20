# Repeat words n times
def make_repeater_of(n):

    # The word to repeat to
    def repeat(my_string):
        assert type(my_string) == str , "Only words allowed"
        return my_string*n
    return repeat


def make_division_by(denom):
    def divide(num):
        assert type(num) == float , "Only numbers allowed"
        return num/denom
    return divide

def run():
    # Use a closure with variable `rep`
    #rep = make_repeater_of(6)
    #print(rep("ThisLine"))

    ref = make_division_by(7.3)
    print(ref(3.2))


if __name__ == "__main__":
    run()