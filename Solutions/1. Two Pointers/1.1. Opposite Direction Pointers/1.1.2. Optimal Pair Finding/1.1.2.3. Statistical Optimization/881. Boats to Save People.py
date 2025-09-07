from typing import List

def numRescueBoats(people: List[int], limit: int) -> int:
    # initialize variables
    n = len(people)
    a = 0
    b = n - 1
    count = 0
    # sorting enable the greedy approach that counts on [a] and [b] being the two extremities, enabling a opposite direction two pointers approach
    people.sort()
    # traverse the array with the opposite direction two pointers approach
    # make the greedy decision: to pick one or to pick two numbers
    # in each iteration, depending on the sum of the two extremities
    while (a <= b) :
        total = people[a] + people[b]
        # greedy decision making
        if total > limit:
            count += 1
            b -= 1
        else :
            # the sum is less or equal to limit, meaning a valid boat can contain both [a] and [b]
            a += 1
            b -= 1
            count += 1
    return count 

if __name__ == "__main__":
	people1 = [1, 2]
	limit1 = 3
	result1 = numRescueBoats(people1, limit1)
	print(f"Input: people = {people1}, limit = {limit1}")
	print(f"Output: {result1}")
	print()
	
	people2 = [3, 2, 2, 1]
	limit2 = 3
	result2 = numRescueBoats(people2, limit2)
	print(f"Input: people = {people2}, limit = {limit2}")
	print(f"Output: {result2}")
	print()
	
	people3 = [3, 5, 3, 4]
	limit3 = 5
	result3 = numRescueBoats(people3, limit3)
	print(f"Input: people = {people3}, limit = {limit3}")
	print(f"Output: {result3}")
	print()