from typing import List, Dict
def decode_moves(moves:str):
    return moves.split()
def is_valid_face(face: List[List[str]]) -> bool:
    x=face[0][0]
    for row in face:
        for sq in row:
            if sq!=x:
                return False
    return True
def count_colors(face: List[List[str]]) -> Dict[str, int]:
    count={}
    for row in face:
        for sq in row:
            count[sq]=count.get(sq,0)+1
    return count
def  rotate_face(face: List[List[str]], direction: str) -> List[List[str]]:
    if direction == 'CW': 
        for i in range(3):
            for j in range(3):
                new_face[j][2 - i] = face[i][j]
    elif direction == 'CCW':  
        for i in range(3):
            for j in range(3):
                new_face[2 - j][i] = face[i][j]
def print_cube(cube: Dict[str, List[List[str]]]):
     def print_face(face: List[List[str]]):
        return [' '.join(row) for row in face]
     U = print_face(cube['U'])
     D = print_face(cube['D'])
     F = print_face(cube['F'])
     B = print_face(cube['B'])
     L = print_face(cube['L'])
     R = print_face(cube['R'])
     for x in U:
         print('        '+x)
     for i in range(3):
         print(f"{L[i]}   {F[i]}   {R[i]}   {B[i]}")
     for x in D:
         print('        '+x)
def perform_move(cube: Dict[str, List[List[str]]], move: str) -> None:
     if move == "U":
        cube['U'] = rotate_face(cube['U'])
        F1 = cube['F'][0][:]           #used [:] to create a new list and not modify original
        R1 = cube['R'][0][:]
        B1 = cube['B'][0][:]
        L1 = cube['L'][0][:]

        cube['F'][0] = L1
        cube['R'][0] = F1
        cube['B'][0] = R1
        cube['L'][0] = B1
     elif move == "U'":
        for _ in range(3):
            perform_move(cube, "U")
     elif move == "U2":
        for _ in range(2):
            perform_move(cube, "U")


        

    
    
    
