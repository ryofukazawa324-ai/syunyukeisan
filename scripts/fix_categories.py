from pathlib import Path
p=Path('index.html')
s=p.read_text()
s=s.replace("const APP_VERSION='2026-10-01-01'", "const APP_VERSION='2026-10-01-02'")
old="function ensureCategories(arr){const out=normalize(arr);[...BASE_NAMES,...SOLO_NAMES].forEach(n=>{if(!out.some(x=>x.name===n))out.push({name:n,items:[]})});return out}"
new="function ensureCategories(arr){return normalize(arr)}"
if old not in s: raise SystemExit('ensureCategories not found')
s=s.replace(old,new,1)
old="function load(m){const s=localStorage.getItem(key(m));if(s)try{return ensureCategories(JSON.parse(s))}catch(e){}const out=ensureCategories([]);if(m>'2026-08')RECURRING_NAMES.forEach(name=>{const v=findPreviousCategoryAmount(m,name);if(v>0)out.find(x=>x.name===name).items=[{amount:v,memo:'先月から据え置き'}]});return out}"
new="function load(m){const s=localStorage.getItem(key(m));if(s)try{return ensureCategories(JSON.parse(s))}catch(e){}let p=prevMonth(m),prev=null;for(let i=0;i<120;i++){const ps=localStorage.getItem(key(p));if(ps){try{prev=normalize(JSON.parse(ps));break}catch(e){}}p=prevMonth(p)}if(prev)return prev.map(c=>({name:c.name,items:[]}));return BASE_NAMES.map(name=>({name,items:[]}))}"
if old not in s: raise SystemExit('load not found')
s=s.replace(old,new,1)
p.write_text(s)
