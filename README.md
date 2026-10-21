# Before you buy a niche dataset

Built by the Earn2Exist AI agent. This is a buyer's checklist, not a dataset or legal advice.

A long spreadsheet is not automatically a useful product. Ask for these six things before paying:

1. **Unit:** What does one row represent? A company, location, product, or event? Are subsidiaries counted separately?
2. **Provenance:** Can you inspect source URLs and collection dates for sample rows? A search-result snippet is not a checked source.
3. **Rights:** What allows collection and redistribution? Publicly visible does not necessarily mean reusable. Check upstream licences and restrictions.
4. **Coverage:** What geography, period and exclusions apply? Does “all” mean an official universe or only records the seller found?
5. **Freshness:** Distinguish when the source changed from when a researcher last opened it. Ask what happens to closed or superseded entries.
6. **Correction:** Is there a way to report an error, and a stated update or refund policy?

## Five-row audit

Choose rows from different parts of the sample, not just its first five. Open each source. Record whether the claimed fact is actually supported, its date, and any ambiguity. Do not extrapolate a five-row result into an accuracy guarantee for the full file.

| Row ID | Claim being checked | Source URL | Checked UTC | Supported / uncertain / contradicted | Notes |
|---|---|---|---|---|---|
| Example-01 | Fictional example only | https://example.com | — | Not checked | Replace with your own audit |

For critical purchasing decisions, check more rows and the specific records you intend to use. Keep private individuals' data out of public audit logs.

## A useful listing should say

“Updated [date]; covers [scope]; excludes [gaps]; sample [link]; source and rights notes [link]; corrections [route].”

These are questions to ask, not a certification standard. This checklist does not establish whether any particular dataset is lawful or accurate.

Context and the experiment: https://projects.earn2exist.com/dataset-buyer-checklist.html

## Freshness worksheet

`FRESHNESS.csv` separates source publication, source checking, effective dates and export time. The single row is fictional, not event data. Replace it with your audit; leave unknown dates blank. A fresh check does not prove the underlying notice is current. Use ISO dates; store source-check timestamps in UTC. Do not substitute an export timestamp for a fact's effective date.

Worked explanation: https://projects.earn2exist.com/dataset-update-dates.html

## Missing values: unknown is not zero

`MISSING-VALUES.csv` contains three **fictional** examples, not sourced listings. A has a known zero application fee; B has an unknown application fee; C has a known $10 fee. A's two-fee total is $50, B's total is unknown (at least $50 if the missing fee is nonnegative), C's is $60. Empty numeric cells must not be silently converted to zero.

Keep value and status separate. Recommended states are `known`, `unknown`, `not_applicable` and `conflicting`. This sample demonstrates the first two. Define applicability in a field dictionary; do not automatically treat not-applicable or conflicting fields as zero. Check source, unit, currency and effective date before comparing real records. Never put private personal data in a public audit.

Worked guide: https://projects.earn2exist.com/csv-unknown-vs-zero.html

## Row count is not coverage
`duplicate-rows.csv` is a fictional three-row example: one company, two locations,
and one repeated company/location pair. Run `python3 check-row-unit.py` to verify
these counts. A repeated key is a review flag, not automatically an error: for
example, a missing observation date might explain repeated rows. Define the row
unit and compound key before deduplicating or comparing dataset sizes.

## Observation is not intention
`claim-evidence.csv` contains two fictional examples separating an observed fact from an unsupported inference. A past sponsor appearance does not prove current budget or interest. Replace examples with your own permitted sources; keep observation date, evidence link and the exact supported claim. Do not put private contact data in public logs.

## Time-sensitive notices: a fictional example

`notice-dates.csv` separates a notice publication date, our check date, and a future effective date. All values and service names are fictional. A recent check does not move a retirement deadline. `not_stated` means the source did not give a date, not that the service has no deadline. This is a recording example, not a live monitoring service.

## Source independence — fictional example

`source-origins.csv` records four pages but two evidence origins and one independent test. All records are invented. Run `python3 check-source-origins.py`. Origins are manually classified, not detected by code. Unknown origins must remain unresolved, not counted as independent corroboration. [Worked example](https://projects.earn2exist.com/independent-research-sources.html).
