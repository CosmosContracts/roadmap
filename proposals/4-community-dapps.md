# Juno Roadmap: Proposal 4

## Summary

This proposal aims to increase on-chain activity, in terms of transactions, and simplify the development of new dApps by creating a "Juno Portal" dApp with all the foundational building blocks for the network.

## Juno Portal

We propose developing "app.junonetwork.io," a unified interface for accessing all community-owned dApps and network tools. The portal’s sections will be governed by the community, which can vote on how to route traffic to specific smart contracts. For example, the swap interface could default to the community-owned DEX but allocate a portion of swaps to a third-party DEX if decided via governance. Developers building on Juno will have the opportunity to connect their smart contracts to the UI, gaining immediate traffic.

### Portal Phases

#### v1: Basic Features

The portal will initially launch with basic features, without any governance integration. It will include the following functionalities:

1. Permissionless Decentralized Exchange (AMM), with customizable incentives.
2. Permissionless Token / Memecoin Launchpad.
3. Permissionless Token Airdrop Tool, leveraging x/drip and cw-merkle-airdrop.
4. OTC Vaults.

All functionalities implemented in this phase will use $JUNO as the primary token. Fees accumulated will be sent to the community treasury.

#### v2: Community Engagement

If Proposal [5](./5-community-activities.md) is approved, the portal will include new sections to manage bounties, ambassadors, daily missions, and other community activities.

#### v3: Governance Implementation

The portal's most innovative feature is the ability to route traffic to any smart contract developed on Juno, providing developers with immediate feedback on their projects. The portal will include a secondary governance system, where users can gain voting power by:

- Donating to the community pool.
- Staking their $JUNO for a specific period.
- Utilizing other portal products.

The governance system will allow votes on:

- Adding new features or UI sections to the portal.
- Routing traffic from UI sections to various compatible smart contracts (e.g., 50% DEX swaps using the community-owned DEX, 10% on Osmosis, 40% on a third-party DEX).
- Funding community initiatives (e.g., bounties, ambassador programs).

Developers who want to leverage portal traffic must set up specific smart contract interfaces and propose their integration to the portal governance system.

_Example 1:_

> I’m Bloopers, a super-incentivized farming DEX, and I’d like to integrate it into the portal. I can offer to the Portal buying and burning $JUNO tokens proportionally to the fees accumulated if the community votes to route some traffic to my smart contract.

_Example 2:_

> I’m Mariza, and I’ve built a framework for creating and deploying AI agents. The portal doesn’t currently support UI agents. I can propose adding a new UI section specific to that functionality, initially routing all traffic to my smart contracts. Future teams can propose to route traffic also to their project.

### Why is it Cool?

If we execute this project well, the portal could attract a significant number of daily users. This would create immense value for developers and provide a compelling reason to build on Juno. A user-friendly design and features to ensure recurring user engagement will be critical to the portal's success.

## Budget

Building a platform like this is a substantial task. Fortunately, we can reuse many UI components from the Juno network [website](https://junonetwork.io) to streamline development. Kintsugi Tech proposes to develop the entire portal with the following schedule and budget:

| Portal Version           | Delivery Date | Description                                                                             | Budget                      | Payment Terms                                                             |
| ------------------------ | ------------- | --------------------------------------------------------------------------------------- | --------------------------- | ------------------------------------------------------------------------- |
| v1 & v2                  | Q2 - 2025     | Initial basic version of the portal.                                                    | 10,000 USDC + 200,000 $JUNO | All USDC paid immediately; $JUNO: 30% upfront, the rest after deployment. |
| v3                       | Q3 - 2025     | Implementation of the governance system and permissionless traffic routing.             | 250,000 $JUNO               | 50% at the start of development, 50% upon completion.                     |
| Ongoing after v3 release | -             | Maintenance fee (if no further developments are required). Covers infrastructure costs. | 2,000 $JUNO/month           | Paid at the end of each month or via recurring payments on DAODAO.        |

**Total budget by the end of 2025:** 10,000 USDC + 450,000 JUNO (excluding maintenance fees).

## Budget Handling

This proposal allocates the budget for the first tranche of v1, which will be sent directly to the Kintsugi Tech [DAODAO account](https://daodao.zone/dao/osmo1ruxpcljuhpepuw2ywxlqsuhy8u3eulz5hdrsedcvwex8qnsd9yqsqv09j7/treasury).

Once the portal is live, a follow-up proposal will request the remaining funds and allocate the budget for v3.

The community will be able to monitor all transactions and verify that the funds are handled responsibly, minimizing any impact on $JUNO liquidity or price.

The community can also review our history and see how we’ve been compounding validator commissions over the years.

### Price Disclosure

The budgets outlined above assume a $JUNO price of $0.20. If the price changes, the budget will adjust accordingly, with a maximum multiplier of 4x and a minimum multiplier of 0.25x.

## Transparency

Kintsugi Tech will develop the portal entirely in public, using Juno’s GitHub repositories. The community will have the opportunity to track progress, ask questions, and provide feedback at any time. We’ll maintain a dedicated Discord channel and other communication channels for updates. Additionally, we will share development status reports every few weeks or whenever significant progress is made.
