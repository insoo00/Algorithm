def get_duration(start, end):
    start_hour, start_min = map(int, start.split(":"))
    end_hour, end_min = map(int, end.split(":"))
    
    return (end_hour*60+end_min) - (start_hour*60+start_min)
    
    
def change(x): #음 치환
    exc = {'C#':'1','D#':'2', 'F#':'3', 'G#':'4', 'A#':'5', 'B#': '6'}
    for k, v in exc.items():
        x = x.replace(k, v)
    return x

def solution(m, musicinfos):
    answer = ''
    musicinfos.sort(key=lambda x: get_duration(x.split(",")[0], x.split(",")[1]), reverse=True)
    for musicinfo in musicinfos:
        print(musicinfo)
        start, end, title, info = musicinfo.split(",")
        duration = get_duration(start, end)
        print(duration)
        info = change(info)
        duration_info = ''
        idx = 0

        for _ in range(duration):
            if idx == len(info):
                idx = 0
            duration_info += info[idx]
            idx += 1

        if change(m) in duration_info:
            answer = title
            break
            
    if answer == '':
        return '(None)'
    return answer
