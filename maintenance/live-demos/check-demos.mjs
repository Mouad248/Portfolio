// Exercise the actual browser modules with a small DOM harness, including filters,
// scenario selection and downloads. No generated site content is executed as code.
import {readFileSync} from 'node:fs';
import {resolve,dirname} from 'node:path';
import {SourceTextModule,createContext} from 'node:vm';
import assert from 'node:assert/strict';
const root=dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/,'$1'));

async function loadDemo(name,tabs){
 const base=resolve(root,name,'dist'),elements=new Map(),buttons=tabs.map(tab=>({dataset:{tab},classList:{toggle(){}},setAttribute(){}}));
 const get=s=>{if(!elements.has(s))elements.set(s,{value:'all',innerHTML:'',focus(){},setSelectionRange(){},insertAdjacentHTML(){}});return elements.get(s)};
 const document={querySelector:get,querySelectorAll(s){if(s==='[data-tab]')return buttons;if(s==='[data-scenario]'){return ['Downside','Base','Upside'].map(s=>{const b=get('scenario-'+s);b.dataset={scenario:s};return b})}return []},createElement(){return {click(){}}}};
 const context=createContext({document,fetch:async()=>({ok:true,json:async()=>JSON.parse(readFileSync(resolve(base,'data.json'),'utf8'))}),console,Intl,Date,Map,Set,URL:{createObjectURL(){return 'blob:test'},revokeObjectURL(){}},Blob,setTimeout});
 const modules=new Map();async function module(file){if(modules.has(file))return modules.get(file);const m=new SourceTextModule(readFileSync(file,'utf8'),{context,identifier:file});modules.set(file,m);await m.link(spec=>module(resolve(dirname(file),spec)));return m}
 const m=await module(resolve(base,'app.js'));await m.evaluate();await new Promise(r=>setTimeout(r,40));
 const select=async(tab)=>{buttons.find(b=>b.dataset.tab===tab).onclick();await new Promise(r=>setTimeout(r,0))};
 return {get,select,html:()=>get('#app').innerHTML};
}

const n=await loadDemo('northpeak',['overview','variance','scenarios','memo']);
assert.match(n.html(),/10\.27M/);assert.match(n.html(),/92\.7%/);
await n.select('variance');assert.match(n.html(),/Budget vs\. actual, line by line/);assert.match(n.html(),/499K/);
const source=JSON.parse(readFileSync(resolve(root,'northpeak/dist/data.json'),'utf8'));
const exitARR=s=>(source.scenarios.filter(r=>r.scenario===s).at(-1).arr/1e6).toFixed(2)+'M';
await n.select('scenarios');assert.ok(n.html().includes(exitARR('Base')));
n.get('scenario-Downside').onclick();assert.ok(n.html().includes(exitARR('Downside')));assert.match(n.html(),/−4\.0%|-4\.0%/);
n.get('scenario-Upside').onclick();assert.ok(n.html().includes(exitARR('Upside')));n.get('#export').onclick();
await n.select('memo');assert.match(n.html(),/Manage the margin/);

const r=await loadDemo('reinsight',['portfolio','cedants','method']);
assert.match(r.html(),/Technical ratio/);assert.doesNotMatch(r.html(),/NaN|undefined/);
r.get('#region').value='no-such-region';r.get('#region').onchange();assert.match(r.html(),/No records match/);
r.get('#reset').onclick();assert.match(r.html(),/Regional performance/);
r.get('#product').value='Life';r.get('#product').onchange();assert.match(r.html(),/Technical ratio/);
await r.select('cedants');assert.match(r.html(),/Cédante/);
r.get('#cedant-search').oninput({target:{value:'no-such-cedant',selectionStart:15}});assert.match(r.html(),/No eligible cedants/);
r.get('#cedant-search').oninput({target:{value:'',selectionStart:0}});
r.get('#maturity').onchange({target:{value:'all'}});assert.match(r.html(),/Cedants in this selection/);
await r.select('method');assert.match(r.html(),/Clear formulas/);r.get('#download').onclick();
console.log('PASS: NorthPeak views, scenario changes and CSV export; Reinsight filters, empty states, cedant search, maturity controls and export.');
