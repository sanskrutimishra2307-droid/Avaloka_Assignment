def can_attend_all(events):
    """True if no two events overlap. Touching events (end == start) are fine."""
    events = sorted(events)                      # sort by start time
    for i in range(1, len(events)):
        if events[i][0] < events[i - 1][1]:      # next starts before previous ends
            return False
    return True


def min_rooms_required(events):
    """Minimum number of rooms so every event can run at the same time as others."""
    starts = sorted(e[0] for e in events)
    ends = sorted(e[1] for e in events)

    rooms = 0        # rooms in use right now
    max_rooms = 0    # the most we ever needed at once
    j = 0            # pointer into ends

    for s in starts:
        if s >= ends[j]:     # an earlier meeting has finished -> reuse its room
            j += 1
        else:                # nobody has finished yet -> need a new room
            rooms += 1
        max_rooms = max(max_rooms, rooms)
    return max_rooms


if __name__ == "__main__":
    print(can_attend_all([(9, 10), (10, 11), (11, 12)]))   # True
    print(can_attend_all([(9, 11), (10, 12)]))             # False
    print(min_rooms_required([(9, 10), (10, 11), (11, 12)]))        # 1
    print(min_rooms_required([(9, 12), (10, 11), (10, 13), (12, 14)]))  # 3
    print(min_rooms_required([]))                          # 0
