import requests
from phe import paillier

r = requests.post("http://com402.epfl.ch/hw5/ex3/get_input",
      json = {'email': 'cosmin.rusu@epfl.ch'})

response = r.json()

public_key, private_key = paillier.generate_paillier_keypair()

features = response['x']

encrypted_number_list = [public_key.encrypt(x) for x in features]
encrypted_input = [x.ciphertext() for x in encrypted_number_list]

r = requests.post("http://com402.epfl.ch/hw5/ex3/securehealth/prediction_service",
      json = {
        'email': 'cosmin.rusu@epfl.ch',
        'pk': public_key.n,
        'encrypted_input': encrypted_input,
        'model': 1
      })

encrypted_prediction = r.json()['encrypted_prediction']

prediction = private_key.decrypt(paillier.EncryptedNumber(public_key, encrypted_prediction))

r = requests.post("http://com402.epfl.ch/hw5/ex3/get_token_1",
      json = {
        'email': 'cosmin.rusu@epfl.ch',
        'prediction': prediction})

print(r.json())

