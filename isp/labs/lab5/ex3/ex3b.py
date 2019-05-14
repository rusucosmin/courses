import requests
from phe import paillier

features = [0] * 12

public_key, private_key = paillier.generate_paillier_keypair()

encrypted_number_list = [public_key.encrypt(x) for x in features]
encrypted_input = [x.ciphertext() for x in encrypted_number_list]

r = requests.post("http://com402.epfl.ch/hw5/ex3/securehealth/prediction_service",
      json = {
        'email': 'cosmin.rusu@epfl.ch',
        'pk': public_key.n,
        'encrypted_input': encrypted_input,
        'model': 2
      })

encrypted_prediction = r.json()['encrypted_prediction']

prediction = private_key.decrypt(paillier.EncryptedNumber(public_key, encrypted_prediction))

b = prediction
print("b =", b)

W = [0] * 12
for i in range(12):
  features = [0] * 12
  features[i] = 1
  encrypted_number_list = [public_key.encrypt(x) for x in features]
  encrypted_input = [x.ciphertext() for x in encrypted_number_list]
  r = requests.post("http://com402.epfl.ch/hw5/ex3/securehealth/prediction_service",
      json = {
        'email': 'cosmin.rusu@epfl.ch',
        'pk': public_key.n,
        'encrypted_input': encrypted_input,
        'model': 2
      })

  encrypted_prediction = r.json()['encrypted_prediction']

  prediction = private_key.decrypt(paillier.EncryptedNumber(public_key, encrypted_prediction))
  W[i] = prediction - b
  print("W[", i, "] =", W[i])

print("W = ", W)
print("b = ", b)

r = requests.post('http://com402.epfl.ch/hw5/ex3/get_token_2',
      json = {
        'email': 'cosmin.rusu@epfl.ch',
        'weights': W,
        'bias': b
      })

print(r.json())
