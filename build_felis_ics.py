#!/usr/bin/env python3
"""Builds felis-natal-2026.ics from events transcribed from the FeLIS Natal archive doc."""
from datetime import date, datetime, timedelta
import re, sys, unicodedata

def slug(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii','ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+','-',s).strip('-')

D = lambda m,d,y=2026: date(y,m,d)
EV = []
def ev(title, loc, blurb, url, start, end=None, t0=None, t1=None, key=None):
    """All-day: start,end are inclusive dates (t0 None). Timed: start date + t0 (+t1 optional)."""
    EV.append(dict(title=title, loc=loc, blurb=blurb, url=url, start=start, end=end, t0=t0, t1=t1, key=key))

T=lambda h,m=0:(h,m)
# ---- Digest 1 ----
ev("28ª Mostra Internacional de Doces & Licores Conventuais","Mosteiro de Alcobaça, Alcobaça","€1 entry. Taste real convent sweets and liqueurs in a UNESCO monastery, a delicious intro to Portuguese Christmas flavours for the whole family.","https://cm-alcobaca.pt/84016/28-mostra-internacional-de-doces-licores-conventuais",D(11,19),D(11,22))
ev("Leiria Natal 2026","Centro Histórico / Jardim Luís de Camões, Leiria","Lights switch on 27 Nov at 21:00. Aldeia do Pai Natal (Santa's Village), Recreio dos Duendes (Elves' Playground), train, carousel, Mercadinho Doce and Parada de Natal: the city's big family Christmas. Full programme still TBA.","https://www.cm-leiria.pt/areas-de-atividade/turismo/leiria-natal",D(11,27),D(2027,1,3) if False else date(2027,1,3))
ev("Óbidos Vila Natal 2026","Cerca do Castelo, Óbidos","Theme: Pinóquio and the world of marionettes. Kids can make their own puppet, write to Pai Natal and go skating. Fri–Sun & holidays 10am–9pm, Mon–Thu 10am–6pm. Closed 25 Dec & 1 Jan. Tickets €12 adult, €8 child (3–11), family from €36. Book a time slot online.","https://obidosvilanatal.pt/en/hours-and-prices",D(11,27),date(2027,1,3))
ev("Natal em Ourém & Fátima: lights & Mercado de Natal","Jardim Le Plessis-Trévise, Ourém (Fátima also gets a Christmas market)","Starts Fri 4 Dec with the light switch-on in Ourém and Fátima. The market runs until 6 Jan, and the garden hosts a regular sound-and-light show. Full programme still to come.","https://www.ourem.pt/camara-aprovou-contratacao-de-iluminacao-de-natal-para-ourem-e-fatima/",D(12,4),date(2027,1,6))
ev("É Natal em Alcobaça","Rossio (in front of the Mosteiro), Alcobaça","Free entry. Casinha do Pai Natal, rides, craft ateliers, storytelling, live music and the Grande Desfile de Natal parade from the town hall to the Mosteiro.","https://www.viralagenda.com/pt/events/1828890/e-natal-em-alcobaca",D(12,5),date(2027,1,6))
# ---- Digest 2 ----
ev("Leiria Natal: lights switch-on","Centro Histórico, Leiria","The whole city lights up at once to open the season. A magical first night out. Aldeia do Pai Natal and Recreio dos Duendes run until 3 Jan.","https://www.diarioleiria.pt/2026/11/06/ja-ha-data-para-a-inauguracao-das-luzes-de-natal/",D(11,27),t0=T(21))
ev("Leiria Natal rides: Comboio, Roda & Carrossel","Jardim Luís de Camões, Leiria","Opening night 7pm–midnight. After that: Mon–Thu 2–8pm, Fri 2pm–midnight, Sat 11am–midnight, Sun 11am–8pm. The Christmas train is for ages 2–16, and the Ferris wheel (age 3+) gives a view over all the lights. €2 per ride.","https://www.teatrojlsilva.pt/evento/comboio-eletrico-2026",D(11,27),date(2027,1,3))
ev("O Grande Concerto das Estrelas","Palco Leiria Natal (Mercado Sant'Ana), Leiria","Free entry (public holiday). A teddy bear, a snowman, reindeer and a gingerbread man sing and dance with simple songs kids can join in with, and Pai Natal arrives for the finale.","https://leiriagenda.cm-leiria.pt/pt/agenda/o-grande-concerto-das-estrelas",D(12,8),t0=T(16),t1=T(18))
for d in [(11,28),(11,29),(12,1),(12,5),(12,6),(12,8),(12,12),(12,13),(12,19),(12,20)]:
    ev("Mercadinho de Natal: Natal à Luz do Mosteiro","Largo do Condestável, Batalha","A cosy village market in the shadow of the Mosteiro, with local crafts, treats and seasonal food cooked by local associations. Open 2–8pm.","https://www.cm-batalha.pt/areas-de-intervencao/cultura/eventos",D(*d),t0=T(14),t1=T(20),key="mercadinho-batalha-%02d%02d"%d)
ev("Natal Encantado, 10th edition (Porto de Mós)","Porto de Mós village","Lights, music, family shows and a market of local makers. Last year it also had a Casa do Pai Natal, a Christmas train and a huge presépio (nativity scene) contest exhibition. Full 2026 programme coming soon.","https://visite.portodemos.pt/pages/1139/?geo_article_id=5212",D(12,5),date(2027,1,6))
# ---- Caldas extra post ----
CAL="https://vadi.agem.pt/eventos/programacao-caldas-rainha-do-natal-2026-2027-caldas-4cb4c74bd3a7"
ev("Caldas, Rainha do Natal (full programme)","Caldas da Rainha","Everything is free. Full Christmas programme with over 3 million LED lights and a 30m tree. See the link for all events.",CAL,D(11,14),date(2027,1,9))
ev("Caldas: Pai Natal arrives","Praça 25 de Abril, Caldas da Rainha","Free. Pai Natal arrives and sets up his house next to the giant tree.",CAL,D(12,1),t0=T(10,30),key="caldas-pai-natal-chega")
for d in [(12,5),(12,6),(12,12),(12,13),(12,19),(12,20)]:
    ev("Caldas: Casa do Pai Natal","Caldas da Rainha","Free. Visit Pai Natal's house, with a Christmas story session at 11:00.",CAL,D(*d),t0=T(10),t1=T(12,30),key="caldas-casa-pai-natal-%02d%02d"%d)
ev("Caldas: free Christmas train","Caldas da Rainha (lit-up streets)","Free train around the lit-up streets, in the afternoons for the public. Donations go to the local firefighters.",CAL,D(12,9),D(12,24))
ev("Caldas: street theatre for kids","Caldas da Rainha","Free. Duendes Perdidos, Jornalistas de Natal and Carteiros do Pai Natal.",CAL,D(12,21),D(12,23))
# ---- Digest 3 ----
MG="https://www.cm-mgrande.pt/viver/cultura/natal-marinha-grande"
ev("Inauguração da Iluminação de Natal (Marinha Grande)","Parque da Cerca (by the giant tree), Marinha Grande","Kids can watch the lights come on with a brass band and a dance crew performing.",MG,D(11,28),t0=T(18),key="marinha-grande-iluminacao")
ev("Presépio Tradicional de Filipe Ferreira","Edifício da Resinagem (Museu do Vidro), Marinha Grande","Free. Wed–Fri 10am–1pm & 2–6pm, weekends/holidays 10am–1pm & 2–8pm, closed Mon–Tue. A traditional Portuguese presépio built as a miniature village with over 1,500 pieces. Kids love spotting the tiny details.",MG,D(11,28),date(2027,1,6))
ev("Cortejo de Luzes (Batalha)","Batalha town streets","Free. A lantern procession that local children take part in, as part of Natal à Luz do Mosteiro. The Christmas village is open weekends & holidays 2–8pm.","https://centralpress.pt/page/156609/redacao/2026/11/19/natal-a-luz-do-mosteiro-da-mote-ao-programa-natalicio-do-municipio-da-batalha",D(11,29),t0=T(16,30))
ev("O Pai Natal e a Rainha da Neve","Palco Leiria Natal (Mercado Sant'Ana), Leiria","Free (public holiday). A children's play where the elf Floco has to save Christmas from the Snow Queen, and the audience gets to help.","https://leiriagenda.cm-leiria.pt/pt/agenda/o-pai-natal-e-a-rainha-da-neve",D(12,1),t0=T(16),t1=T(18))
ev("Contos que Relembram o Natal","Palco Leiria Natal (Mercado Sant'Ana), Leiria","Free. Christmas storytelling by a local Leiria theatre group, sessions at 11am, 2:30pm & 3:30pm each day. More dates 10–18 Dec (see link). Nice for little ones after school or nursery.","https://leiriagenda.cm-leiria.pt/pt/agenda/contos-que-relembram-o-natal",D(12,2),D(12,4))
ev("O Natal Congelado","Palco Leiria Natal (Mercado Sant'Ana), Leiria","Free. A musical with original songs where Fada Estrelinha (Little Star Fairy) frees Pai Natal from the Ice Witch.","https://leiriagenda.cm-leiria.pt/pt/agenda/o-natal-congelado",D(12,5),t0=T(16),t1=T(18))
ev("Parada de Natal (Leiria)","Leiria city streets","A parade with music, colour and Christmas characters. Families are invited to join in.","https://www.cm-leiria.pt/municipio/comunicacao/noticias/noticia/espetaculo-piromusical-e-de-luz-e-coro-gospel-abrem-o-leiria-natal-2026",D(12,6),t0=T(15))
ev("Mercadinho de Natal (Guia, Pombal)","Largo do Rossio, Guia (Pombal)","Free. Opens 6 Dec at 10am. A village Christmas market with local crafts, products and activities, run by the local parish.","https://pombal-acontece.cm-pombal.pt/eventos/-209",D(12,6),D(12,20))
ev("Ninfas do Lis & Orquestra Ars Lusitanae","Teatro Stephens, Marinha Grande","€3 (bol.pt or box office). A festive family concert with choir and orchestra, a good late treat for older kids before the 8 Dec holiday.",MG,D(12,7),t0=T(21,30))
for d in [(12,13),(12,22)]:
    ev("Sopra a tua Bola de Natal (blow your own bauble)","PoeirasGlass studio (by the Museu do Vidro), Marinha Grande","Free, age 10+ with an adult, max 5 people per hour. Kids blow their own glass Christmas bauble with a master glassblower and collect it the next day. Book by 6 Dec at museu.vidro@cm-mgrande.pt.",MG,D(*d),t0=T(15),t1=T(17),key="bola-de-natal-%02d%02d"%d)
# ---- Shared by members ----
ev("Castelo Mágico (Montemor-o-Velho)","Castelo de Montemor-o-Velho","Christmas village in the castle with attractions and family shows. Shared by Wanja.","https://www.castelomagico.eu/",D(11,28),D(12,23))
ev("Natal à Luz do Mosteiro (Batalha)","Largo do Condestável, Batalha","Free activities for all ages: Casa do Pai Natal, kids' train, slide, Floresta de Luz Christmas tree exhibition, Mega Tenda Kids (inflatables, retro gaming, Lego exhibition, workshops, face painting), obstacle circuit, traditional games, Palco Encantado and a Christmas market. Lights switch on 27 Nov. Shared by Deborah.","https://www.instagram.com/p/Df25PwLB8dd/",D(11,27),date(2027,1,6),key="natal-luz-mosteiro-batalha")
for a,b,pl in [((12,5),(12,6),"Praça do Município"),((12,12),(12,13),"Praça Mouzinho de Albuquerque"),((12,19),(12,20),"Largo do Condestável")]:
    ev("Auto de Natal (Batalha)","%s, Batalha"%pl,"New this year: a Christmas play (Auto de Natal) told in three parts, part of Natal à Luz do Mosteiro. Shared by Deborah.","https://www.instagram.com/p/Df25PwLB8dd/",D(*a),D(*b),key="auto-natal-batalha-%02d%02d"%a)
ev("Christmas Concert: Leiria choirs (Aldeia Natal)","Aldeia Natal Leiria, Leiria","Multi-choir Christmas concert bringing together several Leiria choirs, including the Coro Infanto-Juvenil da Academia Coral Mezzo. Shared by a group member.","https://externalvytum.github.io/felis-natal-calendar/",D(11,29),t0=T(15),t1=T(16,30),key="concerto-natal-aldeia-natal-leiria-1129")

# ---------------- render ----------------
def esc(s): return s.replace('\\','\\\\').replace(';','\\;').replace(',','\\,').replace('\n','\\n')
def fold(line):
    out=[]; cur=''; n=0
    for ch in line:
        b=len(ch.encode('utf-8'))
        if n+b>75:
            out.append(cur); cur=' '+ch; n=1+b
        else: cur+=ch; n+=b
    out.append(cur); return '\r\n'.join(out)
now=datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')
L=["BEGIN:VCALENDAR","VERSION:2.0","PRODID:-//FeLIS Natal//Christmas digest calendar//EN","CALSCALE:GREGORIAN","METHOD:PUBLISH",
"X-WR-CALNAME:FeLIS Natal 2026","X-WR-CALDESC:"+esc("Kid-friendly Christmas events around Leiria, from the FeLIS Natal WhatsApp digests. Updated weekly."),
"X-WR-TIMEZONE:Europe/Lisbon","REFRESH-INTERVAL;VALUE=DURATION:PT12H","X-PUBLISHED-TTL:PT12H",
"BEGIN:VTIMEZONE","TZID:Europe/Lisbon","X-LIC-LOCATION:Europe/Lisbon",
"BEGIN:DAYLIGHT","TZOFFSETFROM:+0000","TZOFFSETTO:+0100","TZNAME:WEST","DTSTART:19700329T010000","RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU","END:DAYLIGHT",
"BEGIN:STANDARD","TZOFFSETFROM:+0100","TZOFFSETTO:+0000","TZNAME:WET","DTSTART:19701025T020000","RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU","END:STANDARD",
"END:VTIMEZONE"]
uids=set()
for e in sorted(EV,key=lambda e:(e['start'],e['t0'] or (0,0),e['title'])):
    k=e['key'] or slug(e['title'])
    uid=k+"@felis-natal"
    assert uid not in uids, uid; uids.add(uid)
    L+=["BEGIN:VEVENT","UID:"+uid,"DTSTAMP:"+now,"SEQUENCE:0"]
    if e['t0'] is None:
        end=(e['end'] or e['start'])+timedelta(days=1)   # DTEND exclusive
        L+=["DTSTART;VALUE=DATE:"+e['start'].strftime('%Y%m%d'),"DTEND;VALUE=DATE:"+end.strftime('%Y%m%d')]
    else:
        L.append("DTSTART;TZID=Europe/Lisbon:%sT%02d%02d00"%(e['start'].strftime('%Y%m%d'),*e['t0']))
        if e['t1']: L.append("DTEND;TZID=Europe/Lisbon:%sT%02d%02d00"%(e['start'].strftime('%Y%m%d'),*e['t1']))
    L+=["SUMMARY:"+esc(e['title']),"LOCATION:"+esc(e['loc']),"DESCRIPTION:"+esc(e['blurb']+"\n\n"+e['url']),"URL:"+e['url'],"TRANSP:TRANSPARENT","CATEGORIES:Christmas,Family","END:VEVENT"]
L.append("END:VCALENDAR")
open('/workspace/felis-natal-2026.ics','w',newline='').write('\r\n'.join(fold(l) for l in L)+'\r\n')
print(len(EV),"events")
