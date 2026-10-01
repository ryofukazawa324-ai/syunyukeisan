from pathlib import Path
p=Path('index.html')
s=p.read_text()
s=s.replace("const APP_VERSION='2026-10-01-05'", "const APP_VERSION='2026-10-01-06'")
old="function applySuggestion(i,j){const x=recentSuggestions(data[i].name)[j];if(!x)return;const q=document.querySelectorAll('.quick')[i];if(!q)return;const ins=q.querySelectorAll('input');if(ins[1]){ins[1].value=x.memo;ins[1].focus()}}"
new="function applySuggestion(i,j){const x=recentSuggestions(data[i].name)[j];if(!x)return;const memo=document.getElementById('memo-'+i);if(memo){memo.value=x.memo;memo.focus()}}"
if old not in s: raise SystemExit('applySuggestion target not found')
s=s.replace(old,new,1)
# Give each memo input a stable id so sorting cards does not break the category-index lookup.
old2="placeholder=\"メモ\" value=\"\""
new2="placeholder=\"メモ\" id=\"memo-${i}\" value=\"\""
if old2 in s:s=s.replace(old2,new2)
else:
    # handle template form without explicit empty value
    s=s.replace('placeholder="メモ"', 'placeholder="メモ" id="memo-${i}"')
p.write_text(s)
