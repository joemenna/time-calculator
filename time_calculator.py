# Accept user input for start, duration and optional week
# Turn input into a 24 hour time 
# add duration to start time and give result
# allow the result to show whether the and time is the next day or number of days after
Days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
start = []
duration = []
times = []
per = ''
mil = ''
def add_time(start, duration, day = None):
    #break apart inputs
    start = start.split()
    per = start[1]
    times = str(start[0]).replace(':','')
    if len(times) < 4:
        times = times.zfill(len(times) + 1)
    if 'P' in per:
        mil
    #duration = duration.split(':')
    


    #convert to 24 hour time
    #shour = int(shour) + 12

    #add duration
    #new_time = shour + int(dhour)



    new_time = print(per) 




    return new_time