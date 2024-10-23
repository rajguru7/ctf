d = 15207104768003369637467501018769019066441123663573224946995853553786946901639349019074978411515804733114437924556767552516628401494127697247742779899612209459576094083952838339489561213954536260133838854607149657913730400730767338999438413642404157298963818796141295663453926314825621643270204711245117220247252238615145044742605874419094565211843802760886563769079790325747008002903568257668219503067254244453526995584207530139227058164506701918736505501124344526196358992217672802175438442762565237095756065738818837945132163423342019242575625255083659981512692179453909274547729923246722373013393206687129855205833 # Your d value
n = 17442167786986766235508280058577595032418346865356384314588411668992021895600868350218184780194110761373508781422091305225542546224481473153630944998702906444849200685696584928947432984107850030283893610570516934680203526010120917342029004968274580529974129621496912684782372265785658930593603142665659506699243072516516137946842936290278268697077045538529685782129547539858559544839323949738223228390505139321940994534861711115670206937761214670974876911762247915864144972967596892171732288160028157304811773245287483562194767483306442774467144670636599118796333785601743172345142463479403997891622078353449239584139# Your n value
# cipher_path = '../crypto-adveRSAry/intercepted'

# Read the ciphertext from file
# with open(cipher_path, 'rb') as f:
#     ciphertext = int.from_bytes(f.read(), byteorder='big')

ciphertext_bytes = b'w\n\xa3\xcb\xc2\xe1pjx\x867\x1cn\xc3\x9dB\x02?\xb2\x99\x8a\xb8-9;C\xa4\xb8\xfc\xc3\xca\xfe\x8e\x1e\xa1\xf5\xec[Rn&\xbb\x8b\n\xaf\x83^[P\xf9\x8c\xd5\x95~\xa7\xcb \xb0\x85Vfdu\x9d\xf5\xe4mXe\x95t\x96V\xe2\xcau\xe1\x90\x8cA/\xb1\xf3,\xa8\x04\xb9\xcf\x8fPXf\x0ffg\x8e>C\xc7\x12\xa3F\x04\x1a\t\xc2e\xdb\xc1\xf1iJ\x9e"+\x0b\x9d\xc2{\xe9\x1b\xbfN^\xb1\x14\xc3\xbfv\xeb\x90\xcd\xc7oi\xcc\x8fKQ\xdevy\x86$\x88\xca\xd6\xa9\xe3~\xd1g=ry\xf3\xcb\x85\xb7\xfa\xe1\xe0T\x8b\xcf\x18\xa0\xc3\x15\x15T\x82\xb1\xa16\xbcF\x06\xeb\x9d\xb5\xa4\x80$\x19f\x91\xb5\x8a\xe6\xe0\xf6Iu\x84\x87\xc6\xece\xf5\xfc\xd5D\xd6M\xe4knU\x06\xed\xa3\xdf^V\xc06h\xae\x9c\x89\x96V\xbe@\xf8m\xe0$\x11\x9d\xd9\xe2\xdb\x8an\xaa}\xce:\xa8C\x93\xb6O6\x07\xaf\xfb\x05\xb7}\xad\xdf\xd5%'  # Replace with your actual byte string
ciphertext = int.from_bytes(ciphertext_bytes, byteorder='big')

print(ciphertext)

# Decrypt the ciphertext
plaintext = pow(ciphertext, d, n)

# Convert the plaintext from int back to bytes
plaintext_bytes = plaintext.to_bytes((plaintext.bit_length() + 7) // 8, byteorder='big')

# print(plaintext_bytes.decode('utf-8'))
print(plaintext_bytes)