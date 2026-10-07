#!/usr/bin/env node
const fs = require("fs");
const vm = require("vm");

const assistant = fs.readFileSync("assets/health-assistant.js","utf8");
const trIndex = JSON.parse(fs.readFileSync("ara-tr.json","utf8"));
const enIndex = JSON.parse(fs.readFileSync("ara-en.json","utf8"));

function makeContext(lang){
  const noopEl = () => ({
    classList:{contains:()=>false,toggle:()=>{},add:()=>{},remove:()=>{}},
    setAttribute:()=>{},appendChild:()=>{},addEventListener:()=>{},
    querySelector:()=>null,querySelectorAll:()=>[],
    style:{},textContent:"",innerHTML:"",parentNode:{insertBefore:()=>{}}
  });
  const context = {
    console,
    setTimeout:(fn)=>{ if(typeof fn==="function") fn(); return 1; },
    clearTimeout:()=>{},
    MutationObserver:function(){this.observe=()=>{}},
    location:{pathname:"/"},
    document:{
      documentElement:{lang,classList:{toggle:()=>{},add:()=>{},remove:()=>{}}},
      title:"",
      readyState:"loading",
      addEventListener:()=>{},
      querySelector:()=>null,
      querySelectorAll:()=>[],
      createElement:noopEl,
      body:noopEl(),
      head:noopEl()
    },
    window:{
      __IEAI_LOADED__:false,
      innerHeight:800,
      addEventListener:()=>{},
      SiteCore:{}
    }
  };
  context.window.window=context.window;
  context.window.document=context.document;
  context.globalThis=context;
  context.fetch=async function(url){
    if(String(url).includes("assistant-config.json")) return {ok:true,json:async()=>({enabled:false,endpoint:""})};
    if(String(url).includes("ara-tr.json")) return {ok:true,json:async()=>trIndex};
    if(String(url).includes("ara-en.json")) return {ok:true,json:async()=>enIndex};
    return {ok:false,json:async()=>({})};
  };
  vm.createContext(context);
  vm.runInContext(assistant,context,{filename:"assets/health-assistant.js"});
  return context;
}

const ctx = makeContext("tr");
const api = ctx.window.__IEAI_TEST__;
if(!api || !api.search || !api.routing) throw new Error("Production assistant test API unavailable");

const generic = {
  "bel-agrisi.html":[
    "belim","belimde","bel bölgem","bel tarafım","bel ağrım"
  ],
  "boyun-agrisi.html":[
    "boynum","boynumda","boyun bölgem","boyun tarafım"
  ],
  "omuz-sikismasi.html":[
    "omzum","omzumda","omuzum","omuz bölgem"
  ],
  "diz-onu-agrisi.html":[
    "dizim","dizimde","diz bölgem","diz kapağım"
  ],
  "kalca-kireclenmesi.html":[
    "kalçam","kalçamda","kalça bölgem"
  ],
  "topuk-dikeni.html":[
    "topuğum","topugum","topuğumda","topuk bölgem"
  ],
  "tenisci-dirsegi.html":[
    "dirseğim","dirseği","dirseğimde","dirsek bölgem"
  ],
  "cene-eklemi.html":[
    "çenem","cenem","çenemde","çene bölgem"
  ],
  "karpal-tunel-sendromu.html":[
    "bileğim","bileğimde","el bileğim"
  ],
  "ayak-bilegi-burkulmasi.html":[
    "ayak bileğim","ayak bileğimde"
  ],
  "bas-agrisi.html":[
    "başım","başımda","baş ağrım"
  ]
};

const painPhrases=[
  "{x} ağrıyor","{x} çok ağrıyor","{x} birkaç gündür ağrıyor","{x} sızlıyor",
  "{x} tutuldu","{x} ağrım var","{x} hareket edince ağrıyor","{x} gece ağrıyor",
  "{x} için ne yapabilirim","{x} neden ağrır","{x} ağrısına ne iyi gelir",
  "{x} ağrısı var","{x} acıyor","{x} ağrısı geçmiyor","merhaba {x} ağrıyor",
  "hocam {x} ağrıyor","spor sonrası {x} ağrıyor","sabahları {x} ağrıyor",
  "oturunca {x} ağrıyor","yürürken {x} ağrıyor","uzun süredir {x} ağrıyor",
  "bugün {x} ağrıyor","dünden beri {x} ağrıyor","bazen {x} ağrıyor"
];
const prefixes=["","çok","hafif","ara sıra","son zamanlarda","yaklaşık iki gündür","bir haftadır","üç gündür"];
const suffixes=[""," ne olabilir"," ne yapmalıyım"," egzersiz olur mu"," hangi rehbere bakayım"," bilgi verir misin"," doktora gitmeli miyim"];

const special=[
  ["gebelikte bel ağrısı","gebelikte-bel-agrisi.html"],
  ["hamileyim belim ağrıyor","gebelikte-bel-agrisi.html"],
  ["hamilelikte bel ağrısı","gebelikte-bel-agrisi.html"],
  ["bel fıtığım var","bel-fitigi.html"],
  ["bel fitigi ve siyatik","bel-fitigi.html"],
  ["boyun fıtığım var","boyun-fitigi.html"],
  ["boyun fitigi koluma vuruyor","boyun-fitigi.html"],
  ["başım dönüyor","bas-donmesi.html"],
  ["bppv nedir","bas-donmesi.html"],
  ["fibromiyaljim var","fibromiyalji.html"],
  ["parkinson egzersizleri","parkinson.html"],
  ["ms hastası egzersiz","multipl-skleroz.html"],
  ["multipl skleroz egzersiz","multipl-skleroz.html"],
  ["inme sonrası egzersiz","inme-rehabilitasyonu.html"],
  ["felç sonrası rehabilitasyon","inme-rehabilitasyonu.html"],
  ["idrar kaçırıyorum","idrar-kacirma.html"],
  ["koah egzersizleri","koah.html"],
  ["kalp rehabilitasyonu","kalp-rehabilitasyonu.html"],
  ["romatoid artrit egzersiz","romatoid-artrit.html"],
  ["ankilozan spondilit egzersiz","ankilozan-spondilit.html"],
  ["kemik erimesi egzersiz","kemik-erimesi.html"],
  ["skolyoz egzersiz","skolyoz.html"],
  ["elim titriyor","titreme.html"],
  ["sürekli üşüyorum","surekli-usume.html"],
  ["uyuyamıyorum","uyku.html"],
  ["çok stresliyim","stres.html"],
  ["sık düşüyorum","dusme-onleme.html"],
  ["menisküs yırtığı","menisku-yirtigi.html"],
  ["ön çapraz bağ yaralanması","on-capraz-bag.html"],
  ["rotator manşet yırtığı","rotator-manset-yirtigi.html"],
  ["donuk omuz","donuk-omuz.html"],
  ["karpal tünel","karpal-tunel-sendromu.html"],
  ["ayak bileği burkuldu","ayak-bilegi-burkulmasi.html"],
  ["aşil tendiniti","asil-tendinopatisi.html"],
  ["kanser tedavisinde egzersiz","kanser-egzersiz.html"]
];

// False-positive guards: these must NOT be interpreted as body parts.
const negatives=[
  ["belki egzersiz yaparım","back"],
  ["dize geldi şiir","knee"],
  ["basınca ağrıyor","head"],
  ["omuz omuza verdik","shoulder"],
  ["topu atınca ağrıdı","heel"]
];

let total=0, failures=[];
async function check(q, expected){
  total++;
  const route=api.routing(q);
  const results=await api.search(q);
  const got=results[0] && results[0].u;
  if(got!==expected) failures.push({q,expected,got:got||"none",route});
}

(async()=>{
  for(const [expected,forms] of Object.entries(generic)){
    for(const x of forms){
      for(const phrase of painPhrases){
        for(const pre of prefixes){
          for(const suf of suffixes){
            const q=[pre,phrase.replace("{x}",x),suf].filter(Boolean).join(" ");
            await check(q,expected);
            if(failures.length>=100) break;
          }
          if(failures.length>=100) break;
        }
        if(failures.length>=100) break;
      }
      if(failures.length>=100) break;
    }
    if(failures.length>=100) break;
  }
  for(const [q,e] of special) await check(q,e);
  for(const [q,badIntent] of negatives){
    total++;
    const r=api.routing(q);
    if(r.body===badIntent) failures.push({q,expected:"not "+badIntent,got:r.body,route:r});
  }
  console.log("Production assistant regression: "+total+" questions tested.");
  if(failures.length){
    console.error("FAILED: "+failures.length);
    failures.slice(0,100).forEach(x=>console.error(JSON.stringify(x)));
    process.exit(1);
  }
  console.log("PASS: production routing returned the expected top guide for all generated questions.");
})().catch(e=>{console.error(e);process.exit(1)});
