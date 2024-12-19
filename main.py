places = """66845   37619
94793   99076
76946   36179
27374   48777
47847   92154
83270   97857
19354   94331
69716   58559"""

column_1 = []
column_2 = []

places = places.splitlines()

for place in places:
    part = place.split()
    column_1.append(part[0])
    column_2.append(part[1])

column_1_str = " ".join(column_1)
column_2_str = " ".join(column_2)
suma = 0
