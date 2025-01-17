# Juno Roadmap: Proposal 3 - Reduction of the Validator Set

## Summary

This proposal aims to improve the infrastructure from both an economic perspective and a network organization standpoint during upgrades. To achieve this, we propose reducing the validator set size to 80 validators.

## Reasoning

### 1) Block Size

Currently, Juno has an average block time of 3 seconds, but most blocks are either empty or contain very few transactions. Despite this, the size of an archive node for Juno has been growing steadily and now exceeds 7TB. Only a small percentage of this 7TB is utilized for transactions or real data; the majority is taken up by validator signatures in block headers.

- **Signature size:** 30.94 KB
- **Non-signature size:** 1.58 KB
- **Total size:** 32.52 KB
- **Validator Signatures:** 95.14% of the total size.
- **Non-signature (Real Data):** 4.86% of the total size.

_Note: This does not precisely reflect the blockchain data size, as other factors, such as the indexed database size and smart contract storage, also contribute. However, it provides a general idea._

### 2) Validator Coordination

The majority of validators currently operate at a loss. While it is their decision whether to continue running a validator, this situation affects overall validator coordination. Managing a large group of validators is a challenging task, particularly when there is little economic incentive for timely collaboration.

## Future

In the future, we plan to propose additional changes to the network, such as a new delegation program, a more decentralized stake rewards distribution system, and potentially a revised voting power system for governance. While these changes are not part of this proposal, implementing them will be significantly easier with a smaller validator set.

## Conclusion

- Vote YES if you agree with reducing the validator set size to 80 validators.
- Vote NO if you disagree.
