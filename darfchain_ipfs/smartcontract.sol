pragma solidity ^0.4.17;

contract SynchronizeStorage {
    string storedData;
    uint gaslimit;
    uint gasused;
    string documentHash;
    string DocumentIPFSAddress;
    
    function setData(string x) public {storedData = x; }
   
    function getGasLimit() public  returns (uint gas) { 
    gaslimit =  msg.gas;
         return gaslimit;
    }
    function HashOfDB() public constant returns (string x) { 
    return storedData;}
    function setDocumentIPFSAddress(string ipfs_address) public {    
        DocumentIPFSAddress = ipfs_address;
    }
    function getDocumentIPFSAddress() public constant returns(string x) {   
         return DocumentIPFSAddress;
    }
    function setDocumentHash(string timestamp, string md5) public {     
       documentHash = md5;
        storedData = timestamp;
    }
    function getDocumentHash() public constant returns(string x){    
        return storedData;
    }
    function getDocumentMD5() public constant returns(string x){      
      return documentHash;
    }
}