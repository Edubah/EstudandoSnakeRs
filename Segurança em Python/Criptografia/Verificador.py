import phonenumbers
from phonenumbers import geocoder


phone = input('Digite o telefone no formato +552140022922: ')
phone_number = phonenumbers.parse(phone) #Ele fara o número digitado pelo usuário passar na biblioteca de Phonenumbers e convertidaa números de tel

print(geocoder.description_for_number(phone_number, 'pt'))