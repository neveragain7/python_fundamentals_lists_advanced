number_of_rooms_in_the_building = int(input())

chairs_are_enough = True
total_chairs = 0
total_visitors = 0

for room in range(1, number_of_rooms_in_the_building + 1):
    chairs_list = input().split()
    current_chairs = len(chairs_list[0])
    current_visitors = int(chairs_list[1])

    total_chairs += current_chairs
    total_visitors += current_visitors

    difference = current_visitors - current_chairs
    if difference > 0:
        print(f"{difference} more chairs needed in room {room}")
        chairs_are_enough = False

if chairs_are_enough:
    more_chairs = total_chairs - total_visitors
    print(f"Game On, {more_chairs} free chairs left")
