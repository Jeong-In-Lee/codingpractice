def solution(people, limit):
    people.sort()
    boat = 0
    left = 0
    right = len(people) - 1
    while left <= right:
        boat += 1
        if (people[right] + people[left]) <= limit:
            left += 1
        right -= 1
    return boat
