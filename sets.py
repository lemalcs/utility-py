# Removes duplicates elements from a list
def remove_duplicates(the_list):
    without_duplicates = []
    for element in the_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates

# Removes duplicate elements from a list fast
def remove_duplicates_fast(the_list):
    return set(the_list)

def run():
    list=[1,2,2,3,4,77,33,33]
    print(remove_duplicates(list))
    print(remove_duplicates_fast(list))


if __name__ == "__main__":
    run()
