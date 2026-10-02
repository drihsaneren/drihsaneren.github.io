# Translation brief: drihsaneren.com → English

drihsaneren.com is the site of İhsan Eren, a physiotherapist and intern doctor who provides
**home physiotherapy in Istanbul**. The Turkish "Bilgi köşesi" (health library) pages are
plain-language patient-education guides. We are producing the English version under /en/.
Readers: English-speaking patients and families (often expats) in Istanbul.

## Files
- Input:  `i18n/todo/<name>.json`, a list of `{"id", "kind", "tr"}` units, in page order
  (read them in order, since they form a continuous article).
- Output: `i18n/done/<name>.json`, one JSON object `{"<id>": "<English>", ...}` with **every** id.
- Validate: `python3 i18n/check.py <name>` (run from the scratchpad dir) must report `0 sorun`.
  Fix everything it reports. ("eksik" = missing id, "etiketler farklı" = tags differ,
  "Türkçe karakter kaldı" = Turkish text left, "yer tutucu" = placeholder problem.)
- Tip: build the output as a Python dict in a small script and `json.dump(..., ensure_ascii=False, indent=1)`
  to avoid JSON escaping mistakes with HTML quotes.

## Unit kinds
- `text`: an HTML fragment. Translate the human-readable text only.
  - Keep every tag with **identical attributes** (same `href`, `class`, `target`, `rel`…).
    Do not add, drop or rename tags. You may move an inline tag (`<strong>`, `<em>`, `<a>`, `<b>`,
    `<small>`, `<span>`) to fit English word order, but each tag must still wrap the equivalent words.
  - Keep placeholders like `[[1]]` exactly once each (they stand for icons).
  - Keep entities valid (`&amp;` stays `&amp;`). Do not wrap the result in extra tags.
- `attr`: plain text for an attribute (alt text, aria-label, meta description). No HTML.
  Meta descriptions: keep them to about 150–160 characters.
- `wa`: a pre-filled WhatsApp message the patient sends. Plain text. Pattern:
  "Hello, I would like to book a home assessment and session for my low back pain."
- `ld`: plain text from structured data (JSON-LD). No HTML.

## Style
- **British English** spelling throughout: physiotherapy, orthopaedic, centre, organise, recognise,
  behaviour, programme (plan), tumour, anaemia, oedema, haemorrhage, colour, practise (verb)/practice (noun),
  "towards", "metres".
- Warm, clear, plain-language patient education; address the reader as "you"; short sentences.
  It should read as if written in English originally, not as a literal translation.
- Medical accuracy first. Do **not** add or remove claims, numbers, doses, percentages, time frames,
  warnings or citations. Keep numbers exactly; convert Turkish number style: `%39` → `39%`,
  `1,5` → `1.5`, thousands `1.000` → `1,000`. Keep en dashes in ranges (`2–3`).
- Dates: "28 Eylül 2026" → "28 September 2026".
- Page `<title>` units (they end with ` | İhsan Eren`): English Title Case, keep the ` | İhsan Eren` suffix.
- Exercise names: the natural English name a physiotherapist would use
  (Pelvik eğme → Pelvic tilt, Kedi-deve → Cat–camel, Kuş-köpek → Bird dog, Köprü → Bridge,
  Duvar şınavı → Wall push-up, Havluyla germe → Towel stretch).
- Doses: "10 tekrar, günde 2 kez" → "10 reps, twice a day"; "3 set" → "3 sets"; "30 sn" → "30 s".
- Reference/citation units: keep authors, article titles, journals and URLs unchanged; translate only
  the Turkish words (Erişim → Accessed, Türkçesi → Turkish edition, Londra → London, Cenevre → Geneva).
- Place names: İstanbul → Istanbul.

## Fixed terminology (use exactly)
| Turkish | English |
|---|---|
| Seans planla | Book a session |
| WhatsApp'tan seans planla | Book a session on WhatsApp |
| evde fizyoterapi (hizmeti) | home physiotherapy (service) |
| evde değerlendirme | assessment at home / home assessment |
| Bilgi köşesi | Health library |
| Kendine iyi bak | Look after yourself |
| Tıpta yenilikler | Medical advances |
| Hastalık rehberi | Condition guide |
| Rehabilitasyon rehberi | Rehabilitation guide |
| Sık sorulan sorular | Frequently asked questions |
| Ne zaman hemen başvurmalı? | When to seek help right away |
| hekim / doktor | doctor |
| fizyoterapist | physiotherapist |
| kireçlenme | osteoarthritis |
| bel fıtığı | lumbar disc herniation |
| boyun fıtığı | cervical disc herniation |
| siyatik | sciatica |
| donuk omuz | frozen shoulder |
| omuz sıkışması | shoulder impingement |
| topuk dikeni | heel spur (plantar fasciitis) |
| kemik erimesi | osteoporosis |
| inme (felç) | stroke |
| protez (diz/kalça) | (knee/hip) replacement |
| kortizon iğnesi | cortisone injection |
| kuru iğneleme | dry needling |
| DSÖ | WHO |
| İngiltere kılavuzu (NICE) | UK guideline (NICE) |
| ABD | US |
| 112 | keep "112" (Turkey's emergency number), e.g. "call <strong>112</strong>" |

## Hard rules
- Never use the word "appointment" (the owner does not want it); say "book a session", "session", "visit".
- Never mention any school, university or hospital name in relation to the author.
- The videos on these pages are already in English (Bob & Brad). Where the Turkish text tells readers
  that the videos are English and how to switch on Turkish auto-translated subtitles, drop that advice.
- Keep "İhsan Eren" as is.
