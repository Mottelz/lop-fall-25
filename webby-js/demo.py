def a(x, y):
	print(f"hello {x} {y(10)}")
	print(f"hello {x} {y}")


def b(l):
	return l*2

def c(m):
	return m+5

a("Mottel", lambda z: 5*z)
a("Jeff", b)

print(c(10))
print(b(10))

print(f"b(c(10)): {b(c(10))}")
print(f"c(b(10)): {c(b(10))}")
print(f"b(b(10)): {b(b(10))}")
print(f"c(c(10)): {c(c(10))}")

