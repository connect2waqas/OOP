def soxon():
    print("-----------Soxon Robot activated-----------")

    def Room():
        room_length = float(input("Enter roon length: "))
        room_width = float(input("Enter room width: "))
        room_area = room_length * room_width
        return room_area
    
    def Pool():
        pool_length = float(input("Enter pool length: "))
        pool_width = float(input("Enter pool width: "))
        depth = float(input("Enter pool depth: "))
        volume = pool_length * pool_width * depth

        return volume
    
    room_area = Room()
    pool_volume = Pool()

    print(f"I am going to clean room with {room_area} area and pool with {pool_volume} volume")

soxon()