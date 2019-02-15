# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.


def addUptoK(listOfNumbers, k):
    # Create a hashmap / dictionary of all the numbers in the list
    dictOfNumbers = {}
    for i in listOfNumbers:
        dictOfNumbers[i] = i

    # For every key in the dictionary check if a key2 with the value of K minus key1 exists
    for key in dictOfNumbers.keys():
        print key
        if k-key in dictOfNumbers.keys():
            print key, k-key
            return True


print(addUptoK([1,2,3, 8, 9, 11, 12], 21))