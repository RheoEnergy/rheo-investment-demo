# Rheo · Energy Capital System — Frontend PoC

A single-page proof-of-concept that makes energy infrastructure feel as
understandable and investable as a modern financial platform. Built with
**vanilla HTML5, CSS3 and ES6 modules** — no build step, no framework.

> Consumer-grade simplicity. Institutional-grade intelligence.

---

## Run it

No install, no bundler. Serve the folder over HTTP (required for ES modules
and `fetch` of the local data files):

```powershell
# Python (recommended)
python -m http.server 8080
```

Then open <http://localhost:8080>.

Any static server works equally well:

```powershell
npx serve .          # Node
php -S localhost:8080
```

> Opening `index.html` directly via `file://` will **not** work — browsers block
> ES module + fetch over the file protocol. Always serve over HTTP.

---

## What's inside

Two integrated systems, one account, served to two roles via a live **role
switcher** in the top bar:

| System | Screens |
| --- | --- |
| **Energy Capital** (Investor) | Overview Dashboard · Portfolio (+ asset detail) · Investment Marketplace (+ project detail) · Power Credits |
| **Intelligent Energy** (Operator) | Operations Dashboard · IoT Energy Sensors (+ sensor detail) · Asset Intelligence · Virtual Power Cloud |
| **Shared** | Welcome / role select · Universal Account |

12 views total. Start on the welcome splash, pick a persona, and the navigation,
dashboards and data reshape to that role.

---

## Project structure

```
index.html                      # entry; ambient background + #app mount
assets/
  css/  tokens.css base.css components.css
  js/
    app.js        # shell, role switcher, routes
    router.js     # hash router with :params
    store.js      # role + pub/sub
    config.js     # FEATURE SWITCHES (charts, map, data source)
    components/   charts.js  map.js  ui.js
    data/         provider.js  json-adapter.js  csv-adapter.js  README.md
    util/         format.js  icons.js
    views/        12 screen modules
data/             portfolio.json assets.json marketplace.json
                  power-credits.json network-nodes.json
                  settlements.csv sensor-readings.csv
```

---

## Feature switches

All in [`assets/js/config.js`](assets/js/config.js).

### 1. Charts — `CONFIG.charts`

| Value | Engine |
| --- | --- |
| `'svg'` *(default)* | Built-in zero-dependency SVG charts. Fully offline. |
| `'cdn'` | [Chart.js](https://www.chartjs.org/) loaded lazily from a CDN for richer interaction. |

```js
export const CONFIG = { charts: 'cdn', /* ... */ };
```

The view code is identical for both — `renderChart(el, spec)` dispatches
internally and falls back to SVG if the CDN fails. To pin Chart.js for
production, install it locally and replace `chartCdnUrl`, or `import` it directly.

### 2. Network map — `CONFIG.map`

| Value | Renderer |
| --- | --- |
| `'node-graph'` *(default)* | Abstract animated topology (golden-angle layout), no dependencies. |
| `'geographic'` | Lat/long equirectangular projection over a graticule. |

```js
export const CONFIG = { map: 'geographic', /* ... */ };
```

For a production geographic map, swap the geographic branch in
[`assets/js/components/map.js`](assets/js/components/map.js) for **Leaflet** or
**Mapbox GL** — the node data already carries `lat`/`lng`.

---

## Sample data → production data

Data lives in `/data` as JSON (nested) and CSV (flat time-series). The app reads
everything through one module — [`assets/js/data/provider.js`](assets/js/data/provider.js).
To point at a database, REST/GraphQL API, or on-chain indexer, replace the method
bodies there; **no view changes required**. See
[`assets/js/data/README.md`](assets/js/data/README.md) for concrete examples.

---

## Upgrading to Tailwind (production)

The CSS is structured for a mechanical migration:

1. Every color/spacing/radius/shadow/font value is a token in
   [`assets/css/tokens.css`](assets/css/tokens.css). Copy them into
   `tailwind.config.js` → `theme.extend`.
2. Component class names (`.glass`, `.metric`, `.btn`, `.grid-4`, `.gap-5`) are
   intentionally utility-shaped, so swapping to Tailwind utilities is incremental.
3. Keep `.glass`, gradient and glow primitives as small `@layer components` until
   fully ported.

No structural rewrite is needed — the design system already lives in tokens.

---

## Notes

- Dark-mode-first, luminescent glass-gradient theme.
- Allocation flow in the Marketplace is a **simulation** — no transactions occur.
- All numbers are illustrative sample data.
