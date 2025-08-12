251. Flatten 2D Vector

Description
Design an iterator to flatten a 2D vector. It should support the next and hasNext operations.

Implement the Vector2D class:
Vector2D(int[][] vec) initializes the object with the 2D vector vec.
next() returns the next element from the 2D vector and moves the pointer one step forward. You may assume that all the calls to next are valid.
hasNext() returns true if there are still some elements in the vector, and false otherwise.

Example 1:

Input
["Vector2D", "next", "next", "next", "hasNext", "hasNext", "next", "hasNext"]
[[[[1, 2], [3], [4]]], [], [], [], [], [], [], []]
Output
[null, 1, 2, 3, true, true, 4, false]

Explanation
Vector2D vector2D = new Vector2D([[1, 2], [3], [4]]);
vector2D.next();    // return 1
vector2D.next();    // return 2
vector2D.next();    // return 3
vector2D.hasNext(); // return True
vector2D.hasNext(); // return True
vector2D.next();    // return 4
vector2D.hasNext(); // return False
=====================================================================
class Vector2D:
    def __init__(self, vec):
        self.vec = vec       
        self.i = 0          
        self.j = 0   
        self._forward()
        
    def _forward(self):
        while self.i < len(self.vec) and self.j >= len(self.vec[self.i]):
            self.i += 1
            self.j = 0

    def next(self):
        self._forward()
        val = self.vec[self.i][self.j]
        self.j += 1
        return val

    def hasNext(self):
        self._forward()
        return self.i < len(self.vec)

    

n=int(input("Enter number of commands: "))
commands=input("Enter Commands: ").split()
vec_input = input("Enter 2D list: ").strip()
vec = [list(map(int, row.split())) for row in vec_input.split(',')]

obj = None
output = []
for cmd in commands:
    if cmd == "Vector2D":
        obj = Vector2D(vec)
        output.append("null")
    elif cmd == "next":
        output.append(obj.next())
    elif cmd == "hasNext":
        output.append(obj.hasNext())
print("Output:", output)
=============================================================================
Enter number of commands: 8
Enter Commands: Vector2D next next next hasNext hasNext next hasNext
Enter 2D list: 1 2,3,4
Output: ['null', 1, 2, 3, True, True, 4, False]
