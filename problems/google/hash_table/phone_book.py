"""
Task
Given  names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each  queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for  is not found, print Not found instead.






Sample Input

3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry
Sample Output

sam=99912222
Not found
harry=12299933


"""


n = int(input())
phone_book = {}
for i in range(n):
    entry = input()
    name, number = entry.split()
    phone_book[name] = number

for i in range(n):
    search = input()
    if search in phone_book:
        print(f'{search}={phone_book[search]}')
    else:
        print('Not found')
