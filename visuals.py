from pathlib import Path
ARROW='<svg class="arrow-icon" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M6 18 18 6M6 6h12v12" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def visual(kind, caption=True):
 titles={'lens':'Find the signal. See the whole picture.','profile':'A fuller picture of the applicant.','research':'Connections worth following.','scope':'One clear scope. A considered next step.','experience':'Perspective built through experience.','contact':'One direct connection to DJ.'}
 if kind=='lens':
  art='''<defs><radialGradient id="glass"><stop stop-color="#b9d2e7" stop-opacity=".1"/><stop offset=".6" stop-color="#071728"/><stop offset=".84" stop-color="#527b9e"/><stop offset=".88" stop-color="#e2f4ff"/><stop offset=".92" stop-color="#263d54"/><stop offset="1" stop-color="#02070d"/></radialGradient><linearGradient id="metal" x2="1" y2="1"><stop stop-color="#d9e3ec"/><stop offset=".25" stop-color="#273c51"/><stop offset=".6" stop-color="#91adc1"/><stop offset="1" stop-color="#06121e"/></linearGradient><radialGradient id="glow"><stop stop-color="#71a5d2" stop-opacity=".45"/><stop offset="1" stop-color="#0c1624" stop-opacity="0"/></radialGradient></defs><ellipse cx="410" cy="282" rx="245" ry="110" fill="url(#glow)"/><g transform="translate(380 205)"><circle r="153" fill="url(#metal)"/><circle r="143" fill="#06111e"/><circle r="132" fill="url(#glass)"/><circle r="112" fill="none" stroke="#8cb8d4" stroke-opacity=".4"/><circle r="91" fill="none" stroke="#9fcced" stroke-opacity=".15"/><circle r="67" fill="none" stroke="#83a8c7" stroke-opacity=".3"/><path d="m0-65 57 33v65L0 65-57 33v-65z" fill="none" stroke="#80a6c7" stroke-opacity=".55"/><path d="M0-65 57 33-57 33 0-65M57-32 0 65-57-32Z" fill="none" stroke="#83a6c7" stroke-opacity=".3"/><circle r="28" fill="#142c43"/><circle r="14" fill="#669abd" opacity=".5"/><path d="M-106-80a133 133 0 0 1 180-30" fill="none" stroke="#d4eafa" stroke-width="2" opacity=".6"/></g><g fill="#9eb7cc" font-family="Arial" font-size="9" letter-spacing="2"><text x="50" y="85">RESEARCH</text><text x="590" y="140">CONTEXT</text><text x="555" y="328">CLARITY</text></g><g fill="none" stroke="#6e8ca5" stroke-width=".8"><path d="M140 80h70l43 40M575 135h-50M535 325h-80l-20-20"/><circle cx="253" cy="120" r="3"/><circle cx="525" cy="135" r="3"/></g>'''
 elif kind=='profile':
  art='''<defs><linearGradient id="sheet" x2="1" y2="1"><stop stop-color="#fff"/><stop offset="1" stop-color="#cfd9e6"/></linearGradient></defs><g transform="translate(180 35) rotate(-8 180 170)"><rect x="25" y="20" width="320" height="310" rx="16" fill="#9faec1" opacity=".2"/><rect width="320" height="310" rx="16" fill="url(#sheet)"/><circle cx="76" cy="77" r="30" fill="#bcc9d8"/><circle cx="76" cy="68" r="9" fill="#49647e"/><path d="M57 93q19-31 38 0" fill="#49647e"/><g stroke="#8c9cae" stroke-width="5" stroke-linecap="round"><path d="M134 61h120M134 81h76M40 151h237M40 181h174M40 211h216M40 241h130"/></g><circle cx="260" cy="255" r="25" fill="#182e44"/><path d="m250 255 7 7 14-16" stroke="#d9e6f2" stroke-width="2" fill="none"/></g><g stroke="#6d8aa4" fill="none"><path d="M125 250h80M490 120h100v65M515 295h80"/><circle cx="125" cy="250" r="5"/><circle cx="590" cy="185" r="5"/></g>'''
 elif kind=='research':
  art='''<defs><radialGradient id="center"><stop stop-color="#527a9d"/><stop offset="1" stop-color="#14283d"/></radialGradient></defs><g stroke="#7f9bb4" fill="none" stroke-width="1"><path d="M350 195 180 95 120 260 350 195 550 80 590 265 350 195 370 330M180 95 550 80M120 260 370 330 590 265"/><circle cx="350" cy="195" r="95" stroke-dasharray="3 8" opacity=".4"/></g><g fill="#d6e4f0"><circle cx="180" cy="95" r="14"/><circle cx="120" cy="260" r="9"/><circle cx="550" cy="80" r="11"/><circle cx="590" cy="265" r="16"/><circle cx="370" cy="330" r="8"/></g><circle cx="350" cy="195" r="57" fill="url(#center)" stroke="#b0c7db"/><circle cx="350" cy="195" r="34" fill="none" stroke="#9bb8cf"/><path d="M350 176v38m-19-19h38" stroke="#d6e4f0"/><g fill="#b1c4d5" font-family="Arial" font-size="9" letter-spacing="2"><text x="170" y="60">RECORDS</text><text x="510" y="46">REFERENCES</text><text x="560" y="310">FOLLOW-UP</text></g>'''
 elif kind=='scope':
  art='''<g fill="none" stroke="#718ca7"><rect x="175" y="50" width="355" height="280" rx="24"/><path d="M175 110h355M235 50v280"/><circle cx="205" cy="81" r="4" fill="#bed1e1"/></g><g fill="#d7e3ef" font-family="Arial" font-size="12" letter-spacing="2"><text x="267" y="88">THE ASSIGNMENT</text><text x="275" y="160">PURPOSE</text><text x="275" y="223">SCOPE</text><text x="275" y="286">NEXT STEP</text></g><g fill="#aac5db"><circle cx="205" cy="155" r="8"/><circle cx="205" cy="218" r="8"/><circle cx="205" cy="281" r="8"/></g><g stroke="#657f98"><path d="M205 163v47M205 226v47M275 179h193M275 242h150M275 305h170"/></g>'''
 elif kind=='experience':
  art='''<g fill="none" stroke="#6a8aa5"><circle cx="350" cy="195" r="140"/><circle cx="350" cy="195" r="113" stroke-dasharray="1 10"/><circle cx="350" cy="195" r="83" opacity=".5"/><path d="M145 195h75m260 0h75M350 40v35m0 240v35"/></g><text x="350" y="215" text-anchor="middle" fill="#ebf1f7" font-size="94" font-family="Arial" font-weight="600" letter-spacing="-6">24</text><text x="350" y="251" text-anchor="middle" fill="#a4bbce" font-size="9" font-family="Arial" letter-spacing="3">YEARS OF EXPERIENCE</text>'''
 else:
  art='''<g fill="none" stroke="#718da6"><circle cx="350" cy="195" r="100"/><circle cx="350" cy="195" r="145" opacity=".3"/><path d="M205 195h-60M495 195h60M350 50v45M350 295v45"/></g><rect x="301" y="155" width="98" height="76" rx="12" fill="#d9e6f0"/><path d="m307 163 43 34 43-34" fill="none" stroke="#25415a" stroke-width="3"/><g fill="#b2c9dd"><circle cx="145" cy="195" r="7"/><circle cx="555" cy="195" r="7"/><circle cx="350" cy="50" r="7"/><circle cx="350" cy="340" r="7"/></g>'''
 return f'<div class="visual visual-{kind}"><svg viewBox="0 0 700 390" role="img" aria-label="{titles[kind]}">{art}</svg>'+ (f'<div class="visual-caption"><span>BREAK POINT / {kind.upper()}</span><span>DETAILS MAKE THE DIFFERENCE</span></div>' if caption else '')+'</div>'
def apply(pages):
 result=[]
 for route,title,desc,content in pages:
  if route=='/':
   start=content.index('<div class="hero-bottom');end=content.index('</section>',start)
   hero='''<section class="hero hero-new"><div class="wrap"><p class="eyebrow">BREAK POINT INVESTIGATIONS / FAIRFIELD, CA</p><h1>Clarity.<br><em>At every level.</em></h1><p class="hero-intro">The right information. The full picture.<br>Background investigations led by experienced judgment.</p><div class="button-row"><a class="button dark" href="/contact/">Talk to DJ</a><a class="button subtle" href="/background-investigations/">Explore backgrounds '''+ARROW+'''</a></div></div>'''+visual('lens',False)+'''</section>'''
   content=hero+content[end+len('</section>'):]
   content=content.replace('Uncertainty should not<br>make the decision for you.','See beyond<br>the application.').replace('THE RIGHT INFORMATION CHANGES EVERYTHING','A BETTER PERSPECTIVE')
   content=content.replace('<div class="feature-image"><img src="/assets/casework.webp" alt="Organized case folders and research notebook on a desk" loading="lazy"><span>THOUGHTFUL WORK. INFORMED DECISIONS.</span></div>',visual('profile'))
   content=content.replace('<section class="wrap section intro-grid">','<section class="wrap section intro-grid">',1)
  elif route=='/services/':
   content=content.replace('<div class="feature-image"><img src="/assets/casework.webp" alt="Case research materials arranged on a desk"></div>',visual('research'))
   content=content.replace('<section class="wrap section no-top">','<section class="wrap section no-top service-showcase">',1)
  elif route=='/background-investigations/':
   content=content.replace('<img src="/assets/casework.webp" alt="Neatly arranged investigative casework materials">',visual('profile',False))
   content=content.replace('<section class="wrap section no-top">', '<section class="wrap section no-top">'+visual('scope'),1)
  elif route=='/about/':
   begin=content.index('<div class="identity-panel">');end=content.index('<div class="about-copy">',begin)
   content=content[:begin]+visual('experience')+content[end:]
  elif route=='/contact/':
   content=content.replace('<div class="contact-details">',visual('contact',False)+'<div class="contact-details">',1)
  # All service entries become visual cards, each with its own purpose-built graphic.
  if 'class="service-list"' in content:
   for label,kind in [('PUBLIC SAFETY','profile'),('INVESTIGATIVE SUPPORT','research'),('YOUR ASSIGNMENT','scope')]:
    needle=f'<div><p class="eyebrow">{label}'
    content=content.replace(needle,visual(kind,False)+f'<div><p class="eyebrow">{label}')
  # Small graphic progress marks give each process step a visual anchor.
  content=content.replace('<span>01 / DISCUSS</span>','<span class="step-orbit">01</span><span>01 / DISCUSS</span>').replace('<span>02 / DEFINE</span>','<span class="step-orbit">02</span><span>02 / DEFINE</span>').replace('<span>03 / INVESTIGATE</span>','<span class="step-orbit">03</span><span>03 / INVESTIGATE</span>')
  content=content.replace('↗',ARROW)
  result.append((route,title,desc,content))
 return result
