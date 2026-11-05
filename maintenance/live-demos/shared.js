export const $ = (s) => document.querySelector(s);
export const esc = (v) => String(v??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
export const sum = (rows,key) => rows.reduce((a,r)=>a+Number(r[key]||0),0);
export const money = (n,currency='$') => n==null?'—':`${n<0?'−':''}${currency}${Math.abs(n)>=1e6?(Math.abs(n)/1e6).toFixed(2)+'M':Math.abs(n)>=1e3?(Math.abs(n)/1e3).toFixed(0)+'K':Math.abs(n).toFixed(0)}`;
export const pct = n => n==null?'—':`${Number(n).toFixed(1)}%`;
export const number = n => new Intl.NumberFormat('en-US',{maximumFractionDigits:0}).format(n);
export const metric = (label,value,detail='',tone='') => `<div class="metric"><div class="label">${esc(label)}</div><div class="value ${tone}">${esc(value)}</div><div class="detail">${esc(detail)}</div></div>`;
export const group = (rows,key) => {const m=new Map();for(const r of rows){const k=r[key];if(!m.has(k))m.set(k,[]);m.get(k).push(r)}return [...m.entries()]};
export function downloadCSV(name,columns,rows){const cell=v=>'"'+String(v??'').replace(/"/g,'""')+'"';const content=[columns,...rows].map(r=>r.map(cell).join(',')).join('\r\n');const url=URL.createObjectURL(new Blob([content],{type:'text/csv;charset=utf-8'}));const a=document.createElement('a');a.href=url;a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000)}
export function lines({series,labels,yFormat=n=>money(n),height=240,title='Trend chart'}){
 const w=640,h=height,l=54,r=16,t=18,b=32,values=series.flatMap(s=>s.values).filter(Number.isFinite);if(!values.length)return '<div class="empty">No data for this selection.</div>';
 const lo=Math.min(0,...values),hi=Math.max(...values,1),pad=(hi-lo)*.12,min=lo<0?lo-pad:0,max=hi+pad,x=i=>l+i*(w-l-r)/Math.max(labels.length-1,1),y=v=>h-b-(v-min)/(max-min)*(h-t-b);
 let html=`<svg class="chart" viewBox="0 0 ${w} ${h}" role="img" aria-label="${esc(title)}"><title>${esc(title)}</title>`;
 for(let i=0;i<=4;i++){const v=min+(max-min)*i/4;html+=`<line class="gridline" x1="${l}" y1="${y(v)}" x2="${w-r}" y2="${y(v)}"/><text x="${l-9}" y="${y(v)+4}" text-anchor="end">${esc(yFormat(v))}</text>`}
 const step=Math.max(1,Math.ceil(labels.length/5));labels.forEach((v,i)=>{if(i%step===0||i===labels.length-1)html+=`<text x="${x(i)}" y="${h-7}" text-anchor="middle">${esc(v)}</text>`});
 for(const s of series){const points=s.values.map((v,i)=>Number.isFinite(v)?[x(i),y(v),i,v]:null);let path='';let pen=false;for(const p of points){if(!p){pen=false;continue}path+=`${pen?'L':'M'}${p[0].toFixed(2)},${p[1].toFixed(2)} `;pen=true}html+=`<path d="${path}" stroke="${s.color}" stroke-width="2.6" fill="none" ${s.dashed?'stroke-dasharray="6 4"':''}/>`;for(const p of points.filter(Boolean))html+=`<circle cx="${p[0]}" cy="${p[1]}" r="4" fill="${s.color}" opacity="0"><title>${esc(s.name)} · ${esc(labels[p[2]])}: ${esc(yFormat(p[3]))}</title></circle>`}
 html+='</svg><div class="legend">'+series.map(s=>`<span style="--c:${s.color}">${esc(s.name)}</span>`).join('')+'</div>';return html;
}
export function bars(items,format=n=>money(n),color='#203f61'){
 const max=Math.max(...items.map(x=>Math.abs(x.value)),1);return `<div class="bar-list">${items.map(x=>`<div><div class="bar-top"><span>${esc(x.name)}</span><strong>${esc(format(x.value))}</strong></div><div class="bar-track"><div class="bar-fill" style="width:${Math.abs(x.value)/max*100}%;background:${x.color||color}"></div></div></div>`).join('')}</div>`;
}
