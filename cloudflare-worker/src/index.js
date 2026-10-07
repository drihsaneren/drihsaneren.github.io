
const ALLOWED_ORIGINS = new Set([
  "https://drihsaneren.com",
  "https://www.drihsaneren.com"
]);

const MODEL = "@cf/meta/llama-3.1-8b-instruct-fast";

function cors(origin) {
  return {
    "access-control-allow-origin": ALLOWED_ORIGINS.has(origin) ? origin : "https://drihsaneren.com",
    "vary": "Origin",
    "access-control-allow-methods": "POST, OPTIONS",
    "access-control-allow-headers": "content-type",
    "content-type": "application/json; charset=utf-8",
    "cache-control": "no-store"
  };
}

function json(data, status, origin) {
  return new Response(JSON.stringify(data), { status, headers: cors(origin) });
}

function cleanText(v, max) {
  return String(v || "").replace(/\s+/g, " ").trim().slice(0, max);
}

function emergencyText(lang) {
  return lang === "en"
    ? "These symptoms may need urgent medical assessment. If there is severe chest pain, major breathing difficulty, new one-sided weakness, fainting, severe bleeding, or another immediate danger, seek emergency help now."
    : "Bu belirtiler acil değerlendirme gerektirebilir. Şiddetli göğüs ağrısı, ciddi nefes darlığı, yeni gelişen tek taraflı güçsüzlük, bayılma, ciddi kanama veya başka bir acil tehlike varsa 112’yi arayın ya da acil yardım alın.";
}

function looksEmergency(q, lang) {
  const s = q.toLocaleLowerCase(lang === "tr" ? "tr-TR" : "en-US");
  const terms = lang === "en"
    ? ["severe chest pain","cannot breathe","can't breathe","one-sided weakness","face droop","unconscious","severe bleeding","suicide","kill myself"]
    : ["şiddetli göğüs ağr","göğüs ağr","nefes alam","tek taraflı güçsüz","yüz kayması","bilinçsiz","ciddi kanama","intihar","kendimi öldür"];
  return terms.some(t => s.includes(t));
}

export default {
  async fetch(request, env) {
    const origin = request.headers.get("origin") || "";
    if (request.method === "OPTIONS") {
      if (!ALLOWED_ORIGINS.has(origin)) return json({ error: "origin" }, 403, origin);
      return new Response(null, { status: 204, headers: cors(origin) });
    }
    if (request.method !== "POST") return json({ error: "POST only" }, 405, origin);
    if (!ALLOWED_ORIGINS.has(origin)) return json({ error: "origin" }, 403, origin);

    const length = Number(request.headers.get("content-length") || "0");
    if (length > 18000) return json({ error: "request too large" }, 413, origin);

    let body;
    try { body = await request.json(); } catch { return json({ error: "invalid json" }, 400, origin); }

    const lang = body.lang === "en" ? "en" : "tr";
    const question = cleanText(body.question, 500);
    if (!question) return json({ error: "question required" }, 400, origin);
    if (looksEmergency(question, lang)) return json({ answer: emergencyText(lang), emergency: true }, 200, origin);

    const context = Array.isArray(body.context) ? body.context.slice(0, 4).map(item => ({
      title: cleanText(item?.title, 140),
      url: cleanText(item?.url, 220),
      description: cleanText(item?.description, 500),
      snippets: Array.isArray(item?.snippets) ? item.snippets.slice(0, 3).map(x => cleanText(x, 800)) : []
    })) : [];

    if (!context.length) {
      return json({
        answer: lang === "en"
          ? "I could not find a sufficiently relevant guide on this website."
          : "Bu sitede sorunuzla yeterince ilgili bir rehber bulamadım."
      }, 200, origin);
    }

    const system = lang === "en"
      ? `You are the Health Guide Assistant for drihsaneren.com. Answer ONLY from the supplied website context. Keep the answer concise, plain and cautious. Never diagnose, prescribe medication, change medication, or claim certainty. Never invent facts, studies, numbers or sources. If context is insufficient, say so. For urgent red-flag symptoms, advise urgent medical assessment. Mention that the answer is informational, not personal medical advice. Do not ask for or repeat identifying personal data. Return only the answer text, no markdown table.`
      : `drihsaneren.com Sağlık Rehberi Asistanısın. YALNIZCA verilen site bağlamındaki bilgilere dayan. Kısa, sade ve temkinli cevap ver. Tanı koyma, ilaç önerme/değiştirme, kesinlik iddiasında bulunma. Bilgi, çalışma, sayı veya kaynak uydurma. Bağlam yetersizse bunu söyle. Acil uyarı işaretlerinde acil tıbbi değerlendirme öner. Yanıtın kişisel tıbbi tavsiye değil, bilgilendirme olduğunu belirt. Kimlik belirleyici kişisel bilgi isteme veya tekrarlama. Yalnızca yanıt metnini döndür; markdown tablo kullanma.`;

    const contextText = context.map((c, i) =>
      `[${i+1}] ${c.title}\nURL: ${c.url}\n${c.description}\n${c.snippets.join("\n")}`
    ).join("\n\n");

    try {
      const out = await env.AI.run(MODEL, {
        messages: [
          { role: "system", content: system },
          { role: "user", content: `QUESTION:\n${question}\n\nWEBSITE CONTEXT:\n${contextText}` }
        ],
        max_tokens: 320,
        temperature: 0.2
      });
      const answer = cleanText(out?.response || out?.result?.response || "", 2400);
      if (!answer) throw new Error("empty");
      return json({ answer, model: MODEL }, 200, origin);
    } catch (err) {
      return json({ error: "ai unavailable" }, 503, origin);
    }
  }
};
