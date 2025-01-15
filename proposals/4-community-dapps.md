# Juno Roadmap: Proposal 4

## Summary

This proposal aims to increase onchain activity, in terms of transactions, and simplify the developement of new
dAPPs by creating a "Juno Portal" dApp with all the base building blocks for the network.

## Juno Portal

We propose developing "app.junonetwork.io," a unified interface for accessing all community-owned dApps and network tools. The portal’s sections will be governed by the community, which can vote on how to route traffic to specific smart contracts. For example, the swap interface could default to the community owned DEX but allocate a portion of swaps to a third-party DEX if decided via governance. Anyone building on Juno will have the chance to connect their own smart contracts to the UI, getting immediate traffic.

### Portal phases

#### v1: Basic Features

The portal will be initially launched with only basic features, and without any governance. It will feature the following functionalities:

1. Premissionless Decentralized Exchange (AMM), with customizable incentives
1. Permissionless Token / memecoin Launchpad
1. Permissionless Token airdrop tool, leveraging x/drip and cw-merkle-airdrop
1. OTC Vaults

All the functionalities implemented in this phase will use only $JUNO as main token, fees accumulated will be sent to the community treasury.

#### v2: Community engagement

If proposal [5](./5-community-activities.md) is approved, the portal will feature new sections to manage bounties, ambassadors, dayly missions, and other community activities.

#### v3: Governance implementation

The coolest feature of the portal is the ability to route traffic to any smart contract developed on Juno, giving delopers immediate feedback on the stuff they are building. The portal will feature a secondary governance system, where users can get voting power by donating to the community pool, by keep staking their $JUNO for a period of time or even by utilizing other products of the portal itself.

The governance system will be used to vote on the following items:

- Add new features / UI sections to the portal itself
- How to route traffic from UI sections to various compatible smart contract (e.g. 50% DEX swaps using the community owned Dex, 10% on osmosis, 40% on a third-party built DEX)
- Community initiatives payments (like bounties, ambassador programs and so on)

Developers that want to consume traffic from the portal will have to setup specific smart contract interfaces, and propose something interesting to the Portal goverance system.

_Example 1_

    I'm Bloopers, a super incentivized farming DEX, and I'd like to integrate it in the portal. I can offer to the Portal governance to buy and burn $JUNO tokens proportionally the fees I'm accumulating if the community votes to route some traffic to my smart contract.

_Example 2_

    I'm Mariza and I built a framework to create and deploy AI angets. The portal doesn't have any integration for UI agents. I can submit a governance proposal to implement a UI section specific to that (maybe with some code attached), and initially route all traffic to my smart contracts. Other teams, in the future, can opt in to route some traffic also to themselves.

### Why is it Cool?

If we do a nice job, the portal might feature tons of users every day. This is extremely valuable for developers, and very attractive to build something on it. That's why the portal should feature a nice UX, and have features to get as many recurring users as possible. This is crucial for the success of this project.

## Budget

Of course building a platform like this is no easy task. Thanksfully we have a bunch of great UI compontens from the juno network [website](https://junonetwork.io) that we can re-use to simplify a little the work. Kintsugi Tech team is proposing to develop the entirity of the portal, with the following schedule and budget.

| Portal Version           | Delivery date | Description                                                                                          | Budget                      | Payment Terms                                                                   |
| ------------------------ | ------------- | ---------------------------------------------------------------------------------------------------- | --------------------------- | ------------------------------------------------------------------------------- |
| v1 & v2                  | Q2 - 2025     | Initial basic version of the portal                                                                  | 10,000 USDC + 200,000 $JUNO | All USDC paid immediately, $JUNO 30% immediate the rest after portal deployment |
| v3                       | Q3 - 2025     | Implement the governance system and permissionless traffic routing                                   | 250,000 $JUNO               | 50% when developement starts, other 50% when development ends                   |
| Ongoing after v3 release | -             | Maintenance fee, if no further developments are needed. Mostly used to pay for infrastructure costs. | 2000 $JUNO / month          | At the end of each month, or using recurring payments on daodao                 |

## Budget handling

With this proposal we are only allocating the budget for the first tranche of v1, which will go directly to the Kintsugi Tech [DAODAO account](https://daodao.zone/dao/osmo1ruxpcljuhpepuw2ywxlqsuhy8u3eulz5hdrsedcvwex8qnsd9yqsqv09j7/treasury).

When portal is live, another proposal will be put up to ask the community to pay the remaining amounts and allocate the budget for v3.

Community has the possibility to check all the transactions we do, and confirm that we are handling the amounts in the best way possible without affecting $JUNO liquidity or price too much.

Community can also already see all our history, and notice how we are compounding validator commissions since years.

### Price disclosure

The budgets above are tought with a price of $0.20 per $JUNO. In case the price changes, the budget can be adjusted according to market conditions with a max multiplier of 4x and min multiplier of 0.25x;

## Transparency

Kintsugi Tech will build the portal completely in public, directly on Juno GitHub repositories. Community will have the chance to track the work done there, and ask us any questions anytime. We'll be reachable over a dedicated channel on Discord, and also other communications channels. Additionally, we are going to share development status updates every few weeks or when there is something intersting to share.
