

################################TASK 1

import traceback

#use try, opens the file, will close when done
try:
    with open('diary.txt', 'a') as diary_file:
        
        user_input = input("What happened today? ")  #prompt asks about today
        diary_file.write(user_input + '\n')    #include  newline
        
        #while loop asks until "done for now"
        while user_input != "done for now":
            user_input = input("What else? ")   #continue to ask about day
            diary_file.write(user_input + '\n') #new line

#error 
except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")



    ################################TASK 2
    