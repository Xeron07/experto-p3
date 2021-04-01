def sum_of_odd_ii(n):
    for i in range(0,n):
        x=int(input())
        y=int(input())
        sum=0
        if(x>y):
            x,y=y,x
        x=x+1
        for i in range(x,y):
            if i%2 !=0:
                sum = sum + i
                i=i+1
        print(sum)

sum_of_odd_ii(7)