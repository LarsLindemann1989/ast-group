const menu=document.querySelector('.menu-toggle');
const nav=document.getElementById('nav');
if(menu&&nav){
  const close=()=>{nav.classList.remove('open');menu.setAttribute('aria-expanded','false');menu.setAttribute('aria-label','Open navigation');};
  menu.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';nav.classList.toggle('open',open);menu.setAttribute('aria-expanded',String(open));menu.setAttribute('aria-label',open?'Close navigation':'Open navigation');});
  document.addEventListener('keydown',e=>{if(e.key==='Escape'&&menu.getAttribute('aria-expanded')==='true'){close();menu.focus();}});
  nav.addEventListener('click',e=>{if(e.target.closest('a'))close();});
}
const search=document.getElementById('publication-search');
const type=document.getElementById('publication-type');
if(search&&type){
 const papers=[...document.querySelectorAll('#papers .paper')];
 const groups=[...document.querySelectorAll('[data-year-group]')];
 const normalize=s=>s.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
 const update=()=>{
  const terms=normalize(search.value).trim().split(/\s+/).filter(Boolean);let count=0;
  papers.forEach(p=>{const match=(type.value==='all'||p.dataset.type===type.value)&&terms.every(t=>normalize(p.dataset.search).includes(t));p.hidden=!match;if(match)count++;});
  groups.forEach(g=>{const visible=g.querySelectorAll('.paper:not([hidden])').length;g.hidden=!visible;g.querySelector('h2 span').textContent=visible;document.querySelector(`[data-year-link="${g.dataset.yearGroup}"]`).hidden=!visible;});
  document.getElementById('result-count').textContent=`${count} of ${papers.length} records`;
  document.getElementById('no-results').hidden=count>0;
 };
 search.addEventListener('input',update);type.addEventListener('change',update);
 document.getElementById('reset-filters').addEventListener('click',()=>{search.value='';type.value='all';update();search.focus();});
}
