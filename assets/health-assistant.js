
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
    if(/^omuz/.test(t)||/^omz/.test(t))return "omuz";
    if(/^diz/.test(t))return "diz";
    if(/^kalç/.test(t)||/^kalc/.test(t))return "kalça";
    if(/^topuk/.test(t)||/^topuğ/.test(t)||/^topug/.test(t)||/^topu/.test(t))return "topuk";
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
    if(t==="dirsek")variants.push("dirseğ","dirseg","dirse");
    if(t==="omuz")variants.push("omz");
    if(t==="topuk")variants.push("topuğ","topug","topu");
    if(t==="boyun")variants.push("boyn");
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
  var ts=normalize(q).split(" ").filter(Boolean).map(rootToken);
  var set=new Set(ts);
  if(set.has("boyun"))return "neck";
  if(set.has("bel"))return "back";
  if(set.has("omuz"))return "shoulder";
  if(set.has("diz"))return "knee";
  if(set.has("kalça"))return "hip";
  if(set.has("topuk"))return "heel";
  if(set.has("dirsek"))return "elbow";
  if(set.has("çene"))return "jaw";
  if(set.has("bilek"))return "wrist";
  if(set.has("ayak"))return "ankle";
  // Avoid mapping verbs such as "basınca" to head; accept only common head noun forms.
  var raw=normalize(q).split(" ");
  if(raw.some(function(x){return x==="bas"||/^bas(i|ı)m/.test(x)||/^bas(ta|da|tan|dan)$/.test(x)}))return "head";
  return "";
}
function specificIntent(q){
  var n=normalize(q);
  function hasAny(list){return list.some(function(x){return n.indexOf(x)>=0})}
  var body=bodyIntent(q);
  var pregnancy=hasAny(["gebel","hamil","pregnan"]);
  var disc=hasAny(["fitig","fıtık","fitik","hernia","disc"]);
  if(pregnancy&&body==="back")return "pregnancy-back";
  if(disc&&body==="back")return "lumbar-disc";
  if(disc&&body==="neck")return "cervical-disc";
  if(hasAny(["bas don","baş dön","vertigo","bppv"]))return "vertigo";
  if(hasAny(["fibromiyal","fibromyalgia"]))return "fibromyalgia";
  if(hasAny(["parkinson"]))return "parkinson";
  if(hasAny(["multipl skleroz","multiple sclerosis"])||/(^|\s)ms(?=\s|$)/.test(n))return "ms";
  if(hasAny(["felc","felç","inme","stroke"]))return "stroke";
  if(hasAny(["idrar kac","idrar kaç","urinary incontinence"]))return "incontinence";
  if(hasAny(["koah","copd"]))return "copd";
  if(hasAny(["kalp rehabil","cardiac rehab"]))return "cardiac-rehab";
  if(hasAny(["romatoid","rheumatoid"]))return "ra";
  if(hasAny(["ankilozan","ankylosing"]))return "as";
  if(hasAny(["kemik erimes","osteopor"]))return "osteoporosis";
  if(hasAny(["skolyoz","scoliosis"]))return "scoliosis";
  if(hasAny(["titreme","tremor"]))return "tremor";
  if(hasAny(["surekli us","sürekli üş","cold sensitivity"]))return "cold";
  if(hasAny(["uykusuz","uyku","sleep"]))return "sleep";
  if(hasAny(["stres","stress"]))return "stress";
  if(hasAny(["dusuy","düşüy","dusme","düşme","fall"]))return "falls";
  if(hasAny(["menisk","menisc"]))return "meniscus";
  if(hasAny(["on capraz","ön çapraz","acl"]))return "acl";
  if(hasAny(["rotator"]))return "rotator";
  if(hasAny(["donuk omuz","frozen shoulder"]))return "frozen-shoulder";
  if(hasAny(["karpal","carpal"]))return "carpal";
  if(hasAny(["burkul","sprain"]))return "ankle-sprain";
  if(hasAny(["asil","aşil","achilles"]))return "achilles";
  if(hasAny(["kanser","cancer"]))return "cancer";
  return "";
}
function routing(q){
  var specific=specificIntent(q), body=bodyIntent(q);
  var tr={
    "pregnancy-back":{urls:["gebelikte-bel-agrisi.html","bel-agrisi.html"],primary:"gebelikte-bel-agrisi.html"},
    "lumbar-disc":{urls:["bel-fitigi.html","bel-agrisi.html","dar-kanal.html"],primary:"bel-fitigi.html"},
    "cervical-disc":{urls:["boyun-fitigi.html","boyun-agrisi.html"],primary:"boyun-fitigi.html"},
    vertigo:{urls:["bas-donmesi.html"],primary:"bas-donmesi.html"},
    fibromyalgia:{urls:["fibromiyalji.html"],primary:"fibromiyalji.html"},
    parkinson:{urls:["parkinson.html"],primary:"parkinson.html"},
    ms:{urls:["multipl-skleroz.html"],primary:"multipl-skleroz.html"},
    stroke:{urls:["inme-rehabilitasyonu.html"],primary:"inme-rehabilitasyonu.html"},
    incontinence:{urls:["idrar-kacirma.html"],primary:"idrar-kacirma.html"},
    copd:{urls:["koah.html"],primary:"koah.html"},
    "cardiac-rehab":{urls:["kalp-rehabilitasyonu.html"],primary:"kalp-rehabilitasyonu.html"},
    ra:{urls:["romatoid-artrit.html"],primary:"romatoid-artrit.html"},
    as:{urls:["ankilozan-spondilit.html"],primary:"ankilozan-spondilit.html"},
    osteoporosis:{urls:["kemik-erimesi.html"],primary:"kemik-erimesi.html"},
    scoliosis:{urls:["skolyoz.html"],primary:"skolyoz.html"},
    tremor:{urls:["titreme.html"],primary:"titreme.html"},
    cold:{urls:["surekli-usume.html"],primary:"surekli-usume.html"},
    sleep:{urls:["uyku.html"],primary:"uyku.html"},
    stress:{urls:["stres.html"],primary:"stres.html"},
    falls:{urls:["dusme-onleme.html"],primary:"dusme-onleme.html"},
    meniscus:{urls:["menisku-yirtigi.html","diz-onu-agrisi.html"],primary:"menisku-yirtigi.html"},
    acl:{urls:["on-capraz-bag.html"],primary:"on-capraz-bag.html"},
    rotator:{urls:["rotator-manset-yirtigi.html","omuz-sikismasi.html"],primary:"rotator-manset-yirtigi.html"},
    "frozen-shoulder":{urls:["donuk-omuz.html"],primary:"donuk-omuz.html"},
    carpal:{urls:["karpal-tunel-sendromu.html"],primary:"karpal-tunel-sendromu.html"},
    "ankle-sprain":{urls:["ayak-bilegi-burkulmasi.html"],primary:"ayak-bilegi-burkulmasi.html"},
    achilles:{urls:["asil-tendinopatisi.html"],primary:"asil-tendinopatisi.html"},
    cancer:{urls:["kanser-egzersiz.html"],primary:"kanser-egzersiz.html"}
  };
  var en={
    "pregnancy-back":{urls:["en/pregnancy-back-pain.html","en/low-back-pain.html"],primary:"en/pregnancy-back-pain.html"},
    "lumbar-disc":{urls:["en/lumbar-disc-herniation.html","en/low-back-pain.html","en/lumbar-spinal-stenosis.html"],primary:"en/lumbar-disc-herniation.html"},
    "cervical-disc":{urls:["en/cervical-disc-herniation.html","en/neck-pain.html"],primary:"en/cervical-disc-herniation.html"},
    vertigo:{urls:["en/vertigo-bppv.html"],primary:"en/vertigo-bppv.html"},
    fibromyalgia:{urls:["en/fibromyalgia.html"],primary:"en/fibromyalgia.html"},
    parkinson:{urls:["en/parkinsons-disease.html"],primary:"en/parkinsons-disease.html"},
    ms:{urls:["en/multiple-sclerosis.html"],primary:"en/multiple-sclerosis.html"},
    stroke:{urls:["en/stroke-rehabilitation.html"],primary:"en/stroke-rehabilitation.html"},
    incontinence:{urls:["en/urinary-incontinence.html"],primary:"en/urinary-incontinence.html"},
    copd:{urls:["en/copd-pulmonary-rehabilitation.html"],primary:"en/copd-pulmonary-rehabilitation.html"},
    "cardiac-rehab":{urls:["en/cardiac-rehabilitation.html"],primary:"en/cardiac-rehabilitation.html"},
    ra:{urls:["en/rheumatoid-arthritis.html"],primary:"en/rheumatoid-arthritis.html"},
    as:{urls:["en/ankylosing-spondylitis.html"],primary:"en/ankylosing-spondylitis.html"},
    osteoporosis:{urls:["en/osteoporosis.html"],primary:"en/osteoporosis.html"},
    scoliosis:{urls:["en/scoliosis.html"],primary:"en/scoliosis.html"},
    tremor:{urls:["en/tremor.html"],primary:"en/tremor.html"},
    sleep:{urls:["en/sleep.html"],primary:"en/sleep.html"},
    stress:{urls:["en/stress.html"],primary:"en/stress.html"},
    falls:{urls:["en/fall-prevention.html"],primary:"en/fall-prevention.html"},
    meniscus:{urls:["en/meniscus-tear.html","en/anterior-knee-pain.html"],primary:"en/meniscus-tear.html"},
    acl:{urls:["en/acl-injury.html"],primary:"en/acl-injury.html"},
    rotator:{urls:["en/rotator-cuff-tear.html","en/shoulder-impingement.html"],primary:"en/rotator-cuff-tear.html"},
    "frozen-shoulder":{urls:["en/frozen-shoulder.html"],primary:"en/frozen-shoulder.html"},
    carpal:{urls:["en/carpal-tunnel-syndrome.html"],primary:"en/carpal-tunnel-syndrome.html"},
    "ankle-sprain":{urls:["en/ankle-sprain.html"],primary:"en/ankle-sprain.html"},
    achilles:{urls:["en/achilles-tendinopathy.html"],primary:"en/achilles-tendinopathy.html"},
    cancer:{urls:["en/exercise-and-cancer.html"],primary:"en/exercise-and-cancer.html"}
  };
  var map=lang==="tr"?tr:en;
  if(specific&&map[specific])return {key:specific,urls:map[specific].urls,primary:map[specific].primary,body:body};
  var bodies=lang==="tr"?{
    neck:["boyun-agrisi.html","boyun-fitigi.html","bas-agrisi.html","masa-basi.html"],
    back:["bel-agrisi.html","bel-fitigi.html","dar-kanal.html","gebelikte-bel-agrisi.html"],
    shoulder:["omuz-sikismasi.html","rotator-manset-yirtigi.html","donuk-omuz.html"],
    knee:["diz-onu-agrisi.html","diz-kireclenmesi.html","menisku-yirtigi.html","on-capraz-bag.html"],
    hip:["kalca-kireclenmesi.html","kalca-kirigi.html","protez-sonrasi.html"],
    heel:["topuk-dikeni.html","asil-tendinopatisi.html"],
    head:["bas-agrisi.html","bas-donmesi.html","boyun-agrisi.html"],
    elbow:["tenisci-dirsegi.html"],
    jaw:["cene-eklemi.html"],
    wrist:["karpal-tunel-sendromu.html"],
    ankle:["ayak-bilegi-burkulmasi.html","asil-tendinopatisi.html","topuk-dikeni.html"]
  }:{
    neck:["en/neck-pain.html","en/cervical-disc-herniation.html","en/headache.html","en/desk-work.html"],
    back:["en/low-back-pain.html","en/lumbar-disc-herniation.html","en/lumbar-spinal-stenosis.html","en/pregnancy-back-pain.html"],
    shoulder:["en/shoulder-impingement.html","en/rotator-cuff-tear.html","en/frozen-shoulder.html"],
    knee:["en/anterior-knee-pain.html","en/knee-osteoarthritis.html","en/meniscus-tear.html","en/acl-injury.html"],
    hip:["en/hip-osteoarthritis.html","en/hip-fracture-rehab.html","en/joint-replacement-rehab.html"],
    heel:["en/plantar-fasciitis.html","en/achilles-tendinopathy.html"],
    head:["en/headache.html","en/vertigo-bppv.html","en/neck-pain.html"],
    elbow:["en/tennis-elbow.html"],
    jaw:["en/jaw-joint-tmd.html"],
    wrist:["en/carpal-tunnel-syndrome.html"],
    ankle:["en/ankle-sprain.html","en/achilles-tendinopathy.html","en/plantar-fasciitis.html"]
  };
  var primary=body&&bodies[body]&&bodies[body][0];
  return {key:body||"",urls:body?bodies[body]||[]:[],primary:primary||"",body:body};
}
function matchesRoute(p,route){
  if(!route||!route.urls||!route.urls.length)return true;
  return route.urls.indexOf((p.u||"").toLowerCase())>=0;
}
function contextBoost(p,q){
  var n=normalize(q),u=(p.u||"").toLowerCase(),route=routing(q);
  var boost=(route.primary===u)?260:0;
  var pregnancy=n.indexOf("gebel")>=0||n.indexOf("hamil")>=0||n.indexOf("pregnan")>=0;
  var disc=n.indexOf("fitig")>=0||n.indexOf("fitik")>=0||n.indexOf("hernia")>=0||n.indexOf("disc")>=0;
  if(lang==="tr"){
    if(u==="gebelikte-bel-agrisi.html"&&!pregnancy)boost-=200;
    if(u==="bel-fitigi.html"&&route.body==="back"&&!disc)boost-=70;
    if(u==="boyun-fitigi.html"&&route.body==="neck"&&!disc)boost-=70;
    if(u==="masa-basi.html"&&route.body==="neck")boost-=45;
  }else{
    if(u==="en/pregnancy-back-pain.html"&&!pregnancy)boost-=200;
    if(u==="en/lumbar-disc-herniation.html"&&route.body==="back"&&!disc)boost-=70;
    if(u==="en/cervical-disc-herniation.html"&&route.body==="neck"&&!disc)boost-=70;
    if(u==="en/desk-work.html"&&route.body==="neck")boost-=45;
  }
  return boost;
}
function search(q){
  var ts=tokens(q),route=routing(q);
  if(!ts.length)return Promise.resolve([]);
  return loadIndex().then(function(pages){
    return pages.filter(function(p){return matchesRoute(p,route)}).map(function(p){
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
function localAnswer(results,question){
  if(!results.length)return {text:copy.nohit,sources:[]};
  var r=results[0],bits=[],intent=bodyIntent(question||"");
  var genericCaution={
    tr:{
      elbow:"Dirsek ağrısının birçok nedeni olabilir; aşağıdaki rehber en yakın içeriktir ve tek başına tanı anlamına gelmez.",
      knee:"Diz ağrısının farklı nedenleri olabilir; aşağıdaki rehberler olası konuları ayırt etmek için bilgilendirme amaçlıdır.",
      shoulder:"Omuz ağrısının farklı nedenleri olabilir; aşağıdaki rehberler bilgilendirme amaçlıdır.",
      hip:"Kalça ağrısının farklı nedenleri olabilir; aşağıdaki rehberler bilgilendirme amaçlıdır.",
      heel:"Topuk ağrısının farklı nedenleri olabilir; aşağıdaki rehber en yakın içeriktir ve tek başına tanı anlamına gelmez.",
      jaw:"Çene bölgesi ağrısının farklı nedenleri olabilir; aşağıdaki rehber bilgilendirme amaçlıdır."
    },
    en:{
      elbow:"Elbow pain can have several causes; the guide below is the closest match and is not a diagnosis.",
      knee:"Knee pain can have several causes; the guides below are for information and differential context.",
      shoulder:"Shoulder pain can have several causes; the guides below are for information.",
      hip:"Hip pain can have several causes; the guides below are for information.",
      heel:"Heel pain can have several causes; the guide below is the closest match and is not a diagnosis.",
      jaw:"Jaw-region pain can have several causes; the guide below is for information."
    }
  };
  var caution=genericCaution[lang]&&genericCaution[lang][intent];
  if(caution)bits.push(caution);
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
    sources.forEach(function(s){
      var a=el("a","ieai-source",s.t||s.u);a.href=sourceUrl(s.u);a.target="_self";
      a.addEventListener("click",function(){
        var panel=document.querySelector(".ieai-panel");
        if(panel)panel.classList.remove("is-open");
      });
      box.appendChild(a)
    });
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
      return askAI(q,results).then(function(a){addMsg("bot",a.text,a.sources)}).catch(function(){setMode(copy.local);var a=localAnswer(results,q);addMsg("bot",copy.error+"\n\n"+a.text,a.sources)});
    }else{
      setMode(copy.local);var a=localAnswer(results,q);addMsg("bot",a.text,a.sources);
    }
  }).catch(function(){addMsg("bot",copy.nohit)}).finally(function(){btn.disabled=false;inp.focus()});
}
function addInlineCard(){
  if(document.querySelector(".ieai-inline"))return;
  var host=document.querySelector("footer")||document.body;
  var card=el("section","ieai-inline");
  card.innerHTML=lang==="en"
    ? '<div class="ieai-inline-inner"><div><span class="ieai-inline-kicker">Health Guide Assistant</span><h2>Ask the health guides</h2><p>Type a short question. The assistant searches the information published on this website and points you to the closest guides.</p></div><button type="button" class="ieai-inline-open">Ask a question</button></div>'
    : '<div class="ieai-inline-inner"><div><span class="ieai-inline-kicker">Sağlık Rehberi Asistanı</span><h2>Sağlık rehberlerine sorun</h2><p>Kısa bir soru yazın. Asistan bu sitede yayımlanan bilgileri tarar ve en ilgili rehberleri gösterir.</p></div><button type="button" class="ieai-inline-open">Soru sor</button></div>';
  host.parentNode.insertBefore(card,host);
  card.querySelector(".ieai-inline-open").addEventListener("click",function(){
    var panel=document.querySelector(".ieai-panel");
    if(panel){panel.classList.add("is-open");document.documentElement.classList.add("ieai-open");setTimeout(function(){var i=panel.querySelector(".ieai-input");if(i)i.focus()},50)}
  });
}
function syncBottomControls(){
  var fab=document.querySelector(".fab");
  var active=!!(fab&&fab.classList.contains("on"));
  document.documentElement.classList.toggle("ieai-bottom-control-visible",active);
}
function observeBottomControls(){
  var fab=document.querySelector(".fab");
  if(!fab)return;
  syncBottomControls();
  new MutationObserver(syncBottomControls).observe(fab,{attributes:true,attributeFilter:["class","aria-hidden"]});
  window.addEventListener("resize",syncBottomControls,{passive:true});
}
function build(){
  if(document.querySelector(".ieai-launcher")||location.pathname.endsWith("/404.html")||document.title.indexOf("Sayfa bulunamadı")>=0)return;
  var b=el("button","ieai-launcher");b.type="button";b.setAttribute("aria-label",copy.title);
  b.innerHTML='<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 5.5A3.5 3.5 0 0 1 7.5 2h9A3.5 3.5 0 0 1 20 5.5v7a3.5 3.5 0 0 1-3.5 3.5H11l-4.8 4v-4A3.5 3.5 0 0 1 4 12.5z"/><path d="M8 8h8M8 11.5h5"/></svg><span>'+copy.title+"</span>";
  var p=el("section","ieai-panel");p.setAttribute("role","dialog");p.setAttribute("aria-label",copy.title);
  p.innerHTML='<div class="ieai-head"><div class="ieai-head-main"><div class="ieai-title">'+copy.title+'</div><div class="ieai-sub">'+copy.sub+' · <span class="ieai-status"><span class="ieai-dot"></span><span class="ieai-mode">'+copy.local+'</span></span></div></div><button class="ieai-close" type="button" aria-label="Close">×</button></div><div class="ieai-log"></div><div class="ieai-compose"><div class="ieai-row"><textarea class="ieai-input" maxlength="500" rows="1" placeholder="'+copy.placeholder+'"></textarea><button class="ieai-send" type="button">'+copy.send+'</button></div><div class="ieai-foot">'+copy.note+'</div></div>';
  document.body.appendChild(b);document.body.appendChild(p);
  addMsg("bot",copy.hello);addMsg("note",copy.note);
  b.addEventListener("click",function(){
    p.classList.toggle("is-open");
    document.documentElement.classList.toggle("ieai-open",p.classList.contains("is-open"));
    if(p.classList.contains("is-open"))setTimeout(function(){p.querySelector(".ieai-input").focus()},50)
  });
  p.querySelector(".ieai-close").addEventListener("click",function(){p.classList.remove("is-open");document.documentElement.classList.remove("ieai-open")});
  p.querySelector(".ieai-send").addEventListener("click",submit);
  p.querySelector(".ieai-input").addEventListener("keydown",function(e){if(e.key==="Enter"&&!e.shiftKey){e.preventDefault();submit()}});
  addInlineCard();
  observeBottomControls();
}
function loadConfig(){
  return fetch(CONFIG_URL,{cache:"no-store"}).then(function(r){return r.ok?r.json():{}}).then(function(x){cfg=Object.assign(cfg,x||{})}).catch(function(){});
}
window.__IEAI_TEST__={search:search,normalize:normalize,tokens:tokens,bodyIntent:bodyIntent,specificIntent:specificIntent,routing:routing,matchesRoute:matchesRoute};
loadConfig().then(function(){if(cfg.enabled!==false)build()});
})();
