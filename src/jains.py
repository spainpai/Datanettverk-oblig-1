import sys # use for taking input from command line

def jains(givenList):
    
    if len(givenList) == 0:   # checking that list is not empty
        print("Error: list cant consist of 0 values")
    
    else:
        topside = sum(givenList)     # summarises each value in the list (x1 + x2)
        n = len(givenList)   # number of flows = values in list
        botside = sum(values ** 2 for values in givenList) # square of each list value src: https://ioflood.com/blogsquare-in-python/

        jfi = pow(topside, 2) / (n * botside)  # squares top half, divides by flows * squares of value

        return print("Jains Fairness index is: ", jfi) 

# task 1.1

if __name__ == "__main__":
    givenList = sys.argv[1]      # takes in string
    givenList = givenList.strip('][').split(',') # strip removes characters from string, split splits at given character src: https://www.w3schools.com/python/ref_string_strip.asp , https://www.w3schools.com/python/ref_string_split.asp 
    givenList = [int(values) for values in givenList]   # creates new list with integers from the given list to use arithmetically

    jains(givenList)


# task 1.2

if __name__ == "__main__":
    valueFile = "throughput_values.txt"
    try:
        with open(valueFile, "r") as file:      # src : intro to python (2)
            values = [line.strip() for line in file.readlines()]    # creates a list of strings, removes whitespace in list   
    except FileNotFoundError:
        print(f"File'{valueFile}' does not exist")
        sys.exit(1)         # exit w error indication

    newValues = []       # creathe list to insert values into
    for value in values:     # loop through list of values from file
        if "Mbps" in value:
            newValues.append(int(value.split()[0]))
        elif "Kbps" in value:
            newValues.append(int(value.split()[0])/1000) # converts to mbs in calculation as that is the most used measurement in our file 
        else:
            print(f"Invalid input in file, see : '{value}'")
            sys.exit(1)

    jains(newValues)
