from pathlib import Path
p=Path('index.html')
s=p.read_text()
s=s.replace("const APP_VERSION='2026-10-01-04'", "const APP_VERSION='2026-10-01-05'")
s=s.replace('oninput="calcSolo()"','oninput="saveSoloSimulation();calcSolo()"')
needle="function calcSolo(){"
helper="const SOLO_SIM_KEY='budget-solo-simulation';function loadSoloSimulation(){try{const v=JSON.parse(localStorage.getItem(SOLO_SIM_KEY)||'{}');['simIncome','simRent','simFood','simUtility','simComm','simTransport','simFun','simDaily','simLoan','simInvest'].forEach(id=>{if(v[id]!==undefined&&document.getElementById(id))document.getElementById(id).value=v[id]})}catch(e){}}function saveSoloSimulation(){const v={};['simIncome','simRent','simFood','simUtility','simComm','simTransport','simFun','simDaily','simLoan','simInvest'].forEach(id=>{const el=document.getElementById(id);if(el)v[id]=el.value});localStorage.setItem(SOLO_SIM_KEY,JSON.stringify(v))}"
if needle not in s: raise SystemExit('calcSolo not found')
s=s.replace(needle,helper+needle,1)
# Load saved simulation values before first calculation.
idx=s.rfind('calcSolo()')
if idx<0: raise SystemExit('initial calcSolo call not found')
s=s[:idx]+'loadSoloSimulation();'+s[idx:]
p.write_text(s)
