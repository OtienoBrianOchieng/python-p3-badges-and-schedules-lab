def badge_maker(name):
    message = (f"Hello, my name is {name}.")
    return message

def batch_badge_creator(names):
    badges = [f"Hello, my name is {name}." for name in names]
    return badges

def assign_rooms(names):
    room_assignments = []

    for index, name in enumerate(names, start=1):
        room_assignment = f"Hello, {name}! You'll be assigned to room {index}!"
        room_assignments.append(room_assignment)
    return room_assignments

def printer(names):
    badges = batch_badge_creator(names)
    rooms = assign_rooms(names)

    for badge in badges:
        print (badge)
    for room in rooms:
        print (room)

