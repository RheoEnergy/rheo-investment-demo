# Rheo Product Demo

A working proof of concept demonstrating how energy infrastructure can become measurable, intelligible, and investable through a modern financial interface.

The demo showcases Rheo's approach to connecting energy data, economic intelligence, and capital - turning real-world energy activity into actionable financial insight.

# Product Demo: https://youtu.be/S9eHrZjEKx8

A single-page proof of concept demonstrating how energy infrastructure can be represented through the clarity and accessibility of a modern financial platform. Built as a lightweight, self-contained application using HTML5, CSS3, and modular ES6 JavaScript, with a deliberately minimal runtime architecture

#Data layer & production swap guide

All sample data lives in `/data` as **JSON** (nested portfolio/asset/network data)
and **CSV** (flat ledger/sensor time-series). The application never reads these
files directly — it goes through a single module:

```
assets/js/data/provider.js   ← the only place that knows where data comes from
```

## How it works today (PoC)

```
DataProvider.getPortfolio()  ──▶ fetch data/portfolio.json
DataProvider.getSettlements()──▶ fetch data/settlements.csv ──▶ parseCSV()
```

`json-adapter.js` and `csv-adapter.js` are thin helpers. Views import
`DataProvider` and call semantic methods like `getAssets()` — they have no
knowledge of files, URLs, or formats.

## Swapping to a database / API in production

Replace the method bodies in `provider.js`. The signatures stay identical, so
**no view code changes**. Example:

```js
// REST API
async getPortfolio() {
  const res = await fetch('https://api.rheo.example/v1/portfolio', {
    headers: { Authorization: `Bearer ${token}` },
  });
  return res.json();
}

// GraphQL
async getAssets() {
  const data = await gql(`{ assets { id name capacityMW utilisationPct } }`);
  return data.assets;
}
```

## Swapping to a blockchain / on-chain indexer

Energy-backed value (Power Credits, settlements, asset ownership) maps naturally
to on-chain records. Point the relevant methods at an indexer or RPC:

```js
  const balance = await contract.balanceOf(account);         // on-chain read
  const series  = await indexer.creditHistory(account);      // subgraph/indexer
  return { balance: Number(balance), series, conversions: ... };
}

// Settlement ledger from event logs
async getSettlements() {
  return indexer.query('SettlementSettled', { first: 50 });
}
```

Because the UI is format-agnostic, you can migrate one method at a time
(e.g. keep marketing data in JSON while settlements come from chain).
