
(function(){
"use strict";
if(window.__IEAI_LOADED__) return;
window.__IEAI_LOADED__=true;

var lang=(document.documentElement.lang||"tr").toLowerCase().startsWith("en")?"en":"tr";
var copy=lang==="en"?{
  title:"Health Guide Assistant",
  sub:"Answers from the guides on this website",
  hello:"Hi. Ask a short health or exercise question. I’ll use the information published on this website and show the relevant guides.",
  placeholder:"e.g. What can I do for low back pain?",
  send:"Send",
  note:"For information only; not a diagnosis or personal medical advice. Do not share names, phone numbers or other private information.",
  local:"Site search",
  ai:"Free AI",
  nohit:"I couldn't find a sufficiently relevant guide on the website. Try using fewer, more specific words.",
  error:"The AI service is unavailable right now. I found the closest information from the website instead.",
  emergency:"These symptoms may need urgent medical assessment. If there is severe chest pain, major breathing difficulty, new one-sided weakness, fainting, severe bleeding, or another immediate danger, seek emergency help now.",
  sources:"Related guides"
}:{
  title:"Sağlık Rehberi Asistanı",
  sub:"Bu sitedeki rehberlerden yanıt verir",
  hello:"Merhaba. Sağlık veya egzersizle ilgili kısa bir soru sorun. Bu sitede yayımlanan bilgilerden yararlanıp ilgili rehberleri göstereceğim.",
  placeholder:"Örn. Bel ağrısında ne yapabilirim?",
  send:"Gönder",
  note:"Yalnızca bilgilendirme içindir; tanı veya kişisel tıbbi öneri değildir. İsim, telefon veya başka özel bilgilerinizi yazmayın.",
  local:"Site araması",
  ai:"Ücretsiz AI",
  nohit:"Sitede yeterince ilgili bir rehber bulamadım. Daha kısa ve belirgin birkaç kelimeyle tekrar deneyebilirsiniz.",
  error:"AI servisine şu anda ulaşılamıyor. Bunun yerine sitedeki en yakın bilgileri buldum.",
  emergency:"Bu belirtiler acil değerlendirme gerektirebilir. Şiddetli göğüs ağrısı, ciddi nefes darlığı, yeni gelişen tek taraflı güçsüzlük, bayılma, ciddi kanama veya başka bir acil tehlike varsa 112’yi arayın ya da acil yardım alın.",
  sources:"İlgili rehberler"
};

var CONFIG_URL="/assets/assistant-config.json";
var SEARCH_URL=lang==="en"?"/ara-en.json":"/ara-tr.json";
var cfg={enabled:true,endpoint:"",modelLabel:""};
var indexPromise=null;

function el(tag,cls,text){var x=document.createElement(tag);if(cls)x.className=cls;if(text!=null)x.textContent=text;return x}
function normalize(s){return (s||"").toLocaleLowerCase(lang==="tr"?"tr-TR":"en-US").normalize("NFD").replace(/[\u0300-\u036f]/g,"").replace(/[^a-z0-9çğıöşü\s-]/gi," ").replace(/\s+/g," ").trim()}
var stop=new Set((lang==="en"?
"the a an and or to of in on for with is are was were be been this that what how can do does my your about from at by it i me".split(" "):
"ve veya ile bir bu şu o ne nasıl için gibi da de mı mi mu mü ben benim sen sizin siz bana bende olan olarak çok daha en".split(" ")));
function rootToken(t){
  if(lang==="tr"){
    if(/^bel/.test(t))return "bel";
    if(/^ağr/.test(t)||/^agr/.test(t))return "ağr";
    if(/^gebel/.test(t)||/^hamil/.test(t))return "gebelik";
    if(/^fıt/.test(t)||/^fit/.test(t))return "fıt";
    if(/^boyn/.test(t)||/^boyun/.test(t))return "boyun";
    if(/^omuz/.test(t))return "omuz";
    if(/^diz/.test(t))return "diz";
    if(/^kalç/.test(t)||/^kalc/.test(t))return "kalça";
    if(/^topuk/.test(t))return "topuk";
    if(/^ayak/.test(t))return "ayak";
    if(/^baş/.test(t)||/^bas/.test(t))return "baş";
    if(/^dirsek/.test(t)||/^dirseğ/.test(t)||/^dirseg/.test(t)||/^dirse/.test(t))return "dirsek";
    if(/^bilek/.test(t))return "bilek";
    if(/^çene/.test(t)||/^cene/.test(t))return "çene";
  }
  return t;
}
function tokens(q){
  var seen=new Set();
  return normalize(q).split(" ").filter(function(x){return x.length>2&&!stop.has(x)}).map(rootToken).filter(function(x){
    if(seen.has(x))return false;seen.add(x);return true;
  }).slice(0,14);
}

function flattenPage(p){
  var chunks=[];
  (p.s||[]).forEach(function(sec){
    var h=sec[0]||"";
    (sec[1]||[]).forEach(function(t){if(t&&t.length>24)chunks.push({h:h,t:t})});
  });
  return {u:p.u,t:p.t||"",k:p.k||"",d:p.d||"",chunks:chunks};
}
function loadIndex(){
  if(indexPromise)return indexPromise;
  indexPromise=fetch(SEARCH_URL,{cache:"force-cache"}).then(function(r){if(!r.ok)throw new Error("search index");return r.json()}).then(function(j){return (j.p||[]).map(flattenPage)});
  return indexPromise;
}
function scoreText(text,ts){
  var n=normalize(text),score=0;
  ts.forEach(function(t){
    if(!t)return;
    var variants=[t];
    if(t==="ağr")variants.push("agr");
    if(t==="fıt")variants.push("fit");
    var found=false,c=0;
    variants.forEach(function(v){
      if(found)return;
      var pos=n.indexOf(v);
      if(pos>=0){found=true;c=n.split(v).length-1}
    });
    if(found)score+=2+Math.min(c,3);
  });
  return score;
}
function bodyIntent(q){
  var n=normalize(q);
  if(lang==="tr"){
    if(/\b(boyn\w*|boyun\w*)\b/.test(n))return "neck";
    if(/\bbel\w*\b/.test(n))return "back";
    if(/\bomuz\w*\b/.test(n))return "shoulder";
    if(/\bdiz\w*\b/.test(n))return "knee";
    if(/\b(kalç\w*|kalc\w*)\b/.test(n))return "hip";
    if(/\btopuk\w*\b/.test(n))return "heel";
    if(/\b(baş\w*|bas\w*)\b/.test(n))return "head";
    if(/(^|\s)(dirsek\w*|dirseğ\w*|dirseg\w*|dirse\w*)(?=\s|$)/.test(n))return "elbow";
    if(/\b(çene\w*|cene\w*)\b/.test(n))return "jaw";
  }else{
    if(/\bneck\b/.test(n))return "neck";
    if(/\b(low back|back)\b/.test(n))return "back";
    if(/\bshoulder\b/.test(n))return "shoulder";
    if(/\bknee\b/.test(n))return "knee";
    if(/\bhip\b/.test(n))return "hip";
    if(/\bheel\b/.test(n))return "heel";
    if(/\b(head|headache)\b/.test(n))return "head";
    if(/\belbow\b/.test(n))return "elbow";
    if(/\b(jaw|tmj)\b/.test(n))return "jaw";
  }
  return "";
}
function matchesIntent(p,intent){
  if(!intent)return true;
  var u=(p.u||"").toLowerCase(), t=normalize(p.t||"");
  var rules=lang==="tr"?{
    neck:["boyun-agrisi.html","boyun-fitigi.html","bas-agrisi.html","masa-basi.html"],
    back:["bel-agrisi.html","bel-fitigi.html","dar-kanal.html","gebelikte-bel-agrisi.html"],
    shoulder:["omuz-sikismasi.html","rotator-manset-yirtigi.html","donuk-omuz.html"],
    knee:["diz-kireclenmesi.html","diz-onu-agrisi.html","menisku-yirtigi.html","on-capraz-bag.html"],
    hip:["kalca-kireclenmesi.html","kalca-kirigi.html"],
    heel:["topuk-dikeni.html"],
    head:["bas-agrisi.html","boyun-agrisi.html"],
    elbow:["tenisci-dirsegi.html"],
    jaw:["cene-eklemi.html"]
  }:{
    neck:["en/neck-pain.html","en/cervical-disc-herniation.html","en/headache.html","en/desk-work.html"],
    back:["en/low-back-pain.html","en/lumbar-disc-herniation.html","en/lumbar-spinal-stenosis.html","en/pregnancy-back-pain.html"],
    shoulder:["en/shoulder-impingement.html","en/rotator-cuff-tear.html","en/frozen-shoulder.html"],
    knee:["en/knee-osteoarthritis.html","en/anterior-knee-pain.html","en/meniscus-tear.html","en/acl-injury.html"],
    hip:["en/hip-osteoarthritis.html","en/hip-fracture-rehab.html"],
    heel:["en/plantar-fasciitis.html"],
    head:["en/headache.html","en/neck-pain.html"],
    elbow:["en/tennis-elbow.html"],
    jaw:["en/jaw-joint-tmd.html"]
  };
  return (rules[intent]||[]).indexOf(u)>=0;
}
function contextBoost(p,q){
  var n=normalize(q),u=(p.u||"").toLowerCase();
  var hasBack=n.indexOf("bel")>=0;
  var hasNeck=/\b(boyn\w*|boyun\w*)\b/.test(n)||n.indexOf("neck")>=0;
  var hasPain=n.indexOf("ağr")>=0||n.indexOf("agr")>=0||n.indexOf("pain")>=0;
  var pregnancy=n.indexOf("gebel")>=0||n.indexOf("hamil")>=0||n.indexOf("pregnan")>=0;
  var disc=n.indexOf("fıt")>=0||n.indexOf("fit")>=0||n.indexOf("hernia")>=0||n.indexOf("disc")>=0;

  if(lang==="tr"){
    if(u==="gebelikte-bel-agrisi.html") return pregnancy ? 180 : -180;
    if(u==="bel-fitigi.html") return (hasBack&&disc) ? 170 : (hasBack&&hasPain&&!disc ? -45 : 0);
    if(u==="bel-agrisi.html"&&hasBack&&hasPain&&!pregnancy&&!disc) return 200;
    if(u==="boyun-fitigi.html"&&hasNeck&&disc) return 170;
    if(u==="boyun-agrisi.html"&&hasNeck&&hasPain&&!disc) return 220;
    if(u==="masa-basi.html"&&hasNeck) return -35;
  }else{
    if(u==="en/pregnancy-back-pain.html") return pregnancy ? 180 : -180;
    if(u==="en/lumbar-disc-herniation.html") return (hasBack&&disc) ? 170 : (hasBack&&hasPain&&!disc ? -45 : 0);
    if(u==="en/low-back-pain.html"&&hasBack&&hasPain&&!pregnancy&&!disc) return 200;
    if(u==="en/cervical-disc-herniation.html"&&hasNeck&&disc) return 170;
    if(u==="en/neck-pain.html"&&hasNeck&&hasPain&&!disc) return 220;
    if(u==="en/desk-work.html"&&hasNeck) return -35;
  }
  return 0;
}
function search(q){
  var ts=tokens(q),intent=bodyIntent(q);
  if(!ts.length)return Promise.resolve([]);
  return loadIndex().then(function(pages){
    return pages.filter(function(p){return matchesIntent(p,intent)}).map(function(p){
      var titleScore=scoreText(p.t,ts);
      var s=titleScore*12+scoreText(p.k,ts)*4+scoreText(p.d,ts)*2+contextBoost(p,q);
      var chunks=p.chunks.map(function(c){return {h:c.h,t:c.t,s:scoreText((c.h||"")+" "+c.t,ts)}}).filter(function(c){return c.s>0}).sort(function(a,b){return b.s-a.s}).slice(0,3);
      chunks.forEach(function(c){s+=Math.min(c.s,8)});
      return {u:p.u,t:p.t,d:p.d,chunks:chunks,score:s};
    }).filter(function(x){return x.score>0}).sort(function(a,b){return b.score-a.score}).filter(function(x,i,arr){
      if(i===0)return true;
      return x.score>=Math.max(24,arr[0].score*0.28);
    }).slice(0,4);
  });
}
function emergency(q){
  var n=normalize(q);
  var terms=lang==="en"?
  ["severe chest pain","cant breathe","cannot breathe","one sided weakness","face droop","fainted","unconscious","severe bleeding","suicide","kill myself"]:
  ["şiddetli göğüs ağr","gogus agr","nefes alam","tek taraflı güçsüz","yüz kayması","bayıld","bilinçsiz","ciddi kanama","intihar","kendimi öldür"];
  return terms.some(function(t){return n.indexOf(normalize(t))>=0});
}
function localAnswer(results){
  if(!results.length)return {text:copy.nohit,sources:[]};
  var r=results[0],bits=[];
  if(r.d)bits.push(r.d);
  r.chunks.slice(0,2).forEach(function(c){bits.push(c.t)});
  var text=bits.join(" ").replace(/\s+/g," ").trim();
  if(text.length>720)text=text.slice(0,717).replace(/\s+\S*$/,"")+"…";
  var top=results[0]?results[0].score:0;
  var sources=results.filter(function(x,i){return i===0||x.score>=Math.max(24,top*0.35)}).slice(0,3);
  return {text:text||copy.nohit,sources:sources};
}
function sourceUrl(u){return u.startsWith("http")?u:"/"+u.replace(/^\//,"")}
function addMsg(kind,text,sources){
  var log=document.querySelector(".ieai-log");if(!log)return;
  var m=el("div","ieai-msg "+kind,text);log.appendChild(m);
  if(sources&&sources.length){
    var box=el("div","ieai-sources");
    sources.forEach(function(s){var a=el("a","ieai-source",s.t||s.u);a.href=sourceUrl(s.u);a.target="_self";box.appendChild(a)});
    m.appendChild(box);
  }
  log.scrollTop=log.scrollHeight;
}
function setMode(text){var x=document.querySelector(".ieai-mode");if(x)x.textContent=text}
function askAI(question,results){
  if(!cfg.endpoint)return Promise.reject(new Error("no endpoint"));
  var context=results.slice(0,4).map(function(r){return {title:r.t,url:sourceUrl(r.u),description:r.d,snippets:r.chunks.slice(0,3).map(function(c){return (c.h?c.h+": ":"")+c.t})}});
  return fetch(cfg.endpoint,{method:"POST",headers:{"content-type":"application/json"},body:JSON.stringify({question:question,lang:lang,context:context})})
    .then(function(r){if(!r.ok)throw new Error("AI "+r.status);return r.json()})
    .then(function(j){if(!j||!j.answer)throw new Error("empty");return {text:j.answer,sources:results.slice(0,4)}});
}
function submit(){
  var inp=document.querySelector(".ieai-input"),btn=document.querySelector(".ieai-send");
  var q=(inp.value||"").trim();if(!q)return;
  if(q.length>500)q=q.slice(0,500);
  inp.value="";btn.disabled=true;addMsg("user",q);
  if(emergency(q)){addMsg("bot",copy.emergency);btn.disabled=false;return}
  search(q).then(function(results){
    if(!results.length){addMsg("bot",copy.nohit);btn.disabled=false;return}
    if(cfg.endpoint){
      setMode(copy.ai);
      return askAI(q,results).then(function(a){addMsg("bot",a.text,a.sources)}).catch(function(){setMode(copy.local);var a=localAnswer(results);addMsg("bot",copy.error+"\n\n"+a.text,a.sources)});
    }else{
      setMode(copy.local);var a=localAnswer(results);addMsg("bot",a.text,a.sources);
    }
  }).catch(function(){addMsg("bot",copy.nohit)}).finally(function(){btn.disabled=false;inp.focus()});
}
function build(){
  if(document.querySelector(".ieai-launcher")||location.pathname.endsWith("/404.html")||document.title.indexOf("Sayfa bulunamadı")>=0)return;
  var b=el("button","ieai-launcher");b.type="button";b.setAttribute("aria-label",copy.title);
  b.innerHTML='<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 5.5A3.5 3.5 0 0 1 7.5 2h9A3.5 3.5 0 0 1 20 5.5v7a3.5 3.5 0 0 1-3.5 3.5H11l-4.8 4v-4A3.5 3.5 0 0 1 4 12.5z"/><path d="M8 8h8M8 11.5h5"/></svg><span>'+copy.title+"</span>";
  var p=el("section","ieai-panel");p.setAttribute("role","dialog");p.setAttribute("aria-label",copy.title);
  p.innerHTML='<div class="ieai-head"><div class="ieai-head-main"><div class="ieai-title">'+copy.title+'</div><div class="ieai-sub">'+copy.sub+' · <span class="ieai-status"><span class="ieai-dot"></span><span class="ieai-mode">'+copy.local+'</span></span></div></div><button class="ieai-close" type="button" aria-label="Close">×</button></div><div class="ieai-log"></div><div class="ieai-compose"><div class="ieai-row"><textarea class="ieai-input" maxlength="500" rows="1" placeholder="'+copy.placeholder+'"></textarea><button class="ieai-send" type="button">'+copy.send+'</button></div><div class="ieai-foot">'+copy.note+'</div></div>';
  document.body.appendChild(b);document.body.appendChild(p);
  addMsg("bot",copy.hello);addMsg("note",copy.note);
  b.addEventListener("click",function(){p.classList.toggle("is-open");if(p.classList.contains("is-open"))setTimeout(function(){p.querySelector(".ieai-input").focus()},50)});
  p.querySelector(".ieai-close").addEventListener("click",function(){p.classList.remove("is-open")});
  p.querySelector(".ieai-send").addEventListener("click",submit);
  p.querySelector(".ieai-input").addEventListener("keydown",function(e){if(e.key==="Enter"&&!e.shiftKey){e.preventDefault();submit()}});
}
function loadConfig(){
  return fetch(CONFIG_URL,{cache:"no-store"}).then(function(r){return r.ok?r.json():{}}).then(function(x){cfg=Object.assign(cfg,x||{})}).catch(function(){});
}
window.__IEAI_TEST__={search:search,normalize:normalize,tokens:tokens,bodyIntent:bodyIntent,matchesIntent:matchesIntent};
loadConfig().then(function(){if(cfg.enabled!==false)build()});
})();
