words_dict={}

# the strings come in binary enconding, decode it to UTF-8
# create the dictionary of words mappings
# 11111 a     -> 11111: a
# 11112 aa    -> 11112: aa
# ...            ...
# 12255 anita -> 12255: anita
# ...
for line in wordlist.iter_lines():
   line = line.decode('UTF-8')
   if line != "" and str(line)[0].isdigit():
      words_dict.update({line.split("\t")[0]:line.split("\t")[1]})
#print(words_dict)         

out=""

while rolls > 0:
   response = requests.get(url, headers=header_content)
   if response.status_code == 200:
      data = json.loads(json.dumps(response.json()))
   else:
      print("Error getting random numbers!")
      print("HTTP: " + str(response.status_code))
      exit(response.status_code)
   i=0
   index=0
   # interested in the first digit for the retuned numbers
   # other cool ways to get a digit would be to add the digits
   # until only one remains
   # e.g. 4 + 2 + 4 = 10; 1+0 = 1
   #      4 + 6 + 8 + 6 + 0 = 24; 2 + 4 = 6
   # "data": [424, 46860, 63139, 5946, 62605, 64827]
   for num in data['data']:
      num_i = str(num)[-1]
      print(num_i)
      num_i = int(num_i)
      # if digit is larger than 6 then take modulus 6
      if num_i > 6:
         num_i = num_i % 6
      if num_i == 0:
         num_i = 6
      # build the index by adding the digit*(10^i)
      index = index + num_i*(10**i)
      i=i+1
   index = str(index)
   print(words_dict[index])
   out = out + words_dict[index].title()
   rolls = rolls - 1
print(out)
