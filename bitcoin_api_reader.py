import requests
import json
import pandas as pd
import numpy as np
import openpyxl

# Generic functions
def format_json(json_object): 
    text = json.dumps(json_object, sort_keys=True, indent=4)
    return(text)

def create_python_object_from_json(json_object): 
    python_object = json.loads(json_object)
    return(python_object)

def convert_pd_to_excel(dictionary, name): 

    df = pd.Dataframe(dictionary)

    batch_name = "output_" + str(name) +".xlsx"

    df.to_excel(batch_name)

# Block functions
def get_raw_block_data(block_hash):

    api_front = "https://blockchain.info/rawblock/"
    full_api = api_front + str(block_hash)
    # print(full_api)

    response = requests.get(full_api)

    return(response.json())

def get_block_hash_list(): 
    df = pd.read_excel('formatted_blockhash_list.xlsx')
    mylist = df['block_hash'].tolist()

    return(mylist)

def store_raw_block_data(block_hash_list):

    hash_list = []
    ver_list = []
    prev_block_list = []
    mrkl_root_list = []
    time_list = []
    bits_list = []
    nonce_list = []
    n_tx_list = []
    size_list = []
    block_index_list = []
    main_chain_list = []
    height_list = []
    received_time_list = []
    relayed_by_list = []
    tx_list = []
    
    for i in block_hash_list:
        # Just trying to make sure that the code is actually running 
        print(i)
        block_output = get_raw_block_data(i)
        formatted_block_output = format_json(block_output)
        block_object_output = create_python_object_from_json(formatted_block_output)

        hash_list.append(block_object_output['hash'])
        ver_list.append(block_object_output['ver'])
        prev_block_list.append(block_object_output['prev_block'])
        mrkl_root_list.append(block_object_output['mrkl_root'])
        time_list.append(block_object_output['time'])
        bits_list.append(block_object_output['bits'])
        nonce_list.append(block_object_output['nonce'])
        n_tx_list.append(block_object_output['n_tx'])
        size_list.append(block_object_output['size'])
        block_index_list.append(block_object_output['block_index'])
        main_chain_list.append(block_object_output['main_chain'])
        height_list.append(block_object_output['height'])
        # received_time_list.append(block_object_output['received_time'])
        # relayed_by_list.append(block_object_output['relayed_by'])
        tx_list.append(block_object_output['tx'])

    block_dictionary = {'hash': hash_list, 
        'ver': ver_list, 
        'prev_block': prev_block_list, 
        'mrkl_root': mrkl_root_list, 
        'time': time_list, 
        'bits': bits_list, 
        'nonce': nonce_list, 
        'n_txn': n_tx_list, 
        'size': size_list, 
        'block_index': block_index_list, 
        'main_chain': main_chain_list, 
        'height': height_list, 
        # 'received_time': received_time_list,
        # 'relayed_by': relayed_by_list, 
        'txn': tx_list
        }

    return(block_dictionary)

# Address functions
def get_raw_address_data(address_hash):

    api_front = "https://blockchain.info/rawaddr/"
    full_api = api_front + str(address_hash)
    # print(full_api)

    response = requests.get(full_api)

    return(response.json())

def get_address_from_excel_list(): 
    df = pd.read_excel('pirateat40_data_aml_2.xlsx')
    mylist = df['transaction_address'].tolist()

    return(mylist)

def store_raw_address_data(address_list):

    hash160_list = []
    address_list = []
    n_tx_list = []
    n_unredeemed_list = []
    total_received_list = []
    total_sent_list = []
    final_balance_list = []
    tx_list = []
    
    for i in address_list:
        # Just trying to make sure that the code is actually running 
        print(i)
        address_output = get_raw_address_data(i)
        formatted_address_output = format_json(address_output)
        address_object_output = create_python_object_from_json(formatted_address_output)

        hash160_list.append(address_object_output['hash160'])
        address_list.append(address_object_output['address'])
        n_tx_list.append(address_object_output['n_tx'])
        n_unredeemed_list.append(address_object_output['n_unredeemed'])
        total_received_list.append(address_object_output['total_received'])
        total_sent_list.append(address_object_output['total_sent'])
        final_balance_list.append(address_object_output['final_balance'])
        tx_list.append(address_object_output['txs'])

    address_dictionary = {'hash160':  hash160_list, 
        'address': address_list, 
        'n_tx': n_tx_list, 
        'n_unredeemed': n_unredeemed_list, 
        'total_received': total_received_list, 
        'total_sent': total_sent_list, 
        'final_balance': final_balance_list, 
        'txn': tx_list
        }

    return(address_dictionary)

# Transactions functions
def get_raw_transaction_list_from_blocks(block_dictionary): 

    txn_list = []

    for i in block_dictionary.get('tx'): 
        for j in i: 
            txn_list.append(j)
    
    return(txn_list)

def get_raw_transaction_list_from_address(address_dictionary): 

    txn_list = []

    for i in address_dictionary.get('txs'): 
        for j in i: 
            txn_list.append(j)

    return(txn_list)

def get_raw_transaction_data(txn_hash):

    api_front = "https://blockchain.info/rawtx/"
    full_api = api_front + str(txn_hash)
    # print(full_api)

    response = requests.get(full_api)

    return(response.json())

def store_raw_transaction_data(txn_list):

    hash_list = []
    ver_list = []
    vin_sz_list = []
    vout_sz_list = []
    lock_time_list = []
    size_list = []
    block_height_list = []
    tx_index_list = []
    inputs_list = []
    out_list = []
    
    for i in txn_list:
        # Just trying to make sure that the code is actually running 
        print(i)
        txn_output = get_raw_transaction_data(i)
        formatted_txn_output = format_json(txn_output)
        txn_object_output = create_python_object_from_json(formatted_txn_output)

        hash_list.append(txn_object_output['hash'])
        ver_list.append(txn_object_output['ver'])
        vin_sz_list.append(txn_object_output['vin_sz'])
        vout_sz_list.append(txn_object_output['vout_sz'])
        lock_time_list.append(txn_object_output['lock_time'])
        size_list.append(txn_object_output['size'])
        block_height_list.append(txn_object_output['block_height'])
        tx_index_list.append(txn_object_output['tx_index'])
        inputs_list.append(txn_object_output['inputs'])
        out_list.append(txn_object_output['out'])        

    txn_dictionary = {'hash':  hash_list, 
        'ver': ver_list, 
        'vin_sz': vin_sz_list, 
        'vout_sz': vout_sz_list, 
        'lock_time': lock_time_list, 
        'size': size_list, 
        'block_height': block_height_list, 
        'tx_index': tx_index_list, 
        'inputs': inputs_list, 
        'out': out_list
        }

    return(txn_dictionary)


# Scripts
# Testing block api
block_input = "00000000000000000009293e762758c4d9eb0ef11574f42eb3599d2040269bf4"
block_output = get_raw_block_data(block_input)
formatted_block_output = format_json(block_output)
block_object_output = create_python_object_from_json(formatted_block_output)

# Actual block functions
list_of_block_hash = get_block_hash_list()
block_dictionary = store_raw_block_data(list_of_block_hash)
convert_pd_to_excel(block_dictionary, "block_dictionary")

# Testing address api
address_input = "17piFVhBrJpj1FGeYgGpDUjrtXcP5sQpvn"
address_output = get_raw_address_data(address_input)
formatted_address_output = format_json(address_output)
address_object_output = create_python_object_from_json(formatted_address_output)

# Actual address functions
# Ponzi address info
list_of_addresses = get_address_from_excel_list()
ponzi_address_dictionary = store_raw_address_data(list_of_addresses)
convert_pd_to_excel(ponzi_address_dictionary, "ponzi_address_dictionary")

# Actual txn functions
block_transaction_list = get_raw_transaction_list_from_blocks(block_dictionary)
ponzi_transaction_list = get_raw_transaction_list_from_address(ponzi_address_dictionary)

stored_block_txn_data = store_raw_transaction_data(block_transaction_list)
convert_pd_to_excel(stored_block_txn_data, "stored_block_txn_data")
stored_ponzi_txn_data = store_raw_transaction_data(ponzi_transaction_list)
convert_pd_to_excel(stored_ponzi_txn_data, "stored_ponzi_txn_data")

# Prints for tests
# print(address_object_output["address"])
# print(block_object_output["height"])
# print(list_of_block_hash)
# print(block_dictionary.get('height'))