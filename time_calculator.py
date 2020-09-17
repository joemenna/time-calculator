# Accept user input for start, duration and optional week
# Turn input into a 24 hour time 
# add duration to start time and give result
# allow the result to show whether the and time is the next day or number of days after

def add_time(start, duration, day = 0):
    Days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday', 'Sunday']
    #break apart inputs
    start, period = start.split()
    hour, minutes = start.split(':')
    dHours, dMin = duration.split(':')

    #convert to 24 hour time
    if len(hour) < 2:
        hour = hour.zfill(2)
    if 'PM' in period:
        hour = int(hour) + 12
    
    #add duration
    TotalHours = (int(hour) + int(dHours))
    TotalMinutes = int(minutes) + int(dMin)
    if TotalMinutes > 60:
        TotalMinutes = TotalMinutes % 60
        TotalHours = TotalHours + 1
    new_hours = TotalHours % 24
    if new_hours > 12:
        new_hours = new_hours - 12
        period = 'PM'
    elif new_hours == 12:
        period = 'PM'
    elif new_hours == 0:
        new_hours = new_hours + 12
        period = 'AM'
    else:
        period = 'AM'
    if len(str(TotalMinutes)) < 2:
        TotalMinutes = str(TotalMinutes).zfill(2)
        
    
    # how many days after
    dayAfter = TotalHours // 24
    dayAfter1 = ''
    if dayAfter == 1:
        dayAfter1 = '(next day)'
    elif dayAfter > 1:
        dayAfter1 = '(' + str(dayAfter) + ' days later)'
    





    new_time = str(new_hours) + ':' + str(TotalMinutes) + ' ' + period + ' ' + dayAfter1

    if dayAfter == 0:
        new_time = str(new_hours) + ':' + str(TotalMinutes) + ' ' + period

    if day != 0:
        day = day.lower()
        day = day.capitalize()
        day = Days.index(day)
        if dayAfter == 0:
            day = Days[day]
            new_time = str(new_hours) + ':' + str(TotalMinutes) + ' ' + period + ',' + ' ' + str(day)
        else:
            new_days = (dayAfter + day) % 7
            new_days = Days[new_days]
            new_time = str(new_hours) + ':' + str(TotalMinutes) + ' ' + period + ',' + ' ' + new_days + ' ' + dayAfter1



    return new_time
