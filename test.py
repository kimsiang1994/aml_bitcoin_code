import blocksci
import pandas as pd
import numpy as np
from openpyxl import load_workbook

chain = blocksci.Blockchain("/home/user_cl/workplace_cl/blocksci_made_data_bk_up_2/btc_config_2.json")

# print(chain.blocks[392617])

for i in chain.blocks[392617].txes:
    print(i.index)

# for i in chain.blocks: 
#     print(i)
    

# Testing code
# address = chain.address_from_index(127471408, blocksci.address_type.pubkeyhash).address_string
# try:
#     # address = chain.address_from_index(0x85c84c949b1c29c85b777f2873a19450dbb1a057, blocksci.address_type.pubkeyhash).address_string
#     print(address)
# except: 
#     print("error received")

# How you get address from pure hash
# chain.address_from_string("1GHVNnysiqVQPNMpjyFv6mNjNA8UjzXki5")
# try:
#     address = chain.address_from_string("1GHVNnysiqVQPNMpjyFv6mNjNA8UjzXki5").address_string
#     print(address)
# except: 
#     print("error received")

# Testing functionality
# address = chain.address_from_string("1GHVNnysiqVQPNMpjyFv6mNjNA8UjzXki5")
# print(address.first_tx)
# address.has_been_spent
# address.input_txes_count()
# for i in address.inputs: 
#     print(i)

# Trying to see if we can export values
# df = pd.DataFrame({'address_string': [address]})
# df.to_excel("output.xlsx") 

# How you get address from pure hash
# chain.address_from_string("1GHVNnysiqVQPNMpjyFv6mNjNA8UjzXki5")
