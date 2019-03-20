import binascii
import hashlib
import asyncio
import websockets
import random

H = 'sha256'
N="EEAF0AB9ADB38DD69C33F80AFA8FC5E86072618775FF3C0B9EA2314C9C256576D674DF7496EA81D3383B4813D692C6E0E0D5D8E250B98BE48E495C1D6089DAD15DC7D7B46154D6B6CE8EF4AD69B15D4982559B297BCF1885C529F566660E57EC68EDBC3C05726CC02FD4CBF4976EAA9AFD5138FE8376435B9FC61D2FC0EB06E3"
g = 2

N = int(N, 16)

def encode_str(s):
  return s.encode()

def encode_int(i):
  buff = i.to_bytes((i.bit_length() + 7) // 8, 'big')
  strToSend = binascii.hexlify(buff).decode()
  return strToSend

def decode_int(msgReceived):
  buff = binascii.unhexlify(msgReceived)
  i = int.from_bytes(buff, 'big')
  return i

def sha256(msg):
  return int(hashlib.sha256(msg.encode('utf-8')).hexdigest(), 16)

def sha256_hex(msg):
  return hashlib.sha256(msg.encode('utf-8')).hexdigest()

assert(decode_int(encode_int(100)) == 100)
assert(decode_int(encode_int(200)) == 200)
assert(decode_int(encode_int(1)) == 1)
print(sha256("Nobody inspects the spammish repetition"))

async def hello():
    async with websockets.connect(
            'ws://com402.epfl.ch/hw2/ws') as websocket:
        U = "cosmin.rusu@epfl.ch"

        await websocket.send(encode_str(U))
        print(f"> U = {U}")

        recv = await websocket.recv()
        salt = decode_int(recv)
        print(f"< salt = {salt}")
        a = random.randint(1, 32)
        A = pow(g, a, N)
        await websocket.send(encode_int(A))
        print(f"> A = {A}")
        recv = await websocket.recv()
        B = decode_int(recv)
        print(f"< B = {B}")
        p = "LQoFCBtOXRcbF1UhRRgTAU8NSA=="
        u = sha256(encode_int(A) + encode_int(B))
        x = sha256(encode_int(salt) + encode_int(sha256(U + ":" + p)))
        S = pow((B - pow(g, x, N) + N) % N, a + u * x, N)
        print(S)
        print(f"> S = {S}")
        snd = encode_int(sha256(encode_int(A) + encode_int(B) + encode_int(S)))
        await websocket.send(snd)
        recv = await websocket.recv()
        print(recv)

asyncio.get_event_loop().run_until_complete(hello())
