def main():
    ## Calculate the average and total of the numbers in a file.
    total = 0
    counter = 0
    foundFlag = True
    try:
        infile = open("Numbers.txt", 'r')
    except FileNotFoundError:
        print("File not found.")
        foundFlag = False
    if foundFlag:
        try:
            for line in infile:
                counter += 1 
                total += float(line)