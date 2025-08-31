class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] #decide what the stack is going to hold 
        #sort position and speed, in reverse order (highest position first)
        # pos_speed = list(zip(position,speed))
        indexed = list(enumerate(position))
        print(indexed)
        sortedPosition = (sorted(indexed, key = lambda item: item[1],))
        sortedPosition.reverse()
        print(sortedPosition)
        for i in range(len(sortedPosition)):
            ind = sortedPosition[i][0]
            pos = sortedPosition[i][1]
            curspeed = speed[ind]
            time = (target-pos)/curspeed
            if stack and time <= stack[-1]:
                pass 
            else:
                stack.append(time)
            print(stack)

        return len(stack)
