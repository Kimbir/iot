def find_floor_entrance(room):
    floors = 8
    entrance = 4
    entrance = (room - 1) // (floors) + 1
    floor = floors - (room - 1) % floors
    print(floor, entrance)
room = int(input())
find_floor_entrance(room)
