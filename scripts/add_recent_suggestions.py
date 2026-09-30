from pathlib import Path
p=Path('index.html')
s=p.read_text()
s=s.replace("const APP_VERSION='2026-10-01-02'", "const APP_VERSION='2026-10-01-03'")
s=s.replace(".history{font-size:12px", ".suggestions{display:flex;gap:6px;overflow-x:auto;margin-top:8px;padding-bottom:2px}.suggestionBtn{border:1px solid #d7dde4;background:#f6f8fa;color:#294f7a;border-radius:10px;padding:7px 9px;font-size:12px;white-space:nowrap}.history{font-size:12px",1)
needle="function render(){"
helper="function recentSuggestions(catName){const out=[];let m=current;for(let z=0;z<24&&out.length<3;z++){const cats=m===current?data:(localStorage.getItem(key(m))?normalize(JSON.parse(localStorage.getItem(key(m)))):[]),c=cats.find(x=>x.name===catName);if(c)for(let i=c.items.length-1;i>=0&&out.length<3;i--){const x=c.items[i];if(Number(x.amount)>0)out.push({amount:Number(x.amount),memo:String(x.memo||'')})}m=prevMonth(m)}return out}function applySuggestion(i,j){const x=recentSuggestions(data[i].name)[j];if(!x)return;const q=document.querySelectorAll('.quick')[i];if(!q)return;const ins=q.querySelectorAll('input');if(ins[0])ins[0].value=x.amount;if(ins[1])ins[1].value=x.memo;if(ins[0])ins[0].focus()}"
if helper not in s:
    s=s.replace(needle,helper+needle,1)
# Insert suggestion chips after each quick input area by extending card HTML generation at the common history marker.
old="</div><div class=\"history\">"
new="</div>${recentSuggestions(c.name).length?'<div class=\"suggestions\">'+recentSuggestions(c.name).map((x,j)=>'<button type=\"button\" class=\"suggestionBtn\" onclick=\"applySuggestion('+i+','+j+')\">'+yen(x.amount)+(x.memo?' '+escapeHtml(x.memo):'')+'</button>').join('')+'</div>':''}<div class=\"history\">"
if old not in s:
    raise SystemExit('card history marker not found')
s=s.replace(old,new)
p.write_text(s)
