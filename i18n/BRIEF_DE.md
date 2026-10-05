# Translation brief: drihsaneren.com → German (Deutsch)

drihsaneren.com is the site of İhsan Eren, a physiotherapist and final-year medical student who provides
**home physiotherapy in Istanbul**. The Turkish "Bilgi köşesi" pages are plain-language patient-education
guides. We are producing the German version under /de/. Readers: German-speaking patients and families
(often Turkish-German families and expats) in Istanbul. Turkish is the source of truth; the finished English
translation in `i18n/done/<name>.json` may be consulted when the Turkish is ambiguous.

## Workflow (run everything from `/home/claude/kaynak`)
1. `python3 de_tool.py export <name> > <scratch>/de/src_<name>.tsv` and read it **in order**
   (the units form one continuous article). Lines are `id<TAB>kind<TAB>Turkish`.
   In `text` units every HTML tag has been replaced by a numbered placeholder `{1}`, `{2}`, …
2. Write `<scratch>/de/<name>.tsv` (one file per page is easiest):
   ```
   ## <name>
   <id><TAB><German>
   ```
   One line per unit, a real TAB between id and text, no TAB or line break inside the German.
   Every id of the page must be present.
3. `python3 de_tool.py import <scratch>/de/<name>.tsv` (writes `i18n/done_de/<name>.json`), then
   `python3 i18n/check.py --de <name>` must print `0 sorun`. Fix everything either tool reports
   ("eksik" = missing id, "yer tutucular … olmalı" = placeholder numbers wrong, "etiketler farklı" = tags differ,
   "Türkçe karakter kaldı" = Turkish text left, "Termin" = banned word).
4. Do **not** edit any other file, do not run git, do not run build scripts.

`<scratch>` = `/tmp/claude-0/-home-claude-drihsaneren-github-io/b0063e9c-5c48-589d-b9ce-8371b9238425/scratchpad`

Shortcuts in the German column: `==` copies the Turkish source unchanged (names, purely English citations,
units with nothing to translate); `=en` copies the English translation unchanged.

## Unit kinds
- `text`: translate the human-readable text. Each placeholder `{n}` must appear **exactly once**.
  `{1}…{2}` usually are an opening and a closing tag (`<strong>…</strong>`, `<a href>…</a>`): keep the pair
  around the equivalent German words. You may move a pair as a whole to fit German word order; never
  swap the order inside a pair. A lone placeholder is usually `<br>` or an icon: keep its position.
  Placeholders like `[[1]]` (icons) and word templates like `{day}`, `{time}`, `{score}` stay exactly as they are.
  Keep entities valid (`&amp;` stays `&amp;`, `&lt;` stays `&lt;`).
- `attr`: plain text (alt text, aria-label, meta description, title). No HTML. Meta descriptions about 150–160 characters.
  Video button labels must end in ` abspielen`: "Bel ağrısı egzersizleri videosunu oynat" →
  "Video mit Übungen bei Rückenschmerzen abspielen".
- `wa`: a pre-filled WhatsApp message the patient sends. Plain text. Pattern:
  "Merhaba, bel ağrım için evde değerlendirme ve seans planlamak istiyorum." →
  "Hallo, ich möchte wegen meiner Rückenschmerzen eine Untersuchung und Sitzung zu Hause planen."
- `ld`: plain text from structured data. No HTML.

## Style
- Standard German (Germany), new orthography, real umlauts and ß (never ae/oe/ue/ss substitutes).
- Address the reader formally with **Sie**. Warm, clear, plain patient-education language, short sentences.
  It must read as if written in German, not as a word-for-word translation. Prefer the everyday German term
  and add the technical term in brackets where the Turkish does the same.
- Medical accuracy first. Do **not** add or remove claims, numbers, doses, percentages, time frames,
  warnings or citations. Keep numbers exactly. German number style is the same as Turkish (decimal comma
  `1,5`, thousands point `1.000`), only the percent sign moves: `%39` → `39 %` (type a normal space; the
  import tool makes it non-breaking). Keep en dashes in ranges (`2–3`).
- Quotation marks: „…“ (inner ‚…‘). Turkish “…” becomes „…“.
- Dates: "28 Eylül 2026" → "28. September 2026"; "Nisan 2026" → "April 2026".
- Page `<title>` units end with ` | İhsan Eren`: keep that suffix; normal German capitalisation.
- Headings: no full stop, German capitalisation (nouns capitalised only).
- Citations/reference units: keep authors, article titles, journals and URLs unchanged; translate only the
  Turkish words (Erişim → Abgerufen, Türkçesi → türkische Ausgabe, Londra → London, Cenevre → Genf,
  "Kaynak:" → "Quelle:", "Kaynaklar:" → "Quellen:").
- Place names: İstanbul → Istanbul. Keep "İhsan Eren" as is. Emergency number stays **112**.
- Gender: where natural use neutral wording ("ärztliche Hilfe", "physiotherapeutisch"); otherwise the
  generic form ("Arzt", "Physiotherapeut", "Patienten") is fine. No gender asterisk or colon forms.

## Hard rules
- Never use the word **"Termin"** (the owner avoids "randevu"); say "Sitzung planen", "Sitzung", "Besuch".
- Never mention any school, university or hospital name in relation to the author
  (university names inside research news are fine).
- No phone number, no "anrufen" invitations beyond what the Turkish says.
- The videos are in English (Bob & Brad). Where the Turkish tells readers how to switch on Turkish
  auto-translated subtitles, keep the advice but say **Deutsch** instead of Türkçe
  (… Einstellungen → Untertitel → Automatisch übersetzen → Deutsch).
- Needling (Akupunktur, Dry Needling) is never offered as a service; translate such passages faithfully, do not strengthen them.

## Fixed terminology (use exactly)
| Turkish | German |
|---|---|
| Seans planla | Sitzung planen |
| WhatsApp'tan seans planla | Sitzung per WhatsApp planen |
| evde fizyoterapi (hizmeti) | Physiotherapie zu Hause |
| evde değerlendirme | Untersuchung zu Hause |
| ücretsiz ön görüşme | kostenloses Vorgespräch |
| Ana sayfa | Startseite |
| Bilgi köşesi | Ratgeber |
| Kendine iyi bak | Gut für sich sorgen |
| Bilim gündemi | Wissenschaft aktuell |
| Tıpta yenilikler | Neues aus der Medizin |
| Hastalık rehberi | Krankheitsratgeber |
| Rehabilitasyon rehberi | Reha-Ratgeber |
| … rehberi → (link text) | Ratgeber … → (e.g. "Ratgeber Rückenschmerzen →") |
| Sık sorulan sorular | Häufige Fragen |
| Kaynaklar | Quellen |
| Evde egzersiz | Übungen für zu Hause |
| Ne zaman hemen başvurmalı? | Wann sofort zum Arzt? |
| beklemeden bir hekime başvurun | suchen Sie ohne Abwarten ärztliche Hilfe |
| Son güncelleme: 28 Eylül 2026 | Zuletzt aktualisiert: 28. September 2026 |
| hekim / doktor | Arzt / ärztlich |
| fizyoterapist | Physiotherapeut |
| aile hekimi | Hausarzt |
| bel ağrısı | Rückenschmerzen (wo nötig: Kreuzschmerzen / Schmerzen im unteren Rücken) |
| boyun ağrısı | Nackenschmerzen |
| kireçlenme | Arthrose (diz kireçlenmesi → Kniearthrose, kalça … → Hüftarthrose) |
| bel fıtığı | Bandscheibenvorfall der Lendenwirbelsäule (kurz: Bandscheibenvorfall) |
| boyun fıtığı | Bandscheibenvorfall der Halswirbelsäule |
| siyatik | Ischias |
| dar kanal | Spinalkanalstenose |
| donuk omuz | Schultersteife (Frozen Shoulder) |
| omuz sıkışması | Schulter-Impingement |
| rotator manşet yırtığı | Rotatorenmanschettenriss |
| tenisçi dirseği | Tennisarm (Tennisellenbogen) |
| karpal tünel sendromu | Karpaltunnelsyndrom |
| topuk dikeni | Fersensporn (Plantarfasziitis) |
| aşil tendinopatisi | Achillessehnen-Tendinopathie |
| ayak bileği burkulması | Verstauchung des Sprunggelenks |
| menisküs yırtığı | Meniskusriss |
| diz önü ağrısı | vorderer Knieschmerz (patellofemorales Schmerzsyndrom) |
| kalça kırığı | Hüftfraktur (Oberschenkelhalsbruch, wo passend) |
| kemik erimesi | Osteoporose |
| ankilozan spondilit | Morbus Bechterew (ankylosierende Spondylitis) |
| skolyoz | Skoliose |
| çene eklemi | Kiefergelenk (CMD, wo passend) |
| baş dönmesi | Schwindel |
| baş ağrısı | Kopfschmerzen |
| fibromiyalji | Fibromyalgie |
| idrar kaçırma | Harninkontinenz (Blasenschwäche) |
| pelvik taban | Beckenboden |
| inme (felç) | Schlaganfall |
| MS atağı / yorgunluk (MS) | Schub / Fatigue |
| protez (diz/kalça) | (Knie-/Hüft-)Gelenkersatz, künstliches Gelenk |
| düşme önleme | Sturzprävention / Stürze vermeiden |
| kortizon iğnesi | Kortisonspritze |
| kuru iğneleme | Dry Needling |
| manuel terapi | manuelle Therapie |
| ağrı kesici | Schmerzmittel |
| MR | MRT |
| röntgen | Röntgen |
| tomografi (BT) | CT |
| sinir sıkışması | eingeklemmter Nerv |
| uyuşma / karıncalanma | Taubheit / Kribbeln |
| güçsüzlük | Schwäche (Kraftverlust) |
| eklem sertliği | Gelenksteife |
| duruş | Haltung |
| denge | Gleichgewicht |
| kavrama gücü | Griffkraft |
| yürüme hızı | Gehgeschwindigkeit |
| fonksiyonel yaş | funktionelles Alter |
| Günlük Hareket Skalası | Alltagsbewegungs-Skala |
| otur-kalk testi | Sitz-Steh-Test |
| DSÖ | WHO |
| İngiltere kılavuzu (NICE) | britische Leitlinie (NICE) |
| kılavuz | Leitlinie |
| derleme / sistematik derleme | Übersichtsarbeit / systematische Übersichtsarbeit |
| Cochrane derlemesi | Cochrane-Review |
| randomize kontrollü çalışma | randomisierte kontrollierte Studie |
| ABD | USA |
| İngiltere | Großbritannien (or "England" when the Turkish clearly means England) |

Doses and exercise wording:
| Turkish | German |
|---|---|
| 10 tekrar, günde 2–3 kez | 10 Wiederholungen, 2–3-mal täglich |
| günde 2 kez | 2-mal täglich |
| 3 set | 3 Sätze |
| 2 tur | 2 Runden |
| 30 sn / 5 saniye tutun | 30 Sek. / 5 Sekunden halten |
| 10 dk | 10 Min. |
| her iki taraf / her bacak | beide Seiten / jedes Bein |
| Köprü | Brücke |
| Pelvik eğme | Beckenkippen |
| Kedi-deve | Katze-Kuh |
| Kuş-köpek | Vierfüßlerstand mit Arm- und Beinheben (Bird Dog) |
| Diz göğse çekme | Knie zur Brust ziehen |
| Çene içe çekme | Kinn einziehen |
| Kürek kemiği sıkıştırma | Schulterblätter zusammenziehen |
| Duvar şınavı | Wandliegestütz |
| Tek ayak üzerinde durma | Einbeinstand |
| Sandalyeden kalkıp oturma | Aufstehen und Hinsetzen vom Stuhl |
| Topuk yükseltme | Fersenheben |
| Havluyla germe | Dehnung mit dem Handtuch |
| Sarkaç | Pendelübung |
| germe | Dehnung |
| güçlendirme | Kräftigung |

Before you start, read `i18n/done_de/_common.json` (strings shared by all pages, already translated) and reuse its
wording for exercise names, section headings and stock phrases. `i18n/done_de/fb1.json` and
`i18n/done_de/bilgi.json` show more finished German for tone and terminology (grep them for a term when unsure).
