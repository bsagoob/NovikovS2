def max_meetings(start, end):
    meetings = list(zip(start, end))

    meetings.sort(key=lambda x: x[1])

    current_end_time = 0
    count = 0
    
    for meeting in meetings:
        if meeting[0] >= current_end_time:
            count += 1
            current_end_time = meeting[1] 
    
    return count

def main():
    n = int(input("Введите количество встреч: "))    start = list(map(int, input("Введите время начала встреч: ").strip().split()))
    end = list(map(int, input("Введите время окончания встреч: ").strip().split()))

    result = max_meetings(start, end)
    print(result)

if __name__ == "__main__":
    main()

