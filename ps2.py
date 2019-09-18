def Cloning(li1):
    li_copy = li1[:]
    return li_copy


# Function to calculate sum of each row
def row_sum(matrix):
    sum1 = 0
    sum2 = 0
    sum3 = 0

    # print("\nFinding Sum of each row:\n")

    # finding the row sum

    sum1 = matrix[0] + matrix[1] + matrix[2]
    sum2 = matrix[3] + matrix[4] + matrix[5]             # adding row elemnt
    sum3 = matrix[6] + matrix[7] + matrix[8]

            # Print the row sum
    # print("Sum of the row 1 =", sum1)
    # print("Sum of the row 2 =", sum2)
    # print("Sum of the row 3 =", sum3)

        # Reset the sum
    # sum = 0


# Function to calculate sum of each column
def column_sum(matrix):
    sum4 = 0
    sum5 = 0
    sum6 = 0

    # print("\nFinding Sum of each column:\n")
    # print("\nFinding Sum of each diagonal:\n")

    # finding the row sum

    sum4 = matrix[0] + matrix[3] + matrix[6]
    sum5 = matrix[1] + matrix[4] + matrix[7]          # adding coloumn element
    sum6 = matrix[2] + matrix[7] + matrix[8]

            # Print the row sum
    # print("Sum of the column 1 =", sum4)
    # print("Sum of the column 2 =", sum5)
    # print("Sum of the column 3 =", sum6)
while(1):
    # label1: check
    game=int(input("Enter 1 : game \n 2 : exit"))
    if(game==1):
        count=0
        print (u'Welcome to the Game!')
        # Initialize matrix
        matrix = [0,0,0,0,0,0,0,0,0]
        list1 = [1,3,5,7,9]
        list2 = [2,4,6,8]
        play=int(input("Enter player 1 or 2 :"))
        if(play==1):
            play1=Cloning(list1)
            play2=Cloning(list2)       # cloning the list to player
            print("Player1 turn")
            print("player 1 can add [1,3,5,7,9] numbers only")
            print("player 2 can add [2,4,6,8] numbers only")
        elif(play==2):
            play1=Cloning(list2)
            play2=Cloning(list1)           # cloning the list to player
            print("player2 turn")
            print("player 2 can add [1,3,5,7,9] numbers only")
            print("player 1 can add [2,4,6,8] numbers only")
        else:
            print("wrong choice")
        while(21):
            #int(play1)
            cede=int(input("Enter 1 to exit else for play"))
            if(cede==1):
                print("Bye")
                exit()

            pos=int(input("Enter the position :"))        # Enter the location
            num=int(input("Enter the number :"))
            # if(play ==
            # for i in range(3):		 # A for loop for row entries  # A for loop for column entries
            #     a =[]
            #     for j in range(3):
            #         z=i+j
            #         if (z == pos):
            #             print("hello1")
            #             a.insert(num)
            #     matrix.append(a)
            # print("hello")
            # print(matrix)
            # For printing the matrix
            # for i in range(3):
            # 	for j in range(3):
            # 		print(matrix[i][j], end = ' ')
            # 	print()
            count+=1
            for i in range(9):
              if (i==pos):
                matrix[i-1]=num

            # print( matrix)
            print(matrix[0:3])
            # print("\n")
            print(matrix[3:6])
            # print("\n")
            print(matrix[6:9])
            # print("\n")


            # for i in range(3):
            # 	for j in range(3):
            # 		print(matrix[i][j], end = ' ')
            # 	print()
            # Get each row sum
            row_sum(matrix)

            # Get each column sum
            column_sum(matrix)
            sum1 = matrix[0] + matrix[1] + matrix[2]
            sum2 = matrix[3] + matrix[4] + matrix[5]
            sum3 = matrix[6] + matrix[7] + matrix[8]
            sum4 = matrix[0] + matrix[3] + matrix[6]
            sum5 = matrix[1] + matrix[4] + matrix[7]
            sum6 = matrix[2] + matrix[7] + matrix[8]
            sum7 = matrix[0] + matrix[4] + matrix[8]
            sum8 = matrix[2] + matrix[4] + matrix[6]
            # print(sum8)
            list1 = [sum1, sum2, sum3, sum4, sum5, sum6, sum7, sum8]
            print((list1[0]))
            if(count==10):
                print("Match draw")
                exit()
            if(count%2==0):
                print("Player1 turn")
            else:
                print("Player2 turn")
            for i in list1:

                if (i == 15):
                    print("Element Exists and you win")
                    if(count%2==0 and play == 1):
                        print("Player2 wins")
                        # exit()
                        # goto check
                    elif(count%2==0 and play == 2):
                        print("Player1 wins")
                        # exit()
                        # goto check
                    elif (count % 2 != 0 and play == 2):
                        print("Player2 wins")
                        # exit()
                        # goto check
                    elif (count % 2 != 0 and play == 1):
                        print("Player1 wins")
                        # exit()
                        # goto check
    elif(game==2):
        print("Goodbye")
        exit()
    else:
        print("Enter valid choice")