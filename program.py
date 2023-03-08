import fileinput

# This function reads the file and returns a list with the lines
lines = []
for line in fileinput.input():
    lines.append(line)


def rc4(key, plaintext):
  S = bytearray(range(256))
  key_length = len(key)
  out = bytearray()

  #KSA
  j = 0
  for i in range(256):
    j = (j + S[i] + key[i % key_length]) % 256
    S[i], S[j] = S[j], S[i]

  #PRGA
  i = j = 0
  for char in plaintext:
    i = (i + 1) % 256
    j = (j + S[i]) % 256
    S[i], S[j] = S[j], S[i]
    out.append(char ^ S[(S[i] + S[j]) % 256])
  return out

llave = bytes(lines[0].rstrip('\n'),'utf-8')
textoClaro = bytes(lines[1].rstrip('\n'),'utf-8')

print(rc4(llave, textoClaro).hex().upper())



'''tests = [[b"Key",b"Plaintext"],[b"Wiki",b"pedia"],[b"Secret",b"Attack at dawn"]]
for test in tests:
  print(rc4(test[0],test[1]).hex())'''