from TX1 import parsed_transaction1 as ptx1
from TX2 import parsed_transaction2 as ptx2
from TX3 import parsed_transaction3 as ptx3
from TX1 import raw_hex as raw1
from TX2 import raw_hex as raw2
from TX3 import raw_hex as raw3

import json

class Input:
  txid=""
  vout=0
  scriptSig=""
  sequence=0
  def display(self):
      print("TxId : ",self.txid)
      print("vout : ",self.vout)
      print("scriptSig : ",self.scriptSig)
      print("sequence : ",self.sequence)

class Output:
  amount=0
  scriptPubKey=""
  def display(self):
      print("Amount : ",self.amount)
      print("scriptPubKey : ",self.vout)


txs = [ptx1, ptx2, ptx3]
raw_txs = [raw1, raw2, raw3]

def flexible_outputs(tx, op_list, count):
  for a in range(count):
    o1 = {}
    o1['amount'] = op_list[a].amount
    o1['scriptPubKey'] = op_list[a].scriptPubKey
    tx['outputs'].append(o1)

def flexible_inputs(tx, ip_list, count):
  for b in range(count):
    i1 = {}
    i1['txid'] = ip_list[b].txid
    i1['vout'] = ip_list[b].vout
    i1['scriptSig'] = ip_list[b].scriptSig
    i1['sequence'] = ip_list[b].sequence
    tx['inputs'].append(i1)

# iterate over all the raw txs
for i in range(len(raw_txs)):
  # store raw tx in temp var for manipulation
  rawTxTemp = raw_txs[i]

  # 1. Get 'version' field
  # note: version must be reversed!
  versionLE = bytes.fromhex(rawTxTemp[0:8])[::-1]
  version = int.from_bytes(versionLE, "big")
  rawTxTemp = rawTxTemp[8:]

  # 2. Get 'input_count' field
  inputCountBytes = bytes.fromhex(rawTxTemp[0:2])
  input_count = int.from_bytes(inputCountBytes, "big");
  rawTxTemp = rawTxTemp[2:]

  # 3. Construct inputs object
  inputs = []
  for j in range(0, input_count):
    # 3a. Get 'txid' field (32 bytes)
    txId = rawTxTemp[0:64]
    rawTxTemp = rawTxTemp[64:]

    # 3b. Get 'vout' field
    voutBytes = bytes.fromhex(rawTxTemp[0:8])
    vout = int.from_bytes(voutBytes, "big")
    rawTxTemp = rawTxTemp[8:]

    # 3c. Use first byte to get size of scriptSig in bytes
    sigByteCount = bytes.fromhex(rawTxTemp[0:2])
    sigByteCountInt = int.from_bytes(sigByteCount, "big")
    rawTxTemp = rawTxTemp[2:]

    # 3d. Get 'scriptSig' field
    scriptSig = rawTxTemp[0:sigByteCountInt*2]
    rawTxTemp = rawTxTemp[sigByteCountInt*2:]
    print("Script Sig: ", scriptSig)

    # 3e. Get 'sequence' field
    sequenceBytes = rawTxTemp[0:8]
    print(sequenceBytes)
    rawTxTemp = rawTxTemp[8:]

    # 3f. Use Input object/class to store all input values
    i1 = Input()
    i1.txid = txId
    i1.vout = vout
    i1.scriptSig = scriptSig
    i1.sequence = sequenceBytes

    # 3g. Append to  inputs array
    inputs.append(i1)

  # 4. Get 'output_count' field
  outputCountBytes = bytes.fromhex(rawTxTemp[0:2])
  output_count = int.from_bytes(outputCountBytes, "big")
  rawTxTemp = rawTxTemp[2:]

  # 5. Construct outputs object
  outputs = []
  for k in range(0, output_count):
    # 5a. Get 'amount' field (8 bytes)
    amountBytes = bytes.fromhex(rawTxTemp[0:16])
    amount = int.from_bytes(amountBytes, "little")
    rawTxTemp = rawTxTemp[16:]

    # 5b. Use first byte to get size of scriptPubKey in bytes
    sigPubKeyBytes = bytes.fromhex(rawTxTemp[0:2])
    sigPubKeyInt = int.from_bytes(sigPubKeyBytes, "big")
    rawTxTemp = rawTxTemp[2:]

    # 5c. Get 'scriptPubKey' field
    scriptPubKey = rawTxTemp[0:sigPubKeyInt*2]
    rawTxTemp = rawTxTemp[sigPubKeyInt*2:]

    # 5d. Construct Output object/class
    o1 = Output()
    o1.amount = amount
    o1.scriptPubKey = scriptPubKey

    # 5e. Append to outputs array
    outputs.append(o1)

  # 6. Construct final parsed tx
  # 6a. Add 'locktime' field which should be the remaining
    # bytes left of the sliced rawTxTemp
  locktime = rawTxTemp

  # Add version
  txs[i]['version'] = version

  # Add input_count
  txs[i]['input_count'] = input_count

  # The tx object being used has a dead example tx input, delete it
  del txs[i]['inputs'][0]

  # flexible_inputs is a function that will append all the necessary inputs to the parsed tx object
  flexible_inputs(txs[i], inputs, input_count)

  # Add output_count
  txs[i]['output_count'] = output_count

  # The tx object being used has a dead example tx output, delete it
  del txs[i]['outputs'][0]

  # flexible_inputs is a function that will append all the necessary outputs to the parsed tx object
  flexible_outputs(txs[i], outputs, output_count)

  # Add locktime
  txs[i]['locktime'] = locktime

  
# print parsed txs
for w in range(len(txs)):
    print("PARSED TX", w+1, ":")
    print(json.dumps(txs[w], indent=2), "\n\n")
    print("-"*20)