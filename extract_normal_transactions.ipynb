import blocksci
import pandas as pd
import numpy as np

chain = blocksci.Blockchain("/home/user_cl/workplace_cl/blocksci_made_data_bk_up_2/btc_config_2.json")

###### Supplementary functions ######
# Make sure everything is a list
def check_if_list_and_convert(input): 
    return(input)
    # if type(input) != list: 
    #     another_input = []
    #     another_input.append(input)
    #     return(another_input)
    
    # return list(input)

# Testing functions 
# list_for_check = ["a", "b", "c"]
# string_for_check = "check yes Juliet"

# print("check 1")
# print(type(list_for_check))
# print(type(check_if_list_and_convert(list_for_check)))
# print(check_if_list_and_convert(list_for_check))

# print("check 2")
# print(type(string_for_check))
# print(type(check_if_list_and_convert(string_for_check)))

# Make sure all lists are length of 1
def unify_list_length(input):
    # unified_list = []
    
    # if len(input) != 1: 
    #     unified_list.append(input)
    #     return(unified_list)
    
    return input

# Testing functions 
# list_for_check = ["a", "b", "c"]
# print("check 1")
# print(unify_list_length(list_for_check))
# print(len(unify_list_length(list_for_check)))

###### Writing functions to get data from one address ######
# Getting time between sent transactions for account in locktime
def time_between_sent_accounts(address):

    list_of_all_locktimes = []
    list_of_difference_between_locktimes = []
    dictionary_of_transaction_and_locktime = {}
    
    for i in address.input_txes: 
        locktime = i.block_height
        # dictionary_of_transaction_and_locktime[i] = locktime
        list_of_all_locktimes.append(locktime)
    
    # print(list_of_all_locktimes)
    list_of_all_locktimes.sort()
        
    for j in range(len(list_of_all_locktimes)):
        if j == (len(list_of_all_locktimes)-1):
            break
        
        # print(j)
        # print(list_of_all_locktimes[j])
        # print(list_of_all_locktimes[j+1])

        
        time_difference = list_of_all_locktimes[j+1] - list_of_all_locktimes[j]
        # print(time_difference)
        list_of_difference_between_locktimes.append(time_difference)
    
    # print(list_of_difference_between_locktimes)

#     Tests
#     print(list_of_all_locktimes)
#     print(dictionary_of_transaction_and_locktime)
#     print(list_of_difference_between_locktimes)
        
    return list_of_difference_between_locktimes
        
# Testing functions 
# print("time_between_sent_accounts(address)")
# print(time_between_sent_accounts(address))

# Getting minimum time difference between sent transactions
def min_time_difference_between_sent_accounts(address): 
    list_of_time_differences = time_between_sent_accounts(address)

    if len(list_of_time_differences) == 0: 
        return("NA")

    # print(list_of_time_differences)
    # print("minimum")
    # print(min(list_of_time_differences))
    return min(list_of_time_differences)

# Getting maximum time difference between sent transactions
def max_time_difference_between_sent_accounts(address): 
    list_of_time_differences = time_between_sent_accounts(address)

    if len(list_of_time_differences) == 0: 
        return("NA")

    # print(list_of_time_differences)
    # print("minimum")
    # print(min(list_of_time_differences))
    return max(list_of_time_differences)

# Getting average time difference between sent transactions
def average_time_difference_between_sent_accounts(address): 
    list_of_time_differences = time_between_sent_accounts(address)

    if len(list_of_time_differences) == 0: 
        return("NA")

    # print(list_of_time_differences)
    # print("minimum")
    # print(min(list_of_time_differences))
    return sum(list_of_time_differences)/ len(list_of_time_differences)


# Getting time between received transactions for account in locktime
def time_between_received_accounts(address):

    list_of_all_locktimes = []
    list_of_difference_between_locktimes = []
    dictionary_of_transaction_and_locktime = {}
    
    for i in address.output_txes: 
        locktime = i.block_height
        # dictionary_of_transaction_and_locktime[i] = locktime
        list_of_all_locktimes.append(locktime)
    
    # print(list_of_all_locktimes)
    list_of_all_locktimes.sort()
        
    for j in range(len(list_of_all_locktimes)):
        if j == (len(list_of_all_locktimes)-1):
            break
        
        # print(j)
        # print(list_of_all_locktimes[j])
        # print(list_of_all_locktimes[j+1])

        
        time_difference = list_of_all_locktimes[j+1] - list_of_all_locktimes[j]
        # print(time_difference)
        list_of_difference_between_locktimes.append(time_difference)
    
    # print(list_of_difference_between_locktimes)

#     Tests
#     print(list_of_all_locktimes)
#     print(dictionary_of_transaction_and_locktime)
#     print(list_of_difference_between_locktimes)
        
    return list_of_difference_between_locktimes

# Getting minimum time difference between sent transactions
def min_time_difference_between_received_accounts(address): 
    list_of_time_differences = time_between_received_accounts(address)

    if len(list_of_time_differences) == 0: 
        return("NA")

    # print(list_of_time_differences)
    # print("minimum")
    # print(min(list_of_time_differences))
    return min(list_of_time_differences)

# Getting maximum time difference between sent transactions
def max_time_difference_between_received_accounts(address): 
    list_of_time_differences = time_between_received_accounts(address)

    if len(list_of_time_differences) == 0: 
        return("NA")

    # print(list_of_time_differences)
    # print("minimum")
    # print(min(list_of_time_differences))
    return max(list_of_time_differences)

# Getting average time difference between sent transactions
def average_time_difference_between_received_accounts(address): 
    list_of_time_differences = time_between_received_accounts(address)

    if len(list_of_time_differences) == 0: 
        return("NA")

    # print(list_of_time_differences)
    # print("minimum")
    # print(min(list_of_time_differences))
    return sum(list_of_time_differences)/ len(list_of_time_differences)

# Getting time between first and last transaction in locktime
def time_between_first_and_last_transaction(address):
    list_of_all_transactions = [] 
    
    for i in address.txes: 
        list_of_all_transactions.append(i)

    # print(list_of_all_transactions)

    if (len(list_of_all_transactions)) <= 1: 
        return "One or less transactions"
        
    time_difference = list_of_all_transactions[len(list_of_all_transactions)-1].block_height - list_of_all_transactions[0].block_height

    # print(time_difference)

    return time_difference

# Testing functions 
# print("time_between_first_and_last_transaction(address)")
# print(time_between_first_and_last_transaction(address))

# Total number of sent transactions
def total_sent_accounts(address):

    list_of_all_sent_transactions = []
    
    for i in address.input_txes: 
        list_of_all_sent_transactions.append(i)
        
    return len(list_of_all_sent_transactions)

# Testing functions 
# print("total_sent_accounts(address)")
# print(total_sent_accounts(address))


# Total number of received transactions
def total_received_accounts(address):

    list_of_all_received_transactions = []
    
    for i in address.output_txes: 
        list_of_all_received_transactions.append(i)
        
    return len(list_of_all_received_transactions)

# Testing functions 
# print("total_received_accounts(address)")
# print(total_sent_accounts(address))

# Total number of transactions
def total_number_of_transactions(address):
    
    sum_of_transactions = total_received_accounts(address) + total_sent_accounts(address)
    
    return(sum_of_transactions)

# Testing functions 
# print("total_number_of_transactions(address)")
# print(total_number_of_transactions(address))

# Total number of unique addresses from which account sent transactions
def total_unique_sent_accounts(address):

    list_of_all_sent_transactions = []
    set_of_all_unique_addresses_sent_to = set()
    
    for i in address.input_txes: 
        list_of_all_sent_transactions.append(i)
        
    for j in list_of_all_sent_transactions: 
        for k in j.outputs:
            set_of_all_unique_addresses_sent_to.add(k.address)
        
    return len(list(set_of_all_unique_addresses_sent_to))

# Testing functions 
# print("total_unique_sent_accounts(address)")
# print(total_unique_sent_accounts(address))

# Total number of unique addresses from which account received transactions
def total_unique_received_accounts(address):

    list_of_all_received_transactions = []
    set_of_all_unique_addresses_received = set()
    
    for i in address.output_txes: 
        list_of_all_received_transactions.append(i)
        
    for j in list_of_all_received_transactions: 
        for k in j.inputs:
            set_of_all_unique_addresses_received.add(k.address)
        
    return len(list(set_of_all_unique_addresses_received))

# Testing functions 
# print("total_unique_received_accounts(address)")
# print(total_unique_received_accounts(address))

# Minimum value received
def minimum_received_value(address):
    list_of_received_values = [] 
    
    for i in address.outputs: 
        list_of_received_values.append(i.value/ (10 ** 8))
        
    if (len(list_of_received_values)) == 0: 
        return "List is empty"
    
    return min(list_of_received_values)

# Testing functions 
# print("minimum_received_value(address)")
# print(minimum_received_value(address))

# Maximum value received
def maximum_received_value(address):
    list_of_received_values = [] 
    
    for i in address.outputs: 
        list_of_received_values.append(i.value/ (10 ** 8))
        
    if (len(list_of_received_values)) == 0: 
        return "List is empty"
    
    return max(list_of_received_values)

# Testing functions 
# print("maximum_received_value(address)")
# print(maximum_received_value(address))

# Average value received
def average_received_value(address):
    list_of_received_values = [] 
    
    for i in address.outputs: 
        list_of_received_values.append(i.value/ (10 ** 8))
        
    if (len(list_of_received_values)) == 0: 
        return "List is empty"
    
    return sum(list_of_received_values)/len(list_of_received_values)

# Testing functions 
# print("average_received_value(address)")
# print(average_received_value(address))

# Total value received
def total_received_value(address):
    list_of_received_values = [] 
    
    for i in address.outputs: 
        list_of_received_values.append(i.value/ (10 ** 8))
        
    if (len(list_of_received_values)) == 0: 
        return "List is empty"
    
    return sum(list_of_received_values)

# Testing functions 
# print("total_received_value(address)")
# print(total_received_value(address))

# Minimum value sent
def minimum_sent_value(address):
    list_of_sent_values = [] 
    
    for i in address.inputs: 
        list_of_sent_values.append(i.value/ (10 ** 8))
        
    if (len(list_of_sent_values)) == 0: 
        return "List is empty"
    
    return min(list_of_sent_values)

# Testing functions 
# print("minimum_sent_value(address)")
# print(minimum_sent_value(address))

# Maximum value sent
def maximum_sent_value(address):
    list_of_sent_values = [] 
    
    for i in address.inputs: 
        list_of_sent_values.append(i.value/ (10 ** 8))
        
    if (len(list_of_sent_values)) == 0: 
        return "List is empty"
    
    return max(list_of_sent_values)

# Testing functions 
# print("maximum_sent_value(address)")
# print(maximum_sent_value(address))

# Average value received
def average_sent_value(address):
    list_of_sent_values = [] 
    
    for i in address.inputs: 
        list_of_sent_values.append(i.value/ (10 ** 8))
        
    if (len(list_of_sent_values)) == 0: 
        return "List is empty"
    
    return sum(list_of_sent_values)/len(list_of_sent_values)

# Testing functions 
# print("average_sent_value(address)")
# print(average_sent_value(address))

# Total value received
def total_sent_value(address):
    list_of_sent_values = [] 
    
    for i in address.inputs: 
        list_of_sent_values.append(i.value/ (10 ** 8))
        
    if (len(list_of_sent_values)) == 0: 
        return "List is empty"
    
    return sum(list_of_sent_values)

# Testing functions 
# print("total_sent_value(address)")
# print(total_sent_value(address))

# Account balance
def account_balance(address): 
    
    return address.balance(-1)

# Testing functions 
# print("account_balance(address)")
# account_balance(address)

# Account creation time 
def account_creation_time(address): 
    
    list_of_all_transactions = [] 
    
    for i in address.txes: 
        list_of_all_transactions.append(i.block_height)
    
    if len(list_of_all_transactions) == 0: 
        return("NA")

    return min(list_of_all_transactions)

# Testing functions 
# print("account_creation_time(address)")
# print(account_creation_time(address))

# Account active duration (perceived as time between first and last transaction)
def account_active_duration(address): 
    
    list_of_all_transactions = [] 
    
    for i in address.txes: 
        list_of_all_transactions.append(i.block_height)
    
    if (len(list_of_all_transactions) <= 0): 
        return("1 or less transactions found")
    
    return max(list_of_all_transactions) - min(list_of_all_transactions)

# Testing functions 
# print("account_active_duration(address)")
# print(account_active_duration(address))

def gini_coefficient_accounts_received(address):

    if (total_number_of_transactions(address) == 0):
        return("NA")

    return total_received_accounts(address)/total_number_of_transactions(address)

def gini_coefficient_accounts_sent(address):
    if (total_number_of_transactions(address) == 0):
        return("NA")
    return total_sent_accounts(address)/total_number_of_transactions(address)

def gini_coefficient_value_received(address):
    if (type((total_received_value(address))) != int): 
        return("NA")
    
    if (type((total_sent_value(address))) != int): 
        return("NA")

    sum = total_received_value(address)+total_sent_value(address)

    if (sum == 0):
        return("NA")

    else:
        return total_received_value(address)/sum

def gini_coefficient_value_sent(address):
    if (type((total_sent_value(address))) != int): 
        return("NA")
    
    if (type((total_sent_value(address))) != int): 
        return("NA")

    sum = total_received_value(address)+total_sent_value(address)

    if (sum == 0):
        return("NA")

    return total_sent_value(address)/sum

# Testing functions
# print(gini_coefficient_accounts_received(address))
# print(gini_coefficient_accounts_sent(address))
# print(gini_coefficient_value_received(address))
# print(gini_coefficient_value_sent(address))

# Testing that lengths are the same
def check_export_to_excel(address): 
    print(len(unify_list_length(check_if_list_and_convert(time_between_sent_accounts(address)))))
    print(len(unify_list_length(check_if_list_and_convert(time_between_received_accounts(address)))))
    print(len(unify_list_length(check_if_list_and_convert(time_between_first_and_last_transaction(address)))))
    print(len(unify_list_length(check_if_list_and_convert(total_sent_accounts(address)))))
    print(len(unify_list_length(check_if_list_and_convert(total_received_accounts(address)))))
    print(len(unify_list_length(check_if_list_and_convert(total_number_of_transactions(address)))))
    print(len(unify_list_length(check_if_list_and_convert(total_unique_sent_accounts(address)))))
    print(len(unify_list_length(check_if_list_and_convert(total_unique_received_accounts(address)))))
    print(len(unify_list_length(check_if_list_and_convert(minimum_received_value(address)))))
    print(len(unify_list_length(check_if_list_and_convert(maximum_received_value(address)))))
    print(len(unify_list_length(check_if_list_and_convert(average_received_value(address)))))
    print(len(unify_list_length(check_if_list_and_convert(total_received_value(address)))))
    print(len(unify_list_length(check_if_list_and_convert(minimum_received_value(address)))))
    print(len(unify_list_length(check_if_list_and_convert(maximum_received_value(address)))))
    print(len(unify_list_length(check_if_list_and_convert(average_received_value(address)))))
    print(len(unify_list_length(check_if_list_and_convert(total_received_value(address)))))
    print(len(unify_list_length(check_if_list_and_convert(account_balance(address))))) 
    print(len(unify_list_length(check_if_list_and_convert(account_creation_time(address))))) 
    print(len(unify_list_length(check_if_list_and_convert(account_active_duration(address))))) 

# Test the function
# check_export_to_excel(address)

# def gini_coefficient_accounts_received(address):
#     return total_received_accounts(address)/total_number_of_transactions(address)

# def gini_coefficient_accounts_sent(address):
#     return total_sent_accounts(address)/total_number_of_transactions(address)

# def gini_coefficient_value_received(address):
#     return total_received_value(address)/(total_received_value(address)+total_sent_value(address))

# def gini_coefficient_value_sent(address):
#     return total_sent_value(address)/(total_received_value(address)+total_sent_value(address))

def export_to_excel_normal(address_list): 

    mark_for_df_export = 100000
    batch_number = 1

    address_used = []
    time_between_sent_accounts_list = []
    maximum_time_between_sent_accounts_list = []
    minimum_time_between_sent_accounts_list = []
    average_time_between_sent_accounts_list = []
    time_between_received_accounts_list = []
    maximum_time_between_received_accounts_list = []
    minimum_time_between_received_accounts_list = []
    average_time_between_received_accounts_list = []
    time_between_first_and_last_transaction_list = []
    total_sent_accounts_list = []
    total_received_accounts_list = []
    total_number_of_transactions_list = []
    total_unique_sent_accounts_list = []
    total_unique_received_accounts_list = []
    minimum_received_value_list = []
    maximum_received_value_list = []
    average_received_value_list = []
    total_received_value_list = []
    minimum_sent_value_list = []
    maximum_sent_value_list = []
    average_sent_value_list = []
    total_sent_value_list = []
    account_balance_list = []
    account_creation_time_list = []
    account_active_duration_list = []
    gini_coefficient_accounts_received_list = []
    gini_coefficient_accounts_sent_list = []
    gini_coefficient_value_received_list = []
    gini_coefficient_value_sent_list = []

    for j in address_list: 

        print(address_list.index(j))
    
        if j == address_list[len(address_list) - 1]: 
            print("last transaction has been read")
            batch_name = "normaloutput" + "last" + ".xlsx"
            df.to_excel(batch_name) 

        if address_list.index(j) == mark_for_df_export: 

            # try: 

            print("we are at the export mark")
            i = chain.address_from_index(j,blocksci.address_type.pubkeyhash)
            print(i)     
            
            address_used.append(unify_list_length(check_if_list_and_convert(i)))
            print(j)
            # time_between_sent_accounts_list.append(unify_list_length(check_if_list_and_convert(time_between_sent_accounts(i))))
            maximum_time_between_sent_accounts_list.append(unify_list_length(check_if_list_and_convert(max_time_difference_between_sent_accounts(i))))
            minimum_time_between_sent_accounts_list.append(unify_list_length(check_if_list_and_convert(min_time_difference_between_sent_accounts(i))))
            average_time_between_sent_accounts_list.append(unify_list_length(check_if_list_and_convert(average_time_difference_between_sent_accounts(i))))
            # time_between_received_accounts_list.append(unify_list_length(check_if_list_and_convert(time_between_received_accounts(i))))
            maximum_time_between_received_accounts_list.append(unify_list_length(check_if_list_and_convert(max_time_difference_between_received_accounts(i))))
            minimum_time_between_received_accounts_list.append(unify_list_length(check_if_list_and_convert(min_time_difference_between_received_accounts(i))))
            average_time_between_received_accounts_list.append(unify_list_length(check_if_list_and_convert(average_time_difference_between_received_accounts(i))))
            time_between_first_and_last_transaction_list.append(unify_list_length(check_if_list_and_convert(time_between_first_and_last_transaction(i))))
            total_sent_accounts_list.append(unify_list_length(check_if_list_and_convert(total_sent_accounts(i))))
            total_received_accounts_list.append(unify_list_length(check_if_list_and_convert(total_received_accounts(i))))
            total_number_of_transactions_list.append(unify_list_length(check_if_list_and_convert(total_number_of_transactions(i))))
            total_unique_sent_accounts_list.append(unify_list_length(check_if_list_and_convert(total_unique_sent_accounts(i))))
            total_unique_received_accounts_list.append(unify_list_length(check_if_list_and_convert(total_unique_received_accounts(i))))
            minimum_received_value_list.append(unify_list_length(check_if_list_and_convert(minimum_received_value(i))))
            maximum_received_value_list.append(unify_list_length(check_if_list_and_convert(maximum_received_value(i))))
            average_received_value_list.append(unify_list_length(check_if_list_and_convert(average_received_value(i))))
            total_received_value_list.append(unify_list_length(check_if_list_and_convert(total_received_value(i))))
            minimum_sent_value_list.append(unify_list_length(check_if_list_and_convert(minimum_sent_value(i))))
            maximum_sent_value_list.append(unify_list_length(check_if_list_and_convert(maximum_sent_value(i))))
            average_sent_value_list.append(unify_list_length(check_if_list_and_convert(average_sent_value(i))))
            total_sent_value_list.append(unify_list_length(check_if_list_and_convert(total_sent_value(i))))
            account_balance_list.append(unify_list_length(check_if_list_and_convert(account_balance(i))))
            account_creation_time_list.append(unify_list_length(check_if_list_and_convert(account_creation_time(i))))
            account_active_duration_list.append(unify_list_length(check_if_list_and_convert(account_active_duration(i))))
            gini_coefficient_accounts_received_list.append(unify_list_length(check_if_list_and_convert(gini_coefficient_accounts_received(i))))
            gini_coefficient_accounts_sent_list.append(unify_list_length(check_if_list_and_convert(gini_coefficient_accounts_sent(i))))
            gini_coefficient_value_received_list.append(unify_list_length(check_if_list_and_convert(gini_coefficient_value_received(i))))
            gini_coefficient_value_sent_list.append(unify_list_length(check_if_list_and_convert(gini_coefficient_value_sent(i))))


            df = pd.DataFrame(
                {'address_used': address_used,
                # 'time_between_sent_accounts': time_between_sent_accounts_list,
                'maximum_time_between_sent_accounts': maximum_time_between_sent_accounts_list,
                'minimum_time_between_sent_accounts': minimum_time_between_sent_accounts_list,
                'average_time_between_sent_accounts': average_time_between_sent_accounts_list,
                # 'time_between_received_accounts': time_between_received_accounts_list,
                'maximum_time_between_received_accounts': maximum_time_between_received_accounts_list,
                'minimum_time_between_received_accounts': minimum_time_between_received_accounts_list,
                'average_time_between_received_accounts': average_time_between_received_accounts_list,
                'time_between_first_and_last_transaction': time_between_first_and_last_transaction_list,
                'total_sent_accounts': total_sent_accounts_list,
                'total_received_accounts': total_received_accounts_list,
                'total_number_of_transactions': total_number_of_transactions_list,
                'total_unique_sent_accounts': total_unique_sent_accounts_list,
                'total_unique_received_accounts': total_unique_received_accounts_list,
                'minimum_received_value': minimum_received_value_list,
                'maximum_received_value': maximum_received_value_list,
                'average_received_value': average_received_value_list,
                'total_received_value': total_received_value_list,
                'minimum_sent_value': minimum_sent_value_list,
                'maximum_sent_value': maximum_sent_value_list,
                'average_sent_value': average_sent_value_list,
                'total_sent_value': total_sent_value_list,
                'account_balance': account_balance_list,
                'account_creation_time': account_creation_time_list,
                'account_active_duration': account_active_duration_list,
                'gini_coefficient_accounts_received': gini_coefficient_accounts_received_list,
                'gini_coefficient_accounts_sent': gini_coefficient_accounts_sent_list,
                'gini_coefficient_values_received': gini_coefficient_value_received_list,
                'gini_coefficient_values_sent': gini_coefficient_value_sent_list})

            batch_name = "normaloutput" + str(batch_number) + ".xlsx"

            df.to_excel(batch_name) 
            mark_for_df_export += 1000000
            batch_number += 1

            address_used = []
            time_between_sent_accounts_list = []
            maximum_time_between_sent_accounts_list = []
            minimum_time_between_sent_accounts_list = []
            average_time_between_sent_accounts_list = []
            time_between_received_accounts_list = []
            maximum_time_between_received_accounts_list = []
            minimum_time_between_received_accounts_list = []
            average_time_between_received_accounts_list = []
            time_between_first_and_last_transaction_list = []
            total_sent_accounts_list = []
            total_received_accounts_list = []
            total_number_of_transactions_list = []
            total_unique_sent_accounts_list = []
            total_unique_received_accounts_list = []
            minimum_received_value_list = []
            maximum_received_value_list = []
            average_received_value_list = []
            total_received_value_list = []
            minimum_sent_value_list = []
            maximum_sent_value_list = []
            average_sent_value_list = []
            total_sent_value_list = []
            account_balance_list = []
            account_creation_time_list = []
            account_active_duration_list = []
            gini_coefficient_accounts_received_list = []
            gini_coefficient_accounts_sent_list = []
            gini_coefficient_value_received_list = []
            gini_coefficient_value_sent_list = []
            
            # except: 
            #     print("different type of account")
            #     continue

        # try: 

        i = chain.address_from_index(j,blocksci.address_type.pubkeyhash)      
            
        address_used.append(unify_list_length(check_if_list_and_convert(i)))
        print(j)
        # time_between_sent_accounts_list.append(unify_list_length(check_if_list_and_convert(time_between_sent_accounts(i))))
        maximum_time_between_sent_accounts_list.append(unify_list_length(check_if_list_and_convert(max_time_difference_between_sent_accounts(i))))
        minimum_time_between_sent_accounts_list.append(unify_list_length(check_if_list_and_convert(min_time_difference_between_sent_accounts(i))))
        average_time_between_sent_accounts_list.append(unify_list_length(check_if_list_and_convert(average_time_difference_between_sent_accounts(i))))
        # time_between_received_accounts_list.append(unify_list_length(check_if_list_and_convert(time_between_received_accounts(i))))
        maximum_time_between_received_accounts_list.append(unify_list_length(check_if_list_and_convert(max_time_difference_between_received_accounts(i))))
        minimum_time_between_received_accounts_list.append(unify_list_length(check_if_list_and_convert(min_time_difference_between_received_accounts(i))))
        average_time_between_received_accounts_list.append(unify_list_length(check_if_list_and_convert(average_time_difference_between_received_accounts(i))))    
        time_between_first_and_last_transaction_list.append(unify_list_length(check_if_list_and_convert(time_between_first_and_last_transaction(i))))
        total_sent_accounts_list.append(unify_list_length(check_if_list_and_convert(total_sent_accounts(i))))
        total_received_accounts_list.append(unify_list_length(check_if_list_and_convert(total_received_accounts(i))))
        total_number_of_transactions_list.append(unify_list_length(check_if_list_and_convert(total_number_of_transactions(i))))
        total_unique_sent_accounts_list.append(unify_list_length(check_if_list_and_convert(total_unique_sent_accounts(i))))
        total_unique_received_accounts_list.append(unify_list_length(check_if_list_and_convert(total_unique_received_accounts(i))))
        minimum_received_value_list.append(unify_list_length(check_if_list_and_convert(minimum_received_value(i))))
        maximum_received_value_list.append(unify_list_length(check_if_list_and_convert(maximum_received_value(i))))
        average_received_value_list.append(unify_list_length(check_if_list_and_convert(average_received_value(i))))
        total_received_value_list.append(unify_list_length(check_if_list_and_convert(total_received_value(i))))
        minimum_sent_value_list.append(unify_list_length(check_if_list_and_convert(minimum_sent_value(i))))
        maximum_sent_value_list.append(unify_list_length(check_if_list_and_convert(maximum_sent_value(i))))
        average_sent_value_list.append(unify_list_length(check_if_list_and_convert(average_sent_value(i))))
        total_sent_value_list.append(unify_list_length(check_if_list_and_convert(total_sent_value(i))))
        account_balance_list.append(unify_list_length(check_if_list_and_convert(account_balance(i))))
        account_creation_time_list.append(unify_list_length(check_if_list_and_convert(account_creation_time(i))))
        account_active_duration_list.append(unify_list_length(check_if_list_and_convert(account_active_duration(i))))
        gini_coefficient_accounts_received_list.append(unify_list_length(check_if_list_and_convert(gini_coefficient_accounts_received(i))))
        gini_coefficient_accounts_sent_list.append(unify_list_length(check_if_list_and_convert(gini_coefficient_accounts_sent(i))))
        gini_coefficient_value_received_list.append(unify_list_length(check_if_list_and_convert(gini_coefficient_value_received(i))))
        gini_coefficient_value_sent_list.append(unify_list_length(check_if_list_and_convert(gini_coefficient_value_sent(i))))

        df = pd.DataFrame(
            {'address_used': address_used,
            # 'time_between_sent_accounts': time_between_sent_accounts_list,
            'maximum_time_between_sent_accounts': maximum_time_between_sent_accounts_list,
            'minimum_time_between_sent_accounts': minimum_time_between_sent_accounts_list,
            'average_time_between_sent_accounts': average_time_between_sent_accounts_list,
            # 'time_between_received_accounts': time_between_received_accounts_list,
            'maximum_time_between_received_accounts': maximum_time_between_received_accounts_list,
            'minimum_time_between_received_accounts': minimum_time_between_received_accounts_list,
            'average_time_between_received_accounts': average_time_between_received_accounts_list,
            'time_between_first_and_last_transaction': time_between_first_and_last_transaction_list,
            'total_sent_accounts': total_sent_accounts_list,
            'total_received_accounts': total_received_accounts_list,
            'total_number_of_transactions': total_number_of_transactions_list,
            'total_unique_sent_accounts': total_unique_sent_accounts_list,
            'total_unique_received_accounts': total_unique_received_accounts_list,
            'minimum_received_value': minimum_received_value_list,
            'maximum_received_value': maximum_received_value_list,
            'average_received_value': average_received_value_list,
            'total_received_value': total_received_value_list,
            'minimum_sent_value': minimum_sent_value_list,
            'maximum_sent_value': maximum_sent_value_list,
            'average_sent_value': average_sent_value_list,
            'total_sent_value': total_sent_value_list,
            'account_balance': account_balance_list,
            'account_creation_time': account_creation_time_list,
            'account_active_duration': account_active_duration_list,
            'gini_coefficient_accounts_received': gini_coefficient_accounts_received_list,
            'gini_coefficient_accounts_sent': gini_coefficient_accounts_sent_list,
            'gini_coefficient_values_received': gini_coefficient_value_received_list,
            'gini_coefficient_values_sent': gini_coefficient_value_sent_list})
        # except: 
        #     print("account type different")
        #     continue
        
    return("export fully successful")

# chain = blocksci.Blockchain("/home/user_cl/workplace_cl/blocksci_made_data_bk_up_2/btc_config_2.json")

def getting_list_of_normal_transactions(): 
    list_of_index = []
    
    for i in chain.blocks[392617:402617].txes:
        print(i)
        list_of_index.append(i.index)

    # for j in chain.blocks[500617].txes:
    #     list_of_index.append(j.index)

    # for k in chain.blocks[400617].txes:
    #     list_of_index.append(k.index)    

    return(list_of_index)     

# print(chain.address_from_string("56e6c762e3dcd87d52a79b75899cd9f0e806b04398b3f7efe6e416621f8ef1a9"))

# address = chain.address_from_index(102707021,blocksci.address_type.pubkeyhash)
# print(address)

list_of_normal_transactions = getting_list_of_normal_transactions()
export_to_excel_normal(list_of_normal_transactions)
