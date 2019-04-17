import hashlib

HashPass = [
  "d3ca7d365a945314d2f703b3d3d7d3a884d16687d7bc7d004f83f9a89b8519ef",
  "391039c3a0c36a08817320e290baab2b3b3df4c6e808ecf5e888b04eb8e223f4",
  "69c417793a3f7c500b9aadf24ee45e0bc0300b05f8f0fd3bcafdb37febbe1f10",
  "f9da88b1da81fa092d6a0afb8903353b27c6de5eb7b1fd4746c8ac01d520e07d",
  "856e5b0b9cdae6c5a4d2cea4b694f0dd441e0f1ed25128c2d8c6f105a92f9bc3",
  "d70500ad106ecf24b028765cec5e622f91e73a07a638974919ef555c968b5e64",
  "7a217a29bd591936a9b26602d093df0306d3546d4ab132a3670a9d7e9f246300",
  "f4b3acdd8b1696f47ec80f806a73cd94034a9a072218a48f46d1727175ce0e2e",
  "98992899842aacafb997f67c613faf0a4f621a2dd16c11a5a08572cfb18c406b",
  "05a8d5430009f79fd84a48dc7479ddaf540041132f45b6db1adf80ef513fbd08",
]

assert(len(HashPass) == 10)

PossibleCharacters = []
for x in range(97,123):
  PossibleCharacters.append(chr(x))
for x in range(48, 58):
  PossibleCharacters.append(chr(x))

AnswerPass = []

for x in PossibleCharacters:
  print(x)
  print(AnswerPass)
  for i in PossibleCharacters:
    for j in PossibleCharacters:
      for k in PossibleCharacters:
        StrtoHash = x + i + j + k
        BytestoHash = StrtoHash.encode('utf-8')
        hash_object = hashlib.sha256(BytestoHash)
        u = hash_object.hexdigest()
        for passw in HashPass:
          if (u == passw):
            AnswerPass.append(StrtoHash)
        for l in PossibleCharacters:
          StrtoHash2 = StrtoHash + l
          BytestoHash2 = StrtoHash2.encode('utf-8')
          hash_object2 = hashlib.sha256(BytestoHash2)
          u2 = hash_object2.hexdigest()
          for passw in HashPass:
            if (u2 == passw):
              AnswerPass.append(StrtoHash2)
          for z in PossibleCharacters:
            StrtoHash3 = StrtoHash2 + z
            BytestoHash3 = StrtoHash3.encode('utf-8')
            hash_object3 = hashlib.sha256(BytestoHash3)
            u3 = hash_object3.hexdigest()
            for passw in HashPass:
              if (u3 == passw):
                AnswerPass.append(StrtoHash3)

print(AnswerPass)
