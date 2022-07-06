# this is the follow on transaction by Hal from that original payment from satoshi
txid = 'ea44e97271691990157559d0bdd9959e02790c34db6c006d779e82fa5aee708e'

raw_hex = '0100000001169e1e83e930853391bc6f35f605c6754cfead57cf8387639d3b4096c54f18f400000000484730440220576497b7e6f9b553c0aba0d8929432550e092db9c130aae37b84b545e7f4a36c022066cb982ed80608372c139d7bb9af335423d5280350fe3e06bd510e695480914f01ffffffff0100ca9a3b000000001976a914340cfcffe029e6935f4e4e5839a2ff5f29c7a57188ac00000000'

# Exercise: Parse the above TX by hand!

# python dict format you should use

parsed_transaction2 = {
    "version": 0,
    "input_count": 1,
    "inputs": [
        {
            "txid": '',
            "vout": 0,
            "scriptSig": '',
            "sequence": 0,
        },
    ],
    "output_count": 1,
    "outputs": [
        {
            "amount": 0,
            "scriptPubKey": ''
        },
    ],
    "locktime": 0
}



# version: 01000000
# input_count: 01
# inputs:   
#   txId: 169e1e83e930853391bc6f35f605c6754cfead57cf8387639d3b4096c54f18f4
#   vout: 00000000
#   scriptSig: [48]4730440220576497b7e6f9b553c0aba0d8929432550e092db9c130aae37b84b545e7f4a36c022066cb982ed80608372c139d7bb9af335423d5280350fe3e06bd510e695480914f01
#   sequence: ffffffff
# output_count: 01
# outputs:
#   amount: 00ca9a3b00000000
#   scriptPubKey: 1976a914340cfcffe029e6935f4e4e5839a2ff5f29c7a57188ac
# locktime: 00000000