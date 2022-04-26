/*
# Copyright IBM Corp. All Rights Reserved.
#
# SPDX-License-Identifier: Apache-2.0
*/

'use strict';
const shim = require('fabric-shim');
const util = require('util');

let Chaincode = class {

  // The Init method is called when the Smart Contract 'fabcar' is instantiated by the blockchain network
  // Best practice is to have any Ledger initialization in separate function -- see initLedger()
  async Init(stub) {
    console.info('=========== Instantiated record chaincode ===========');
    return shim.success();
  }

  // The Invoke method is called as a result of an application request to run the Smart Contract
  // 'fabcar'. The calling application program has also specified the particular smart contract
  // function to be called, with arguments
  async Invoke(stub) {
    let ret = stub.getFunctionAndParameters();
    console.info(ret);

    let method = this[ret.fcn];
    if (!method) {
      console.error('no function of name:' + ret.fcn + ' found');
      throw new Error('Received unknown function ' + ret.fcn + ' invocation');
    }
    try {
      let payload = await method(stub, ret.params);
      return shim.success(payload);
    } catch (err) {
      console.log(err);
      return shim.error(err);
    }
  }

  async queryRecord(stub, args) {
    if (args.length != 1) {
      throw new Error('Incorrect number of arguments. Expecting itemID hash value');
    }
    let recordId = args[0];

    let recordAsBytes = await stub.getState(recordId); //get the car from chaincode state
    if (!recordAsBytes || recordAsBytes.toString().length <= 0) {
      throw new Error(recordId + ' does not exist: ');
    }
    console.log(recordAsBytes.toString());
    return recordAsBytes;
  }

  async initLedger(stub, args) {
    console.info('============= START : Initialize Ledger ===========');
    let records = [];
    records.push({
      itemIdHash: 'RECORD0',
      itemIdAES: '0',
      itemHash: 'test',
      ownedTableAES: 'test'
    });

    for (let i = 0; i < records.length; i++) {
      records[i].docType = 'record';
      await stub.putState(records[i].itemIdHash, Buffer.from(JSON.stringify(records[i])));
      console.info('Added <--> ', records[i]);
    }
    console.info('============= END : Initialize Ledger ===========');
  }

  async createRecord(stub, args) {
    console.info('============= START : Create Record ===========');
    if (args.length != 4) {
      throw new Error('Incorrect number of arguments. Expecting 4');
    }

    var record = {
      docType: 'record',
      itemIdHash: args[0], // shouldn't this be arg 0?
      itemIdAES: args[1],
      itemHash: args[2],
      ownedTableAES: args[3]
    };

    await stub.putState('i' + record.itemIdHash, Buffer.from(JSON.stringify(record)));
    console.info('============= END : Create Record ===========');
  }

  async queryAllRecords(stub, args) {

    let startKey = 'RECORD0';
    let endKey = 'RECORD999';

    let iterator = await stub.getStateByRange(startKey, endKey);

    let allResults = [];
    while (true) {
      let res = await iterator.next();

      if (res.value && res.value.value.toString()) {
        let jsonRes = {};
        console.log(res.value.value.toString('utf8'));

        jsonRes.Key = res.value.key;
        try {
          jsonRes.Record = JSON.parse(res.value.value.toString('utf8'));
        } catch (err) {
          console.log(err);
          jsonRes.Record = res.value.value.toString('utf8');
        }
        allResults.push(jsonRes);
      }
      if (res.done) {
        console.log('end of data');
        await iterator.close();
        console.info(allResults);
        return Buffer.from(JSON.stringify(allResults));
      }
    }
  }

  async updateRecord(stub, args) {
    console.info('============= START : updateRecord ===========');
    if (args.length != 2) {
      throw new Error('Incorrect number of arguments. Expecting 2');
    }

    let recordAsBytes = await stub.getState(args[0]);
    let record = JSON.parse(recordAsBytes);
    record.itemHash = args[1];

    await stub.putState(args[0], Buffer.from(JSON.stringify(record)));
    console.info('============= END : updateRecord ===========');
  }

};

shim.start(new Chaincode());

