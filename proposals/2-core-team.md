# Juno Roadmap: Proposal 2 - Core team

## Summary

With this proposal, we suggest appointing two teams: Kintsugi Tech and Digital Kitchen, to focus on the maintenance and upgrade of the Juno Blockchain Core. Each team will have distinct responsibilities and will report directly to the community.

**Who is Kintsugi Tech?**

Kintsugi Tech is a validator and software development company founded in 2022 by me (Dimi) and a group of dedicated partners, focused on advancing decentralized technology with innovative solutions. We operate numerous validators across and beyond the Cosmos Ecosystem and bring extensive experience in CosmWasm and Cosmos-SDK development. Though our team is small (around 8 highly specialized individuals), we are committed to delivering impactful contributions. Recently, we’ve worked on projects like the custom UI for [Namada mainnet genesis](https://x.com/namada/status/1841105851488354504), the [DeQuiz dApp](https://dequiz.zone/) on Juno, and a Cosmos-SDK upgrade for [Firmachain](https://medium.com/firmachain/firmachain-roadmap-2024-with-a-summary-of-the-progress-made-in-2023-d47cb60b8b22). More details about our work can be found in our [expired proposal](https://github.com/CosmosContracts/council/blob/main/departments/development/rfp/006-Community_owned_DEX/submission_1/initial_proposal.pdf) for Mercury Dex that we proposed to the charter a while ago. Collaborating with Juno is an incredible opportunity but also a bet for us. If successful, it will benefit both Juno and Kintsugi immensely. If not, we risk wasting time and resources, potentially holding a large bag of worthless tokens. However, we firmly believe that with our dedication and expertise, we can help the Juno network shine again.

**Who is Digital Kitchen?**

Digital Kitchen is a Cosmos-aligned, collaborative software development group based in Germany. Founded by Marius (@vexxvakan) in 2021 as validator service, Digital Kitchen transformed into a software development group in 2022 while setting up the [Juno Apes](https://daodao.zone/dao/juno14zcdg8w3pyp7nfzaye7jp0tzynk8xpstqax5g9ypj2u66n4lst2strvwjs/home) token, [NFT collection](https://omniflix.market/c/onftdenomd7ba07c7b185461f862b9014c90a9e62/collect-now) and DAO structure on Juno. In 2023 Digital Kitchen got hired by the team at Hopers to [rebuild their app](https://hopers-landing-v2.vercel.app/) from the ground up. Since then Digital Kitchen released [a predictions market](https://app.velo.space) on another Cosmos ecosystem blockchain and also started working on a standalone blockchain using the Cosmos SDK in 2024. Working on the very core of where our journey started years ago is an honor as well an opportunity to breath fresh air into Juno and it's vibrant community.

## Deliverables

### Q1 Deliverables

The two teams will collaborate to deliver the following items by the end of Q1 2025:

| Team            | Deliverable                                                                     |
| --------------- | ------------------------------------------------------------------------------- |
| Digital Kitchen | Write the software upgrade to Cosmos-SDK v50                                    |
| Digital Kitchen | Convert/update custom modules to be compatible with the new version             |
| Digital Kitchen | Implement CosmWasm v2                                                           |
| Digital Kitchen | Implement feemarket module                                                      |
| Kintsugi Tech   | Maintain the repository, ensuring CI/CD and E2E tests are functioning correctly |
| Kintsugi Tech   | Write new contribution guidelines                                               |

### Q1-4 Continuous Deliverables

The two teams will provide continuous support for the following items until the end of 2025:

| Team            | Deliverable                                                                                                    |
| --------------- | -------------------------------------------------------------------------------------------------------------- |
| Digital Kitchen | Keep the core updated with third-party libraries (e.g., Cosmos SDK 52 LTS and others)                          |
| Kintsugi Tech   | Handle security patches in a timely manner to ensure the network’s security and stability                      |
| Kintsugi Tech   | Manage the Juno GitHub organization, ensuring only relevant personnel have access and can submit code          |
| Kintsugi Tech   | Update documentation as needed                                                                                 |
| Kintsugi Tech   | Coordinate validators and governance proposals for software upgrades and patches                               |
| Kintsugi Tech   | Provide support to validators and node operators on Discord for issues strictly related to the blockchain core |

## Transparency

As outlined in [Proposal 1](./1-general-overview.md), we aim to keep the community informed about the network’s progress. To achieve this, we will publish a quarterly report detailing the network’s status and the activities of the teams. Additionally, we will host community calls to discuss ongoing work and share development updates.

## Budget

The majority of the work will take place in Q1. Therefore, we propose two budgets: one for Q1 and one for the continuous activities throughout 2025.

### Q1 Budget

| Team            | Budget                                                                                       |
| --------------- | -------------------------------------------------------------------------------------------- |
| Digital Kitchen | 12,000 USDC – To be paid 1/3 immediately, 1/3 at the end of february, 1/3 a the end of march |
| Kintsugi Tech   | No funding required                                                                          |

### Continuous Budget

| Team            | Budget                                                                                    |
| --------------- | ----------------------------------------------------------------------------------------- |
| Digital Kitchen | 20,000 JUNO – To be paid at the end of each quarter, contingent on feedback and work logs |
| Kintsugi Tech   | 20,000 JUNO – To be paid at the end of each quarter, contingent on feedback and work logs |

### Totals

- **To be paid in Q1:** 12,000 USDC
- **Quarterly payments after Q1:** 20,000 JUNO + 20,000 JUNO
- **Total expenditure by the end of 2025:** 12,000 USDC + 120,000 JUNO

## Budget Handling

With this proposal we are sending only Q1 budget (12,000 USDC) to a multisig wallet controlled by Kintsugi, who will send the payments each month to Digital Kitchen. Q2-4 Budgets will be requested with an additional proposal in April.

### Price disclosure

The budgets have been calculated based on a $JUNO price of $0.20. In case of price fluctuations, the budget will be adjusted according to market conditions, with a maximum multiplier of 4x and a minimum multiplier of 0.25x.

### Development notes

Despite this proposal coming only now in the middle of Q1, we already started working on the deliverables.
You can find the draft Cosmos-SDK v50 upgrade [here](https://github.com/CosmosContracts/juno/pull/1089), and the security upgrades already implemented by looking at upgrades ([v25](https://github.com/CosmosContracts/juno/releases/tag/v25.0.0), [v26](https://github.com/CosmosContracts/juno/releases/tag/v26.0.0), [v27](https://github.com/CosmosContracts/juno/releases/tag/v27.0.0)) made by Kintsugi.

## Conclusion

- Vote YES if you agree to appoint Digital Kitchen and Kintsugi Tech as core teams, and you agree allocating the Q1 budget (12,000 USDC) by sending it to a wallet controlled by Kintsugi committing to the monthly payments outlined above.
- Vote NO if you disagree with appointing these teams or allocating these budgets.
