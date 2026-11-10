# -*- coding: utf-8 -*-
# Yeni rehber (73): Diş sıkma ve gıcırdatma (bruksizm). self15_part.py'den sonra exec edilir. Video yok.
# Kullanıcı isteği (7–8 Kasım 2026): ders niteliğinde, kapsamlı; Cihan Hoca (Prof. Dr. Cihan Aksoy) tanıtımı; dört alan (diş, eklem, boyun, beyin);
# çene sesi, dilde diş izleri, kuvvet, ruhsal etkenler, plak, ilaçlar (etken madde adıyla, marka adı yok), botulinum toksini çizimi, tarihçe, klinik gözlem kutusu.
# Kaynaklar ve notlar: denetim/notlar_bruksizm.md (7–8 Kasım 2026'da okundu).

_ex2("br_breath", "plb", "Gevşeme nefesi", "Rahatça oturun; omuzlarınızı ve çenenizi gevşetin, dişleriniz birbirine değmesin. Burnunuzdan sakin bir nefes alın ve yavaşça verin. Nefes verirken yüzünüzün iki yanındaki kasların ve şakaklarınızın yumuşadığını hissedin.", "5–10 nefes, günde birkaç kez")
SV["br_breath"] = SV["br_breath"].replace("<figcaption>Büzük dudak nefesi</figcaption>", "<figcaption>Gevşeme nefesi</figcaption>")


# Yeni egzersizler (9 Kasım 2026, kullanıcı isteği): sağa sola kaydırma (önden görünüş) ve öne itme (yandan). Dozlar: Guy's and St Thomas' NHS 4454/VER4.
_BRF = ('<path class="fig" d="M38 62 C33 40 40 20 60 20 C80 20 87 40 82 62"/>'
        '<circle cx="51" cy="44" r="2.6" fill="#2A6F6B"/><circle cx="69" cy="44" r="2.6" fill="#2A6F6B"/>'
        '<path class="fig" d="M52 88 L50 108 M68 88 L70 108"/>')
SV["br_side"] = fig(GRD + _BRF +
    '<g><animateTransform attributeName="transform" type="translate" values="0 0;-6 0;0 0;6 0;0 0" keyTimes="0;0.25;0.5;0.75;1" dur="4.4s" repeatCount="indefinite" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1;0.45 0 0.55 1;0.45 0 0.55 1"/>'
    '<path class="fig hl" d="M40 60 Q42 86 60 88 Q78 86 80 60"/></g>'
    '<path d="M32 74 H20 M24 70 L20 74 L24 78 M88 74 H100 M96 70 L100 74 L96 78" stroke="#C8963E" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
    "Çeneyi sağa sola kaydırma")
SV["br_fwd"] = fig(GRD + SKULL + TONGUE +
    '<g><animateTransform attributeName="transform" type="translate" values="0 0;6 1;0 0" keyTimes="0;0.5;1" dur="3.6s" repeatCount="indefinite" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"/>'
    + JAW + '</g>'
    '<path d="M86 84 H100 M96 80 L100 84 L96 88" stroke="#C8963E" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"><animate attributeName="opacity" values="0.2;1;0.2" dur="1.8s" repeatCount="indefinite"/></path>',
    "Alt çeneyi öne itme")
EXT["br_side"] = ("Çeneyi sağa sola kaydırma", "Ağzınızı hafifçe aralayın. Alt çenenizi yavaşça sola kaydırın, 10 saniye tutun ve ortaya dönün; aynısını sağa yapın. Hareketin dudaklarınızdan değil çenenizden geldiğinden emin olun ve ağrısız aralıkta kalın.", "5–10 tekrar, günde 5–8 kez")
EXT["br_fwd"] = ("Alt çeneyi öne itme", "Ağzınızı hafifçe aralayın. Çenenizi öne doğru itin; alt çeneniz üst çenenizin önüne geçsin. 5–10 saniye tutun ve dinlenme pozisyonuna dönün. Ağrı ya da takılma olursa zorlamayın.", "5–10 tekrar, günde 5–8 kez")

# Dört alan çizimi (diş, eklem, boyun, beyin) — numaralar dilden bağımsız, açıklamalar HTML'de
_BR_HEAD = ('<path d="M84 226 L80 180 C60 160 50 130 54 100 C58 58 92 30 134 30 C174 30 198 58 198 90 L202 104 L214 124 L203 131 L206 141 L202 149 L204 157 L196 168 C184 172 166 172 156 176 L160 226" '
            'fill="none" stroke="#2A6F6B" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>'
            '<ellipse cx="122" cy="114" rx="8" ry="13" fill="none" stroke="#2A6F6B" stroke-width="2.5"/>'
            '<path d="M176 98 Q182 94 188 98" fill="none" stroke="#2A6F6B" stroke-width="2.5" stroke-linecap="round"/>'
            '<path d="M130 106 Q152 100 178 108" fill="none" stroke="#8FA8A2" stroke-width="2.5" stroke-linecap="round"/>'
            '<path d="M130 124 L137 160 Q140 166 150 166 L194 166" fill="none" stroke="#8FA8A2" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>'
            '<path d="M186 148 H203" stroke="#8FA8A2" stroke-width="2.5" stroke-linecap="round"/>')

def _br_mark(x, y, n, col, delay):
    return (f'<circle cx="{x}" cy="{y}" r="10" fill="{col}"><animate attributeName="r" values="10;12;10" dur="2.4s" begin="{delay}s" repeatCount="indefinite"/></circle>'
            f'<text x="{x}" y="{y + 4.5}" text-anchor="middle" font-size="13" font-weight="700" fill="#FFFFFF" font-family="sans-serif">{n}</text>')

BR_FIG_AREAS = ('<figure class="br-fig"><svg viewBox="0 0 240 230" role="img" aria-labelledby="br-fa-t"><title id="br-fa-t">Diş sıkmanın etkilediği dört alan: beyin, eklem, diş ve boyun</title>'
                + _BR_HEAD +
                '<path d="M146 170 C138 186 128 194 122 198" fill="none" stroke="#C8963E" stroke-width="2.5" stroke-dasharray="4 4" stroke-linecap="round"/>'
                '<path d="M112 76 C120 92 132 104 138 112" fill="none" stroke="#C8963E" stroke-width="2.5" stroke-dasharray="4 4" stroke-linecap="round"/>'
                + _br_mark(108, 66, 1, "#2A6F6B", 0) + _br_mark(140, 118, 2, "#C8963E", 0.6) + _br_mark(190, 148, 3, "#2A6F6B", 1.2) + _br_mark(120, 202, 4, "#C8963E", 1.8) +
                '</svg></figure>')

# Botulinum toksini uygulama bölgeleri — şematik
def _br_dot(x, y, d):
    return (f'<circle cx="{x}" cy="{y}" r="3.6" fill="#7A2E2E"><animate attributeName="opacity" values="1;.3;1" dur="2s" begin="{d}s" repeatCount="indefinite"/></circle>')

BR_FIG_BOTOX = ('<figure class="br-fig"><svg viewBox="0 0 240 230" role="img" aria-labelledby="br-fb-t"><title id="br-fb-t">Şakak kası ve çiğneme kası: botulinum toksini uygulamasında kullanılan kaslar (şematik)</title>'
                '<path d="M120 102 C108 74 126 46 160 46 C186 48 194 70 186 92 C170 100 146 104 126 106 Z" fill="#C8963E" fill-opacity=".28" stroke="#C8963E" stroke-width="2" stroke-linejoin="round"/>'
                '<path d="M138 110 L176 112 L180 162 L146 164 Z" fill="#2A6F6B" fill-opacity=".28" stroke="#2A6F6B" stroke-width="2" stroke-linejoin="round"/>'
                + _BR_HEAD +
                _br_dot(140, 76, 0) + _br_dot(160, 64, .3) + _br_dot(176, 82, .6) + _br_dot(152, 126, .9) + _br_dot(166, 134, 1.2) + _br_dot(156, 150, 1.5) +
                '</svg></figure>')

BR_FIG_TONGUE = '<figure class="br-fig"><svg viewBox="0 0 240 200" role="img" aria-labelledby="br-ft-t"><title id="br-ft-t">Dilde diş izleri: sıkma sırasında dişlere itilen dilin kenarlarında oluşan çentikler (şematik, üstten görünüş)</title><path d="M120.0 48.0 L120.0 48.0 L126.7 48.5 L130.0 49.0 L132.4 49.5 L134.5 50.0 L136.3 50.5 L138.0 51.0 L139.5 51.5 L141.1 52.0 L142.5 52.5 L144.0 53.0 L145.5 53.5 L147.0 54.0 L148.5 54.5 L150.0 55.0 L151.6 55.5 L153.1 56.0 L154.7 56.5 L156.2 57.0 L157.7 57.5 L159.3 58.0 L160.6 58.5 L161.4 59.0 L161.9 59.5 L162.1 60.0 L162.4 60.5 L162.6 61.0 L162.8 61.5 L163.1 62.0 L163.4 62.5 L163.8 63.0 L164.2 63.5 L164.6 64.0 L165.2 64.5 L165.7 65.0 L166.4 65.5 L167.1 66.0 L167.9 66.5 L168.7 67.0 L169.6 67.5 L170.6 68.0 L171.6 68.5 L172.4 69.0 L173.3 69.5 L174.3 70.0 L175.2 70.5 L176.2 71.0 L176.7 71.5 L177.1 72.0 L177.5 72.5 L177.8 73.0 L177.7 73.5 L177.4 74.0 L177.2 74.5 L177.0 75.0 L176.8 75.5 L176.7 76.0 L176.7 76.5 L176.7 77.0 L176.7 77.5 L176.9 78.0 L177.1 78.5 L177.4 79.0 L177.7 79.5 L178.2 80.0 L178.7 80.5 L179.3 81.0 L179.9 81.5 L180.6 82.0 L181.4 82.5 L182.2 83.0 L183.1 83.5 L184.0 84.0 L184.9 84.5 L185.8 85.0 L186.2 85.5 L186.5 86.0 L186.8 86.5 L187.1 87.0 L187.3 87.5 L187.0 88.0 L186.7 88.5 L186.5 89.0 L186.2 89.5 L186.1 90.0 L185.9 90.5 L185.8 91.0 L185.8 91.5 L185.9 92.0 L186.0 92.5 L186.2 93.0 L186.5 93.5 L186.8 94.0 L187.3 94.5 L187.8 95.0 L188.4 95.5 L189.0 96.0 L189.7 96.5 L190.5 97.0 L191.3 97.5 L192.1 98.0 L193.0 98.5 L193.8 99.0 L194.6 99.5 L194.8 100.0 L195.1 100.5 L195.2 101.0 L195.4 101.5 L194.9 102.0 L194.5 102.5 L194.1 103.0 L193.6 103.5 L193.3 104.0 L192.9 104.5 L192.7 105.0 L192.4 105.5 L192.3 106.0 L192.2 106.5 L192.2 107.0 L192.2 107.5 L192.3 108.0 L192.6 108.5 L192.8 109.0 L193.2 109.5 L193.6 110.0 L194.1 110.5 L194.6 111.0 L195.1 111.5 L195.7 112.0 L196.4 112.5 L197.0 113.0 L197.7 113.5 L197.7 114.0 L197.8 114.5 L197.8 115.0 L197.8 115.5 L197.9 116.0 L197.9 116.5 L197.9 117.0 L198.0 117.5 L198.0 118.0 L198.0 118.5 L198.0 119.0 L198.0 119.5 L198.0 120.0 L198.0 120.5 L198.0 121.0 L198.0 121.5 L198.0 122.0 L198.0 122.5 L198.0 123.0 L198.0 123.5 L198.0 124.0 L198.0 124.5 L198.0 125.0 L198.0 125.5 L198.0 126.0 L198.0 126.5 L198.0 127.0 L198.0 127.5 L198.0 128.0 L198.0 128.5 L198.0 129.0 L198.0 129.5 L198.0 130.0 L198.0 130.5 L198.0 131.0 L198.0 131.5 L198.0 132.0 L198.0 132.5 L198.0 133.0 L198.0 133.5 L198.0 134.0 L198.0 134.5 L198.0 135.0 L198.0 135.5 L198.0 136.0 L198.0 136.5 L198.0 137.0 L198.0 137.5 L198.0 138.0 L198.0 138.5 L198.0 139.0 L198.0 139.5 L198.0 140.0 L198.0 140.5 L198.0 141.0 L198.0 141.5 L198.0 142.0 L198.0 142.5 L198.0 143.0 L198.0 143.5 L198.0 144.0 L198.0 144.5 L198.0 145.0 L198.0 145.5 L198.0 146.0 L198.0 146.5 L198.0 147.0 L198.0 147.5 L198.0 148.0 L198.0 148.5 L198.0 149.0 L198.0 149.5 L198.0 150.0 L198.0 150.5 L198.0 151.0 L198.0 151.5 L198.0 152.0 L198.0 152.5 L198.0 153.0 L198.0 153.5 L198.0 154.0 L198.0 154.5 L198.0 155.0 L198.0 155.5 L198.0 156.0 L198.0 156.5 L198.0 157.0 L198.0 157.5 L198.0 158.0 L198.0 158.5 L198.0 159.0 L198.0 159.5 L198.0 160.0 L198.0 160.5 L197.9 161.0 L197.9 161.5 L197.8 162.0 L197.6 162.5 L197.5 163.0 L197.3 163.5 L197.1 164.0 L196.8 164.5 L196.5 165.0 L196.2 165.5 L195.9 166.0 L195.5 166.5 L195.1 167.0 L194.7 167.5 L194.2 168.0 L193.7 168.5 L193.2 169.0 L192.6 169.5 L192.0 170.0 L191.4 170.5 L190.7 171.0 L190.0 171.5 L189.2 172.0 L188.4 172.5 L187.5 173.0 L186.7 173.5 L185.7 174.0 L184.7 174.5 L183.7 175.0 L182.6 175.5 L181.5 176.0 L180.3 176.5 L179.0 177.0 L177.7 177.5 L176.3 178.0 L174.8 178.5 L173.2 179.0 L171.6 179.5 L169.8 180.0 L168.0 180.5 L166.0 181.0 L163.9 181.5 L161.6 182.0 L159.1 182.5 L156.4 183.0 L153.4 183.5 L150.0 184.0 L146.1 184.5 L141.4 185.0 L135.2 185.5 L104.8 185.5 L98.6 185.0 L93.9 184.5 L90.0 184.0 L86.6 183.5 L83.6 183.0 L80.9 182.5 L78.4 182.0 L76.1 181.5 L74.0 181.0 L72.0 180.5 L70.2 180.0 L68.4 179.5 L66.8 179.0 L65.2 178.5 L63.7 178.0 L62.3 177.5 L61.0 177.0 L59.7 176.5 L58.5 176.0 L57.4 175.5 L56.3 175.0 L55.3 174.5 L54.3 174.0 L53.3 173.5 L52.5 173.0 L51.6 172.5 L50.8 172.0 L50.0 171.5 L49.3 171.0 L48.6 170.5 L48.0 170.0 L47.4 169.5 L46.8 169.0 L46.3 168.5 L45.8 168.0 L45.3 167.5 L44.9 167.0 L44.5 166.5 L44.1 166.0 L43.8 165.5 L43.5 165.0 L43.2 164.5 L42.9 164.0 L42.7 163.5 L42.5 163.0 L42.4 162.5 L42.2 162.0 L42.1 161.5 L42.1 161.0 L42.0 160.5 L42.0 160.0 L42.0 159.5 L42.0 159.0 L42.0 158.5 L42.0 158.0 L42.0 157.5 L42.0 157.0 L42.0 156.5 L42.0 156.0 L42.0 155.5 L42.0 155.0 L42.0 154.5 L42.0 154.0 L42.0 153.5 L42.0 153.0 L42.0 152.5 L42.0 152.0 L42.0 151.5 L42.0 151.0 L42.0 150.5 L42.0 150.0 L42.0 149.5 L42.0 149.0 L42.0 148.5 L42.0 148.0 L42.0 147.5 L42.0 147.0 L42.0 146.5 L42.0 146.0 L42.0 145.5 L42.0 145.0 L42.0 144.5 L42.0 144.0 L42.0 143.5 L42.0 143.0 L42.0 142.5 L42.0 142.0 L42.0 141.5 L42.0 141.0 L42.0 140.5 L42.0 140.0 L42.0 139.5 L42.0 139.0 L42.0 138.5 L42.0 138.0 L42.0 137.5 L42.0 137.0 L42.0 136.5 L42.0 136.0 L42.0 135.5 L42.0 135.0 L42.0 134.5 L42.0 134.0 L42.0 133.5 L42.0 133.0 L42.0 132.5 L42.0 132.0 L42.0 131.5 L42.0 131.0 L42.0 130.5 L42.0 130.0 L42.0 129.5 L42.0 129.0 L42.0 128.5 L42.0 128.0 L42.0 127.5 L42.0 127.0 L42.0 126.5 L42.0 126.0 L42.0 125.5 L42.0 125.0 L42.0 124.5 L42.0 124.0 L42.0 123.5 L42.0 123.0 L42.0 122.5 L42.0 122.0 L42.0 121.5 L42.0 121.0 L42.0 120.5 L42.0 120.0 L42.0 119.5 L42.0 119.0 L42.0 118.5 L42.0 118.0 L42.0 117.5 L42.1 117.0 L42.1 116.5 L42.1 116.0 L42.2 115.5 L42.2 115.0 L42.2 114.5 L42.3 114.0 L42.3 113.5 L43.0 113.0 L43.6 112.5 L44.3 112.0 L44.9 111.5 L45.4 111.0 L45.9 110.5 L46.4 110.0 L46.8 109.5 L47.2 109.0 L47.4 108.5 L47.7 108.0 L47.8 107.5 L47.8 107.0 L47.8 106.5 L47.7 106.0 L47.6 105.5 L47.3 105.0 L47.1 104.5 L46.7 104.0 L46.4 103.5 L45.9 103.0 L45.5 102.5 L45.1 102.0 L44.6 101.5 L44.8 101.0 L44.9 100.5 L45.2 100.0 L45.4 99.5 L46.2 99.0 L47.0 98.5 L47.9 98.0 L48.7 97.5 L49.5 97.0 L50.3 96.5 L51.0 96.0 L51.6 95.5 L52.2 95.0 L52.7 94.5 L53.2 94.0 L53.5 93.5 L53.8 93.0 L54.0 92.5 L54.1 92.0 L54.2 91.5 L54.2 91.0 L54.1 90.5 L53.9 90.0 L53.8 89.5 L53.5 89.0 L53.3 88.5 L53.0 88.0 L52.7 87.5 L52.9 87.0 L53.2 86.5 L53.5 86.0 L53.8 85.5 L54.2 85.0 L55.1 84.5 L56.0 84.0 L56.9 83.5 L57.8 83.0 L58.6 82.5 L59.4 82.0 L60.1 81.5 L60.7 81.0 L61.3 80.5 L61.8 80.0 L62.3 79.5 L62.6 79.0 L62.9 78.5 L63.1 78.0 L63.3 77.5 L63.3 77.0 L63.3 76.5 L63.3 76.0 L63.2 75.5 L63.0 75.0 L62.8 74.5 L62.6 74.0 L62.3 73.5 L62.2 73.0 L62.5 72.5 L62.9 72.0 L63.3 71.5 L63.8 71.0 L64.8 70.5 L65.7 70.0 L66.7 69.5 L67.6 69.0 L68.4 68.5 L69.4 68.0 L70.4 67.5 L71.3 67.0 L72.1 66.5 L72.9 66.0 L73.6 65.5 L74.3 65.0 L74.8 64.5 L75.4 64.0 L75.8 63.5 L76.2 63.0 L76.6 62.5 L76.9 62.0 L77.2 61.5 L77.4 61.0 L77.6 60.5 L77.9 60.0 L78.1 59.5 L78.6 59.0 L79.4 58.5 L80.7 58.0 L82.3 57.5 L83.8 57.0 L85.3 56.5 L86.9 56.0 L88.4 55.5 L90.0 55.0 L91.5 54.5 L93.0 54.0 L94.5 53.5 L96.0 53.0 L97.5 52.5 L98.9 52.0 L100.5 51.5 L102.0 51.0 L103.7 50.5 L105.5 50.0 L107.6 49.5 L110.0 49.0 L113.3 48.5 L120.0 48.0 Z" fill="#EDB8AE" stroke="#B5655A" stroke-width="2.2" stroke-linejoin="round"/><path d="M120 76 V160" stroke="#C98A80" stroke-width="2" stroke-linecap="round" fill="none"/><rect x="107.0" y="21.2" width="10" height="11" rx="3.5" transform="rotate(-9.6 112.0 26.7)" fill="#FFFFFF" stroke="#8FA8A2" stroke-width="2"/><rect x="123.0" y="21.2" width="10" height="11" rx="3.5" transform="rotate(9.6 128.0 26.7)" fill="#FFFFFF" stroke="#8FA8A2" stroke-width="2"/><rect x="92.0" y="26.1" width="10" height="11" rx="3.5" transform="rotate(-25.8 97.0 31.6)" fill="#FFFFFF" stroke="#8FA8A2" stroke-width="2"/><rect x="138.0" y="26.1" width="10" height="11" rx="3.5" transform="rotate(25.8 143.0 31.6)" fill="#FFFFFF" stroke="#8FA8A2" stroke-width="2"/><rect x="78.0" y="34.9" width="10" height="11" rx="3.5" transform="rotate(-37.9 83.0 40.4)" fill="#FFFFFF" stroke="#8FA8A2" stroke-width="2"/><rect x="152.0" y="34.9" width="10" height="11" rx="3.5" transform="rotate(37.9 157.0 40.4)" fill="#FFFFFF" stroke="#8FA8A2" stroke-width="2"/><rect x="65.0" y="46.8" width="10" height="11" rx="3.5" transform="rotate(-46.5 70.0 52.3)" fill="#FFFFFF" stroke="#8FA8A2" stroke-width="2"/><rect x="165.0" y="46.8" width="10" height="11" rx="3.5" transform="rotate(46.5 170.0 52.3)" fill="#FFFFFF" stroke="#8FA8A2" stroke-width="2"/><rect x="52.5" y="59.7" width="13" height="11" rx="3.5" transform="rotate(-52.1 59.0 65.2)" fill="#FFFFFF" stroke="#8FA8A2" stroke-width="2"/><rect x="174.5" y="59.7" width="13" height="11" rx="3.5" transform="rotate(52.1 181.0 65.2)" fill="#FFFFFF" stroke="#8FA8A2" stroke-width="2"/><rect x="42.5" y="73.6" width="13" height="11" rx="3.5" transform="rotate(-56.2 49.0 79.1)" fill="#FFFFFF" stroke="#8FA8A2" stroke-width="2"/><rect x="184.5" y="73.6" width="13" height="11" rx="3.5" transform="rotate(56.2 191.0 79.1)" fill="#FFFFFF" stroke="#8FA8A2" stroke-width="2"/><rect x="33.5" y="87.9" width="13" height="11" rx="3.5" transform="rotate(-59.3 40.0 93.4)" fill="#FFFFFF" stroke="#8FA8A2" stroke-width="2"/><rect x="193.5" y="87.9" width="13" height="11" rx="3.5" transform="rotate(59.3 200.0 93.4)" fill="#FFFFFF" stroke="#8FA8A2" stroke-width="2"/><rect x="25.5" y="102.0" width="13" height="11" rx="3.5" transform="rotate(-61.6 32.0 107.5)" fill="#FFFFFF" stroke="#8FA8A2" stroke-width="2"/><rect x="201.5" y="102.0" width="13" height="11" rx="3.5" transform="rotate(61.6 208.0 107.5)" fill="#FFFFFF" stroke="#8FA8A2" stroke-width="2"/><path d="M160.0 80.0 L176.0 74.0 M172.4 78.8 L176.0 74.0 L170.2 72.8" stroke="#C8963E" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"><animate attributeName="opacity" values=".45;1;.45" dur="2.2s" repeatCount="indefinite"/></path><path d="M80.0 80.0 L64.0 74.0 M69.8 72.8 L64.0 74.0 L67.6 78.8" stroke="#C8963E" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"><animate attributeName="opacity" values=".45;1;.45" dur="2.2s" repeatCount="indefinite"/></path><path d="M170.0 104.0 L186.0 100.0 M181.9 104.3 L186.0 100.0 L180.4 98.1" stroke="#C8963E" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"><animate attributeName="opacity" values=".45;1;.45" dur="2.2s" repeatCount="indefinite"/></path><path d="M70.0 104.0 L54.0 100.0 M59.6 98.1 L54.0 100.0 L58.1 104.3" stroke="#C8963E" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"><animate attributeName="opacity" values=".45;1;.45" dur="2.2s" repeatCount="indefinite"/></path></svg></figure>'

BR_FAQ = [
 ("Plak takarsam diş sıkmam geçer mi?", "Genellikle geçmez. Beş çalışmayı inceleyen Cochrane derlemesi, plağın uyku bruksizmini azalttığını gösterecek yeterli kanıt bulamadı; plak daha çok dişleri aşınmaya karşı koruyabilir. Sıkma sürebileceği için kaslar ve eklem üzerindeki yük devam edebilir. Bu yüzden plak tek başına değil; stres yönetimi, alışkanlıkları değiştirme ve kas çalışmasıyla birlikte düşünülür. Plağın türüne ve ne zaman takılacağına diş hekiminiz karar verir."),
 ("Dilimin kenarında diş izleri var; diş sıktığım anlamına mı gelir?", "Olabilir. Türkiye'de 98 hastanın incelendiği 2026 tarihli bir çalışmada, uyku testiyle doğrulanmış bruksizmi olanların %65,3'ünde dil kenarında diş izleri vardı; yalnızca kendisi diş sıktığını söyleyenlerde bu oran %34,7 idi. Yanağın iç yüzünde dişlerin hizasında beyaz bir çizgi de sırasıyla %75,5 ve %42,9 oranında görüldü. Bu işaretler tek başına tanı koydurmaz: Dil ve yanak izleri yutkunma gibi olağan ağız hareketlerinden de kaynaklanabilir. Dildeki izler ayrıca dilin geniş olmasıyla ya da dişlerdeki yapısal farklılıklarla ilgili olabilir ve bir çalışmada ağır uyku apnesiyle ilişkili bulundu. Diş hekimi muayenesiyle birlikte değerlendirilir; horlamanız da varsa hekiminize söyleyin."),
 ("Çenemden klik sesi geliyor; diş sıkmayla ilgisi var mı?", "Klik sesi, çene ekleminin içindeki diskin ağız açılıp kapanırken yer değiştirmesiyle ilgili olabilir. Ağrısız klik sesi sık görülür ve tek başına tedavi gerektirmez. Sesle birlikte ağrı, ağız açmada kısıtlılık ya da takılma varsa değerlendirme yapılmalıdır. Diş sıkma, çiğneme kası ve çene eklemi ağrısı için bir risk etkeni olabilir; ayrıntılar için <a href=\"cene-eklemi.html\">çene eklemi rahatsızlıkları</a> rehberine bakabilirsiniz."),
 ("Stres diş sıkmaya neden olur mu?", "Stres ve kaygı en sık sayılan etkenler arasında. Altı çalışmayı inceleyen (üçü meta-analizde) bir sistematik derlemede, stresi olanlarda bruksizm olasılığı yaklaşık iki kat (OR 2,07) daha yüksekti; ancak kanıtın kesinliği düşüktü. Cihan Hoca'nın da yazarları arasında olduğu ve çene eklemi polikliniğine başvuran 273 hastanın incelendiği çalışmada, kadın olmak, sosyal desteğin yetersiz olması ve kas kaynaklı yüz ağrısı, kaygı ya da depresyon olasılığını artırıyordu; yazarlar tedavi planlanırken kaygı ve depresyonun da göz önünde bulundurulmasını önerdi."),
 ("Botulinum toksini iğnesi diş sıkmayı tedavi eder mi?", "Botulinum toksini, yalnızca hekimlerin uyguladığı bir iğnedir ve diş sıkmada çiğneme kasına ve şakak kasına yapılır. 14 sistematik derlemeyi inceleyen 2025 tarihli bir genel değerlendirmede ağrıda azalma 10, diş sıkma olaylarında azalma 7, en büyük ısırma kuvvetinde azalma 5 derlemede bildirildi. Ancak derlemelerin hepsinin güvenilirliği düşük ya da kritik düzeyde düşüktü ve kesin bir sonuç çıkarılamadı. Uyku testiyle yapılan 20 kişilik küçük bir çalışmada ise diş sıkma olaylarının sıklığı değişmedi, kasılmaların şiddeti azaldı; yani iğne asıl olarak kasın gücünü etkiliyor olabilir. Etkisi birkaç ay sürer. Uygun olup olmadığına hekiminiz karar verir."),
 ("Diş sıkma için ilaç kullanmam gerekir mi?", "Çoğu kişide gerekmez. Uyku bruksizminde ilaçları inceleyen Cochrane derlemesi, yedi küçük çalışmada ilaçların etkili olduğunu gösterecek yeterli kanıt bulamadı; bazı ilaçlarda yan etkiler görüldü. Sinir ağrısında kullanılan bir ilaç olan gabapentin, 20 kişilik küçük bir çalışmada gece çiğneme kası etkinliğini plak kadar azalttı. Gabapentinle aynı ilaç grubundan olan pregabalin için yer verebildiğimiz tek yayın, kaygı bozukluğu olan ve gün içinde diş sıkan tek bir hastanın olgu sunumu. Bu ilaçlar yalnızca uzman hekim reçetesiyle ve kontrolle kullanılır; kendi başınıza kullanmayın. Hangisinin uygun olduğunu hekiminize sorun."),
 ("Çocuğum gece diş gıcırdatıyor; ne yapmalıyım?", "Diş gıcırdatma çocuklarda da görülebilir. Çoğunlukla süt dişleri ya da kalıcı dişler ilk çıktıktan sonra ortaya çıkar ve kalıcı dişler tamamen oluştuktan sonra genellikle durur. Endişeleniyorsanız, özellikle çocuğunuzun uykusunu etkiliyorsa, bir hekime başvurun; dişlerde aşınma ya da ağrı varsa diş hekimi de değerlendirebilir."),
 ("Diş sıkma tamamen geçer mi?", "Şu an dünyada diş sıkmayı kesin olarak ortadan kaldırdığı gösterilmiş bir tedavi yok. Derlemelerde plak, biyolojik geri bildirim ve botulinum toksini kısa vadede kesin bir etkinlik göstermedi; bazı ilaçlar uykudaki diş sıkma olaylarını azaltmış olsa da yan etkileri nedeniyle temkin gerekiyor ve bu derlemelerin güvenilirliği çok düşük. Bruksizm esas olarak beyin tarafından düzenlenen bir davranış olduğu için amaç; dişleri, eklemi ve kasları korumak, tetikleyicileri azaltmak ve yakınmaları hafifletmektir. Bu da çoğu zaman birden fazla branşın birlikte çalışmasını gerektirir."),
]

BR_SRC = [
 "Lobbezoo F, Ahlberg J, Raphael KG, et al. " + ext("https://pure.uva.nl/ws/files/31008698/Lobbezoo_et_al_2018_Journal_of_Oral_Rehabilitation.pdf", "International consensus on the assessment of bruxism: report of a work in progress") + ". J Oral Rehabil. 2018;45(11):837-844.",
 "Zieliński G, Pająk A, Wójcicki M. " + ext("https://mdpi.com/2077-0383/13/14/4259", "Global prevalence of sleep bruxism and awake bruxism in pediatric and adult populations: a systematic review and meta-analysis") + ". J Clin Med. 2024;13(14):4259.",
 "Nishigawa K, et al. " + ext("https://acnpsearch.tweb-dev.unibo.it/singlejournalindex/82533805", "Quantitative study of bite force during sleep associated bruxism") + ". J Oral Rehabil. 2001;28(5):485-491.",
 "Guinness World Records. " + ext("https://www.guinnessworldrecords.com/world-records/75273-strongest-human-bite", "Strongest human bite") + ".",
 "Diraçoğlu D, Alptekin K, Çifter ED, Güçlü B, Karan A, Aksoy C. " + ext("https://research.bau.edu.tr/en/publications/relationship-between-maximal-bite-force-and-tooth-wear-in-bruxist-2/", "Relationship between maximal bite force and tooth wear in bruxist and non-bruxist individuals") + ". Arch Oral Biol. 2011;56(12):1569-1575.",
 "Diraçoğlu D, Yıldırım NK, Saral İ, Özkan M, Karan A, Özkan S, Aksoy C. " + ext("https://content.iospress.com/articles/journal-of-back-and-musculoskeletal-rehabilitation/bmr644", "Temporomandibular dysfunction and risk factors for anxiety and depression") + ". J Back Musculoskelet Rehabil. 2016;29(3):487-491.",
 "Lobbezoo F, Naeije M. " + ext("https://read.qxmd.com/read/11874505/bruxism-is-mainly-regulated-centrally-not-peripherally", "Bruxism is mainly regulated centrally, not peripherally") + ". J Oral Rehabil. 2001.",
 "Kato T, Rompré P, Montplaisir JY, Sessle BJ, Lavigne GJ. " + ext("https://pubmed.ncbi.nlm.nih.gov/11706956/", "Sleep bruxism: an oromotor activity secondary to micro-arousal") + ". J Dent Res. 2001;80(10):1940-1944.",
 "Chemelo VS, et al. " + ext("https://www.frontiersin.org/articles/10.3389/fneur.2020.590779", "Is there association between stress and bruxism? A systematic review and meta-analysis") + ". Front Neurol. 2020;11:590779.",
 "Koca CG, Yıldırım B, Tunç S, Ongun İ, Sadry S. " + ext("https://dergipark.org.tr/en/download/article-file/6249057", "Intraoral findings, soft palate dimensions, and body mass index in PSG-confirmed versus self-reported bruxism: a comparative study") + ". Cumhuriyet Dent J. 2026;29(3):552-560.",
 "nidirect (NHS içeriği). " + ext("https://www.nidirect.gov.uk/conditions/teeth-grinding", "Teeth grinding (bruxism)") + ".",
 "Macedo CR, Silva AB, Machado MAC, Saconato H, Prado GF. " + ext("https://www.cochrane.org/fr/evidence/CD005514_occlusal-splints-treating-sleep-bruxism-tooth-grinding", "Occlusal splints for treating sleep bruxism (tooth grinding)") + ". Cochrane Database Syst Rev. 2007;(4):CD005514.",
 ext("https://cochranelibrary.com/cdsr/doi/10.1002/14651858.CD005578.pub2", "Pharmacotherapy for sleep bruxism") + ". Cochrane Database Syst Rev. CD005578.",
 "Cerón L, et al. " + ext("https://dmp.umw.edu.pl/pdf/2023/60/2/335.pdf", "Therapies for sleep bruxism in dentistry: a critical evaluation of systematic reviews") + ". Dent Med Probl. 2023;60(2):335-344.",
 "Coelho MS, de Oliveira JMD, Polmann H, Pauletto P, Stefani CM, De Luca Maciel LC, De Luca Canto G. " + ext("https://www.mdpi.com/2072-6651/17/5/249", "Botulinum toxin for bruxism: an overview") + ". Toxins. 2025;17(5):249.",
 "Madani ve ark. 2012; özet: " + ext("https://cats.uthscsa.edu/published_cats_friendly.php?id=2762", "Gabapentin is as effective as an occlusal appliance in controlling nighttime masticatory EMG activity") + " (UT Health San Antonio).",
 "Tecco JM, Tecco S. " + ext("https://hrcak.srce.hr/en/262356", "Awake bruxism treated with pregabaline in a patient with generalized anxiety disorder") + ". Psychiatr Danub. 2020;32(Suppl 1):33-35.",
 "Amorim CSM, Espirito Santo AS, Sommer M, Marques AP. " + ext("https://search.pedro.org.au/search-results/record-detail/54184", "Effect of physical therapy in bruxism treatment: a systematic review") + ". J Manipulative Physiol Ther. 2018;41(5):389-404.",
 "Headache Classification Committee of the International Headache Society. " + ext("https://ichd-3.org/11-headache-or-facial-pain-attributed-to-disorder-of-the-cranium-neck-eyes-ears-nose-sinuses-teeth-mouth-or-other-facial-or-cervical-structure/11-7-headache-attributed-to-temporomandibular-disorder-tmd/", "ICHD-3, 11.7 Headache attributed to temporomandibular disorder (TMD)") + ".",
 "Réus JC, Polmann H, Mendes Souza BD, et al. " + ext("https://repositorio.unesp.br/entities/publication/a1c9007f-994a-416c-a323-fe9c7c7e8316/full", "Association between primary headaches and temporomandibular disorders: a systematic review and meta-analysis") + ". J Am Dent Assoc. 2022;153(2):120-.",
 "Yakkaphan P, Renton T, Tan H, et al. " + ext("https://kclpure.kcl.ac.uk/portal/en/publications/temporomandibular-disorders-and-fibromyalgia-prevalence-a-systema/", "Temporomandibular disorders and fibromyalgia prevalence: a systematic review and meta-analysis") + ". J Oral Facial Pain Headache. 2023;37(3):177-193.",
 "Bizzarri P, Giusti A, Pernici M, et al. " + ext("https://research.birmingham.ac.uk/en/publications/temporomandibular-disorders-and-orofacial-outcomes-in-subjects-wi/", "Temporomandibular disorders and orofacial outcomes in subjects with neck pain and/or cervicogenic headache: a systematic review with meta-analysis") + ". J Clin Med. 2026;15(1):266.",
 "Ciuffolo F, Manzoli L, Ferritto AL, Tecco S, D'Attilio M, Festa F. " + ext("https://cris.unibo.it/handle/11585/918009", "Surface electromyographic response of the neck muscles to maximal voluntary clenching of the teeth") + ". J Oral Rehabil. 2005;32:79-84.",
 "NHS Lothian. " + ext("https://policyonline.nhslothian.scot/wp-content/uploads/2024/07/Physio-Temporomandibular-Joint-Disorders.pdf", "Physiotherapy: temporomandibular joint disorders") + ". Version 2.0, June 2024.",
 "University Hospitals of Leicester. " + ext("https://www.uhleicester.nhs.uk/wp-content/uploads/2025/06/436_122022-Managing-jaw-joint-disorders.pdf", "Managing jaw joint disorders") + ". Leaflet 436.",
 "National Institute of Dental and Craniofacial Research (NIDCR). " + ext("https://www.nidcr.nih.gov/health-info/tmj/more-info", "TMD: more info") + ".",
 "nidirect (NHS içeriği). " + ext("https://www.nidirect.gov.uk/conditions/giant-cell-arteritis", "Giant cell arteritis") + ".",
 "Dentalcare (Procter & Gamble). " + ext("https://dentalcare.com/en-us/ce-courses/ce485/history-of-bruxism", "Bruxism: history") + " ve " + ext("https://www.dentalcare.com/en-us/ce-courses/ce485/diagnosis", "Bruxism: diagnosis") + ".",
 "Manfredini D, Lobbezoo F. " + ext("https://research.vu.nl/en/publications/role-of-psychosocial-factors-in-the-etiology-of-bruxism/", "Role of psychosocial factors in the etiology of bruxism") + ". J Orofac Pain. 2009;23(2):153-166.",
 "NHS. " + ext("https://www.nhs.uk/symptoms/teeth-grinding/", "Teeth grinding (bruxism)") + ".",
 "Serra-Negra JM, Lobbezoo F, Martins CC, Stellini E, Manfredini D. " + ext("https://www.research.unipd.it/retrieve/e14fb26b-6d51-3de1-e053-1705fe0ac030/serranegra2017.pdf", "Prevalence of sleep bruxism and awake bruxism in different chronotype profiles: hypothesis of an association") + ". Med Hypotheses. 2017.",
 "Mortazavi N, Tabatabaei AH, Mohammadi M, et al. " + ext("https://www.nature.com/articles/s41432-023-00911-6", "Is bruxism associated with temporomandibular joint disorders? A systematic review and meta-analysis") + ". Evid Based Dent. 2023;24:144.",
 "Sobral de Oliveira Souza AI, Raposo J, Barbosa da Silva J, et al. " + ext("https://dmp.umw.edu.pl/en/article/2026/63/3/707/", "Physical therapy interventions for awake and sleep bruxism: what has been the approach over the last decades? A systematic review of the evidence and research gaps") + ". Dent Med Probl. 2026;63(3):707-733.",
 "NHS Fife Musculoskeletal Physiotherapy Service. " + ext("https://www.nhsfife.org/media/33087/temporomandibular_joint_disorders_v7.pdf", "Temporomandibular joint disorders") + ".",
 "Leicestershire Partnership NHS Trust. " + ext("https://leicspart.nhs.uk/wp-content/uploads/2022/07/557-Managing-jaw-pain-TMJ.pdf", "Managing jaw pain (TMJ)") + ". Leaflet 557.",
 "Guy's and St Thomas' NHS Foundation Trust. " + ext("https://guysandstthomas.nhs.uk/health-information/jaw-opening-exercises-and-advice", "Jaw opening exercises and advice") + ". 4454/VER4, December 2025.",
 "StatPearls. " + ext("https://www.statpearls.com/point-of-care/20595", "Mandible dislocation") + ". Updated July 2023.",
 "Bracci A, Djukic G, Favero L, Salmaso L, Guarda-Nardini L, Manfredini D. " + ext("https://research.unipd.it/handle/11577/3271005", "Frequency of awake bruxism behaviours in the natural environment. A 7-day, multiple-point observation of real-time report in healthy young adults") + ". J Oral Rehabil. 2018;45:423-429.",
 "Guimarães FN, Canadas J, Cunha MG, et al. " + ext("https://www.frontiersin.org/articles/10.3389/frsle.2025.1652532/full", "Scalloped tongue: an additional, accessible and useful tool to detect severe obstructive sleep apnea?") + ". Front Sleep. 2025;4.",
 "Shim YJ, Lee MK, Kato T, Park HU, Heo K, Kim ST. " + ext("https://read.qxmd.com/read/24634627/effects-of-botulinum-toxin-on-jaw-motor-events-during-sleep-in-sleep-bruxism-patients-a-polysomnographic-evaluation", "Effects of botulinum toxin on jaw motor events during sleep in sleep bruxism patients: a polysomnographic evaluation") + ". J Clin Sleep Med. 2014.",
 "Malcangi G, Patano A, Pezzolla C, et al. " + ext("https://ricerca.uniba.it/retrieve/5c8c70c2-8d4d-4bc1-9971-e50924e0dffa/jcm-12-04586.pdf", "Bruxism and botulinum injection: challenges and insights") + ". J Clin Med. 2023;12:4586.",
 "Bartsch T, Goadsby PJ. " + ext("https://link.springer.com/doi/10.1007/s11916-003-0036-y", "The trigeminocervical complex and migraine: current concepts and synthesis") + ". Curr Pain Headache Rep. 2003;7(5):371-376.",
]

BR_TL = [
 ("Eski metinler", "Diş gıcırdatma, Mezmurlar'ın birkaç ayetinde de geçer."),
 ("20. yüzyıl başı", "Viyanalı diş hekimi Karolyi, diş sıkma ve gıcırdatmayı \"travmatik nevralji\" olarak tanımladı."),
 ("1907", "Marie ve Pietkiewicz, diş gıcırdatma için Fransızca bir terim önerdi."),
 ("1931", "Frohman, Yunanca \"dişleri gıcırdatmak\" anlamındaki sözcüklerden türeyen \"bruksizm\" terimini ortaya attı."),
 ("1960'lar–2007", "Dişlerin kapanışındaki (oklüzyon) bozuklukların ana neden olduğu düşüncesi öne çıktı; araştırma ve tedaviler kapanış düzeltmelerine ve plaklara odaklandı."),
 ("2001", "Uykuda diş sıkmadan önce beyin dalgalarında bir uyanma artışı ve kalp hızında hızlanma olduğu gösterildi (J Dent Res). Aynı yıl bruksizmin esas olarak beyin tarafından düzenlendiği, kapanışın ise küçük bir rol oynadığı yazıldı."),
 ("2007", "Cochrane derlemesi: plağın uyku bruksizmini azalttığına dair yeterli kanıt yok; plak dişleri aşınmaya karşı koruyabilir."),
 ("2011", "Cihan Hoca'nın da yazarları arasında olduğu çalışma (Arch Oral Biol): diş sıkanlarda en büyük ısırma kuvveti ve diş aşınması daha yüksekti ve ikisi birbiriyle güçlü biçimde ilişkiliydi; araştırmacılar bunun bu ilişkiyi gösteren ilk çalışma olduğunu yazdı."),
 ("2013", "Uluslararası uzmanlar bruksizm için ortak bir tanım üzerinde uzlaştı."),
 ("2018", "Uluslararası uzlaşı: uyku ve uyanıklık bruksizmi için iki ayrı tanım; sağlıklı kişilerde bir hastalık değil, sonuçları olabilecek bir davranış."),
 ("2024", "176 popülasyonu birleştiren meta-analiz (J Clin Med): dünyada uyku bruksizmi yaklaşık %21, uyanıklık bruksizmi %23."),
]

BR_OBS = '''Cihan Hoca'yla birlikte çalıştığımız dönemde, bize gelen ve önceki tedavilere rağmen çözülemeyen boyun ağrılarının birçoğunda diş sıkma görüyorduk. Bugün de pek çok kişi yorgun uyanma, sabah baş ağrısı, boyun ve omuz ağrısı gibi yakınmalar için farklı farklı tedavilere yöneliyor; klinikte bu yakınmaların altından zaman zaman diş sıkmanın çıkabildiğini görüyorum. İlerlemiş ve geçmeyen olgularda, boyundan kola yayılan ve sinir kökü basısını andıran ama gerçek bir kök basısı olmayan ağrılarla da karşılaşıyorum. Sinir kökü basısının ne olduğunu <a href="boyun-fitigi.html">boyun fıtığı</a> rehberinde okuyabilirsiniz.'''

BR_CSS = '''.br-fig{margin:18px auto 8px;max-width:340px;background:#F7F2E7;border-radius:18px;padding:12px}.br-fig svg{display:block;width:100%;height:auto}
.br-leg{list-style:none;padding:0;margin:8px auto 18px;max-width:560px;display:grid;gap:8px}
.br-leg li{display:flex;gap:10px;align-items:flex-start;line-height:1.5}
.br-num{flex:0 0 26px;height:26px;border-radius:50%;color:#fff;font-weight:700;display:flex;align-items:center;justify-content:center;font-size:14px}
.br-sw{flex:0 0 16px;height:16px;border-radius:4px;margin-top:4px}'''

BR_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Diş sıkma ve gıcırdatma (bruksizm)</h1>
    <p class="lede">Diş sıkma ve gıcırdatma (bruksizm), çiğneme kaslarının uykuda ya da gün içinde gereğinden fazla çalışmasıdır. Dünyada yaklaşık her dört-beş kişiden birinde görülüyor ve çoğu kişi bunu fark etmiyor. Etkileri yalnızca dişlerle sınırlı değil: çene eklemi, boyun kasları, uyku ve baş ağrısı da etkilenebilir. Boyun ağrısıyla ilişkisini ayrıca anlatıyoruz. Bu rehberde bruksizmi bir ders gibi baştan sona anlatıyoruz.</p>
    <p class="meta">Son güncelleme: 10 Kasım 2026</p>
  </div>
</header>
<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%23</b><span>Dünyada uyanıkken diş sıkan ya da dişlerini birbirine bastıranların tahmini oranı; uykuda %21 (2024 meta-analizi)</span></div>
        <div class="stat"><b>42 kg</b><span>Gece diş sıkmasında ölçülen en yüksek kuvvetin kişi başına ortalaması (kilogram-kuvvet); en yüksek değer 81 kg</span></div>
        <div class="stat"><b>%77</b><span>Fibromiyaljisi olanlarda çene eklemi sorunu görülme oranı</span></div>
        <div class="stat"><b>4–5 kat</b><span>Migreni olanlarda çene eklemi sorunu görülme olasılığı (2022 meta-analizi; kanıt düşük–çok düşük)</span></div>
      </div>
      {g_toc([("nedir", "Bruksizm nedir?"), ("kuvvet", "Dişlere binen kuvvet"), ("etkiler", "Dört alanda etkiler"), ("isaretler", "Dilde diş izleri ve diğer işaretler"), ("cikik", "Çene çıkığı"), ("karisabilir", "Birlikte görülen durumlar"), ("nedenler", "Nedenler ve ruhsal etkenler"), ("plak", "Plak"), ("tedavi", "Çok yönlü tedavi"), ("evde", "Evde neler yapılabilir?"), ("egzersizler", "Egzersizler"), ("cocuklar", "Çocuklarda"), ("tarihce", "Geçmişten bugüne"), ("sss", "Sık sorulan sorular"), ("uyari", "Uyarı işaretleri")])}
      <div class="callout">
        <p><strong>Bu rehber hakkında.</strong> Bu rehberdeki yaklaşımı yazarımız İhsan Eren, Türkiye'de çene eklemi bozuklukları ve diş sıkma alanında 2005'ten bu yana uluslararası dergilerde yayımlanan çalışmalarıyla bu alanın öncülerinden olan Fiziksel Tıp ve Rehabilitasyon uzmanı Prof. Dr. Cihan Aksoy'un (Cihan Hoca) yanında öğrendi. Cihan Hoca, diş sıkmada diş hekimliği, psikiyatri ve diğer branşların birlikte çalışmasını ve hangi durumda hangi tedavinin tıbben uygun olduğunu ortaya koyan bir yaklaşım geliştirdi. Bu sayfada Cihan Hoca'nın da yazarları arasında olduğu iki çalışmaya yer veriyoruz.</p>
      </div>
    </div>
  </section>

  <section id="nedir">
    <div class="wrap">
      <h2>Bruksizm nedir?</h2>
      <p class="soft">2018'deki uluslararası uzlaşıya göre bruksizm, uykuda ya da uyanıkken ortaya çıkan çiğneme kası etkinliğidir ve iki ayrı biçimi vardır. Kişi dişlerini gıcırdatmadan, yalnızca sıkarak ya da alt çenesini iterek de bruksizm yaşayabilir.</p>
      <div class="kinds g-cmp">
        <div class="kind"><h3>Uyku bruksizmi</h3><dl><dt>Uykuda</dt><dd>Uyku sırasında çiğneme kaslarının ritmik ya da ritmik olmayan etkinliği: diş gıcırdatma ve sıkma. Çoğu kişi fark etmez; gıcırtıyı birlikte uyunan kişi fark edebilir.</dd></dl></div>
        <div class="kind"><h3>Uyanıklık bruksizmi</h3><dl><dt>Gün içinde</dt><dd>Uyanıkken dişlerin tekrarlayan ya da süren biçimde birbirine değmesi, sıkılması ya da alt çenenin itilmesi. Konsantrasyon, stres ya da yoğun iş sırasında, farkında olmadan olabilir.</dd></dl></div>
      </div>
      <h3 class="g-h3">Hastalık mı, davranış mı?</h3>
      <p class="soft">Uzlaşıya göre bruksizm, sağlıklı kişilerde tek başına bir hastalık değil, bir davranıştır; ancak diş aşınması, çiğneme kası ve çene eklemi ağrısı gibi sonuçlar için risk etkeni olabilir. Bruksizmin varlığı üç düzeyde değerlendirilir:</p>
      <ul class="tx">
        <li><b>Olası</b><span>Yalnızca kişinin kendi bildirimine dayanır (\"dişlerimi sıkıyorum\").</span></li>
        <li><b>Muhtemel</b><span>Muayenede bulgu vardır (diş aşınması, dilde diş izleri gibi), kişinin bildirimi olsun ya da olmasın.</span></li>
        <li><b>Kesin</b><span>Uyku testi (polisomnografi) gibi bir cihazla ölçülerek doğrulanır.</span></li>
      </ul>
      <h3 class="g-h3">Ne kadar yaygın?</h3>
      <p class="soft">176 popülasyonu birleştiren 2024 tarihli meta-analize göre dünyada bruksizm yaklaşık %22 oranında görülüyor: uyku bruksizmi %21, uyanıklık bruksizmi %23. Yani yaklaşık her dört kişiden biri gün içinde dişlerini sıkıyor olabilir. Uyanıklık bruksizmi kadınlarda erkeklere göre yaklaşık iki kat daha sık bildirildi (%17'ye karşı %8); kıtalar arasında anlamlı bir fark bulunmadı.</p>
    </div>
  </section>

  <section id="kuvvet">
    <div class="wrap">
      <h2>Dişlere ne kadar kuvvet biner?</h2>
      <p class="soft">Normalde dişler gün boyu birbirine değmez: Dinlenme sırasında dudaklar kapalı, dişler hafifçe ayrık, dil damakta durur. Diş sıkmada ise kaslar dişleri saatlerce birbirine bastırabilir.</p>
      <div class="kinds g-cmp">
        <div class="kind"><h3>Gece diş sıkması</h3><dl><dt>J Oral Rehabil, 2001</dt><dd>10 kişilik bir çalışmada uykuda ölçülen en yüksek kuvvet kişi başına ortalama 42 kilogram-kuvvetti, en yüksek değer 81'di. Bazı kişilerde gece kuvveti, kişinin gündüz bilerek yapabildiği en güçlü ısırmayı aştı (grupta gündüz ortalaması 79 kilogram-kuvvet).</dd></dl></div>
        <div class="kind"><h3>Rekor ısırma</h3><dl><dt>Guinness Dünya Rekorları</dt><dd>Kayıtlara geçen en güçlü insan ısırması 442 kilogram, yani yarım tona yakın; 1986'da bir diş hekimliği fakültesinde ölçüldü ve yaklaşık 2 saniye sürdü.</dd></dl></div>
        <div class="kind"><h3>Kuvvet ve aşınma</h3><dl><dt>Arch Oral Biol, 2011</dt><dd>Cihan Hoca'nın da yazarları arasında olduğu çalışmada, diş sıkanlarda en büyük ısırma kuvveti ve diş aşınması daha yüksekti; ikisi arasındaki ilişki güçlüydü. Araştırmacılar bunun, bu ilişkiyi gösteren ilk çalışma olduğunu yazdı.</dd></dl></div>
      </div>
    </div>
  </section>

  <section id="etkiler">
    <div class="wrap">
      <p class="eyebrow">Halk için özet</p>
      <h2>Dört alanda etkiler: diş, eklem, boyun, beyin</h2>
      <p class="soft">Diş sıkmayı yalnızca bir diş sorunu gibi düşünmek, tablonun yarısını görmek olur. Kesikli çizgiler, etkinin çeneden eklem ve boyun kaslarına doğru bir zincir gibi yayılabileceğini gösteriyor.</p>
      {BR_FIG_AREAS}
      <ul class="br-leg">
        <li><span class="br-num" style="background:#2A6F6B">1</span><span><b>Beyin:</b> Bruksizmi başlatan ve düzenleyen merkez; uyku, stres ve baş ağrısıyla bağlantılı.</span></li>
        <li><span class="br-num" style="background:#C8963E">2</span><span><b>Eklem:</b> Kulağın hemen önündeki çene eklemi ve çevresindeki çiğneme kasları.</span></li>
        <li><span class="br-num" style="background:#2A6F6B">3</span><span><b>Diş:</b> Aşınma, kırık ve çatlaklar; dil ve yanakta izler.</span></li>
        <li><span class="br-num" style="background:#C8963E">4</span><span><b>Boyun:</b> Diş sıkarken birlikte kasılan boyun kasları.</span></li>
      </ul>
      <h3 class="g-h3">1. Beyin: işin başladığı yer</h3>
      <p class="soft">Bruksizm bugün esas olarak beyin tarafından düzenlenen bir davranış olarak kabul ediliyor; dişlerin kapanışı ve çenenin yapısı ise küçük bir rol oynuyor. Uyku bruksizmi olan hastalarla yapılan bir çalışmada, diş sıkma olaylarının %79'unda kas etkinliğinden yaklaşık 4 saniye önce beyin dalgalarında bir uyanma artışı, hemen öncesinde de kalp hızında hızlanma görüldü. Yani uykuda diş sıkma, çoğu zaman uykunun kısa süreli hafiflemesiyle (mikro uyanma) birlikte ortaya çıkıyor. Diş gıcırdatmayla ilişkili yakınmalar arasında uykunun bölünmesi (sizin ya da birlikte uyuduğunuz kişinin) ve baş ağrısı da sayılıyor. Horlama ve uykuda nefes durması (uyku apnesi) de bruksizmle ilişkili bulunuyor.</p>
      <h3 class="g-h3">2. Eklem: çene eklemi ve çiğneme kasları</h3>
      <p class="soft">Uzun süre sıkılan çiğneme kasları yorulur ve ağrır; çene ekleminde ağrı, ağız açmada kısıtlılık ve klik sesi görülebilir. Uluslararası baş ağrısı sınıflamasına göre çene eklemi sorunları, diş ağrısından sonra yüz ağrısının en sık nedenidir. Ağrısız klik sesi sık görülür ve tek başına tedavi gerektirmez; ağrı, kilitlenme ya da ağız açmada kısıtlılık varsa değerlendirme gerekir. Ayrıntılar için <a href="cene-eklemi.html">çene eklemi rahatsızlıkları</a> rehberine bakabilirsiniz.</p>
      <h3 class="g-h3">3. Diş: aşınma, kırık ve ağız içindeki izler</h3>
      <p class="soft">Diş sıkma ve gıcırdatma dişlerde aşınmaya, sıcak-soğuk hassasiyetine, dolgu ve diş kırıklarına, dişlerde çatlaklara ve protez sorunlarına yol açabilir. Ağız içinde de ipuçları vardır: Türkiye'de 98 hastanın incelendiği 2026 tarihli bir çalışmada, uyku testiyle doğrulanmış bruksizmi olanların %65,3'ünde dil kenarında diş izleri, %75,5'inde yanağın iç yüzünde dişlerin hizasında beyaz bir çizgi vardı. Diş hekimi dişlerdeki aşınmayı ve kapanışı (oklüzyon) inceler; ancak kapanış bugün bruksizmin ana nedeni olarak görülmüyor. Ağız içindeki işaretlerin ayrıntıları aşağıdaki <a href="#isaretler">dilde diş izleri ve diğer işaretler</a> bölümünde.</p>
      <h3 class="g-h3">4. Boyun: zincirin devamı</h3>
      <p class="soft">Diş sıkarken yalnızca çene kasları çalışmaz: Sağlıklı kişilerde yapılan bir kas aktivitesi çalışmasında, en güçlü diş sıkma sırasında ön boyun kaslarının etkinliği belirgin olarak arttı. Boyun ağrısı olanlarda da çene eklemi sorunları daha sık: Dokuz çalışmayı inceleyen 2026 tarihli bir meta-analizde boyun ağrısı olanlarda çene eklemi sorunu görülme olasılığı yaklaşık 3,6 kat yüksekti (kanıtın kesinliği çok düşük).</p>
      <p class="soft">Bu bağlantının olası bir açıklaması sinir sistemindedir: Trigeminoservikal kompleks denen sinir hücresi grubunda, baştan gelen ağrı sinyallerini taşıyan sinirlerle üst boyundan gelen sinirler aynı sinir hücrelerinde birleşir. Bu birleşmenin, ağrının baş ve boyun arasında yayılmasına ve başka bir yerde hissedilmesine (yansıyan ağrı) katkıda bulunduğu düşünülüyor. Çene ve boyun ağrılarının birlikte görülmesine de bu mekanizmanın katkıda bulunabileceği öne sürülüyor.</p>
      <div class="callout obs"><p class="obs-k">Kişisel klinik gözlemim</p><p>{BR_OBS} Bunları bir araştırma sonucu olarak değil, kendi klinik gözlemlerim olarak paylaşıyorum; herkes aynı yanıtı vermeyebilir.</p></div>
      <h3 class="g-h3">Boyun ağrısı açısından üç önemli nokta</h3>
      <ul class="tx">
        <li><b>Ruhsal sebepler</b><span>Stres ve kaygı özellikle gündüz diş sıkmayla ilişkili görünüyor; kas gerginliğini ve ağrıya duyarlılığı da artırabilir. Bu yüzden boyun ağrısı geçmiyorsa ruhsal yük de sorgulanmalı (<a href="#nedenler">ruhsal etkenler</a>).</span></li>
        <li><b>Plak</b><span>Diş hekiminin verdiği plak dişleri ve diş minesini aşınmaya karşı koruyabilir; ancak sıkmayı azalttığına dair yeterli kanıt yok. Sıkma sürdükçe çene eklemi ve boyun kaslarındaki yük devam edebilir (<a href="#plak">plak</a>).</span></li>
        <li><b>Botulinum toksini</b><span>Yapıldığı çiğneme ve şakak kaslarının gücünü azaltır. Uyku testiyle yapılan bir çalışmada sıkma olaylarının sıklığı değişmedi; boyun kaslarını da doğrudan ele almaz (<a href="#botoks">neyi etkiler, neyi etkilemez?</a>).</span></li>
      </ul>
      <p class="soft">Boyun ağrısının diğer nedenleri, egzersizleri ve uyarı işaretleri için <a href="boyun-agrisi.html">boyun ağrısı</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section id="isaretler">
    <div class="wrap">
      <p class="eyebrow">Kendinizde fark edin</p>
      <h2>Dilde diş izleri, yanakta çizgi ve diğer işaretler</h2>
      <p class="soft">Diş sıkan pek çok kişi bunu bilmez; ama ağız ve yüz çoğu zaman ipuçları verir. 2018 uluslararası uzlaşısında "muhtemel" bruksizm için muayenede bakılan işaretler arasında dil ya da dudakta diş izleri, yanağın iç yüzünde beyaz çizgi, çiğneme kaslarının büyümesi, dişlerde mekanik aşınma, çatlak dişler ve tekrar tekrar bozulan dolgu ya da protezler sayılıyor.</p>
      {BR_FIG_TONGUE}
      <ul class="br-leg">
        <li><span class="br-sw" style="background:#C8963E"></span><span><b>Oklar:</b> Sıkma sırasında dil dişlere doğru itilir.</span></li>
        <li><span class="br-sw" style="background:#EDB8AE;border:2px solid #B5655A"></span><span><b>Dil kenarı:</b> Dişlerin iç yüzleri, dilin iki yanında sıra sıra çentikler bırakabilir (dalgalı dil). Çizim şematiktir.</span></li>
      </ul>
      <h3 class="g-h3">Dilde diş izleri (dalgalı dil)</h3>
      <p class="soft">Dilin iki yan kenarında, dişlerin hizasında sıra sıra çentikler görülmesine dalgalı dil denir. Diş sıkma sırasında dil sürekli olarak dişlere doğru itildiği için dişlerin iç yüzleri dil kenarında iz bırakabilir. Türkiye'de yapılan 2026 tarihli çalışmada, uyku testiyle doğrulanmış bruksizmi olanların %65,3'ünde dil kenarında diş izleri vardı; yalnızca kendisi diş sıktığını söyleyenlerde bu oran %34,7 idi.</p>
      <p class="soft">Ancak bu iz yalnızca diş sıkmaya özgü değildir. Uzlaşı raporu, dil ve yanak izlerinin yutkunma gibi olağan ağız hareketlerinden de kaynaklanabileceğini belirtiyor. Dilin geniş olması, dili dişlere doğru itme alışkanlığı ve dişlerdeki yapısal farklılıklar da dalgalı dile yol açabilir. Tam uyku testi yapılan ve çoğu uyku apnesi şüphesiyle yönlendirilmiş 160 hastanın incelendiği 2025 tarihli bir çalışmada dalgalı dil hastaların yaklaşık yarısında görüldü; dalgalı dili olanlarda ağır uyku apnesi olasılığı yaklaşık 3 kat yüksekti. Bu yüzden dilinizde izler varsa ve horluyorsanız ya da uykuda nefesinizin durduğu söyleniyorsa, bunu hekiminize mutlaka söyleyin.</p>
      <h3 class="g-h3">Diğer işaretler</h3>
      <div class="kinds g-cmp">
        <div class="kind"><h3>Yanakta beyaz çizgi</h3><dl><dt>Linea alba</dt><dd>Yanağın iç yüzünde, arka dişlerin hizasında uzanan beyaz çizgi. Sıkma ve gıcırdatma sırasında yanakların dişlere baskısıyla oluşabilir. 2026 çalışmasında doğrulanmış bruksizmi olanların %75,5'inde görüldü.</dd></dl></div>
        <div class="kind"><h3>Çiğneme kasında büyüme</h3><dl><dt>Masseter</dt><dd>Sürekli çalışan çiğneme kası zamanla kalınlaşabilir. Gıcırdatmada bir taraf daha baskınsa büyüme tek taraflı olabilir.</dd></dl></div>
        <div class="kind"><h3>Dişlerde aşınma izleri</h3><dl><dt>Aşınma yüzeyleri</dt><dd>Dişlerde düzleşmiş aşınma yüzeyleri, ön dişlerde aşırı aşınma; bazen dişin diş etine yakın kısmında çentikler (abfraksiyon). Bu çentiklerin başka nedenleri de olabilir.</dd></dl></div>
        <div class="kind"><h3>Çatlak dişler ve dolgular</h3><dl><dt>Sert dokular</dt><dd>Dişlerde çatlaklar, tekrar tekrar kırılan ya da düşen dolgular ve protezler.</dd></dl></div>
        <div class="kind"><h3>Sabah belirtileri</h3><dl><dt>Uyanınca</dt><dd>Uyanınca hissedilen baş ağrısı; çenede yorgunluk, ağrı ya da sertlik.</dd></dl></div>
      </div>
      <h3 class="g-h3">Aynada kendinizi kontrol edin</h3>
      <ul class="tx">
        <li><b>Dil</b><span>Dilinizi çıkarın ve iki yan kenarına bakın: dişlerin hizasında dalgalı çentikler var mı?</span></li>
        <li><b>Yanak</b><span>Yanağınızın içine bakın: arka dişlerinizin hizasında beyaz bir çizgi var mı?</span></li>
        <li><b>Kas</b><span>Dişlerinizi hafifçe sıkıp iki elinizle yanaklarınızdaki çiğneme kasını yoklayın: kas sert ya da hassas mı, iki taraf farklı mı?</span></li>
        <li><b>Sabah</b><span>Uyanınca çenenizde yorgunluk ya da baş ağrısı oluyor mu? Birlikte uyuduğunuz kişi gıcırtı duyuyor mu?</span></li>
      </ul>
      <p class="soft">Bu kontrol tanı koydurmaz. İşaretlerden biri ya da birkaçı varsa diş hekiminize, çene ve boyun ağrısı da varsa bir fizyoterapiste ya da hekime başvurabilirsiniz.</p>
    </div>
  </section>
  <section id="cikik">
    <div class="wrap">
      <h2>Çene çıkığı: ağız açık kalırsa</h2>
      <p class="soft">Çene eklemi, ağız çok açıldığında (esneme, gülme, şarkı söyleme, kusma gibi), diş tedavisi sırasında ya da yüze gelen bir darbeyle yerinden çıkabilir; en sık öne doğru çıkar. Ağız açık kalır ve kapanmaz; kulağın önünde ağrı, konuşma güçlüğü ve salya akması olabilir. Çıkık tek taraflıysa çene bir yana kayar.</p>
      <div class="kinds g-cmp">
        <div class="kind"><h3>Ne yapmalı?</h3><dl><dt>Acil durum</dt><dd>Hemen acil servise başvurun. Çeneyi kendiniz ya da bir yakınınız zorlayarak yerine oturtmaya çalışmayın; yerine oturtmadan önce kırık olup olmadığının değerlendirilmesi gerekebilir.</dd></dl></div>
        <div class="kind"><h3>Elle yerine oturtma</h3><dl><dt>Hekim yapar</dt><dd>En bilinen yöntemde hekim başparmaklarını alt arka dişlerin üzerine koyar ve çeneyi önce aşağıya, sonra geriye doğru iterek eklemi yerine oturtur. Ağrıyı, kaygıyı ve kas kasılmasını azaltmak için gerektiğinde ilaç ya da sedasyon kullanılır.</dd></dl></div>
        <div class="kind"><h3>Sonrasında</h3><dl><dt>1–3 hafta</dt><dd>Ağzı 2 cm'den fazla açmamak, esnerken çeneyi elle desteklemek ve birkaç gün ile iki hafta arasında yumuşak gıdalarla beslenmek önerilir; 2–3 gün içinde kulak burun boğaz ya da ağız, diş ve çene cerrahisi kontrolü önerilir.</dd></dl></div>
        <div class="kind"><h3>Tekrarlarsa</h3><dl><dt>Yineleme</dt><dd>Daha önce çıkık geçirmiş olmak, çene ekleminin aşırı hareketli olması ve bağ dokusunu etkileyen bazı hastalıklar çıkık riskini ve yinelemeyi artırabilir. Tekrarlayan çıkıklar eklem bağlarına ve kapsüle zarar verebilir; bu durumda uzman değerlendirmesi gerekir.</dd></dl></div>
      </div>
    </div>
  </section>
  <section id="karisabilir">
    <div class="wrap">
      <h2>Migren, fibromiyalji ve boyun ağrısıyla birlikte görülebilir</h2>
      <p class="soft">Çene eklemi ve çiğneme kası sorunları, başka tanılarla sık sık birlikte görülür ve belirtileri örtüşebilir. Bu yüzden baş ağrısı, yaygın vücut ağrısı ya da boyun ağrısı nedeniyle değerlendirilen birinde çene eklemi ve çiğneme kasları da muayene edilmelidir.</p>
      <div class="kinds g-cmp">
        <div class="kind"><h3>Baş ağrısı ve migren</h3><dl><dt>ICHD-3; JADA, 2022</dt><dd>Sınıflamada ayrı bir başlık var: çene eklemi bozukluğuna bağlı baş ağrısı. Genellikle şakakta olur, çiğneme ve diş sıkmayla artar; gerilim tipi baş ağrısıyla karışabilir. Bir meta-analizde migreni olanlarda çene eklemi sorunu görülme olasılığı 4–5 kat yüksekti (kanıt düşük–çok düşük kesinlikte).</dd></dl></div>
        <div class="kind"><h3>Fibromiyalji</h3><dl><dt>J Oral Facial Pain Headache, 2023</dt><dd>19 çalışmayı birleştiren meta-analizde fibromiyaljisi olanların %76,8'inde çene eklemi sorunu vardı; çene eklemi sorunu olanların yaklaşık üçte birinde (%32,7) de fibromiyalji bulunuyordu.</dd></dl></div>
        <div class="kind"><h3>Boyun ağrısı</h3><dl><dt>J Clin Med, 2026</dt><dd>Boyun ağrısı olanlarda çene eklemi sorunu görülme olasılığı yaklaşık 3,6 kat yüksekti (kanıtın kesinliği çok düşük). Yazarlar boyun ve çenenin birlikte değerlendirilmesini öneriyor.</dd></dl></div>
      </div>
      <p class="soft">İlgili rehberler: <a href="bas-agrisi.html">baş ağrısı</a>, <a href="fibromiyalji.html">fibromiyalji</a>, <a href="boyun-agrisi.html">boyun ağrısı</a>.</p>
    </div>
  </section>

  <section id="nedenler">
    <div class="wrap">
      <h2>Neden olur? Ruhsal ve diğer etkenler</h2>
      <p class="soft">Bruksizmin tek bir nedeni yok; birden fazla etken birlikte rol oynuyor. Eskiden dişlerin kapanışındaki bozuklukların ana neden olduğu düşünülürdü; bugün bu etkenlerin küçük bir rol oynadığı, bruksizmin esas olarak beyin tarafından düzenlendiği kabul ediliyor.</p>
      <ul class="tx">
        <li><b>Stres ve kaygı</b><span>En sık sayılan etkenler. Bir sistematik derlemede stresi olanlarda bruksizm olasılığı yaklaşık iki kat yüksekti (kanıtın kesinliği düşük).</span></li>
        <li><b>Uyku sorunları</b><span>Horlama ve uykuda nefes durması (uyku apnesi) bruksizmle ilişkili.</span></li>
        <li><b>İlaçlar</b><span>Bazı ilaçların yan etkisi olarak ortaya çıkabilir; ilacınızı kendi başınıza bırakmayın, hekiminizle konuşun.</span></li>
        <li><b>Alışkanlıklar</b><span>Alkol, sigara, bazı uyuşturucu maddeler ve günde altı ya da daha fazla fincan kafeinli içecek (çay, kahve) riski artırabilir.</span></li>
      </ul>
      <h3 class="g-h3">Ruhsal etkenler: neden önemli?</h3>
      <p class="soft">Stresli ya da gergin anlarda pek çok kişi farkında olmadan dişlerini sıkar. Hasta broşürlerinde de duygusal stresin diş sıkma olarak ortaya çıkabileceği ve gerginliğin çene ağrısını artırabileceği belirtiliyor. 45 yayını inceleyen bir derlemeye göre özellikle gündüz diş sıkma (uyanıklık bruksizmi) ruhsal ve sosyal etkenlerle ve bazı psikolojik belirtilerle ilişkili görünüyor; kaygı, strese duyarlılık, depresyon ve bazı kişilik özellikleriyle ilişki bildirilmiş. Uyku bruksizminin ruhsal ve sosyal sorunlarla ilişkisini destekleyen kanıt ise bulunamamış. Yazarlar, ilişki bildiren verilerin çoğunun klinik muayeneye ya da kişilerin kendi bildirimine dayandığını, uyku laboratuvarı çalışmalarının ise bu bulgularla çeliştiğini not ediyor.</p>
      <div class="kinds g-cmp">
        <div class="kind"><h3>Stres</h3><dl><dt>En sık sayılan</dt><dd>Bir sistematik derlemede stresi olanlarda bruksizm olasılığı yaklaşık iki kat yüksekti (kanıtın kesinliği düşük). Derlemedeki çalışmalarda iş stresi ve stresli yaşam olayları gibi farklı stres türleri incelendi.</dd></dl></div>
        <div class="kind"><h3>Kaygı</h3><dl><dt>Kaygıya yatkınlık</dt><dd>Kaygıya yatkınlık ve strese duyarlılık, hem çocuk ve gençlerde hem yetişkinlerde bruksizmle ilişkili başlıca psikolojik etkenler olarak sayılıyor.</dd></dl></div>
        <div class="kind"><h3>Depresyon</h3><dl><dt>Ruh hali</dt><dd>Depresyonla ilişki bildirildi; çene eklemi ağrısı olanlarda da kaygı ve depresyon sık görülüyor.</dd></dl></div>
        <div class="kind"><h3>Kişilik özellikleri</h3><dl><dt>Bir varsayım</dt><dd>Kaygıya ve olumsuz duygulara yatkın (nevrotiklik), sorumluluk duygusu yüksek ve kaygılı beklentileri olan kişilerin duygusal gerginliği diş sıkarak ya da gıcırdatarak boşaltabileceği öne sürülüyor; bu henüz kanıtlanmış bir bulgu değil, bir varsayım.</dd></dl></div>
      </div>
      <h3 class="g-h3">Ruh hali, diş sıkma ve ağrı birbirini etkiler</h3>
      <p class="soft">20 çalışmayı birleştiren bir meta-analizde bruksizmi olanlarda çene eklemi bozukluğu görülme olasılığı yaklaşık 2,2 kat, uyanıklık bruksizminde 2,5 kat yüksekti. Çene eklemi ağrısı da kaygı ve depresyonla ilişkili. Bu ilişkiler bir kısır döngüye işaret ediyor olabilir: Stres sıkmayı, sıkma ağrıyı, ağrı da yeniden stresi artırabilir. Ancak bu çalışmalar ilişkinin yönünü kesin olarak göstermiyor. Bu yüzden tedavide yalnızca dişler ve kaslar değil, ruh hali de ele alınır.</p>
      <p class="soft">Cihan Hoca'nın da yazarları arasında olduğu ve çok branşlı bir çene eklemi polikliniğine başvuran 273 hastanın incelendiği çalışmada, kadın olmak, sosyal desteğin yetersiz olması ve kas kaynaklı yüz ağrısı kaygı ya da depresyon olasılığını artırıyordu. Yazarlar, tedavi planlanırken kas ve eklem sorunlarının yanında kaygı ve depresyonun da göz önünde bulundurulmasını önerdi. Stresle başa çıkmak için <a href="stres.html">stresli anlarda ne yapabilirsiniz?</a> sayfasına bakabilirsiniz.</p>
      <h3 class="g-h3">Ruhsal yönden neler yapılabilir?</h3>
      <ul class="tx">
        <li><b>Fark etmek</b><span>Gün içinde hangi durumlarda sıktığınızı gözlemleyin: iş, trafik, ekran başı, tartışma ya da endişe anları.</span></li>
        <li><b>Gevşeme ve nefes</b><span>Sessiz bir yerde, ellerinizi karnınıza koyup burnunuzdan yavaş ve derin nefes alın; yaklaşık 5 dakika uygulayın. Öğrendikten sonra gerildiğiniz her an kullanabilirsiniz.</span></li>
        <li><b>Düzenli hareket ve uyku düzeni</b><span>Düzenli egzersiz gevşemeye yardımcı olabilir. Her gece aynı saatte yatarak uykunuzu düzenlemek de diş gıcırdatmayı azaltmak için önerilen adımlar arasında.</span></li>
        <li><b>Profesyonel destek</b><span>Kaygı, depresyon ya da uyku sorunu belirginse psikiyatri ya da psikoloji desteği alın; bilişsel davranışçı terapi bu yöntemlerden biridir. Bir sistematik derlemenin yazarlarına göre gevşeme eğitimi ya da biyolojik geri bildirim içeren yöntemler, özellikle uyanıklık bruksizminde stresle ilişkili kas etkinliğini azaltabilir; ancak kanıtın kesinliği çok düşük.</span></li>
      </ul>
    </div>
  </section>

  <section id="plak">
    <div class="wrap">
      <h2>Plak: dişi korur, sorunu çözmez</h2>
      <p class="soft">Gece plağı (ağız koruyucu), diş hekiminin hazırladığı ve genellikle geceleri takılan bir apareydir. Dişleri birbirinden ayırarak aşınmayı önlemeye yardımcı olur; sıkma hissini ve ağrıyı azaltabilir. Ancak plağın sıkma davranışını azalttığı gösterilmedi.</p>
      <div class="kinds g-cmp">
        <div class="kind"><h3>Dişler</h3><dl><dt>Cochrane, 2007</dt><dd>Plak dişleri ve diş minesini aşınmaya karşı koruyabilir.</dd></dl></div>
        <div class="kind"><h3>Diş sıkma</h3><dl><dt>Cochrane, 2007; Dent Med Probl, 2023</dt><dd>Plağın uyku bruksizmini azalttığına dair yeterli kanıt yok; derlemelerde plaklar kısa vadede etkinlik göstermedi.</dd></dl></div>
        <div class="kind"><h3>Kaslar ve eklem</h3><dl><dt>Sonuç</dt><dd>Sıkma sürebileceği için kaslar ve eklem üzerindeki yük devam edebilir; bu yüzden plak diğer yaklaşımlarla birlikte kullanılır.</dd></dl></div>
      </div>
      <div class="callout"><p><strong>Kısacası:</strong> Diş hekiminin verdiği plak, diş minesine binen zararı azaltabilir. Diş sıkmanın kendisini durdurduğu gösterilmedi; bu yüzden çene eklemi ve boyun kaslarındaki etki sürebilir. Plak takıyorsanız bile sıkmanın nedenleri (stres, uyku, alışkanlıklar) ayrıca ele alınmalı.</p></div>
      <p class="soft">Diş hekimi dişlerdeki aşınmayı, kırık ve çatlakları ve dişlerin kapanışını (oklüzyon) değerlendirir; plağın gerekip gerekmediğine ve türüne karar verir.</p>
    </div>
  </section>

  <section id="tedavi">
    <div class="wrap">
      <h2>Çok yönlü tedavi: kim ne yapar?</h2>
      <p class="soft">Şu an dünyada diş sıkmayı kesin olarak ortadan kaldırdığı gösterilmiş bir tedavi yok. Derlemelerde plak, biyolojik geri bildirim ve botulinum toksini kısa vadede kesin bir etkinlik göstermedi; bazı ilaçlar uykudaki diş sıkma olaylarını azaltmış olsa da yan etkileri nedeniyle temkin gerekiyor ve bu derlemelerin güvenilirliği çok düşük. Bu yüzden amaç; dişleri, eklemi ve kasları korumak, tetikleyicileri azaltmak ve yakınmaları hafifletmektir. Bu da çoğu zaman birden fazla branşın birlikte çalışmasını gerektirir.</p>
      <div class="kinds g-cmp">
        <div class="kind"><h3>Diş hekimi</h3><dl><dt>Dişler ve kapanış</dt><dd>Aşınma, kırık ve kapanış değerlendirmesi; gerekirse plak.</dd></dl></div>
        <div class="kind"><h3>Psikiyatri ve psikoloji</h3><dl><dt>Stres ve kaygı</dt><dd>Kaygı, depresyon ya da yoğun stres varsa değerlendirme ve tedavi; bilişsel davranışçı terapi gibi yöntemler.</dd></dl></div>
        <div class="kind"><h3>Uyku değerlendirmesi</h3><dl><dt>Horlama ve nefes durması</dt><dd>Uyku apnesinden şüpheleniliyorsa hekim değerlendirmesi ve gerekirse uyku testi.</dd></dl></div>
        <div class="kind"><h3>Fizyoterapi</h3><dl><dt>Kaslar ve alışkanlıklar</dt><dd>Farkındalık ve alışkanlık değiştirme, gevşeme, çene ve boyun egzersizleri, kas masajı, duruş. 24 çalışmayı inceleyen bir derlemede kas ağrısı ve etkinliği, ağız açıklığı, kaygı ve stres iyileşebildi; ancak kanıtın kalitesi çok düşüktü.</dd></dl></div>
        <div class="kind"><h3>İlaçlar</h3><dl><dt>Yalnızca uzman hekim reçetesiyle</dt><dd>Kanıt sınırlı: Cochrane derlemesi yedi küçük çalışmada yeterli kanıt bulamadı. Gabapentin 20 kişilik bir çalışmada gece kas etkinliğini plak kadar azalttı; aynı gruptan pregabalin için yer verebildiğimiz tek yayın, tek bir hastanın olgu sunumu. Kendi başınıza kullanmayın; hangisinin uygun olduğunu hekiminize sorun.</dd></dl></div>
        <div class="kind"><h3>Botulinum toksini</h3><dl><dt>Yalnızca hekim uygular</dt><dd>Çiğneme ve şakak kasına yapılır. 14 derlemeyi inceleyen 2025 tarihli değerlendirmede ağrıda azalma 10, diş sıkma olaylarında 7, ısırma kuvvetinde 5 derlemede bildirildi; ancak hepsinin güvenilirliği düşük ya da kritik düzeyde düşüktü ve kesin sonuç çıkarılamadı.</dd></dl></div>
      </div>
      <h3 class="g-h3">Botulinum toksini hangi kaslara yapılır?</h3>
      <p class="soft">Aşağıdaki şematik çizim, diş sıkmada botulinum toksini uygulamasında kullanılan iki kası gösteriyor. Noktalar yalnızca bölgeyi anlatmak içindir; gerçek uygulama noktalarını ve dozu hekim belirler.</p>
      {BR_FIG_BOTOX}
      <ul class="br-leg">
        <li><span class="br-sw" style="background:#C8963E"></span><span><b>Şakak kası (temporalis):</b> Şakakta, kulağın üstünde yelpaze biçiminde uzanır; çeneyi kapatır ve dişleri sıkar.</span></li>
        <li><span class="br-sw" style="background:#2A6F6B"></span><span><b>Çiğneme kası (masseter):</b> Elmacık kemiğinden alt çenenin köşesine uzanır; dişleri sıktığınızda yanağınızda sertleştiğini hissedebilirsiniz.</span></li>
      </ul>
      <h3 class="g-h3" id="botoks">Botulinum toksini neyi etkiler, neyi etkilemez?</h3>
      <p class="soft">Botulinum toksini diş sıkmada giderek daha çok uygulanıyor; bu yüzden neyi değiştirip neyi değiştirmediğini bilmek önemli.</p>
      <ul class="tx">
        <li><b>Neyi etkiler?</b><span>İğnenin yapıldığı kasta, sinirden kasa kasılma sinyalini taşıyan maddenin (asetilkolin) salınımını geçici olarak engeller; kas zayıflar ve kasılma gücü azalır. Uyku testiyle değerlendirilen 20 kişilik küçük bir çalışmada (plasebo grubu yoktu, izlem 4 hafta) iğne, yapıldığı kaslardaki kasılmaların şiddetini azalttı.</span></li>
        <li><b>Neyi etkilemez?</b><span>Aynı çalışmada uykudaki diş sıkma olaylarının sıklığı ve süresi değişmedi. Yazarlara göre iğne, kasılmanın ortaya çıkışını değil şiddetini azaltıyor. Yine de katılımcıların çoğu 4 hafta sonra sabah çene sertliğinin azaldığını bildirdi. Bruksizmin büyük ölçüde merkezi sinir sistemi tarafından düzenlendiği düşünülüyor; iğne ise yalnızca yapıldığı kası etkiler. Bu yüzden stres ve uyku gibi etkenlerin ayrıca ele alınması gerekir.</span></li>
        <li><b>Ne kadar sürer?</b><span>Etkisi kalıcı değildir; birkaç ay içinde azalarak kaybolur. Etkinin sürmesi için iğnenin tekrarlanması gerekir.</span></li>
        <li><b>Yan etkiler</b><span>Bir derlemede iğne yerinde ağrı ve morarma, çoğunlukla geçici çiğneme güçsüzlüğü, ağız kuruluğu, yutma ve konuşma güçlüğü, yüzün alt kısmında hafif asimetri ve gülüşte değişiklik bildirildi; bu sorunlar genellikle 1–4 hafta içinde geçti, çiğneme güçlüğü bazen 12 haftaya kadar sürdü.</span></li>
        <li><b>Boyun ve duruş</b><span>Çiğneme ve şakak kasına yapılan iğne, boyun kaslarını ve duruşu doğrudan ele almaz. Boyun ağrısı da varsa egzersiz ve fizyoterapi ayrıca planlanır.</span></li>
      </ul>
    </div>
  </section>

  <section id="evde">
    <div class="wrap">
      <h2>Evde neler yapılabilir?</h2>
      <h3 class="g-h3">Önce fark etmek</h3>
      <p class="soft">Uyanıklık bruksizmi çoğu zaman farkında olmadan olur. 46 diş hekimliği öğrencisinin bir hafta boyunca akıllı telefon uygulamasıyla günde 15 kez, rastgele zamanlarda çenelerinin o anki durumunu bildirdiği bir çalışmada, yanıtların %71,7'sinde çene kasları gevşekti. En sık görülen davranışlar dişlerin birbirine değmesi (%14,5) ve dişler değmeden çenenin sıkılmasıydı (%10). Dişleri sıkma ve gıcırdatma da eklendiğinde, bu sağlıklı genç yetişkinlerde gün içindeki anların yaklaşık %28'inde bir uyanıklık bruksizmi davranışı vardı. Kendinizi gözlemlemek için gün içinde birkaç kez "Dişlerim şu an birbirine değiyor mu?" diye sorabilirsiniz.</p>
      <ul class="tx">
        <li><b>Dinlenme pozisyonu</b><span>Dudaklar kapalı, dişler hafifçe ayrık, dil damakta. Gün içinde dişlerinizi sıktığınızı fark ettiğinizde bu pozisyona dönün.</span></li>
        <li><b>Hatırlatıcılar</b><span>Konsantrasyon ya da endişe anlarında sıkmayı fark etmek için telefon hatırlatıcısı ya da masanıza küçük bir not koyabilirsiniz; alışkanlığı değiştirmenin ilk adımı fark etmektir.</span></li>
        <li><b>Çeneyi yormayın</b><span>Sakız çiğnemeyin; tırnak, dudak, dil ya da diş eti ısırmaktan kaçının, kalem çiğnemeyin; esnerken çenenizi elinizle destekleyin.</span></li>
        <li><b>Ilık ve soğuk</b><span>Ağrılı kaslara 10–15 dakika ılık uygulama ya da 5–10 dakika buz masajı rahatlatabilir.</span></li>
        <li><b>Uyku ve alışkanlıklar</b><span>Düzenli uyku saatleri; özellikle akşamları kafein, alkol ve sigarayı azaltmak. Uyku için öneriler <a href="uyku.html">uyku</a> sayfasında.</span></li>
        <li><b>Gevşeme</b><span>Yavaş nefes, düzenli egzersiz ve farkındalık çalışmaları stresin kaslara yansımasını azaltabilir.</span></li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Egzersizler</p>
      <h2>Çene ve boyun için sekiz egzersiz</h2>
      <p class="soft">Hareketleri ağrısız aralıkta, yavaşça yapın. Ağrı artıyorsa durun ve bir fizyoterapiste ya da hekime danışın. Sağa sola kaydırma ve öne itme, çeneyi açıp kapamanın dışındaki yönlerde de çalıştırır. Yakın zamanda çene çıkığı geçirdiyseniz, ilk 1–3 haftada ağzınızı 2 cm'den fazla açmayın; egzersizlere hekiminizin ya da fizyoterapistinizin önerisiyle başlayın.</p>
      {ex_grid(["jaw_rest", "jaw_mass", "jaw_open", "jaw_res", "br_side", "br_fwd", "chin", "br_breath"])}
    </div>
  </section>

  <section id="cocuklar">
    <div class="wrap">
      <h2>Çocuklarda diş gıcırdatma</h2>
      <p class="soft">Diş gıcırdatma çocuklarda da görülebilir. Çoğunlukla süt dişleri ya da kalıcı dişler ilk çıktıktan sonra ortaya çıkar ve kalıcı dişler tamamen oluştuktan sonra genellikle durur. Endişeleniyorsanız, özellikle çocuğunuzun uykusunu etkiliyorsa, bir hekime başvurun; dişlerde aşınma ya da ağrı varsa diş hekimi de değerlendirebilir.</p>
    </div>
  </section>

  <section id="tarihce">
    <div class="wrap">
      <p class="eyebrow">Geçmişten bugüne</p>
      <h2>Mezmurlar'dan uluslararası uzlaşıya</h2>
      <p class="soft">Diş gıcırdatma çok eski çağlardan beri biliniyor. 20. yüzyılda adı kondu; uzun yıllar dişlerin kapanışı ana neden sayıldı. Son 25 yılda ise bruksizmin esas olarak beyin tarafından düzenlenen bir davranış olduğu anlaşıldı.</p>
      {g_tl(BR_TL)}
    </div>
  </section>

  <section id="sss">
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(BR_FAQ)}
    </div>
  </section>

  <section id="uyari">
    <div class="wrap">
      <h2>Ne zaman başvurmalı?</h2>
      <p class="soft">Aşağıdaki durumlarda bir hekime ya da diş hekimine başvurun; ne kadar acil olduğu her grubun başında belirtilmiştir.</p>
      <p class="soft"><strong>Hemen 112'yi arayın:</strong></p>
      <ul class="dots redflags">
        <li>Göğüs ağrısı, nefes darlığı ya da terlemeyle birlikte çene ağrısı</li>
        <li>Yüzde ani uyuşma ya da güçsüzlük, konuşma bozukluğu</li>
      </ul>
      <p class="soft"><strong>Hemen acil servise gidin:</strong></p>
      <ul class="dots redflags">
        <li>Ağzın açık kalıp kapanmaması (çene çıkığı)</li>
      </ul>
      <p class="soft"><strong>Aynı gün bir hekime ya da diş hekimine:</strong></p>
      <ul class="dots redflags">
        <li>Çenenin kilitlenmesi: ağzın açılmaması</li>
        <li>Yüzde ya da çenede şişlikle birlikte ateş</li>
        <li>50 yaşın üstünde yeni başlayan şakak ağrısı, çiğnerken ya da konuşurken çene ağrısı veya görme bozukluğu</li>
      </ul>
      <p class="soft"><strong>Birkaç gün içinde bir hekime ya da diş hekimine:</strong></p>
      <ul class="dots redflags">
        <li>Kırık ya da çatlak diş, kırık dolgu</li>
        <li>Horlama ve uykuda nefes durması fark edildiyse</li>
        <li>Birkaç haftada geçmeyen çene, yüz ya da şakak ağrısı</li>
      </ul>
      {CTA_CARD("Diş sıkma ve çene ağrısı", "diş sıkma ve çene ağrısı")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(BR_SRC)}
    </div>
  </section>
</main>'''

page("dis-sikma.html", "Diş Sıkma ve Gıcırdatma (Bruksizm)",
     "Diş sıkma ve gıcırdatma (bruksizm) nedir, dişlere ne kadar kuvvet biner, diş, eklem, boyun ve beyin nasıl etkilenir? Migren ve fibromiyaljiyle ilişkisi, ruhsal etkenler, plağın yeri, çok yönlü tedavi, botulinum toksini, çene çıkığı, tarihçe ve evde sekiz egzersiz.",
     "dis-sikma.html", NECK_CSS + BR_CSS, BR_BODY, "",
     seo_title="Diş Sıkma ve Gıcırdatma (Bruksizm): Nedenleri, Etkileri ve Tedavi | İhsan Eren",
     condition="Bruksizm", faq_items=BR_FAQ)
