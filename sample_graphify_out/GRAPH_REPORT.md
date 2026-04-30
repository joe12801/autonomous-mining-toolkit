# Graph Report - winboat_mining  (2026-04-30)

## Corpus Check
- 58 files · ~135,175 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1361 nodes · 2800 edges · 19 communities detected
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 151 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 19|Community 19]]

## God Nodes (most connected - your core abstractions)
1. `wa` - 67 edges
2. `oa` - 48 edges
3. `ta` - 44 edges
4. `ia` - 43 edges
5. `ka` - 42 edges
6. `$a` - 40 edges
7. `se()` - 36 edges
8. `ya` - 36 edges
9. `n()` - 35 edges
10. `mi()` - 34 edges

## Surprising Connections (you probably didn't know these)
- `startElectron()` --calls--> `on()`  [INFERRED]
  scripts/dev-server.ts → src/renderer/public/xel/xel.js
- `start()` --calls--> `on()`  [INFERRED]
  scripts/dev-server.ts → src/renderer/public/xel/xel.js
- `refreshApps()` --calls--> `getApps()`  [INFERRED]
  src/renderer/views/Apps.vue → guest_server/main.go
- `applyUpdate()` --calls--> `copy()`  [INFERRED]
  guest_server/main.go → scripts/dev-server.ts
- `applyUpdate()` --calls--> `start()`  [INFERRED]
  guest_server/main.go → scripts/dev-server.ts

## Communities

### Community 0 - "Community 0"
Cohesion: 0.02
Nodes (46): cancelAddCustomApp(), handleLaunchApp(), launchApp(), refreshApps(), removeCustomApp(), resetCustomAppForm(), saveApp(), capitalizeFirstLetter() (+38 more)

### Community 1 - "Community 1"
Cohesion: 0.02
Nodes (73): MessageBus, createWindow(), ComposePortEntry, $(), ae(), an(), at, bi() (+65 more)

### Community 2 - "Community 2"
Cohesion: 0.03
Nodes (9): Ca, Da, $i(), Ma, mi(), Sa, se(), va (+1 more)

### Community 3 - "Community 3"
Cohesion: 0.03
Nodes (9): aa, Fa, ja(), Pa, r(), vi(), wr, Xa (+1 more)

### Community 4 - "Community 4"
Cohesion: 0.04
Nodes (8): $a, ea, fr, getConfig(), Os(), Qa, rr, setConfig()

### Community 5 - "Community 5"
Cohesion: 0.03
Nodes (8): constructor(), ia, is(), na, oa, wi(), #x(), yi()

### Community 6 - "Community 6"
Cohesion: 0.05
Nodes (7): er, lr, mr, n(), pr, ur, xr

### Community 7 - "Community 7"
Cohesion: 0.04
Nodes (4): gr, hn, Hs(), ta

### Community 8 - "Community 8"
Cohesion: 0.03
Nodes (5): cr, dr, ra, tr, Zn()

### Community 9 - "Community 9"
Cohesion: 0.05
Nodes (4): onScroll(), openContextMenu(), Ha, sr

### Community 10 - "Community 10"
Cohesion: 0.05
Nodes (3): Ci(), ki(), wa

### Community 11 - "Community 11"
Cohesion: 0.05
Nodes (3): ka, Nn(), ya

### Community 12 - "Community 12"
Cohesion: 0.05
Nodes (4): hr, La, or, rt()

### Community 13 - "Community 13"
Cohesion: 0.06
Nodes (3): Ei(), jn(), Ua

### Community 14 - "Community 14"
Cohesion: 0.12
Nodes (4): br, clearConfig(), gs(), #v()

### Community 15 - "Community 15"
Cohesion: 0.13
Nodes (13): parseArgon2Hash(), verifyPasswordSecure(), copy(), copyStaticFiles(), restartElectron(), start(), startElectron(), startRenderer() (+5 more)

### Community 16 - "Community 16"
Cohesion: 0.19
Nodes (2): ComposePortMapper, Range

### Community 17 - "Community 17"
Cohesion: 0.31
Nodes (6): Add-AppToListIfValid(), Add-SpacesToCamelCase(), Get-ApplicationIcon(), Get-ApplicationName(), Get-PrettifyName(), Get-UWPApplicationName()

### Community 19 - "Community 19"
Cohesion: 1.0
Nodes (2): openAnchorLink(), openLink()

## Knowledge Gaps
- **3 isolated node(s):** `Metrics`, `RDPStatusResponse`, `Argon2Configuration`
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 16`** (14 nodes): `ComposePortMapper`, `.composeFormat()`, `.constructor()`, `.findGuestPortIndex()`, `.getShortPortMapping()`, `.hasShortPortMapping()`, `.isPortOpen()`, `.pushPortEntry()`, `.setShortPortMapping()`, `Range`, `.constructor()`, `.isRange()`, `.toString()`, `port.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 19`** (3 nodes): `openAnchorLink()`, `openLink()`, `openLink.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `gr` connect `Community 7` to `Community 0`, `Community 1`, `Community 5`, `Community 8`?**
  _High betweenness centrality (0.103) - this node is a cross-community bridge._
- **Why does `ta` connect `Community 7` to `Community 1`, `Community 2`, `Community 3`, `Community 5`, `Community 8`, `Community 9`?**
  _High betweenness centrality (0.058) - this node is a cross-community bridge._
- **Why does `ka` connect `Community 11` to `Community 1`, `Community 2`, `Community 4`, `Community 6`, `Community 8`, `Community 9`, `Community 10`?**
  _High betweenness centrality (0.049) - this node is a cross-community bridge._
- **What connects `Metrics`, `RDPStatusResponse`, `Argon2Configuration` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.02 - nodes in this community are weakly interconnected._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.02 - nodes in this community are weakly interconnected._
- **Should `Community 2` be split into smaller, more focused modules?**
  _Cohesion score 0.03 - nodes in this community are weakly interconnected._