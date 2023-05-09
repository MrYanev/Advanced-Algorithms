myList = [] #Iniciates an empty list to store the elements to be sorted
lowest = 0  #Variable to store the element with lowest value

def selection_sort(myList): #Iniciating the sortation finction which takes myList as input
    for i in range(len(myList) - 1):    #For loop to go over all elements
        lowest = i  #The lowest value is being stored to the variable
        for j in range(i + 1, len(myList)): #New for loop to go over the rest of the elemets
            if myList[j] < myList[lowest]:  #Check whether the new elemt is lower than the lowest so far
                lowest = j  #If lower overwite the old one 
        myList[i], myList[lowest] = myList[lowest], myList[i]  #Swap the possitions 
    print(myList)
    return myList   #Returns the sorted list

selection_sort([3, 5, 7, 1, 2, 4, 8, 6, 9])