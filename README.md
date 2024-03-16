### Elliptic Curves Basics

**1. Given a random point n, is n a valid point on the sepc265k1 curve?**

- [checkSpecp256k1Point](checkSpecp256k1Point.py)
  - `python3 checkSpecp256k1Point.py x y` **(should check x,y must in [1,p-1])?**
  - `python3 GetRandomPoint.py `

**2. generate an address that starts with 0x0000** [GenerateProfanityAddress](GenerateProfanityAddress.py)

- `python3 GenerateProfanityAddress.py`

  - `private_key 0x3447dbf8b5f32b1dbae7abc969c9ab3da88a54f0c4d719c4c74bbac362102a8e
  - eth_addr 0x0000defe1e41e5da8303fedfd9b380664590ac3d`

**3. [Fuzzy-identity](https://capturetheether.com/challenges/accounts/fuzzy-identity/)**

1. Deployed the contract on-chain [FuzzyIdentityChallenge.sol](https://sepolia.etherscan.io/address/0x780a1ccCD0A4D6BAd93ca95CF020bEf83fe6cDcc#code)

2. howt to get the contract's identity?

   For hacking the authenticate

   1. one point is the caller should as smart contract supplying one funtion `function name() external pure returns (bytes32) {
    return bytes32("smarx");
}`,
   2. Another point is the smart contract's address should include `badc0de` no matter its postion in the address.

3. The steps to get the identity.

   1. Create the [ExploitContract](https://github.com/sodexx7/security_related/blob/e8004d42dde45389abaae4315880012254d61dcc/capture-the-ether-foundry/FuzzyIdentitiy/contracts/ExploitContract.sol#L5)

   2. Using create2 to create above contract by selecting a rondom salt to make the smart contract's address inludes `badc0de`

   3. As create2 creating one contract, there are three params needed, one is the factory contract, one is the created contract's creationCode, one is salt.

      1. For the facotry contract [CreateContract](https://github.com/sodexx7/security_related/blob/e8004d42dde45389abaae4315880012254d61dcc/capture-the-ether-foundry/FuzzyIdentitiy/contracts/CreateContract.sol#L5), which will create the ExploitContract contract, deployed address is
         [CreateContract](https://sepolia.etherscan.io/address/0xb310c509d117bD53D50EfBC652c043d24764e783#code)
      2. As factory contract address, CreateContract's creationCode code known, Calculatingthe possible salt brutely force which make the CreateContract's address includes `badc0de`.

      **Considering the efficiency, I use the this tool [github:styled-evm-address](https://github.com/morpho-labs/styled-evm-address),[styled-evm-addres](styled-evm-address/main.py)**。

      3. Then using the salt call CreateContract's createDesiredAddress function.

   4. Now the [ExploitContract](https://sepolia.etherscan.io/address/0x6add85814c50973e3174badc0de81199087a8760#writeContract) was deployed and its address includes `badc0de`, directly call exploit() getting the identity.
      [on-chain-tx](https://sepolia.etherscan.io/tx/0x3d0359e1e7c4f27cae990ef1b9f9860a30e853bd0cd18f3647a6f6c32073213d#statechange)

## Other info

1. https://0xfoobar.substack.com/p/vanity-addresses
2. https://github.com/0age/create2crunch
3. The efficient ways to minting the vantiy address
   1. [VanityEth](https://github.com/MyEtherWallet/VanityEth), which use more cpus to generate address and the random seed is based on 2^256.
   2. [create2crunch](https://github.com/0age/create2crunch) using rust language
   3. Spin up a GPU Example instance using vast.ai.
4. The private-key can be calculated by the generated vanity-addresses which have some problem. [the-profanity-address-hack-how-are-vanity-addresses-generated](https://medium.com/coinmonks/the-profanity-address-hack-how-are-vanity-addresses-generated-cce40ba5ed39)
   1. `python generate_vanity_address_ethereum_problem.py`, the logic generate the vulnerability address.
   2. implement the code to hack the vanity_address which has problem **toodo**

## Questions

1. when checking point(x,y) # x,y must in the field [1,p-1] todo check ?
