from algosdk.future import transaction
from algosdk import mnemonic


# Payment transaction
def payment(client, sender, receiver, amt, note):

    # get suggested params
    params = client.suggested_params()

    # get the private key of the sender
    private_key = mnemonic.to_private_key("adult collect grape unique stamp six replace group siren glow ice dune thrive eagle modify admit excite onion hole expire use canyon trick abandon session")

    txn = transaction.PaymentTxn(
        sender=sender, receiver=receiver, amt=amt, note=note, sp=params
    )

    stxn = txn.sign(private_key)
    tx_id = stxn.get_txid()

    # sent the transaction to blockchain
    client.send_transactions([stxn])

    return tx_id