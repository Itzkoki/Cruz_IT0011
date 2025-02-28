#1.) Set
set_a = {"a", "b", "c", "d", "f", "g" }
set_b = {"b", "c", "h", "l", "m", "o"}
set_c = {"c", "d", "f", "h", "i", "j", "k"}

#A. How many elements are there in set A and B
print("How many elements are there in set A and B")
print(len(set_a | set_b))

#B. How many elements are there in B that is not part of A and C
print("How many elements are there in B that is not part of A and C")
print(len(set_b - (set_a | set_c)))

#C. Show the following using set operations
print("i.", (sorted(set_c - set_a ))) #[h, i, j, k]
print("ii.", (sorted(set_a & set_c)))#[c, d, f]
print("iii.", (sorted(set_b & (set_a | set_c))))#[b, c, h]
print("iv.", (sorted({"d", "f"} & (set_a | set_c) - set_b)))#[d, f]
print("v.", (sorted(set_b & set_a & set_c)))#[c]
print("vi.", (sorted(set_b - (set_a | set_c))))#[l, m, o]

