# This was the first ever bitcoin transaction where Satoshi sent Hal 10 BTC

txid = 'f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16'
raw_hex = '0100000001c997a5e56e104102fa209c6a852dd90660a20b2d9c352423edce25857fcd3704000000004847304402204e45e16932b8af514961a1d3a1a25fdf3f4f7732e9d624c6c61548ab5fb8cd410220181522ec8eca07de4860a4acdd12909d831cc56cbbac4622082221a8768d1d0901ffffffff0200ca9a3b00000000434104ae1a62fe09c5f51b13905f07f06b99a2f7159b2225f374cd378d71302fa28414e7aab37397f554a7df5f142c21c1b7303b8a0626f1baded5c72a704f7e6cd84cac00286bee0000000043410411db93e1dcdb8a016b49840f8c53bc1eb68a382e97b1482ecad7b148a6909a5cb2e0eaddfb84ccf9744464f82e160bfa9b8b64f9d4c03f999b8643f656b412a3ac00000000'


# Exercise: Parse the above TX by hand!

# python dict format you should use

parsed_transaction1 = {
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
#   txId: c997a5e56e104102fa209c6a852dd90660a20b2d9c352423edce25857fcd3704
#   vout: 00000000
#   scriptSig: [48]47304402204e45e16932b8af514961a1d3a1a25fdf3f4f7732e9d624c6c61548ab5fb8cd410220181522ec8eca07de4860a4acdd12909d831cc56cbbac4622082221a8768d1d0901
#   sequence: ffffffff
# output_count: 02
#   outputs: 00ca9a3b00000000
#   scriptPubKey: [43]4104ae1a62fe09c5f51b13905f07f06b99a2f7159b2225f374cd378d71302fa28414e7aab37397f554a7df5f142c21c1b7303b8a0626f1baded5c72a704f7e6cd84cac00286bee

# locktime: 00000000



# version: 01000000
# input_count: 01
# inputs:   
#   txId: c997a5e56e104102fa209c6a852dd90660a20b2d9c352423edce25857fcd3704
#   vout: 00000000
#   scriptSig: [48]47304402204e45e16932b8af514961a1d3a1a25fdf3f4f7732e9d624c6c61548ab5fb8cd410220181522ec8eca07de4860a4acdd12909d831cc56cbbac4622082221a8768d1d0901
#   sequence: ffffffff
# output_count: 02
#   outputs:
#     amount: 00ca9a3b00000000
#     scriptPubKey:   [43]4104ae1a62fe09c5f51b13905f07f06b99a2f7159b2225f374cd378d71302fa28414e7aab37397f554a7df5f142c21c1b7303b8a0626f1baded5c72a704f7e6cd84cac00286bee0000000043410411db93e1dcdb8a016b49840f8c53bc1eb68a382e97b1482ecad7b148a6909a5cb2e0eaddfb84ccf9744464f82e160bfa9b8b64f9d4c03f999b8643f656b412a3ac

# locktime: 00000000






# 01000000
# 01
#     c997a5e56e104102fa209c6a852dd90660a20b2d9c352423edce25857fcd3704
#     00000000
# 4847304402204e45e16932b8af514961a1d3a1a25fdf3f4f7732e9d624c6c61548ab5fb8cd410220181522ec8eca07de4860a4acdd12909d831cc56cbbac4622082221a8768d1d0901
#     ffffffff
# 02
#     00ca9a3b00000000
# 434104ae1a62fe09c5f51b13905f07f06b99a2f7159b2225f374cd378d71302fa28414e7aab37397f554a7df5f142c21c1b7303b8a0626f1baded5c72a704f7e6cd84cac
#     00286bee00000000
# 43410411db93e1dcdb8a016b49840f8c53bc1eb68a382e97b1482ecad7b148a6909a5cb2e0eaddfb84ccf9744464f82e160bfa9b8b64f9d4c03f999b8643f656b412a3ac
# 00000000