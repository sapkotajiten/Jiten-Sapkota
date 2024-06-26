class Solution: 
    def toh(self, N, fromm, to, aux):
        # Base case: If there is only one disk to move, move it directly from 'fromm' to 'to'
        if N == 1: 
            print("move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to)) 
            return 1 # Return 1 move made

        # Recursive case: Move N-1 disks from 'fromm' to 'aux', using 'to' as an auxiliary rod
        moves = self.toh(N-1, fromm, aux, to) # Recursive call

        # Move the remaining largest disk from 'fromm' to 'to'
        print("move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to)) 
        moves += 1 # Increment the total moves count for the current step
    
        # Recursive call: Move the N-1 disks from 'aux' to 'to', using 'fromm' as an auxiliary rod
        moves += self.toh(N-1, aux, to, fromm) # Recursive call

        return moves # Return the total moves made for this step and all recursive steps 

# Create an instance of the Solution class
s = Solution() 

# Test the method with 1 disk
print(s.toh(1, 1, 3, 2))
