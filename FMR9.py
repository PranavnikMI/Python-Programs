import functools

CheckEven = lambda No : (No % 2 == 0)
Increase = lambda No : No+2
Add = lambda A,B : A+B

# Task : Name of function
# Elements : List of data elements
def filterX(Task, Elements):
    Result = []
    for no in Elements:
        if(Task(no) == True):
            Result.append(no)
    return Result

# Task : Name of function
# Elements : List of data elements
def mapX(Task,Elements):
    Result = []
    for no in Elements:
        Ret = Task(no)
        Result.append(Ret)
    return Result

def main():
    Data = []
    
    print('Enter number of elements : ')
    Size = int(input())

    print("Enter the elments : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)
    
    print("Input data : ",Data)

    output = list(filterX(CheckEven,Data))
    print("Output after filter : ",output)
    
    moutput = list(mapX(Increase,output))
    print("Output after map : ",moutput)

    Sum = int(functools.reduce(Add,moutput))
    print("Output after reduce : ",Sum)


if __name__ == "__main__":
    main()