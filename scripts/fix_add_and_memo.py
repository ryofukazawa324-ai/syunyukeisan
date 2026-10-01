from pathlib import Path
p=Path('index.html')
s=p.read_text()
s=s.replace("const APP_VERSION='2026-10-01-06'", "const APP_VERSION='2026-10-01-07'")
# Avoid DOM-position/index mismatches entirely: suggestion buttons pass category index and set memo through a dedicated data attribute.
s=s.replace("function applySuggestion(i,j){const x=recentSuggestions(data[i].name)[j];if(!x)return;const memo=document.getElementById('memo-'+i);if(memo){memo.value=x.memo;memo.focus()}}","function applySuggestion(i,j){const x=recentSuggestions(data[i].name)[j];if(!x)return;const memo=document.querySelector('[data-memo-index=\"'+i+'\"]');if(memo){memo.value=x.memo;memo.focus()}}")
# Repair memo input markup if previous patch created malformed/duplicate id attributes.
import re
s=re.sub(r'\s+id=\\?"memo-\$\{i\}\\?"','',s)
# Add a safe data marker to memo input template.
s=s.replace('placeholder="メモ"', 'placeholder="メモ" data-memo-index="${i}"')
# Ensure Add button is explicit type=button so it cannot submit/reload anything.
s=s.replace('<button onclick="add(', '<button type="button" onclick="add(')
# Same for suggestion chips.
s=s.replace('<button type="button" class="suggestionBtn"', '<button type="button" class="suggestionBtn"')
p.write_text(s)
