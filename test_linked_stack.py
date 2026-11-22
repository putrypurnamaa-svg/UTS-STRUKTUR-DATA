
from linked_stack import LinkedStack

stack = LinkedStack()

print("=== PENGUJIAN LINKED STACK ===")

# Pengujian push
stack.push("A")
stack.push("B")
stack.push("C")

print("Data teratas:", stack.peek())
print("Jumlah data:", stack.size())

# Pengujian pop
print("Data dihapus:", stack.pop())
print("Data teratas sekarang:", stack.peek())

# Pengujian is_empty
print("Apakah stack kosong?", stack.is_empty())
