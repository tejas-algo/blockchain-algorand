from algosdk.v2client import algod, indexer


# Connection to the algorand network
def algo_conn():
    algod_address = "https://testnet-algorand.api.purestake.io/ps2"
    algod_token = "ksZOvoviIZ163QVUoTht86g0qMBmLJIS9hcFpcNl"
    headers = {"X-API-Key": algod_token}
    conn = algod.AlgodClient(algod_token, algod_address, headers)

    return conn


# Connection to Algorand Indexer
def connect_indexer():
    algod_indexer = "https://testnet-algorand.api.purestake.io/idx2"
    indexer_token = "ksZOvoviIZ163QVUoTht86g0qMBmLJIS9hcFpcNl"
    headers = {"X-API-Key": indexer_token}
    myindexer = indexer.IndexerClient(indexer_token, algod_indexer, headers)
    return myindexer
