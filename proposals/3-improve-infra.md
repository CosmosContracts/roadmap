# Juno Roadmap: Proposal 3

## Summary

This proposal has the objective to improve the infrastructure, both from an economic point of view and to better organize the network during upgrades. To do so, we propose to reduce the validator set size to 80 validators.

## Reasonings

### 1) Block size

As of today, Juno has an average block time of 3 seconds but most of the blocks are empty or with very few transactions. Despite this, the size of an archive node for Juno has been growing constantly and is not over 7TB. Out of this 7TB only ~5% is used because of transactions or real data, the other ~95% is just for validator signatures inside block headers.

- **Signature size:** 30.94 KB
- **Non-signature size:** 1.58 KB
- **Total size:** 32.52 KB
- **Validator Signatures:** 95.14% of the total size.
- **Non-signature (Real Data):** 4.86% of the total size.

_Note: This doesn't reflect 100% precisely the blockchain data size, since that is affected also by other factors such as the indexed database size, but it's to give an overall idea_

### 2) Validator coordination

Majority of the validators are currently running at a loss, while it's completely up to them to decide if they want to run a validator or not, this affects validator coordination. Coordinating a large group of validators is an hard task, especially if they don't have the economic incentive to collaborate in a timely manner.

## Future

In the future we plan to propose additional changes to the network, such as a new delegation program, a more decentralized stake rewards distribution system and maybe even a different voting power system for governance. It's not a matter of this proposal, but looking at the future any of these changes will be much easier to implement with a smaller validator set.

## Conclusion

- Vote YES if you agree on reducing the validator set size to 80 validators.
- Vote NO if you don't agree.
