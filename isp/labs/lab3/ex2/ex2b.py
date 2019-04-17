import hashlib

HashPass = [None]*10
HashPass = [
"6055ceef808c47562f6d1a3fcd03a32150bd4cbe95a63e360de248ee951f24ac",
"09df158d9b624fd7b160814293fda8360a165f23965a28f979a4b9fd63fe7ac3",
"527f218de70270669f19cdff07d408966dd2897cd36510f62992a73b1bb78d0e",
"76b54ca16278c21f3c1ed8675742f5856ae89f289f626d93136c07bdce29e51c",
"2c009ca2a665dd533a975aba825d495f0a738f92e1951d8336f43186bc117435",
"fc8adb79bf5ff31dcb0c0a90fe559244eb9f6f22c4f859a8520bd51a81e7e9fa",
"1cd788994b26fa850933bb1af49b85b9361ab2045d48cb1b6a39d2c91ef46f88",
"446775fdc6447ea1bf38ed8bc74c50c25a26a0461ff9f0a0dd1162ed5ac51cec",
"5d025a2f482be7b9f5174c7fb70e2c7c8095b5531f6ec417c54d659a9308ecf2",
"a114a42647423909528f954ae316eed6d5676627ee3505314d28c1cf4a48cc67"
]

assert(len(HashPass) == 10)

AnswerPass = []

with open("rockyou.txt", errors = 'ignore') as f:
    content = f.readlines()

content = [x.strip() for x in content]

count = 0

for word in content:

  if (count == 10):
    print(AnswerPass)
    break

  WordtoHash = word
  BytestoHash = WordtoHash.encode('utf-8')
  hash_object = hashlib.sha256(BytestoHash)
  u = hash_object.hexdigest()
  for passw in HashPass:
    if (u == passw):
      s = set(AnswerPass)
      if WordtoHash in s:
        print("Word is already there.")
      else:
        AnswerPass.append(WordtoHash)
        print(WordtoHash)
        count = count + 1


  ##########   Code to be Later Commented Out
  WordtoHash = WordtoHash.title()
  BytestoHash2 = WordtoHash.encode('utf-8')
  hash_object2 = hashlib.sha256(BytestoHash2)
  u = hash_object2.hexdigest()
  for passw in HashPass:
    if (u == passw):
      s = set(AnswerPass)
      if WordtoHash in s:
        print("Word is already there.")
      else:
        AnswerPass.append(WordtoHash)
        print(WordtoHash)
        count = count + 1
  #########

  S = list(WordtoHash)
  for t in range(0, len(S)):
    if (S[t] == 'e'):
      S[t] = '3'
  WordtoHash = ''.join(S)
  BytestoHash3 = WordtoHash.encode('utf-8')
  hash_object3 = hashlib.sha256(BytestoHash3)
  u = hash_object3.hexdigest()
  for passw in HashPass:
    if (u == passw):
      s = set(AnswerPass)
      if WordtoHash in s:
        print("Word is already there.")
      else:
        AnswerPass.append(WordtoHash)
        print(WordtoHash)
        count = count + 1

  S = list(WordtoHash)
  for t in range(0, len(S)):
    if (S[t] == 'o'):
      S[t] = '0'
  WordtoHash = ''.join(S)
  BytestoHash4 = WordtoHash.encode('utf-8')
  hash_object4 = hashlib.sha256(BytestoHash4)
  u = hash_object4.hexdigest()
  for passw in HashPass:
    if (u == passw):
      s = set(AnswerPass)
      if WordtoHash in s:
        print("Word is already there.")
      else:
        AnswerPass.append(WordtoHash)
        print(WordtoHash)
        count = count + 1

  S = list(WordtoHash)
  for t in range(0,len(S)):
    if (S[t] == 'i'):
      S[t] = '1'
  WordtoHash = ''.join(S)
  BytestoHash5 = WordtoHash.encode('utf-8')
  hash_object5 = hashlib.sha256(BytestoHash5)
  u = hash_object5.hexdigest()
  for passw in HashPass:
    if (u == passw):
      s = set(AnswerPass)
      if WordtoHash in s:
        print("Word is already there.")
      else:
        AnswerPass.append(WordtoHash)
        print(WordtoHash)
        count = count + 1

print(AnswerPass)

#Note: to get all passwords, we have to first run this code once (get 9 password matches)
#and then comment out the block of code between # # to get the 10'th password!
