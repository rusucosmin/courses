import hashlib

SaltHashPass = [
  ("ae", "f4ff98e367309505eeea669d511ff149ce079f22c8c786b3716c3b240842846a"),
  ("69", "4ddd5afa17bf71021f9282e7bfa0af1d7154a6aaed4b0945097d1f3013887542"),
  ("d9", "c109a0cc0e391f96e27a0e0e85dcc4694446396a89eebb5ac92f3cfd7b96586d"),
  ("fc", "a88bb8ff790bffdcb0fb7b11f62204f6e32c8996676ca81e1d06069afec07601"),
  ("c4", "c20d04edeef343e7e5bf2d556385d142010a975f5de7953ad5678288a350dfba"),
  ("62", "2aae063183a42cc09b1a5e3af90b1f96674054de8f7484ff1b3e202bd655850c"),
  ("94", "e496a24a601f3e16cd64262863018d74668d784c4b653b06b210f4dfdc0492ab"),
  ("68", "674cfb9c3c8924a13c6244062739f19cbc50f04ef5af73dcb9489731e02304ff"),
  ("c1", "07e3f176b5231f8046904d41c15ac53d73ce5c1343621790edfa166bb0047460"),
  ("68", "2faef52a631b567689b64d766083564495fcd9aac56c95fa797d6dd432462245")
]

assert(len(SaltHashPass) == 10)

AnswerPass = []

with open("rockyou.txt", errors = 'ignore') as f:
    content = f.readlines()

content = [x.strip() for x in content]

count = 0

for SaltHashPair in SaltHashPass:
  for word in content:
    word2 = word + SaltHashPair[0]
    BytestoHash = word2.encode('utf-8')
    hash_object = hashlib.sha256(BytestoHash)
    u = hash_object.hexdigest()
    if (u == SaltHashPair[1]):
      AnswerPass.append(word)
      count = count + 1
      if (count == 10):
        print (AnswerPass)
        break

print (AnswerPass)

