#!/usr/bin/env python
# coding: utf-8

# In[10]:


import requests, os
from bs4 import BeautifulSoup
#from OpenSSL import crypto ###pyopenssl is installed
#import ssl
#print (SSl.OPENSSL_VERSION);
#print (dir(requests));

# --- Specify explicit cert/file location if needed ---
#dir = "/Users/jack/PycharmProjects/YN/"
outfilename = "output" #set the filename for the outfile if using beautyfulsoup html.parser

# --- Start the script ---
print ("Starting Script...\n" + "Locating Cert and Key files...");
cert_file_path = "SUDCert.pem" #dir + "Cert.pem"
print (cert_file_path + " file found at: " + str(os.path.dirname(os.path.realpath(cert_file_path))) + "\\" + cert_file_path);

key_file_path = "SUDKey.pem" #dir + "Key.pem"
print (key_file_path + " file found at: " + str(os.path.dirname(os.path.realpath(key_file_path))) + "\\" +  key_file_path);

# --- Uncomment/add to specify connection point ---
url = "https://erst-apitest.virk.dk/sud-ws/"
#url = "https://erstpreprod.virk.dk/ri/showMe"
#url = "/pogo-webservices/entitetsopslag/findLoginprofilViaUidOgIdp"
print ("Connecting to: " + url);

# --- Setup headers, cert and payload for the connection ---
headers = {'user-agent': 'SUD_test'}
params = {"key_a": "value_b"}
cert = (cert_file_path, key_file_path)

# --- Connect and prettify the content / write to new file ---
try:
    r = requests.post(url, headers=headers, params=params, cert=cert, verify=False)
except requests.exceptions.RequestException as e:  # This is the correct syntax
    print ("\nAn exception was caught: \n" + str(e));
    
#soup = BeautifulSoup(r.content)
soup = BeautifulSoup(r.content, "html.parser")

# --- print returned and sent repsonse and headers ---
print ("\nHeaders: "); print (r.headers);

#option to output html as text or write to file.
#print ("\nContent: "); print (r.content);#(soup.prettify());
print ("\nContent: "); print ("Dowloaded as file to: " + str(os.path.dirname(os.path.realpath(cert_file_path))) + "\\" +  outfilename + ".html");
with open(outfilename + ".html", "w", encoding='utf-8') as file:
    file.write(str(soup))
    
print ("\nStatus Code (is empty except for code 200): "); print (r.status_code, "STATUS CODE");

print ("\n" + "Requests repsonse: " + str(r));

print ("\nResponse history (is empty except for code 200, all codes to complete request, in order): "); print (r.history); #Response objects that were created in order to complete the request. The list is sorted from the oldest to the most recent response.

print ("\nResponse: "); print (r.raw);





###test to see if connection should be done explicitly specifying protocol.

# import ssl
# from urllib3.poolmanager import PoolManager
#
# from requests.adapters import HTTPAdapter
#
#
# class Ssl3HttpAdapter(HTTPAdapter):
#     """"Transport adapter" that allows us to use SSLv3."""
#
#     def init_poolmanager(self, connections, maxsize, block=False):
#         self.poolmanager = PoolManager(
#             num_pools=connections, maxsize=maxsize,
#             block=block, ssl_version=ssl.PROTOCOL_SSLv3)


# In[ ]:




