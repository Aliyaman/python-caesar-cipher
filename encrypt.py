from string import ascii_letters
kelime = "word" #enter your text here to encrypt without using space
key = 7 # enter your key here key must be between 1 and 25
harfler = []
enc_msg = []
decrypt = []
mesaj = []

def caesar(harf,key):
  enc = harf + key
  encmsg = enc_msg.append(ascii_letters[enc].lower())
  

for harf in kelime:
  harfler.append(harf)
  
for i in harfler:
  k = int(ascii_letters.index(i))
  caesar(k,key)

print(f"şifreli mesaj: {"".join(enc_msg)}") 
