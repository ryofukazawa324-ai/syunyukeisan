from pathlib import Path
p=Path('index.html')
s=p.read_text()
s=s.replace("const APP_VERSION='2026-10-01-03'", "const APP_VERSION='2026-10-01-04'")
old="function applySuggestion(i,j){const x=recentSuggestions(data[i].name)[j];if(!x)return;const q=document.querySelectorAll('.quick')[i];if(!q)return;const ins=q.querySelectorAll('input');if(ins[0])ins[0].value=x.amount;if(ins[1])ins[1].value=x.memo;if(ins[0])ins[0].focus()}"
new="function applySuggestion(i,j){const x=recentSuggestions(data[i].name)[j];if(!x)return;const q=document.querySelectorAll('.quick')[i];if(!q)return;const ins=q.querySelectorAll('input');if(ins[1]){ins[1].value=x.memo;ins[1].focus()}}"
if old not in s: raise SystemExit('applySuggestion not found')
s=s.replace(old,new,1)
# Chips should display memo only, deduplicated; preserve free typing in memo field.
old="function recentSuggestions(catName){const out=[];let m=current;for(let z=0;z<24&&out.length<3;z++){const cats=m===current?data:(localStorage.getItem(key(m))?normalize(JSON.parse(localStorage.getItem(key(m)))):[]),c=cats.find(x=>x.name===catName);if(c)for(let i=c.items.length-1;i>=0&&out.length<3;i--){const x=c.items[i];if(Number(x.amount)>0)out.push({amount:Number(x.amount),memo:String(x.memo||'')})}m=prevMonth(m)}return out}"
new="function recentSuggestions(catName){const out=[],seen=new Set();let m=current;for(let z=0;z<24&&out.length<3;z++){const raw=localStorage.getItem(key(m)),cats=m===current?data:(raw?normalize(JSON.parse(raw)):[]),c=cats.find(x=>x.name===catName);if(c)for(let i=c.items.length-1;i>=0&&out.length<3;i--){const memo=String(c.items[i].memo||'').trim();if(memo&&!seen.has(memo)){seen.add(memo);out.push({memo})}}m=prevMonth(m)}return out}"
if old not in s: raise SystemExit('recentSuggestions not found')
s=s.replace(old,new,1)
# Replace chip label expression from amount+memo to memo only.
s=s.replace("'+yen(x.amount)+(x.memo?' '+escapeHtml(x.memo):'')+'", "'+escapeHtml(x.memo)+'")
p.write_text(s)
