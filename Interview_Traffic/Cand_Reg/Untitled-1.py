
import datetime
data = [{"id":1,"available_start_date":"2021-03-24T06:00:00Z","available_end_date":"2021-03-24T10:00:00Z"}]
start_u = datetime.datetime.strptime(data[0]['available_start_date'],'%Y-%m-%dT%H:%M:%SZ')
stop_u = datetime.datetime.strptime(data[0]['available_end_date'],'%Y-%m-%dT%H:%M:%SZ')
start_time = start_u.time().isoformat()
stop_time = stop_u.time().isoformat()
slot_time = datetime.timedelta(hours=1)
date = start_u.date()
days = []
if date == stop_u.date():
    hours1 = []
    time = datetime.datetime.strptime(start_time, '%H:%M:%S')
    end = datetime.datetime.strptime(stop_time, '%H:%M:%S')
    while time  < end:
        hours1.append(time.strftime("%H:%M:%S"))
        time += datetime.timedelta(hours=1)
    print(hours1)


    
