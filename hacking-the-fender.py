# password.csv
'''
Username,Password
jean49,Da*E%OuGuc9$V1m
haydenashley,l$r^9eGg8f@BZhy
michaelastephens,$1sp++bga8H+eCr
denisephillips,Vj)T7AsfRHkfpvw
andrew24,T^mH8LMM&0C3VVk
kaylaabbott,!nN05pv3tc(DBO(
tmartinez,V46_Xx85_gKg7rt
mholden,(sd44x3x*A7D1dA
randygilbert,A7+E0YfB+MLPJ8Z
watsonlouis,i!4(DEkBLNq)C7G
mdavis,c$2VXHnxQ+6ifpx
patrickprice,Es_r0GlF&zDkJKG
kgriffith,%0dUpqgwFfA$Dma
hannasarah,c(9au%x)tyC#HDd
xaviermartin,e7!gWemxlde3K6p
hrodriguez,od@9P!dfQj8NH&A
erodriguez,hB+4A(si*vdHl4c
danielleclark,2lv3HKAs+Or8R48
timothy26,oz7ExOUI2&*S87h
elizabeth19,x3C8yYtI!(e3+z(
'''

import csv
import json

compromised_users = []

with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)
  for row in password_csv:
    password_row = row
    compromised_users.append(password_row['Username'])

with open('compromised_users.txt', 'w') as compromised_user_file:
  for compromised_user in compromised_users:
    compromised_user_file.write(compromised_user)

with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {
    'recipient': 'The Boss',
    'message': 'Mission Success'
  }
  json.dump(boss_message_dict, boss_message)
  
with open('new_passwords.csv', 'w') as new_passwords_obj:
  slash_null_sig = '''
  _  _     ___   __  ____             
  / )( \   / __) /  \(_  _)            
  ) \/ (  ( (_ \(  O ) )(              
  \____/   \___/ \__/ (__)             
  _  _   __    ___  __ _  ____  ____  
  / )( \ / _\  / __)(  / )(  __)(    \ 
  ) __ (/    \( (__  )  (  ) _)  ) D ( 
  \_)(_/\_/\_/ \___)(__\_)(____)(____/ 
          ____  __     __   ____  _  _ 
  ___   / ___)(  )   / _\ / ___)/ )( \
  (___)  \___ \/ (_/\/    \\___ \) __ (
        (____/\____/\_/\_/(____/\_)(_/
  __ _  _  _  __    __                
  (  ( \/ )( \(  )  (  )               
  /    /) \/ (/ (_/\/ (_/\             
  \_)__)\____/\____/\____/

  '''
new_passwords_obj.write(slash_null_sig)
