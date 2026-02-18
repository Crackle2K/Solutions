plaintext, ciphertext, secret = input(), input(), input()
mapping = {}
ans = ""
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

for i in range(len(ciphertext)):
    mapping[ciphertext[i]] = plaintext[i]

if len(mapping) == 26:
    missing_c = [c for c in chars if c not in mapping][0]
    missing_p = [c for c in chars if c not in mapping.values()][0]
    mapping[missing_c] = missing_p

for letter in secret:
    ans += mapping.get(letter, ".")

print(ans)
