#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - sam. août 17:09 2019
#   - Initial Version 1.0
#  =================================================

codes = """102A:RTL:104,60:RTL:
141A:Euroherz, Hof:88,00:EUROHERZ:
14A0:Seefunk:::
2311:FUN R, Bratislava:87,70:FUNRADIO:
2320:R Kiks, Michalovce(?):103,30::
232D:Cesky Rozhlas 3, Plzen:95,60:  CR3: 
232F:Cesky Rozhlas:89,10:  CR1:
2241:R Twist, Bratislava:101,80:TWIST:
2423:South East Radio:96,40:changing:
3068:Klas FM, Istanbul:98,70:KLAS FM:
30CA:Power FM, Istanbul:100,00:POWER FM:
3232:Radio Maryja:0,00:R/MARYJA:
3F44:RMF FM, Kielce:88,20:-RMF FM-:
4001:Radio Sunshine:88,00:SUNSHINE:
43B2:DRS 2:96,60:DRS 2:
43D3:RSR 3:100,10:COULEUR3:
4D32:DRS 2:95,40:DRS 2:
4E+031:RSI 1:106,20:CH-RETE1:
4F20:R Framboise:88,20:changing:
5000:R FM, (MN):89,35:RADIO FM:
5001:R Rosa-CNR (MN):93,45:ROSA-CNR:
507B:R Pavia, (PV):105,30:changing:
507C:R Sound, (FE):104,85:SOUND:
50DA:R Lodi:89,00:R. LODI:
50FA:R Pirata:94,90:PIRATA:
50FF:R Energy:90,10:R.ENERGY:
5141:Italia Network:88,85:ITALIA *:
5201:Slovensky Rozhlas 1:0,00:SRo - S1:
5201:RAI 1-3:::
5211:Rete 105:0,00:R105:
5213:R Montecarlo:89,20:RMC FM:
5214:Deejay:0,00:DEEJAY:
5215:One O One Network:0,00:ONEOONE:
5218:RTL 102,5 Hit Radio:102,50:RTL102,5:
5219:Capital NTW:0,00:CAPITAL:
5220:R.I.S.M.I:0,00:RITALIA:
5264:Dimensione Suono Ntw.:0,00:DIMSUONO:
52FD:R Subasio:0,00:SUBASIO:
532F:R Cuore:90,30:changing:
5340:R Tele Trentino:88,20:R.T.T:
5342:Rete Malvisi:106,80:changing:
5347:R Zeta, (BG):96,20:*R.ZETA:
5350:R Company, (PD):100,50: :
5353:R Norba:106,60:R-NORBA:
5355:Lattemiele:0,00:LATMIELE:
5358:R Delta 1, (CH):88,60:R.DELTA1:
535F:Radio Nitra:88,80:changing:
539C:R Cooperativa, (MI):90,10:changing:
53C7:Play Studio Dance NTW:100,70:changing:
53DC:Rete Piu FM (PG):88,10: :
53DD:Jam FM:95,10:JAM FM:
53EF:R Base:87,50:R. BASE:
53F2:R Pico, (MO):106,60:*R PICO:
53FB:R Studio Delta, (FO):92,80:changing:
5400:R Montestella, (MI):103,20:M.STELLA:
541D:Idea R Bubble, (PR):93,80: :
5423:Europa R, (MI):88,30:EUROPA R:
54AC:Rete Alfa, (BO):91,40:RETEALF:
54FB:R Alba, (CN):105,60:R. ALBA:
551C:Radio Aut, (AP):91,65:RADIOAUT:
5643:R Baccano, (TS):107,10:BACCANO:
5800:Prima Rete, (MO):107,65:changing:
5844:Onda R.Emilia Romagna:102,80: :
584D:R Bruno:103,80:R. BRUNO:
5851:R Punto Zero, Ravenna:105,55:changing:
5855:Canale 7, (MO):104.05:changing:
58A8:R Monte Kanate, (PR):103,10:RMKANATE:
5A45:Azzurra Network, (PG):105,00:changing:
5A4C:R Ricerca, Padova (PD):88,70:changing:
5A56:R Puglia Network, (BA):96,20:R<PUGLIA:
5B60:R Veronica One, (TO):93.6: :
5B65:R Manila, (TO):98,50:MANILA:
5B70:R Vega, Canelli (AT):88,55:V E G A:
5BA9:R Studio Aperto, (TO):88,20:changing:
5BAC:R Alfa, (TO):95,39:R. ALFA:
5BAE:R Master, Nichelino(TO):90,00:changing:
6201:R Utar, Odessa:101,80:UTAR:
6250:R Prosto, Odessa:105,30:PROSTO R:
6302:BRTN R 2:0,00:RADIO 2:
6305:BRTN R Donna:89,00:DONNA:
63A1:R Slovenija 1:88,50:SLOVEN\'1:
63A2:R Slovenija 2:92,40:VAL 202:
6351:RTBF 1:87,60:PREMIERE:
6352:RTBF 2:91,50:WALLONIE:
6354:RTBF 21 Hainaut:104,60:RADIO21:
6366:Belgischer Rundfunk:88,50:  BRF:
63C1:R Beograd:95,30:BGD 1:
63F5:Radio Val, Kokoska:90,30:changing:
644A:HR3 Radio Pula:101,30:R-PULA:
7111:RTL Radio:97,00:RTLRADIO:
7202:R Tunisia Int.:0,00:RTCI:
7210:RTL R Luxembourg:88,90:RTL-LUX:
7212:RTL R Socieculturelle:100,70:100,7:
7250:R Roks:105,20:R O K S:
8202:NOS 2:88,00:RADIO 2:
8411:Omrop Fryslan:88,60:FRYSLAN:
90A8:R Maribor International:102,80:RMI:
9201:DR1:0,00:DR P1:
A902:ÖRF R Steiermark:95,40:RADIO-ST:
ABCD:BB Radio, Bjelovar:100,10:BBR100.1 :
AC02:ÖRF R Wien:89,90: :
AC40:88,6 Live, Wien:88,60:  88,6:
B104:Petöfi R:94,80:PETOFI:
B206:Slager Radio:0,00:SLAGER:
B302:Danubius R:100,50:DANUBIUS:
B303:Juventus R, Budapest:93,90:JUVENTUS:
C2A1:Classic FM:0,00:Classic:
C319:BBC Ulster:94,50:BBC Ulst:
C327:BBC Cymru:96,80:BBC Cymr:
C3AA:Kiss 105, Yorkshire:105,10:KISS FM:
C486:News 97,3:97,30:NEWS97,3:
C4B0:Metro FM:97,10:METRO FM:
C4B1:Forth FM:97,30:FORTH FM:
C513:BBC Hereford&Worchester:104,00:BBC H&W:
C586:City FM:96,70:CITYFM:
C614:BBC Merseyside:95,80:BBC Mrsy:
C712:BBC Cornwall:103,90:BBC Cnwl:
C811:BBC Essex:103,50: :
C886:Invicta FM:103,10:INVICTA:
C912:BBC Solent:96,10:BBC Slnt:
CA11:BBC Suffolk:103,90:BBC Suff:
CA12:BBC Wiltshire:104,30:BBC WLTS:
CA14:BBC Newcastle:95,40:BBC Ncwl:
CA86:Northants Radio:96,60:NORTHNTS:
CB11:BBC Thames Valley:95,20:BBCTVFM:
CB15:BBC R Scotland:93,50:BBC Scot:
CC11:BBC GLR:94,90:BBC GLR:
CB15:BBC R Scotland:0,00:BBC Scot:
CD84:The Eagle:96,40:EAGLE:
CE12:BBC Southern Counties R:104,60:BBC SCR:
CF86:2-Ten-FM:97,00: :
D210:Deutschlandfunk:106,60:DLF:
D220:Deutschlandradio Berlin:89,30:D-Radio:
D301:SDR1:98,80:: 
D308:R Regenbogen:100,40:REGNBOGN:
D30A:Antenne RT4:103,40:Ant. RT4:
D30B:Radio 7:102,50:RADIO 7:
D311-4:Bayerischer Rf 1-4:0,00:BAYERN?:
D315:B 5 Aktuell:90,00:B 5 AKT:
D342:R Bremen 2:88,30:BREMEN2:
D364:Hessischer Rf 4:107,30:HR4:
D368:NDR Njoy:100,30: :
D383:NDR3:98,70:NDR3:
D392:WDR 2:103,30:WDR 2:
D395:WDR Radio 5:88,80:RADIO5:
D3A3:SWF3:92,80:SWF3:
D3A8:RPR1:103,10:RPR1:
D3B1:Saarlandischer Rf 1:88,00:SR1 SAAR:
D3B8:R Salu:100,00:: 
D3C2:MDR Life:96,90:MDR LIFE:
D3C3:MDR Kult:0,00:MDR KULT:
D3D8:R Brocken:89,00:BROCKEN:
D3F8:Antenne Thüringen:107,60:ANT.THUE:
D3F9:Landeswelle Thüringen:104,20:LW THUER:
D40A:Antenne1 Stud.Heilbronn:100,10:Antenne1:
D40D:R Ohr:107,40:O H R:
D4A1:SWF1 Rheinland-Pfalz:91,10:SWF1 RP:
D4A2:S2 Kultur:93,00:S2KULTUR:
D511:BR1 Franken Radio:88,90:BR 1 FRA:
D5A1:SWF1 Baden-Württenberg:88,30:SWF1 BW:
D5A2:S2 Kultur:88,80:S2KULTUR:
D5C1:MDR 1 Sachsen:92,80:MDR SACH:
D704:S4 Baden-Württenberg:107,30:S4_BW_TU:
D70A:Antenne 1:105,20:Antenne1:
D70D:Radio Ton:103,20:RADIOTON:
D79B:Radio Berg:99,70:LR BERG:
D7D1:MDR Sachsen-Anhalt:88,10:MDR S-AN:
D80B:Radio 7:105,00:: 
D904:S4 Württemberg R:90,10:S4_WUERT:
DA04:S4 Bodensee R:89,00:S4_BW_RV:
DC04:S4 Kurpfalz R:107,50:S4_BW_MA:
DD04:S4 Frankenradio:106,60:S4_BW_HN:
F201:RF Inter:0,00:INTER:
F202:RF Culture:0,00:CULTURE:
F203:RF Musique:0,00:MUSIQUE:
F211:RTL:0,00:RTL:
F213:RMC:0,00:RMC FM:
F214:Skyrock:0,00:SKYROCK:
F215:RTL2:87,60:RTL2:
F217:Fun Radio:0,00:F U N:
F218:Nostalgie:0,00:NOSTALGI:
F219:Europe 2:0,00:EUROPE2:
F220:NRJ:0,00:NRJ:
F221:R Classique:0,00:CLASSICQ:
F224:Cherie FM:99,20:CHERIEFM:
F226:Rire & Chansons:97,40:RIRE&:
F505:RF Berry Sud:103,20:RF BERRY:
F705:RF Normandie Caen:102,60:RF CAEN:
F732:Dreyeckland (67):101,90:DREYECKD:
F734:R Top Music (67):90,10:TOPMUSIC:
F805:RF Alsace:102,60:RF ALSAC:
F851:RCF:0,00:R.C.F:
F905:RF Armorique:103,10:RF ARMOR:
F905:RF Drome:87,90:RF DROME:
F905:RF Besancon:101,40:RF BESAN:
F938:Voix FM, Lille (62):91,60:VOIX FM:
FA05:RF Loire Ocean:101,80:R.F.L.O.:
FA05:RF Corse Mora:100,50:R.C.F.M.:
FC31:Evasion Jura FM (39):89,30:EVASION:
FD05:RF Picardie:100,20:RF PICAR:
FE10:R France International:89,00:R F I:
FE42:Fugue FM (60):88,30:FUGUE FM:
FE49:R Force 7 (35) ???:97,40: :
FF05:RF Bretagne Ouest:93,00:RF R.B.O:"""


CSA = """Couleur 3	43D3 	COULEUR	Lyon	04/03/2008
﻿France Inter	F201 	INTER	Radio France	04/03/2008
France Culture	F202 	_CULTURE	Radio France	04/03/2008
France Musique	F203 	MUSIQUE_	Radio France	04/03/2008
FIP	F204 	__F_I_P_	Radio France	04/03/2008
France Bleu Breizh Izel	F205 	BLEU-BZH	Radio France	03/02/2009
France Bleu Berry	F205 	BLEU.BER	Radio France	03/02/2009
France Bleu Cotentin	F205 	BLEU.COT	Radio France	03/02/2009
France Bleu Gironde	F205 	BLEU.GIR	Radio France	03/02/2009
France Bleu Pays Basque	F205 	BLEUBASQ	Radio France	03/02/2009
France Bleu Bourgogne	F205 	BLEUBOUR	Radio France	03/02/2009
France Bleu Drôme Ardèche	F205 	BLEUDROM	Radio France	03/02/2009
France Info	F206 	INFO	Radio France	04/03/2008
France Bleu Limousin à Tulle	F207 	BLEU.LIM	Radio France	03/02/2009
France Bleu Orléans	F207 	BLEU.ORL	Radio France	03/02/2009
France Bleu Armorique	F207 	BLEUARMO	Radio France	03/02/2009
France Bleu Azur	F207 	BLEUAZUR	Radio France	03/02/2009
France Bleu Besançon	F207 	BLEUBESA	Radio France	03/02/2009
France Bleu Champagne	F207 	BLEUCHAM	Radio France	03/02/2009
France Bleu Gard Lozère	F207 	BLEUGARD	Radio France	03/02/2009
France Bleu Gascogne	F207 	BLEUGASC	Radio France	03/02/2009
France Bleu Poitou	F207 	BLEUPOIT	Radio France	03/02/2009
Le Mouv'	F208 	LE_MOUV'	Radio France	04/03/2008
France Bleu Auxerre	F209 	BLEU.AUX	Radio France	03/02/2009
France Bleu Basse-Normandie	F209 	BLEU.B.N	Radio France	03/02/2009
France Bleu Béarn	F209 	BLEU.BEA	Radio France	03/02/2009
France Bleu Creuse	F209 	BLEU.CRE	Radio France	03/02/2009
France Bleu Isère	F209 	BLEU.ISE	Radio France	03/02/2009
France Bleu Loire Océan à La Roche sur Yon	F209 	BLEU.L.O	Radio France	03/02/2009
France Bleu Picardie	F209 	BLEU.PIC	Radio France	03/02/2009
France Bleu Touraine	F209 	BLEU.TOU	Radio France	03/02/2009
France Bleu Belfort Montbéliard	F209 	BLEUBELF	Radio France	03/02/2009
France Bleu Lorraine Nord	F209 	BLEULORN	Radio France	03/02/2009
France Bleu Périgord	F209 	BLEUPERI	Radio France	03/02/2009
France Bleu Frequenza Mora	F209 	BLEURCFM	Radio France	03/02/2009
France Bleu Roussillon	F209 	BLEUROUS	Radio France	03/02/2009
France Bleu Vaucluse	F209 	BLEUVAUC	Radio France	03/02/2009
France Bleu Île de France	F20A 	BLEU-IDF	Radio France	03/02/2009
France Bleu Pays d'Auvergne	F20A 	BLEU.AUV	Radio France	03/02/2009
France Bleu Hérault	F20A 	BLEU.HER	Radio France	03/02/2009
France Bleu La Rochelle	F20A 	BLEU.LR.	Radio France	03/02/2009
France Bleu Mayenne	F20A 	BLEU.MAY	Radio France	03/02/2009
France Bleu Pays de Savoie	F20A 	BLEU.SAV	Radio France	03/02/2009
France Bleu Nord	F20A 	BLEUNORD	Radio France	03/02/2009
France Bleu Sud Lorraine	F20A 	BLEUSLOR	Radio France	03/02/2009
Sud Radio +	F20B 	SUD PLUS	National	15/11/2011
RCF Pays de l'Ain	F20C 	RCF 01	Lyon	27/05/2019
RCF Vivarais	F20C 	RCF 07	Lyon	27/05/2019
RCF PAYS D'AUDE	F20C 	RCF 11	Toulouse	18/04/2019
DIALOGUE RCF	F20C 	RCF 13	Marseille	19/04/2019
RCF Charente	F20C 	RCF 16	Bordeaux	14/03/2019
RCF Corrèze	F20C 	RCF 19	Clermont-Ferrand	08/04/2019
RCF CORSICA	F20C 	RCF 20	Marseille	17/05/2019
RCF EN BOURGOGNE	F20C 	RCF 21	Dijon	17/04/2019
RCF CÔTES-D'ARMOR	F20C 	RCF 22	Rennes	19/03/2019
RCF Besançon	F20C 	RCF 25	Dijon	26/06/2019
RCF 26	F20C 	RCF 26	Lyon	27/05/2019
RCF MAGUELONE HERAULT	F20C 	RCF 34	Toulouse	18/04/2019
RCF Isère	F20C 	RCF 38	Lyon	01/07/2019
RCF JURA	F20C 	RCF 39	Dijon	26/06/2019
RCF Saint-Etienne	F20C 	RCF 42	Lyon	27/05/2019
RCF LOIRET	F20C 	RCF 45	Poitiers	21/01/2019
RCF ORNE	F20C 	RCF 61	Caen	30/01/2019
RCF Lyon	F20C 	RCF 69	Lyon	01/07/2019
RCF SARTHE	F20C 	RCF 72	Caen	30/01/2019
RCF Savoie	F20C 	RCF 73	Lyon	01/07/2019
RCF Haute-Savoie	F20C 	RCF 74	Lyon	27/05/2019
RCF HAUTE-NORMANDIE	F20C 	RCF 76	Caen	30/01/2019
RCF POITOU	F20C 	RCF 79-86	Poitiers	13/05/2019
RCF VAUCLUSE	F20C 	RCF 84	Marseille	18/03/2019
RCF Email Limousin	F20C 	RCF 87	Clermont-Ferrand	08/04/2019
RCF EN BERRY	F20C 	RCF BERRY	Poitiers	13/05/2019
RCF Nord de France	F20C 	RCF Nord	Lille	27/02/2019
RCF Aube / Haute-Marne	F20C 	RCF10 52	Nancy	08/04/2019
RCF Reims-Ardennes	F20C 	RCF51-08	Nancy	03/06/2019
RTL	F211 	RTL	National	04/03/2008
RFM	F212 	RFM	National	04/03/2008
Europe 1	F213 	EUROPE 1	National	04/03/2008
Skyrock	F214 	SKYROCK	National	04/03/2008
RTL 2	F215 	RTL2	National	04/03/2008
RMC	F216 	RMC	National	04/03/2008
Fun Radio	F217 	FUN	National	04/03/2008
Nostalgie	F218 	NOSTALGI	National	04/03/2008
Virgin Radio	F219 	VIRGIN	National	04/03/2008
Radio Néo	F21A 	NEO	National	06/11/2008
SWIGG	F21B 	SWIGG	National	17/05/2017
LATINA	F21C 	LATINA	National	26/06/2019
Oui FM	F21D 	OUI FM	National	22/06/2010
NRJ	F220 	NRJ	National	04/03/2008
Radio Classique	F221 	CLASSIQ	National	04/03/2008
Autoroute Info	F222 	AUTOROUT	National	04/03/2008
Radio VINCI Autoroutes	F222 	R107.7	National	19/03/2014
TSF JAZZ	F223 	TSF JAZZ	National	04/03/2008
Chérie FM	F224 	CHERIE	National	04/03/2008
MFM	F225 	MFM	National	04/03/2008
Rire et Chansons	F226 	RIRE &	National	04/03/2008
BFM	F227 	BFM	National	04/03/2008
Radio Courtoisie	F228 	COURTOIS	National	04/03/2008
Beur FM	F229 	BEUR FM	National	04/03/2008
Radio Nova	F22A 	NOVA	National	04/03/2008
Radio Orient	F22B 	ORIENT	National	04/03/2008
Radio FG	F22C 	FG.	National	12/07/2017
France Maghreb 2	F22D 	FMAGHREB	National	04/03/2008
Jazz Radio	F22F 	JAZZ	National	04/03/2008
Radio Soleil	F230 	R SOLEIL	National	04/03/2008
Radio Rivière Saint-Louis	F2FF 	RSL FM	La Réunion - Mayotte	04/03/2008
Radio Temporaire	F340 à F34F 	à déterminer par le CTA	Marseille	04/03/2008
Radio Temporaire	F350 à F35F 	à déterminer par le CTA	Poitiers	04/03/2008
Radio Temporaire	F360 à F36F 	à déterminer par le CTA	Toulouse	04/03/2008
Radio Temporaire	F370 à F37F 	à déterminer par le CTA	Nancy	04/03/2008
Radio Temporaire	F380 à F38F 	à déterminer par le CTA	Lyon	04/03/2008
Radio Temporaire	F390 à F39F 	à déterminer par le CTA	Lille	04/03/2008
Radio Temporaire	F3A0 à F3AF 	à déterminer par le CTA	Rennes	04/03/2008
Radio Temporaire	F3B0 à F3BF 	à déterminer par le CTA	Caen	04/03/2008
Radio Temporaire	F3C0 à F3CF 	à déterminer par le CTA	Dijon	04/03/2008
Radio Temporaire	F3D0 à F3DF 	à déterminer par le CTA	Bordeaux	04/03/2008
Radio Temporaire	F3E0 à F3EF 	à déterminer par le CTA	Paris	04/03/2008
Radio Temporaire	F3E0 à F3EF 	à déterminer par le CTA	La Réunion - Mayotte	04/03/2008
Radio Temporaire	F3E0 à F3EF 	à déterminer par le CTA	Antilles - Guyane	04/03/2008
Radio Temporaire	F3E0 à F3EF 	à déterminer par le CTA	Nouvelle Calédonie	04/03/2008
Radio Temporaire	F3E0 à F3EF 	à déterminer par le CTA	Polynésie	04/03/2008
Radio Temporaire	F3F0 à F3FF 	à déterminer par le CTA	Clermont-Ferrand	04/03/2008
France Bleu Haute-Normandie	F405 	BLEU.H.N	Radio France	03/02/2009
France Bleu Loire Océan	F405 	BLEU.L.O	Radio France	03/02/2009
France Bleu Limousin	F405 	BLEU.LIM	Radio France	03/02/2009
France Bleu Occitanie	F405 	BLEU.OC	Radio France	29/11/2017
France Bleu Alsace	F405 	BLEUALSA	Radio France	03/02/2009
France Bleu Provence	F405 	BLEUPROV	Radio France	04/03/2008
Alpes 1	F431 	ALPES 1	Marseille	04/03/2008
Radio Vitamine	F433 	VITAMINE	Marseille	04/03/2008
Radio Alpine Meilleure	F435 	R A M	Marseille	04/03/2008
Radio Maritima	F436 	MARITIMA	Marseille	04/03/2008
La Ciotat Fréquence Nautique	F437 	F.NAUTIQ	Marseille	27/05/2008
Kiss FM	F438 	KISS FM	Marseille	04/03/2008
RADIO EMOTION	F439 	EMOTION	Marseille	28/09/2012
Radio Star	F440 	STAR	Marseille	04/03/2008
Cannes radio	F441 	CANNES R	Marseille	11/09/2013
Radio Top FM	F442 	TOP FM	Marseille	04/03/2008
Costa Serena FM	F443 	RCM	Marseille	04/03/2008
Fréquence K	F444 	FREQUE.K	Marseille	04/03/2008
Radio Grenouille	F445 	GRENOUIL	Marseille	04/03/2008
Soleil FM	F446 	SOLEIL	Marseille	04/03/2008
Mistral FM	F447 	MISTRAL	Marseille	04/03/2008
Radio As	F448 	RADIO AS	Marseille	04/03/2008
Alta Fréquenza	F450 	ALTA	Marseille	04/03/2008
RADIO VALLEE	F452 	R VALLEE	Marseille	13/12/2013
UNITED RADIO	F454 	United	Marseille	07/04/2017
Radio Salve Regina	F455 	SALVEREG	Marseille	27/01/2012
Dici Radio	F456 	DICI	Marseille	27/01/2012
ZAP FM	F458 	ZAP FM	Marseille	22/09/2009
Alta Serena	F459 	SERENA	Marseille	30/03/2012
Mosaïque FM	F45A 	MOSAIQUE	Marseille	06/06/2014
NEBBIA CAMPUS CORTE	F45B 	NEBBIA	Marseille	26/02/2016
DIVA FM	F45C 	DIVA FM	Marseille	03/06/2016
Fréquenza Nostra	F45E 	F.NOSTRA	Marseille	21/06/2019
Radio Corse Bellevue	F460 	R.C.B.	Marseille	21/01/2011
STUDIO 20	F461 	STUDIO20	Marseille	17/05/2019
Radio Active	F480 	ACTIVE	Marseille	04/03/2008
Radio Camargue	F481 	CAMARGUE	Marseille	04/03/2008
Métropole Radio	F482 	METROPOL	Marseille	04/03/2008
Radio Chalom Nitsan	F483 	CHALOM	Marseille	04/03/2008
Radio JM Radio Juive Marseille	F484 	RADIO JM	Marseille	04/03/2008
Radio Calvi Citadelle	F486 	R CALVI	Marseille	04/03/2008
Radio Verdon	F488 	VERDONFM	Marseille	04/03/2008
Agora FM	F489 	AGORA FM	Marseille	04/03/2008
Radio TSF	F490 	TSF98.10	Marseille	04/03/2008
Clin d'Oeil FM	F491 	CL DOEIL	Marseille	04/03/2008
Mix la Radio Etudiante	F493 	M I X	Marseille	04/03/2008
Radio Balagne	F494 	BALAGNE	Marseille	04/03/2008
Nice Radio	F495 	NICE-FM	Marseille	04/03/2008
Grimaldi FM	F496 	GRIMALDI	Marseille	04/03/2008
Radio Corti Vivu	F497 	R.C.V	Marseille	04/03/2008
Radio Zinzine	F498 	ZINZINE	Marseille	04/03/2008
Voce Nustrale	F499 	VOCE	Marseille	04/03/2008
Radio Sainte Baume	F4A0 	STEBAUME	Marseille	04/03/2008
Radio Golfe d'Amour (RGA)	F4A1 	RGA	Marseille	04/03/2008
Fréquence Mistral	F4A2 	MISTRAL	Marseille	04/03/2008
Là La Radio	F4A3 	LA RADIO	Marseille	04/03/2008
Durance FM	F4A5 	DURANCE	Marseille	04/03/2008
Comète FM	F4A6 	COMETE	Marseille	04/03/2008
R'Alpes Sud	F4A7 	R'ALPSUD	Marseille	04/03/2008
R'Grand Briançonnais	F4A8 	R'GBRIAN	Marseille	04/03/2008
Contact FM prog.Radio Star Monaco	F4A9 	STAR MC	Marseille	04/03/2008
GALERE	F4AA 	GALERE	Marseille	25/11/2011
IMAGINE	F4AB 	IMAGINE	Marseille	25/11/2011
RFL 101	F532 	RFL 101	Poitiers	22/09/2009
Radio Pulsar	F534 	PULSAR	Poitiers	04/03/2008
Génération FM	F536 	GENERAT	Poitiers	04/03/2008
Radio Béton	F537 	BETON	Poitiers	04/03/2008
C2L, Chalette Loiret Loing	F538 	C2L	Poitiers	05/04/2013
Resonance	F539 	RESO96.9	Poitiers	04/03/2008
Radio D 4 B	F541 	D 4 B	Poitiers	04/03/2008
Collines FM	F542 	COLLINES	Poitiers	04/03/2008
Radio Gatine	F544 	GATINE	Poitiers	04/03/2008
REC (Echos des Choucas)	F545 	REC103.7	Poitiers	04/03/2008
Radio Clash	F546 	CLASH FM	Poitiers	04/03/2008
Radio Arc-en-Ciel	F547 	ARC/CIEL	Poitiers	04/03/2008
Radio Campus	F548 	CAMPUS	Poitiers	04/03/2008
Graffic FM	F549 	GRAFFIC	Poitiers	04/03/2008
Radio Forum	F552 	FORUM	Poitiers	04/03/2008
Vibration	F560 	VIBRA	Poitiers	04/03/2008
RCF Saint-Martin	F561 	RCF 37	Poitiers	04/04/2014
STUDIO ZEF	F563 	ZEF 91.1	Poitiers	10/11/2010
RCF 41	F564 	RCF 41	Poitiers	04/04/2014
Radio Vag	F580 	VAG'FM	Poitiers	04/03/2008
Styl'FM	F582 	STYL'FM	Poitiers	04/03/2008
Radio Val d'Or	F583 	VAL D'OR	Poitiers	04/03/2008
Radio Antenne Portugaise	F585 	PORTUGAL	Poitiers	04/03/2008
Berry FM	F586 	BERRY FM	Poitiers	04/04/2014
Connexion FM	F587 	CONEXION	Poitiers	04/03/2008
RMZ	F588 	R M Z	Poitiers	04/03/2008
Delta FM	F589 	DELTA	Poitiers	04/03/2008
Radio Agora	F58A 	AGORA	Poitiers	06/11/2008
Radio Balistiq	F58B 	BALISTIQ	Poitiers	06/11/2008
Radio Campus Tours	F58C 	CAMPUS	Poitiers	06/11/2008
MEGA FM	F590 	MEGA FM	Poitiers	00/00/0000
Radio Active	F5A1 	R-ACTIVE	Poitiers	04/03/2008
Totem	F631 	TOTEM	Toulouse	04/03/2008
Chérie FM Pyrénées	F632 	RPCHERIE	Toulouse	04/03/2008
Radio Menergy	F633 	MENERGY	Toulouse	04/03/2008
R.D.C.	F634 	R D C	Toulouse	04/03/2008
Radio Plus	F635 	R.PLUS	Toulouse	04/03/2008
Radio Saint-Affrique	F636 	R.STAFF	Toulouse	04/03/2008
Radio Aviva	F637 	AVIVA	Toulouse	04/03/2008
Radio Marseillette	F638 	RMARSEIL	Toulouse	04/03/2008
Présence Lourdes Pyrénées	F639 	PRESENCE	Toulouse	04/03/2008
Radio Peinard Skyrock	F63E 	SKYROCK	Toulouse	10/02/2016
CFM 82	F640 	CFM 82	Toulouse	04/03/2008
Radio Altitude	F641 	ALTITUDE	Toulouse	04/03/2008
Grand Sud FM	F642 	GRANDSUD	Toulouse	18/05/2010
Radio Cagnac	F643 	R.CAGNAC	Toulouse	04/03/2008
Radio Présence	F644 	PRESENCE	Toulouse	04/03/2008
RTS FM	F645 	RTS FM	Toulouse	04/03/2008
R d'Autan	F646 	Rd'AUTAN	Toulouse	22/09/2009
Radio Galaxie	F647 	GALAXIE	Toulouse	04/03/2008
Radio Muret	F648 	MURET	Toulouse	04/03/2008
FM 81	F649 	FM 81	Toulouse	04/03/2008
Sud Radio	F650 	SUDRADIO	Toulouse	04/03/2008
RFM Quercy Rouergue	F651 	F BLEUE	Toulouse	04/03/2008
Divergence FM	F652 	DIVERGEN	Toulouse	04/03/2008
Fréquence Adour	F653 	F ADOUR	Toulouse	04/03/2008
Radio Occitanie	F654 	OCCITANA	Toulouse	04/03/2008
RDM	F655 	R D M	Toulouse	04/03/2008
Radio d'Artagnan	F656 	R D A.	Toulouse	04/03/2008
FM PLUS	F658 	FM-PLUS	Toulouse	10/04/2018
Radio VALLESPIR	F659 	VALLESPI	Toulouse	17/12/2013
Radio Ecclesia	F660 	ECCLESIA	Toulouse	20/01/2011
Nostalgie Bagneres Hautes Pyrénées	F679 	NOSTALG	Toulouse	15/01/2014
Radio Albiges	F680 	ALBIGES	Toulouse	04/03/2008
Oxygène FM	F682 	OXYGENE	Toulouse	04/03/2008
Contact FM 88.8	F683 	CONTACT	Toulouse	04/03/2008
Radio Espoir 82	F684 	ESPOIR82	Toulouse	04/03/2008
Delta FM	F685 	DELTA FM	Toulouse	04/03/2008
Radio ciel bleu	F686 	CIELBLEU	Toulouse	04/03/2008
Radio Fil de L'eau	F687 	FILD'EAU	Toulouse	04/03/2008
FMR	F688 	FMR	Toulouse	04/03/2008
Transparence	F689 	TRANSPAR	Toulouse	04/03/2008
Toulouse FM	F68A 	TOULOUSE	Toulouse	06/11/2008
Distortion	F68B 	DISTO	Toulouse	06/11/2008
Radio TER	F68C 	O2 TER	Toulouse	15/12/2009
Radio Larzac	F68D 	R.LARZAC	Toulouse	15/12/2009
Radio Temps	F68E 	R TEMPS	Toulouse	11/06/2010
Radio Kol Aviv	F691 	KOL AVIV	Toulouse	04/03/2008
100 %	F692 	100/100	Toulouse	04/03/2008
100 % Catalogne	F692 	100% CAT	Toulouse	13/03/2018
Radio de la Save	F694 	R D L S	Toulouse	04/03/2008
Canal Sud	F695 	CANALSUD	Toulouse	04/03/2008
Antenne d'Oc	F696 	ANT.D'OC	Toulouse	04/03/2008
Radio Coteaux	F697 	RCOTEAUX	Toulouse	04/03/2008
Radio 16	F698 	RADIO 16	Toulouse	04/03/2008
Radio Clapas	F6A0 	CLAPAS	Toulouse	04/03/2008
L'Echo des Garrigues	F6A1 	EKO 88.5	Toulouse	04/03/2008
Fréquence Luz	F6A2 	FREQ LUZ	Toulouse	04/03/2008
Radio Lodéve	F6A3 	LODEVE	Toulouse	04/03/2008
Radio Radio	F6A4 	R.RADIO	Toulouse	04/03/2008
Présence Lot	F6A5 	PRESENCE	Toulouse	04/03/2008
VFM	F6A6 	VFM	Toulouse	04/03/2008
Barousse FM	F6A8 	BAROUSSE	Toulouse	04/03/2008
Radio Arrels	F6A9 	ARRELS	Toulouse	04/03/2008
Radio Fréquence Soleil Toulouse	F6AA 	SOLEIL	Toulouse	04/03/2008
Présence Figeac	F6AB 	PRESENCE	Toulouse	04/03/2008
Radio Présence Pyrénées	F6AC 	PRESENCE	Toulouse	04/03/2008
Radio Mon Pais	F6AD 	MON PAIS	Toulouse	04/03/2008
Décibel FM	F6AE 	DECIBEL	Toulouse	04/03/2008
Radio Salvetat Peinard	F6AF 	SALVETAT	Toulouse	04/03/2008
Booster	F6B1 	@BOOSTER	Toulouse	04/03/2008
Radio Fréquence Nîmes	F6B2 	R.F.N	Toulouse	04/03/2008
PIC FM	F6B3 	R V A	Toulouse	04/03/2008
FM Plus Grille Ouverte	F6B4 	R.G.O	Toulouse	04/03/2008
RADIO BARTAS	F6B5 	BARTAS	Toulouse	18/12/2012
Radio Pays d'Hérault	F6B6 	R-P-H	Toulouse	06/05/2011
RPH-SUD	F6B6 	R-P-H	Toulouse	06/05/2011
Radio Flash	F6B7 	PICSTLOU	Toulouse	04/03/2008
Littoral FM	F6B8 	LITTORAL	Toulouse	04/03/2008
3D FM	F6B9 	3D FM	Toulouse	04/03/2008
Radio Païs	F6C0 	PAIS	Toulouse	04/03/2008
Radio Lenga d'Oc Narbonna	F6C1 	LENGADOC	Toulouse	04/03/2008
Radio Escapades	F6C2 	ESCAPADE	Toulouse	04/03/2008
Radio Margeride	F6C3 	MARGERID	Toulouse	04/03/2008
Radio Ballade	F6C4 	BALLADE	Toulouse	04/03/2008
Radio Campus Toulouse	F6C5 	CAMPUSFM	Toulouse	00/00/0000
Gascogne FM	F6C6 	GASCOGNE	Toulouse	04/03/2008
FM Evangile 66	F6C7 	EVANGILE	Toulouse	04/03/2008
Agora	F6C8 	AGORA FM	Toulouse	04/03/2008
Radio Lacaune	F6C9 	LACAUNE	Toulouse	04/03/2008
DFM 930	F6CA 	DFM 930	Toulouse	00/00/0000
Radio Alliance Plus	F6D0 	ALLIANCE	Toulouse	04/03/2008
Radio Inter-Val	F6D1 	INTERVAL	Toulouse	04/03/2008
Système	F6D2 	SYSTEME	Toulouse	04/03/2008
Plus FM	F6D3 	PLUS FM	Toulouse	04/03/2008
Radio Axe Sud	F6D4 	R AXESUD	Toulouse	04/03/2008
Lenga d'Oc	F6D5 	LENGADOC	Toulouse	04/03/2008
Raje	F6D6 	RAJE	Toulouse	04/03/2008
RAJE Avignon	F6D6 	RAJE	Marseille	21/09/2018
Radio Montaillou	F6D7 	MtAILLOU	Toulouse	04/03/2008
Radio Montaillou	F6D7 	MtAILLOU	Toulouse	22/09/2009
Radio Association	F6D8 	RAD ASSO	Toulouse	04/03/2008
Radio La Locale	F6D9 	LALOCALE	Toulouse	04/03/2008
Radio Val Pireneos	F6E0 	PIRENEOS	Toulouse	04/03/2008
Radio Festival	F6E2 	FESTIVAL	Toulouse	04/03/2008
ONE FM	F6E3 	ONE	Toulouse	16/11/2010
Accent 4	F731 	ACCENT 4	Nancy	04/03/2008
Radio Dreyeckland	F732 	DREYECKD	Nancy	04/03/2008
Latitude FM	F733 	LATITUDE	Nancy	04/03/2008
Top Music	F734 	TOPMUSIC	Nancy	04/03/2008
Kit FM	F735 	KIT FM	Nancy	21/09/2011
Radio Arc-en-ciel	F738 	ARCnCIEL	Nancy	22/09/2009
Radio en construction	F738 	R.E.C	Nancy	04/03/2008
Radio Jerico	F739 	JERICO 57	Nancy	04/03/2008
Magnum La Radio	F73B 	MAGNUM	Nancy	05/09/2011
Radio 8	F742 	RADIO 8	Nancy	04/03/2008
Direct FM	F743 	DIRECTFM	Nancy	04/03/2008
Judaïca	F744 	JUDAICA	Nancy	04/03/2008
Champagne FM	F748 	CHAMP FM	Nancy	04/03/2008
Fajet 94,2 FM Nancy	F749 	FAJET	Nancy	04/03/2008
RVM	F750 	R V M	Nancy	04/03/2008
Phare FM Haguenau	F751 	PHARE	Nancy	05/09/2011
Vosges FM	F752 	VOSGESFM	Nancy	02/04/2012
RCF Lorraine Nancy	F753 	RCF LOR	Nancy	02/03/2015
Fréquence verte	F75B 	FR VERTE	Nancy	22/09/2009
DYNAMYK	F75C 	DYNAMYK	Nancy	04/06/2018
Happy	F783 	HAPPY FM	Nancy	04/03/2008
Azur FM	F784 	AZUR FM	Nancy	04/03/2008
Soleil Média	F785 	RSM	Nancy	04/03/2008
Radio Peltre Loisirs	F786 	RPL	Nancy	04/03/2008
Radio Florival	F787 	FLOR FM	Nancy	06/11/2008
Radio Campus Troyes	F789 	CAMPUS	Nancy	04/03/2008
RDS Chérie FM Nancy	F790 	RDS100.9	Nancy	18/10/2011
Est FM	F791 	EST FM	Nancy	04/03/2008
Radio Mélodie	F793 	MELODIE	Nancy	04/03/2008
Radio ECN	F795 	ECN	Nancy	04/03/2008
Radio Déclic	F796 	DECLIC	Nancy	04/03/2008
Meuse FM	F797 	MEUSE FM	Nancy	04/03/2008
Radio A.R.I.A.	F798 	ARIA	Nancy	04/03/2008
Thème Radio	F799 	THEME	Nancy	04/03/2008
Radio Liberté	F7A0 	LIBERTE	Nancy	04/03/2008
Radio Cocktail FM	F7A1 	COCKTAIL	Nancy	04/03/2008
Radio Bienvenue Strasbourg	F7A2 	R B S	Nancy	04/03/2008
Radio Fugi	F7A4 	FUGI FM	Nancy	04/03/2008
Radio Dreyeckland Centre Alsace Colmar	F7A5 	RDL	Nancy	04/03/2008
Radio Cristal	F7A6 	CRISTAL	Nancy	04/03/2008
Radio des Ballons	F7A7 	RBALLONS	Nancy	04/03/2008
Radio Cigale FM	F7A8 	CIGALEFM	Nancy	04/03/2008
Radio Graffiti's	F7A9 	GRAFFITI	Nancy	04/03/2008
Radio Canal Myrtille	F7AA 	RCM 97.6	Nancy	04/03/2008
Radio Lor'FM	F7AB 	LOR'FM	Nancy	04/03/2008
Radio Studio 1	F7AC 	STUDIO 1	Nancy	04/03/2008
Phare FM Haute-Normandie	F7AD 	PHARE FM	Caen	00/00/0000
Phare FM	F7AD 	PHARE FM	Nancy	04/03/2008
Radio Activités	F7AE 	ACTIVITE	Nancy	04/03/2008
Cerise FM	F7AF 	CERISEFM	Nancy	09/07/2012
Radio Bellevue	F7B0 	BELLEVUE	Nancy	04/03/2008
Radio Bouton	F7B1 	BOUTON	Nancy	04/03/2008
Radio Mau-Nau	F7B2 	R M N	Nancy	04/03/2008
ViVradio	F7B3 	ViVradio	Nancy	04/04/2016
Radio Rupt de Mad	F7B4 	RDM	Nancy	04/03/2008
RCB La Radio de la Vallée	F7B5 	R.C.B	Nancy	04/03/2008
Radio Contact	F7B6 	CONTACT	Nancy	04/03/2008
La Radio Primitive	F7B7 	LAPRIM	Nancy	04/03/2008
Radio Graffiti	F7B8 	GRAFFITI	Nancy	04/03/2008
Radio Aube etSeine	F7B9 	R A S	Nancy	04/03/2008
Radio Iris	F7BA 	IRIS	Nancy	04/03/2008
Radio Saint-Nabor	F7BB 	R S N	Nancy	04/03/2008
Sud Ardennes Radio	F7BC 	S.A.R.	Nancy	04/03/2008
Radio Caraïb Nancy (RCN)	F7BD 	R.C.N	Nancy	04/03/2008
Radio Jeunes Reims (RJR)	F7BE 	R J R	Nancy	04/03/2008
Résonnance FM	F7BF 	RESO FM	Nancy	04/03/2008
Active Radio	F7C0 	ACTIVE	Nancy	22/09/2009
Bulle FM	F7C1 	BULLE FM	Nancy	27/05/2008
Radio Gué Mozot	F7C2 	GUEMOZOT	Nancy	06/09/2010
La Radio Plus	F832 	PLUS	Lyon	04/03/2008
Radio 74	F833 	RADIO 74	Lyon	04/03/2008
FC Radio	F837 	FC RADIO	Lyon	04/03/2008
ODS Radio	F838 	ODS	Lyon	04/03/2008
MTI	F83A 	M T I	Lyon	23/04/2014
Radio Espace	F842 	ESPACE	Lyon	04/03/2008
Rock FM	F843 	ROCK FM	Lyon	04/03/2008
TFM	F844 	TFM	Lyon	04/03/2008
Montagne FM	F845 	MONTAGNE	Lyon	04/03/2008
Perrine FM	F846 	PERRINE	Lyon	04/03/2008
Radio Mont-Blanc	F847 	MT.BLANC	Lyon	04/03/2008
Impact FM	F848 	IMPACT	Lyon	04/03/2008
Radio Grésivaudan	F850 	GRESIVAU	Lyon	04/03/2008
Déclic	F852 	DECLIC	Lyon	28/10/2011
R-DWA	F853 	RDWA	Lyon	28/10/2011
Radio Dio	F857 	RADIODIO	Lyon	03/02/2009
Radio FMR	F859 	RADIOFMR	Lyon	23/11/2011
Séquence FM	F85A 	SEQUENCE	Lyon	28/10/2011
Radio Altitude	F85B 	ALTITUDE	Lyon	23/11/2011
Radio Valloire	F85C 	VALLOIRE	Lyon	28/10/2011
C' Radio	F85D 	C RADIO	Lyon	28/10/2011
RADIO MILLENIUM	F85E 	MILENIUM	Lyon	28/06/2012
RADIO ROYANS	F85F 	R ROYANS	Lyon	05/04/2013
RADIOMAGNY	F861 	RADMAGNY	Lyon	23/05/2014
Radio Espérance	F864 	ESPERANCE	Lyon	04/03/2008
Radio Scoop	F865 	SCOOP	Lyon	04/03/2008
Radio Alto	F866 	ALTO	Lyon	07/10/2010
RADIO SEMNOZ	F867 	SEMNOZ	Lyon	10/03/2016
RADIO DRAGON	F868 	DRAGON	Lyon	30/09/2016
Phare FM Grenoble	F869 	PHARE FM	Lyon	07/02/2017
Phare FM aux Portes du Dauphiné	F86A 	PHARE FM	Lyon	07/02/2017
H2O	F86B 	__H2O___	Lyon	02/03/2018
RADIO FESTIVAL	F86C 	FESTIVAL	Lyon	02/02/2018
RETRO FM (RADIO BUIS)	F86D 	R. BUIS	Lyon	02/03/2018
GLOBULE RADIO	F86E 	GLOBULE	Lyon	26/10/2018
Hot Radio	F880 	HOT	Lyon	04/03/2008
PASSION FM	F881 	PFMRADIO	Lyon	05/02/2016
Radio Isa	F882 	ISA	Lyon	04/03/2008
Lyon Première	F883 	LYON1ère	Lyon	04/03/2008
Radio Trait d'Union	F884 	RTU 89,8	Lyon	04/03/2008
Radio 100 Kol Hachalom	F885 	R K H	Lyon	04/03/2008
Soleil FM	F886 	SOLEIL	Lyon	04/03/2008
Tonic Radio, la radio du sport	F887 	TONIC	Lyon	23/11/2011
Fréquence 7	F888 	FREQ 7	Lyon	04/03/2008
Radio Loire FM	F889 	LOIRE FM	Lyon	04/03/2008
Radio Canut	F890 	CANUT	Lyon	04/03/2008
Radio Campus	F891 	CAMPUS	Lyon	04/03/2008
Radio Des Boutières	F892 	R D B FM	Lyon	04/03/2008
Pixel FM	F893 	PIXEL FM	Lyon	04/03/2008
Radio Samoens	F894 	SAMOENS	Lyon	04/03/2008
New FM	F895 	NEW'S FM	Lyon	04/03/2008
Radio Passion	F896 	PASSION	Lyon	04/03/2008
Sun 101.5	F897 	SUN101.5	Lyon	27/04/2012
Radio Salam	F898 	R-SALAM	Lyon	04/03/2008
Radio Judaïca Lyon	F899 	JUDAICA	Lyon	04/03/2008
Max FM	F8A1 	MAX FM	Lyon	04/03/2008
Sorgia FM	F8A2 	SORGIAFM	Lyon	04/03/2008
Radio Fontaine	F8A3 	FONTAINE	Lyon	04/03/2008
RCT Cap Sao	F8A4 	CAPSAO	Lyon	22/09/2009
Radio Plaine	F8A5 	R PLAINE	Lyon	04/03/2008
Radio Ellebore	F8A6 	ELLEBORE	Lyon	04/03/2008
RADIO KALEIDOSCOPE	F8A7 	RKS	Lyon	27/05/2019
Radio Méga	F8A8 	MEGA	Lyon	04/03/2008
Sol FM	F8A9 	SOL FM	Lyon	04/03/2008
Oxygène Radio	F8AA 	OXYGENE	Lyon	04/03/2008
Info RC	F8AB 	INFORC	Lyon	04/03/2008
Radio A	F8AC 	RADIO A	Lyon	04/03/2008
Radio Pluriel	F8AD 	PLURIEL	Lyon	04/03/2008
OR FM	F8AE 	OR FM	Lyon	04/03/2008
Radio M	F8AF 	RADIO M	Lyon	04/03/2008
Radio Pytagor	F8B0 	PYTAGOR	Lyon	04/03/2008
Radio BLV	F8B1 	RADIOBLV	Lyon	04/03/2008
Radio Zig Zag	F8B2 	ZIG-ZAG	Lyon	04/03/2008
Activ Radio	F8B3 	ACTIV	Lyon	04/03/2008
Radio Val de Reins	F8B4 	R.V.R	Lyon	04/03/2008
Radio Arménie	F8B5 	ARMENIE	Lyon	04/03/2008
Couleurs FM	F8B8 	COULEURS	Lyon	04/03/2008
Radio d'Ici	F8C0 	R. D'ICI	Lyon	04/03/2008
R'Tignes	F8C1 	R'TIGNES	Lyon	04/03/2008
R'Les Arcs	F8C2 	R'ARCS	Lyon	04/03/2008
R'Méribel	F8C3 	R'MERIBL	Lyon	04/03/2008
R'La Plagne	F8C4 	R'PLAGNE	Lyon	04/03/2008
Radio Val d'Isère	F8C5 	VAL 96.1	Lyon	04/03/2008
Radio Ondaine	F8C6 	ONDAINE	Lyon	04/03/2008
Radio Zones	F8C7 	ZONES938	Lyon	04/03/2008
Radio Saint-Ferréol	F8C8 	FERREOL	Lyon	04/03/2008
Radio Courchevel	F8C9 	R'COURCH	Lyon	04/03/2008
Radio Brume	F8CA 	BRUME	Lyon	07/05/2010
Contact	F931 	CONTACT	Lille	04/03/2008
Radio 6	F932 	RADIO 6	Lille	04/03/2008
Mona FM	F933 	MONA FM	Lille	04/03/2008
Roc FM	F934 	ROC FM	Lille	04/03/2008
Delta FM	F935 	DELTA FM	Lille	04/03/2008
Canal Sambre Avesnois	F939 	CANAL S	Lille	04/03/2008
Radio Uylenspiegel	F941 	UYLENSPI	Lille	04/03/2008
RDL	F942 	RDLradio	Lille	15/04/2015
Horizon	F943 	HORIZON	Lille	20/12/2013
RADIO BRUAYSIS programme RDL	F944 	BruayRDL	Lille	15/04/2015
Radio Pacot Lambersart RPL	F946 	RPL 99	Lille	04/03/2008
Radio Fréquence Laon RFL	F947 	RFL LAON	Lille	04/03/2008
Radio Plus	F948 	PLUS	Lille	04/03/2008
Echo FM	F949 	ECHO FM	Lille	04/03/2008
Best FM Arras	F950 	BEST FM	Lille	04/03/2008
Campus Amiens	F952 	_CAMPUS_	Lille	07/02/2012
Radio 3 des	F953 	RADIO 3D	Lille	30/09/2015
R2M La Radio plus	F980 	R2M +	Lille	04/03/2008
Pastel FM	F981 	PASTEL	Lille	04/03/2008
Planète FM	F982 	PLANETE	Lille	04/03/2008
Radio Condé Macou	F984 	RCM 98,4	Lille	04/03/2008
Radio B L C	F985 	BLC 90,9	Lille	04/03/2008
Radio Galaxie	F986 	GALAXIE	Lille	04/03/2008
Radio 13	F987 	R13/RBM	Lille	04/03/2008
RBM Radio Billy Montigny	F987 	R13/RBM	Lille	04/03/2008
Radio Galaxie	F988 	GALAXIE	Lille	04/03/2008
Radio Campus	F989 	CAMPUS	Lille	04/03/2008
Radio Banquise	F990 	BANQUISE	Lille	04/03/2008
Radio Rencontre	F991 	RENCONTR	Lille	04/03/2008
Transat FM	F992 	TRANSAT	Lille	04/03/2008
Radio P.FM	F993 	PFM 99.9	Lille	04/03/2008
Radio Club	F994 	CLUB1057	Lille	04/03/2008
Rado Picardie Littoral	F995 	RPL 91.6	Lille	04/03/2008
Hit West	FA31 	HIT WEST	Rennes	04/03/2008
Tempo La Radio	FA32 	TEMPO	Rennes	04/03/2008
RADIO OXYGENE	FA33 	OXYGENE	Rennes	22/02/2016
NTI	FA37 	NTI	Rennes	04/03/2008
Radio Neptune	FA38 	NEPTUNE	Rennes	04/03/2008
FORUM MAINE ET LOIRE	FA40 	FORUM	Rennes	22/05/2017
Graffiti Urban Radio	FA41 	GRAFFITI	Rennes	04/03/2008
Radio Caroline	FA43 	CAROLINE	Rennes	04/03/2008
Jet FM	FA44 	JET FM	Rennes	04/03/2008
RFC	FA45 	R.F.C.	Rennes	04/03/2008
Radiocéan	FA47 	R.OCEAN	Rennes	04/03/2008
RMS 89,6	FA48 	R AURAY	Rennes	04/03/2008
RLK	FA52 	RLK	Rennes	03/02/2009
Radio Kerne	FA53 	KERNE	Rennes	04/03/2008
RADIO PAYS DE LEON	FA54 	RPL	Rennes	18/09/2018
Radio Chrono	FA55 	CHRONO	Rennes	04/03/2008
Alternantes FM	FA56 	ALTERNAN	Rennes	04/03/2008
Radio Cote d'amour	FA58 	FMC	Rennes	04/03/2008
RMN	FA59 	R M N	Rennes	04/03/2008
Station Millenium	FA5A 	MILENIUM	Rennes	20/06/2016
TIMBRE FM	FA5B 	TIMBRE	Rennes	27/01/2014
Radio Atlantis FM	FA5D 	ATLANTIS	Rennes	15/09/2014
FREQUENCE 8	FA5E 	FREQ 8	Rennes	13/02/2017
Alouette	FA61 	ALOUETTE	Rennes	04/03/2008
Radio Campus Angers	FA62 	CAMPUS	Rennes	12/10/2015
JADE FM	FA63 	JADE FM	Rennes	21/11/2016
RADIO BALISES	FA64 	BALISES	Rennes	11/09/2017
Radio Laser	FA80 	LASER	Rennes	04/03/2008
Radio Fidélité	FA81 	FIDELITE	Rennes	04/03/2008
Radio Emeraude	FA82 	EMERAUDE	Rennes	04/03/2008
JAIME	FA83 	JAIME	Rennes	13/02/2012
Radio Bonheur	FA84 	BONHEUR	Rennes	04/03/2008
Radio Bonheur Centre Bretagne	FA84 	RCC RB	Rennes	05/09/2018
Canal B	FA85 	CANAL B	Rennes	04/03/2008
Plum FM	FA86 	PLUM'FM	Rennes	04/03/2008
Radio Haute Angevine	FA87 	ANGEVINE	Rennes	04/03/2008
Océane FM	FA88 	OCEANE	Rennes	04/03/2008
OCÉANE BRETAGNE NORD	FA88 	OCÉANE	Rennes	20/02/2018
Sun FM	FA89 	SUN FM	Rennes	04/03/2008
Fréquence 10	FA91 	FREQ 10	Rennes	04/03/2008
Arvorig FM	FA92 	ARVORIG	Rennes	04/03/2008
Radio Campus Rennes	FA93 	R.CAMPUS	Rennes	04/03/2008
Radio Evasion (le Faou)	FA94 	REVASION	Rennes	04/03/2008
Sing Sing	FA95 	SINGSING	Rennes	04/03/2008
Radio Cité Bretagne	FA96 	RCB	Rennes	04/03/2008
Radio Parole de Vie	FA97 	R.P.V	Rennes	04/03/2008
Fréquence Mutine	FA98 	MUTINE	Rennes	04/03/2008
Radio Kreiz Breizh	FA99 	R K B	Rennes	04/03/2008
Radio Rennes	FA9A 	R RENNES	Rennes	04/03/2008
Radio Soleil 35	FA9B 	SOLEIL35	Rennes	04/03/2008
Radio Nord Bretagne	FA9C 	RNB	Rennes	04/03/2008
Cob FM	FA9D 	COB FM	Rennes	04/03/2008
Radio Evasion (Saint-Méen-le-Grand)	FA9E 	EVASION	Rennes	04/03/2008
Radio G !	FA9F 	RADIO G	Rennes	04/03/2008
Zénith FM	FAA0 	ZENITHFM	Rennes	04/03/2008
Radio Univers	FAA1 	UNIVERS	Rennes	04/03/2008
RADIO BRO GWENED	FAA2 	RBG	Rennes	19/03/2019
Nov FM	FAA3 	NOV FM	Rennes	04/03/2008
RPS FM	FAA4 	RPS FM	Rennes	04/03/2008
RADIO HARMONIE CORNOUAILLE	FAA5 	HARMONIE	Rennes	13/02/2012
Ploubaz FM	FAA6 	PLOUBAZ	Rennes	04/03/2008
La Radio de la Mer	FAA7 	OUI MER	Rennes	12/04/2011
La Tribu	FAA8 	LA TRIBU	Rennes	04/03/2008
Radio Activ'	FAA9 	ACTIV'	Rennes	04/03/2008
Prun'	FAB1 	PRUN'	Rennes	04/03/2008
Kernews	FAB2 	KERNEWS	Rennes	04/03/2008
Radio U	FAB4 	RADIO U	Rennes	04/03/2008
Euradionantes	FAB6 	EURADIO	Rennes	04/03/2008
NEPTUNE FM	FAB8 	NEPTUNE	Rennes	28/06/2010
Vire FM	FB32 	VIRE FM	Caen	04/03/2008
Sea FM	FB35 	SEA FM	Caen	04/03/2008
TENDANCE OUEST	FB38 	TENDANCE OUEST	Caen	27/06/2018
TENDANCE OUEST ORNE	FB38 	TENDANCE OUEST ORNE	Caen	27/06/2018
TENDANCE OUEST SEINE MARITIME	FB38 	TENDANCE OUEST SEINE MARITIME	Caen	27/06/2018
Radio Cristal	FB39 	CRISTAL	Caen	04/03/2008
CRISTAL NORMANDIE	FB39 	CRISTAL NORMANDIE	Caen	27/06/2018
666	FB42 	666	Caen	04/03/2008
Plus FM	FB43 	PLUS FM	Caen	04/03/2008
Radio Albatros	FB44 	ALBATROS	Caen	04/03/2008
Fréquence Sillé FM	FB46 	FREQSILL	Caen	04/03/2008
Radio La Sentinelle	FB47 	RLS	Caen	04/03/2008
Radio Prevert	FB48 	PREVERT	Caen	04/03/2008
TSF 98	FB49 	TSF 98	Caen	04/03/2008
Radio Phénix-Campus Caen	FB52 	PHENIX	Caen	07/05/2013
ORNITHORYNQUE	FB53 	ORNITHO	Caen	18/10/2010
Radio Principe Actif	FB54 	P.ACTIF	Caen	05/09/2011
Contact FM	FB55 	CONTACT	Caen	27/01/2014
HAG'FM	FB56 	HAG FM	Caen	14/12/2015
OXYGENE RADIO LAVAL	FB57 	OXYGENE	Caen	22/02/2016
RCF CALVADOS-MANCHE	FB59 	RCF14-50	Caen	13/09/2016
PRINCIPE ACTIF VERNEUIL BRETEUIL CONCHES	FB5A 	PRINCIPE ACTIF VERNEUIL BRETEUIL CONCHES	Caen	27/06/2018
Radio Vallée de la Lézarde	FB80 	R.V.L	Caen	04/03/2008
Radio Intensité	FB81 	INTENS'	Caen	04/03/2008
Radio Alpes Mancelle	FB83 	R.A.M	Caen	04/03/2008
Radio des Trois Vallées	FB84 	RTV 95.7	Caen	04/03/2008
Radio Alpa	FB86 	ALPA	Caen	04/03/2008
RC 2	FB87 	R.C.2	Caen	04/03/2008
Radio des Hauts deRouen	FB88 	RADIOHDR	Caen	04/03/2008
Sweet FM	FB89 	SWEET FM	Caen	04/03/2008
SWEET FM CENTRE	FB89 	SWEET FM	Poitiers	03/07/2018
RADIO GRAND CIEL	FB90 	RGC	Caen	18/05/2017
Espace	FB91 	ESPACE	Caen	04/03/2008
Radio Flam	FB92 	FLAM	Caen	04/03/2008
Cartable FM	FB93 	CARTABLE	Caen	04/03/2008
Pulse	FB94 	PULSE	Caen	04/03/2008
Radio Coup de Foudre	FB95 	RCDF 104	Caen	04/03/2008
Horizon FM	FB96 	HORIZON	Caen	04/03/2008
Radio Les Vaux Village	FB97 	R.L.W.	Caen	04/03/2008
L'autre radio	FB9B 	L'AUTRE	Caen	03/02/2009
Radio Nevers	FC33 	NEVERS	Dijon	04/03/2008
Fréquence Plus	FC34 	F PLUS	Dijon	04/03/2008
Radio Sud Besançon	FC35 	RADIOSUD	Dijon	04/03/2008
Radio Oméga	FC36 	OMEGA	Dijon	04/03/2008
Radio Numéro 1	FC37 	NUMERO 1	Dijon	19/06/2013
Radio Villages FM	FC38 	VILLAGES	Dijon	04/03/2008
Diversité FM	FC39 	DIVERSIT	Dijon	09/10/2017
Radio Campus Besançon	FC3A 	CAMPUS	Dijon	06/11/2008
SNR	FC40 	SNR100.1	Dijon	04/03/2008
Bac FM	FC41 	BAC FM	Dijon	04/03/2008
Plein Air	FC42 	PLEINAIR	Dijon	04/03/2008
97,2 Radio Nord Bourgogne	FC44 	R N B	Dijon	04/03/2008
Eole	FC45 	EOLE	Dijon	04/03/2008
Radio Bresse	FC46 	R.BRESSE	Dijon	04/03/2008
Fréquence des Loisirs	FC47 	F.D.L.	Dijon	04/03/2008
Fréquence Amitié Vesoul	FC48 	F.AMITIE	Dijon	04/03/2008
Triage FM	FC49 	TRIAGEFM	Dijon	04/03/2008
Flotteurs FM	FC50 	FLOTTEUR	Dijon	04/03/2008
Radio Bip	FC51 	BIP 96.9	Dijon	03/10/2011
RCV 105.0	FC52 	RCV105FM	Dijon	17/12/2012
Radio Collège Pergaud	FC53 	R. C. P.	Dijon	16/12/2014
Radio Télévision Saône-et-Loire (RTS)	FC56 	RTSFPLUS	Dijon	19/05/2014
Radio Star	FC67 	STAR	Dijon	04/03/2008
Radio Amitié	FC81 	AMITIE	Dijon	04/03/2008
Radio Dijon Campus	FC82 	CAMPUS	Dijon	04/03/2008
Radio Cactus	FC83 	CACTUS	Dijon	04/03/2008
Radyonne FM	FC84 	RADYONNE	Dijon	04/03/2008
Radio Morvan	FC85 	R.MORVAN	Dijon	04/03/2008
Radio Shalom Dijon	FC86 	SHALOM	Dijon	04/03/2008
VTI	FC87 	V.T.I	Dijon	04/03/2008
Tonic FM	FC88 	TONIC FM	Dijon	04/03/2008
RVM	FC89 	RVM FM	Dijon	04/03/2008
Radio Prévert	FC90 	PREVERT	Dijon	04/03/2008
Aléo	FC91 	ALEO	Dijon	04/03/2008
Radio Avallon	FC92 	AVALLON	Dijon	04/03/2008
Radio Swing	FC93 	R.SWING	Dijon	04/03/2008
Radio Cultures Dijon	FC94 	CULTURES	Dijon	04/03/2008
Radio K6 FM	FC95 	K6FM	Dijon	04/03/2008
Plein C?ur	FC96 	PL_C?UR	Dijon	04/03/2008
Vintage	FC97 	VINTAGE	Dijon	04/03/2008
Azur FM	FC99 	AZUR FM	Dijon	04/03/2008
Club Altitude	FC9A 	CLUB ALT	Dijon	06/11/2008
Auxois FM	FCA3 	AUXOISFM	Dijon	07/06/2010
Radio Vallée Vézère	FD30 	R.V.V.	Bordeaux	04/03/2008
Xiberoko Botza	FD31 	X. BOTZA	Bordeaux	06/11/2008
RCF Charente	FD32 	RCF16	Bordeaux	10/03/2016
Radio Vallée d'Isle (RVI)	FD33 	RVI	Bordeaux	12/04/2017
Wit FM	FD34 	WIT FM	Bordeaux	04/03/2008
Hélène FM	FD37 	HELENEFM	Bordeaux	04/03/2008
MIXX	FD38 	MIXX FM	Bordeaux	11/04/2018
Radio Bonne Nouvelle	FD41 	R B N	Bordeaux	04/03/2008
Radio MDM	FD42 	MDM	Bordeaux	04/03/2008
Isabelle FM	FD43 	ISA FM	Bordeaux	04/03/2008
ARL	FD44 	ARL FM	Bordeaux	04/03/2008
Radio Blackbox	FD45 	BLACKBOX	Bordeaux	04/03/2008
Gure Irratia	FD46 	GURE IR	Bordeaux	04/03/2008
Orion 87,6 La Voix de la Vallée	FD47 	ORION	Bordeaux	04/03/2008
Radio Lapurdi Irratia	FD48 	LAPURDI	Bordeaux	04/03/2008
Newest	FD49 	NEWWEST	Bordeaux	04/03/2008
Euro-Infos Pyrénées Métropole	FD53 	EUROINFO	Bordeaux	04/03/2008
VOGUE RADIO	FD54 	VOGUE	Bordeaux	15/10/2013
IRULEGIKO IRRATIA	FD55 	IRULEGI	Bordeaux	25/03/2014
Radios libres en Périgord	FD56 	RLP102.3	Bordeaux	30/01/2015
Côte Sud FM	FD57 	COTE SUD	Bordeaux	02/04/2015
Albret FM	FD58 	ALBRETFM	Bordeaux	11/10/2017
Attitude	FD59 	ATTITUDE	Bordeaux	14/01/2016
Radio Cap Ferret	FD5A 	RCFERRET	Bordeaux	08/09/2016
Radio Bassin Arcachon	FD5B 	RBA 90.4	Bordeaux	08/09/2016
Radio Dunes	FD5C 	R.DUNES	Bordeaux	08/09/2016
RIO	FD5D 	RIO	Bordeaux	24/05/2018
ARD RADIO	FD5E 	ARDRADIO	Bordeaux	20/06/2019
AQUA FM	FD81 	AQUA FM	Bordeaux	21/01/2014
Mélodie FM	FD82 	MELODIFM	Bordeaux	22/09/2009
Radio Collége	FD83 	COLLEGE	Bordeaux	04/03/2008
Radio Pau d'Ousse	FD84 	R.P.O.	Bordeaux	04/03/2008
Demoiselle FM	FD85 	DEMOISEL	Bordeaux	04/03/2008
Radio Cadence Musique	FD86 	RCM FM	Bordeaux	04/03/2008
Radio Sauvagine	FD87 	SAUVAG	Bordeaux	04/03/2008
Radio Télé des Graves	FD88 	TRG	Bordeaux	04/03/2008
Radio Star	FD89 	STAR FM	Bordeaux	04/03/2008
Radio Vallée Bergerac	FD90 	RVB	Bordeaux	04/03/2008
Radio 4 Cantons	FD91 	RADIO 4	Bordeaux	04/03/2008
Cristal FM	FD92 	CRISTAL	Bordeaux	04/03/2008
Radio Mendililia	FD93 	MENDILIA	Bordeaux	04/03/2008
Bergerac 95	FD94 	BERGERAC	Bordeaux	04/03/2008
La Voix de l'Armagnac	FD95 	V. D.A	Bordeaux	04/03/2008
Radio Oloron	FD96 	R.OLORON	Bordeaux	04/03/2008
Radio Iguanodon Gironde - RIG	FD97 	RIG	Bordeaux	04/03/2008
Radio Espoir	FD98 	ESPOIR	Bordeaux	04/03/2008
Radio La Clé des Ondes	FD99 	LA CLE	Bordeaux	04/03/2008
Terre Marine	FDA0 	T MARINE	Bordeaux	04/03/2008
Radio Bulle	FDA1 	BULLE	Bordeaux	04/03/2008
O2 Radio	FDA2 	O2RADIO	Bordeaux	04/03/2008
Castel FM	FDA3 	CFMRADIO	Bordeaux	14/02/2012
VDB Fréquence Béarn	FDA4 	VOIXBEAR	Bordeaux	04/03/2008
Radio Liberté	FDA5 	RLIBERTE	Bordeaux	04/03/2008
Aqui FM	FDA7 	AQUI FM	Bordeaux	04/03/2008
Plage FM	FDA8 	PLAGE FM	Bordeaux	26/02/2013
Radio Campus	FDA9 	CAMPUS	Bordeaux	04/03/2008
Radio Pons	FDB0 	R. PONS	Bordeaux	04/03/2008
Radio Entre Deux Mers	FDB1 	R.E.M.	Bordeaux	04/03/2008
ZOOM RADIO	FDB2 	ZOOM	Bordeaux	15/10/2013
Souvenirs FM	FDB3 	SOUVENIR	Bordeaux	04/03/2008
Inside	FDB4 	INSIDE	Bordeaux	04/03/2008
NA RADIO	FDB5 	NA RADIO	Bordeaux	24/05/2018
47 FM	FDB6 	47 FM	Bordeaux	04/03/2008
RDC	FDB7 	R.D.C.	Bordeaux	04/03/2008
Gold FM	FDB8 	GOLD FM	Bordeaux	04/03/2008
Radio Bonne Humeur	FDB9 	R.B.H.	Bordeaux	04/03/2008
Positif Radio	FDC1 	POSITIF	Bordeaux	02/03/2010
Fréquence Grands Lacs	FDF8 	F G L	Bordeaux	04/03/2008
Radio Périgueux 103	FDFA 	RADIO103	Bordeaux	27/05/2008
Saint-Pierre-et-Miquelon 1ère	FE02 	SPM 1ERE	Paris	06/09/2017
Guadeloupe 1ère	FE03 	MAR 1ERE	Antilles - Guyane	06/09/2017
Martinique 1ère	FE04 	MAR 1ERE	Antilles - Guyane	06/09/2017
Guyane 1ère	FE05 	GUY 1ERE	Antilles - Guyane	06/09/2017
Mayotte 1ère	FE06 	MAY 1ERE	La Réunion - Mayotte	06/09/2017
Réunion 1ère	FE07 	REU 1ERE	La Réunion - Mayotte	06/09/2017
Wallis-et-Futuna 1ère	FE08 	WAL 1ERE	Nouvelle-Calédonie et Wallis-et-Futuna	06/09/2017
Nouvelle-Calédonie 1ère	FE09 	NC 1ERE	Nouvelle-Calédonie et Wallis-et-Futuna	06/09/2017
Polynésie 1ère	FE0A 	POLY 1ERE	Polynésie française	06/09/2017
Radio Saint-Martin	FE10 	RADIOSXM	Antilles - Guyane	04/03/2008
RFI	FE10 	RFI	Radio France	04/03/2008
NRJ Nouvelle-Calédonie	FE11 	NRJ	Nouvelle Calédonie	04/03/2008
Radio Saint-Barth FM	FE11 	RSB FM	Antilles - Guyane	04/03/2008
Radio 2000	FE30 	R2000	Antilles - Guyane	04/03/2008
Radio Free Dom	FE31 	FREEDOM	La Réunion - Mayotte	04/03/2008
Ici et Maintenant	FE31 	ICI & MT	Paris	04/03/2008
Radio Mosaïque	FE31 	MOSAIQUE	Antilles - Guyane	04/03/2008
Radio Néo	FE31 	NEO	Paris	03/02/2009
NRJ Polynésie	FE31 	NRJ	Polynésie	04/03/2008
Fréquence Protestante	FE32 	F.PROTES	Paris	04/03/2008
Radio Kalimé	FE32 	KALIME	La Réunion - Mayotte	04/03/2008
Radio Notre Dame	FE32 	N. DAME	Paris	04/03/2008
Radio Tiare	FE32 	TIARE FM	Polynésie	04/03/2008
Vinyle Radio	FE32 	VINYLE	Antilles - Guyane	04/03/2008
ELLES FM	FE33 	ELLES FM	Paris	15/12/2009
Radio Rythme Bleu	FE33 	R R B	Nouvelle Calédonie	04/03/2008
Radio 1	FE33 	RADIO 1	Polynésie	04/03/2008
Radio Voix dans le Désert	FE33 	RVLD	Antilles - Guyane	04/03/2008
Sky Réunion	FE33 	SKY FM	La Réunion - Mayotte	24/06/2013
Radio Arc-en-Ciel	FE34 	ARC CIEL	La Réunion - Mayotte	04/03/2008
Radio Bleue	FE34 	BLEUE	Polynésie	04/03/2008
Radio Djiido	FE34 	DJIIDO	Nouvelle Calédonie	04/03/2008
Tropiques FM	FE34 	TROPIQUE	Paris	04/03/2008
Radio 102 FM	FE35 	102 FM	La Réunion - Mayotte	04/03/2008
Radio Evasion	FE35 	EVASION	Paris	04/03/2008
Radio Kikiwi	FE35 	KFM 91.6	Antilles - Guyane	04/03/2008
Radio Maohi	FE35 	MAOHI	Polynésie	04/03/2008
NRJ Guyane	FE36 	N R J	Antilles - Guyane	04/03/2008
Radio Plus FM	FE36 	PLUS FM	La Réunion - Mayotte	04/03/2008
Radio Te Reo o Tefana	FE36 	TEFANA	Polynésie	04/03/2008
Radio La Voix de l'Espérance	FE37 	L V D L	Polynésie	04/03/2008
Toucan Fréquence International - TFI	FE37 	T.F.I.	Antilles - Guyane	04/03/2008
Métis FM	FE38 	METIS FM	Antilles - Guyane	04/03/2008
Radio Star	FE38 	STAR FM	Polynésie	04/03/2008
Radio Star	FE39 	STAR	La Réunion - Mayotte	04/03/2008
Radio Média Tropique	FE39 	METROPIQ	Antilles - Guyane	04/03/2008
Radio Te Vevo	FE39 	RTV	Polynésie	04/03/2008
TAUI FM	FE3A 	TAUI FM	Polynésie	03/02/2009
Rires et Chansons Tahiti	FE3B 	RIRE&CH	Polynésie	24/07/2013
Radio Bora Bora	FE40 	BORA	Polynésie	04/03/2008
Ouest FM (Guyane)	FE40 	OUEST FM	Antilles - Guyane	04/03/2008
Radio des Iles	FE40 	R.I.L.	La Réunion - Mayotte	04/03/2008
Espace FM	FE41 	ESPACE	Paris	04/03/2008
Radio Sud Plus	FE41 	SUD PLUS	La Réunion - Mayotte	04/03/2008
Fugue FM programme Contact FM	FE42 	CONTACT	Paris	04/03/2008
NRJ Réunion	FE42 	NRJ	La Réunion - Mayotte	04/03/2008
Chante France	FE43 	CHANTE F	Paris	04/03/2008
Exo FM	FE43 	EXO FM	La Réunion - Mayotte	04/03/2008
Radio Salazes	FE44 	SALAZES	La Réunion - Mayotte	04/03/2008
First Radio	FE45 	FIRST	La Réunion - Mayotte	04/03/2008
Voltage FM	FE45 	VOLTAGE	Paris	04/03/2008
Aligre FM	FE46 	ALIGRE	Paris	04/03/2008
Radio Pays	FE46 	PAYS	Paris	04/03/2008
RFM	FE46 	RFM	La Réunion - Mayotte	29/06/2012
Radio Est Réunion	FE47 	RER	La Réunion - Mayotte	04/03/2008
Radio Festival	FE48 	FESTIVAL	La Réunion - Mayotte	04/03/2008
Radio Vieille Eglise	FE48 	R V E	Paris	04/03/2008
Radio Plainoise FM	FE49 	104 F M	La Réunion - Mayotte	04/03/2008
Générations	FE50 	GENE88.2	Paris	04/03/2008
Radio Kanal Océan Indien	FE50 	K O I	La Réunion - Mayotte	04/03/2008
Radio 100% Jazz	FE51 	100% Jazz	La Réunion - Mayotte	09/06/2009
Radio Marquises	FE51 	MARQUISE	Polynésie	24/07/2013
Radio Sun FM Music	FE51 	SUN FM	Antilles - Guyane	02/06/2010
Caribou FM	FE52 	Caribou	La Réunion - Mayotte	09/06/2009
Radio Enghien	FE52 	ENGHIEN	Paris	04/03/2008
Radio Hiti FM	FE52 	HITI FM	Polynésie française	25/10/2017
Radio Cosmique One	FE52 	R.C.O.	Antilles - Guyane	02/06/2010
MBS Music Box Stéréo	FE53 	MUSICBOX	Paris	04/03/2008
Radio Mission Pionnière	FE53 	R.M.P.	Antilles - Guyane	02/06/2010
Antenne Réunion Radio	FE55 	ANTENNE	La Réunion - Mayotte	28/10/2011
Radio Puisaleine	FE55 	PUISALEI	Paris	04/03/2008
Azot Radio	FE56 	A Z O T	La Réunion - Mayotte	28/10/2011
Horizon FM	FE56 	HORIZON	Paris	12/12/2011
Radio Saint Gabriel	FE56 	SGABRIEL	Antilles - Guyane	12/10/2011
Capital FM	FE57 	CAPITAL	La Réunion - Mayotte	28/10/2011
Oxygène	FE57 	OXYGENE	Paris	04/03/2008
Radio Bonne Nouvelle de Guyane	FE57 	R.B.N.G	Antilles - Guyane	12/10/2011
CHIC FM	FE58 	CHIC FM	La Réunion - Mayotte	28/10/2011
MEGA FM	FE58 	MEGA FM	Antilles - Guyane	28/05/2013
Radio Valois Multien RVM	FE58 	RVM 93.7	Paris	04/03/2008
Radio AYP	FE59 	AYP FM	Paris	04/03/2008
Entre-deux FM	FE59 	ENTRE2FM	La Réunion - Mayotte	28/10/2011
France Maghreb	FE59 	FMAGHREB	Paris	04/03/2008
Radio KARATA	FE59 	KARATA	Antilles - Guyane	28/05/2013
EvryOne	FE5A 	EVRYONE	Paris	22/09/2009
Free Dom 2	FE5A 	FREEDOM2	La Réunion - Mayotte	28/10/2011
Radio Massabielle	FE5A 	R.MASSAB	Antilles - Guyane	28/05/2013
Fun Radio	FE5B 	FUN	La Réunion - Mayotte	28/10/2011
NRB (Nouvelle Radio Berbère)	FE5B 	NRB	Paris	18/09/2013
Graph'hit	FE5C 	Graph'hit	Paris	22/09/2009
LFM Réunion	FE5C 	LFM	La Réunion - Mayotte	28/10/2011
Radio Musiques Informations Guyanaises (MIG)	FE5C 	MIG FM	Antilles - Guyane	19/06/2014
Lo Rénioné	FE5D 	RENIONE	La Réunion - Mayotte	28/10/2011
Viv'FM	FE5D 	Viv'FM	Paris	20/05/2019
Radio Libertaire	FE5E 	RL.89.4	Paris	13/09/2011
Trace FM	FE5E 	TRACE FM	La Réunion - Mayotte	17/08/2016
Radio Rossignol	FE5F 	RSSIGNOL	Antilles - Guyane	03/02/2015
RTL 2	FE5F 	RTL 2	La Réunion - Mayotte	28/10/2011
CLASSICA	FE60 	CLASSICA	Antilles - Guyane	03/02/2015
Zinfosradio	FE60 	Zinfos	La Réunion - Mayotte	28/10/2011
Radio Kontak	FE61 	KONTAK	La Réunion - Mayotte	20/02/2012
Mayouri FM	FE61 	MAYOURI	Antilles - Guyane	03/02/2015
Radio Peyi Guyane	FE62 	PEYI	Antilles - Guyane	03/02/2015
Radio Terre Blanche FM	FE62 	RTB FM	La Réunion - Mayotte	24/03/2014
Radio GAIAC	FE63 	GAIAC FM	Antilles - Guyane	03/02/2015
Kwezi FM	FE63 	KWEZI FM	La Réunion - Mayotte	13/10/2014
Radio Kon Yere	FE64 	KON YERE	Antilles - Guyane	03/02/2015
RDJ Mayotte	FE64 	RDJ976	La Réunion - Mayotte	17/04/2019
Radio Mawoua	FE65 	MAWOUA	La Réunion - Mayotte	24/02/2016
Radio Voix du Fleuve Maroni	FE65 	RVFM	Antilles - Guyane	03/02/2015
Chiconi FM	FE66 	CHICONI	La Réunion - Mayotte	06/04/2017
Radio Tour de l'Isle	FE66 	R-T-I	Antilles - Guyane	21/04/2015
Nostalgie Guyane	FE67 	NOSTALGI	Antilles - Guyane	21/04/2015
Nostalgie Martinique	FE67 	NOSTALGI	Antilles - Guyane	21/04/2015
Nostalgie Guadeloupe	FE67 	NOSTALGI	Antilles - Guyane	21/04/2015
Radio PAROLE	FE67 	RP	La Réunion - Mayotte	06/04/2017
CHERIE Guadeloupe	FE68 	CHERIE	Antilles - Guyane	14/09/2017
CHERIE Guyane	FE68 	CHERIE	Antilles - Guyane	14/09/2017
CHERIE Martinique	FE68 	CHERIE	Antilles - Guyane	14/09/2017
RDJ Réunion	FE68 	RDJ	La Réunion - Mayotte	17/04/2019
RMV	FE69 	RMV	La Réunion - Mayotte	01/08/2017
Mayotte One la Radio	FE6A 	MayotOne	La Réunion - Mayotte	01/08/2017
ANTEOU FM	FE6B 	ANTEOU FM	La Réunion - Mayotte	29/11/2017
Jobs et Musik Antilles	FE6C 	JOBS&MUS	Antilles - Guyane	12/12/2018
TROPIC FM	FE6C 	TROPICFM	La Réunion - Mayotte	10/01/2018
Chante FM	FE6D 	CHANTEFM	La Réunion - Mayotte	22/08/2018
Radio Casilindo	FE6D 	KSILINDO	Antilles - Guyane	12/12/2018
Bleu FM	FE6E 	BLEU FM	La Réunion - Mayotte	06/02/2019
Radio Kourou Savanes	FE6E 	R.K.S	Antilles - Guyane	12/01/2019
ZOUK’ NEWS	FE79 	ZOUKNEWZ	Antilles - Guyane	28/05/2013
C10 FM	FE7A 	C10 FM	Antilles - Guyane	07/11/2017
FMC Radio	FE80 	F.M.C.	Paris	04/03/2008
RCI Martinique	FE80 	R C I	Antilles - Guyane	03/02/2009
RCI Guadeloupe	FE80 	RCI	Antilles - Guyane	03/02/2009
Radio Zirondel FM	FE80 	RZFM	La Réunion - Mayotte	04/03/2008
Radio Fréquence Sud	FE81 	FRE-SUD	La Réunion - Mayotte	04/03/2008
NRJ Guadeloupe	FE81 	NRJ	Antilles - Guyane	03/10/2013
NRJ Martinique	FE81 	NRJ	Antilles - Guyane	03/10/2013
Radio Vexin Val-de-Seine	FE81 	RVVS	Paris	22/09/2009
Radio Kréol FM	FE82 	KREOL FM	La Réunion - Mayotte	04/03/2008
RADIO LOVELY	FE82 	LOVELY	Paris	20/05/2019
Zouk Radio	FE82 	ZOUK	Antilles - Guyane	04/03/2008
Trace FM	FE83 	TRACE FM	Antilles - Guyane	04/03/2008
Vallée FM Radio Marne-la-Vallée	FE83 	VALLEE	Paris	04/03/2008
Radio Velly Music	FE83 	VELLY	La Réunion - Mayotte	04/03/2008
Handi FM	FE84 	HANDI FM	Paris	04/03/2008
HIT FM	FE84 	HIT.FM.	La Réunion - Mayotte	04/03/2008
Radio Basses Internationale (R.B.I.)	FE84 	R B I	Antilles - Guyane	04/03/2008
Chérie FM	FE85 	CHERIE	La Réunion - Mayotte	04/03/2008
Madras FM (M.F.M.)	FE85 	M F M	Antilles - Guyane	04/03/2008
Sensation	FE86 	SENSA	Paris	22/09/2009
Radio Top FM	FE86 	TOP FM	La Réunion - Mayotte	04/03/2008
Digital FM	FE87 	DIGITAL	La Réunion - Mayotte	04/03/2008
Maxi FM	FE87 	MAXXI	Antilles - Guyane	04/03/2008
Radio Mercure	FE87 	MERCURE	Paris	04/03/2008
Radio Vie	FE88 	VIE	La Réunion - Mayotte	04/03/2008
Radio Balisier	FE89 	BALISIER	Antilles - Guyane	04/03/2008
Only Raï	FE89 	ONLY RAï	Paris	04/03/2008
Radio Soleil	FE89 	SOLEIL	La Réunion - Mayotte	04/03/2008
Radio Banlieue Relax (RBR)	FE90 	R B R	Antilles - Guyane	04/03/2008
Radio Mixte 9	FE90 	R M 9	La Réunion - Mayotte	04/03/2008
Radio Plus	FE90 	R PLUS	Paris	04/03/2008
Marmite FM	FE91 	MARMITE	Paris	04/03/2008
Radio Jeunesse Lumière	FE91 	RJL	La Réunion - Mayotte	04/03/2008
Yvelines Radio	FE91 	YVELINES	Paris	04/03/2008
Radio Ase Plere A Nou Lite	FE92 	APAL	Antilles - Guyane	04/03/2008
Fréquence Oasis	FE92 	FR.OASIS	La Réunion - Mayotte	04/03/2008
Radio Ginglet la Boucle	FE92 	RGB 99.2	Paris	04/03/2008
Africa n° 1	FE93 	AFRICA 1	National	04/03/2008
EXO FM Mayotte	FE93 	EXO FM	La Réunion - Mayotte	30/03/2016
Radio Inter Tropicale	FE93 	TROPICAL	Antilles - Guyane	04/03/2008
Radio Case Infos	FE94 	CASEINFO	La Réunion - Mayotte	04/03/2008
Radio Eclair	FE94 	ECLAIR F	Antilles - Guyane	04/03/2008
77 FM	FE95 	77FM	Paris	04/03/2008
Radio Actif Martinique	FE95 	ACTIF	Antilles - Guyane	04/03/2008
Radio Sun'Lazes	FE95 	SUNLAZES	La Réunion - Mayotte	04/03/2008
Radio Mille Pattes	FE96 	MIL'PAT'	Paris	04/03/2008
Radio Pikan	FE96 	PIKAN	La Réunion - Mayotte	04/03/2008
Atlantic FM	FE96 	RMC 95.1	Antilles - Guyane	04/03/2008
Radio Campus FM	FE97 	CAMPUS	Antilles - Guyane	04/03/2008
Radio Dziani	FE97 	DZIANI	La Réunion - Mayotte	04/03/2008
Mangembo FM	FE97 	MANGEMBO	Paris	04/03/2008
Radio Capucins	FE98 	CAPUCINS	Paris	04/03/2008
Yao FM	FE98 	YAO FM	La Réunion - Mayotte	04/03/2008
BPM	FE99 	B-P-M	Paris	04/03/2008
Radio Musique Infos Mayotte (MIM)	FE99 	MIM.E1	La Réunion - Mayotte	04/03/2008
ZOUK FM Martinique	FE99 	ZOUK FM	Antilles - Guyane	28/05/2013
Radio Décibel	FEA0 	DECIBEL	La Réunion - Mayotte	04/03/2008
Radio Haute Tension	FEA0 	RHT 89.8	Antilles - Guyane	04/03/2008
Radio Alizés FM	FEA1 	ALIZE FM	Antilles - Guyane	04/03/2008
Radio Série One	FEA1 	SERIE 1	La Réunion - Mayotte	04/03/2008
Radio Saphir FM	FEA2 	SAPHIR	Antilles - Guyane	04/03/2008
Radio Néo	FEA2 	NEO-FM	La Réunion - Mayotte	04/03/2008
Radio Saint-Louis	FEA3 	RS LOUIS	Antilles - Guyane	04/03/2008
Radio Sun Light FM	FEA3 	SUN FM	La Réunion - Mayotte	04/03/2008
Vivre FM	FEA3 	VIVRE FM	Paris	06/11/2008
Radio Campus Paris	FEA4 	CAMPUS	Paris	06/11/2008
Radio Mayotte	FEA4 	MAYOT-FM	La Réunion - Mayotte	04/03/2008
Radio Evangélique de la Martinique	FEA4 	R E M	Antilles - Guyane	04/03/2008
Radio La Voix du Nord	FEA5 	RVN-FM	La Réunion - Mayotte	04/03/2008
Radio Sud-Est	FEA5 	SUD-EST	Antilles - Guyane	04/03/2008
Super Radio	FEA6 	C'SUPER	Antilles - Guyane	11/04/2018
Radio Carrefour	FEA6 	CARFOUR	La Réunion - Mayotte	04/03/2008
Radio Espoir	FEA7 	FMESPOIR	Antilles - Guyane	04/03/2008
Radio L.G.B.	FEA7 	LGB 91.9	La Réunion - Mayotte	04/03/2008
Chérie FM	FEA8 	CHERIEFM	Antilles - Guyane	04/03/2008
Radio Vie Meilleure (RVM)	FEA8 	RVM-93,3	Antilles - Guyane	04/03/2008
Radio Zantak	FEA8 	ZANTAK	La Réunion - Mayotte	04/03/2008
Kayanm FM	FEA9 	KAYANMFM	La Réunion - Mayotte	04/03/2008
Radio Souffle de Vie	FEA9 	R.S.V	Antilles - Guyane	04/03/2008
Radio Leve Doubout Matinik (RLDM)	FEB0 	R.L.D.M	Antilles - Guyane	04/03/2008
Radio Inter S'cool	FEB0 	RIS	Antilles - Guyane	04/03/2008
Radio Espérance	FEB1 	SPERANCE	Antilles - Guyane	04/03/2008
Radio Imagine	FEB3 	IMAGINE	Antilles - Guyane	04/03/2008
Radio Fréquence Caraibe	FEB4 	R.F.C	Antilles - Guyane	04/03/2008
Radio As	FEB5 	AS	Antilles - Guyane	04/03/2008
Radio 22	FEB6 	RADIO-22	Antilles - Guyane	04/03/2008
Radio Côte sous le vent (RCV)	FEB7 	R.C.V.	Antilles - Guyane	04/03/2008
Radio Arago	FEB8 	A*F*M	Antilles - Guyane	04/03/2008
Radio Média Tropical Guadeloupe	FEB9 	TROPICAL	Antilles - Guyane	04/03/2008
Radio Gaiac	FEC0 	GAYAK-FM	Antilles - Guyane	04/03/2008
Radio Fréquence Atlantique (RFA)	FEC1 	*R.F.A*	Antilles - Guyane	04/03/2008
Climax FM	FEC2 	CLIMAX	Antilles - Guyane	04/03/2008
Radio Contact	FEC3 	CONTACT	Antilles - Guyane	04/03/2008
Radio Transat	FEC4 	TRANSAT	Antilles - Guyane	04/03/2008
Radio Liberté	FEC5 	LIBERTE	Antilles - Guyane	04/03/2008
Kilti FM	FEC6 	KILTI FM	Antilles - Guyane	04/03/2008
Horizon FM +	FEC7 	FM PLUS	Antilles - Guyane	04/03/2008
Radio Tanbou	FEC8 	TANBOU	Antilles - Guyane	04/03/2008
Radio Tout'Moune	FEC9 	TOUTMOUN	Antilles - Guyane	04/03/2008
Radio Mouv'Matnik	FECA 	MOUV' M	Antilles - Guyane	22/09/2009
Nature Space Radio FM	FECB 	NATURE	Antilles - Guyane	22/09/2009
Fréquences Alizés Europe 3	FECC 	EUROPE 3	Antilles - Guyane	22/09/2009
Ouest FM (Guadeloupe)	FECD 	OUEST FM	Antilles - Guyane	22/09/2009
Radio Loisirs Guyane	FECE 	LOISIR FM	Antilles - Guyane	22/09/2009
Bel'Radio Guadeloupe	FECF 	BELRADIO	Antilles - Guyane	03/10/2013
Bel'Radio Martinique	FECF 	BELRADIO	Antilles - Guyane	03/10/2013
Radio Ouassailles	FED0 	R.O.M.	Antilles - Guyane	04/03/2008
Radio Sofaïa Atitude	FED1 	RSA	Antilles - Guyane	04/03/2008
Fun Radio Guyane	FED2 	FUN	Antilles - Guyane	06/07/2010
Radio Pays d'Aurillac	FF35 	RPA107,4	Clermont-Ferrand	06/11/2008
Radio Altitude	FF36 	ALTITUDE	Clermont-Ferrand	04/03/2008
Radio Bort Artense	FF37 	RBA FM	Clermont-Ferrand	04/03/2008
Radio Grand Brive (RGB)	FF38 	RGB 94.3	Clermont-Ferrand	26/03/2012
Bréniges FM	FF39 	BRENIGES	Clermont-Ferrand	04/03/2008
Emergence FM	FF3A 	EMERGENC	Clermont-Ferrand	04/03/2008
Radio Pays de Guéret	FF3B 	R.P.G.	Clermont-Ferrand	04/03/2008
Bram'FM	FF3C 	BRAM FM	Clermont-Ferrand	04/03/2008
Plein Cœur Auvergne	FF3D 	PL_COEUR	Clermont-Ferrand	24/09/2018
Radio Trouble Fête	FF40 	RTF 95.4	Clermont-Ferrand	04/03/2008
Beaub'FM	FF41 	BEAUB'FM	Clermont-Ferrand	04/03/2008
Radio Campus	FF42 	R CAMPUS	Clermont-Ferrand	04/03/2008
Swing FM	FF43 	SWING FM	Clermont-Ferrand	04/03/2008
Radio Logos	FF44 	LOGOS FM	Clermont-Ferrand	04/03/2008
Fusion FM	FF45 	FUSION	Clermont-Ferrand	04/03/2008
Radio des Meilleurs Jours	FF46 	RMJ	Clermont-Ferrand	04/03/2008
Radio Vassivière	FF47 	R VASSIV	Clermont-Ferrand	04/03/2008
Radio Arverne	FF48 	ARVERNE	Clermont-Ferrand	04/03/2008
Kaolin FM	FF49 	KAOLIN	Clermont-Ferrand	04/03/2008
Variance FM	FF4A 	VARIANCE	Clermont-Ferrand	15/12/2009
RMB	FF52 	RMB	Clermont-Ferrand	04/03/2008
RVA	FF53 	RVA	Clermont-Ferrand	04/03/2008
FM 43	FF54 	FM43	Clermont-Ferrand	26/03/2012
Cosmic FM	FF5A 	COSMICFM	Clermont-Ferrand	22/09/2009
Jordanne FM	FF63 	JORDANNE	Clermont-Ferrand	04/03/2008
Radio Open FM	FF70 	OPEN FM	Clermont-Ferrand	16/09/2013
Radio Bocage	FF80 	BOCAGE	Clermont-Ferrand	04/03/2008
Radio PAC	FF81 	PAC101.9	Clermont-Ferrand	04/03/2008
Radio Craponne	FF82 	CRAPONNE	Clermont-Ferrand	04/03/2008
Magic FM	FF84 	MAGIC FM	Clermont-Ferrand	04/03/2008
FLASH FM	FF85 	FLASH FM	Clermont-Ferrand	00/00/0000
Radio Tartasse	FF86 	TARTASSE	Clermont-Ferrand	04/03/2008
Radio Qui Q'en Grogne	FF87 	RQQG101	Clermont-Ferrand	04/03/2008
RJFM	FF88 	RJFM	Clermont-Ferrand	04/03/2008
Radio Coquelicot	FF89 	COCLICOT	Clermont-Ferrand	04/03/2008
Radio Vicomté	FF8A 	VICOMTE	Clermont-Ferrand	10/05/2010"""

lines = codes.split("\n")
print("%s lines"%(len(lines)))

PI = {}
for l in lines:
    item = l.split(":")
    PI[item[0].strip()]=("%s"%item[1])

lines = CSA.split("\n")
print("%s lines"%(len(lines)))

for l in lines:
    item = l.split("\t")
    PI[item[1].strip()]=("%s"%item[0])

fid = open("./myRdsPiCodes.py","w")
fid.write("""#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - sam. août 17:09 2019
#   - Initial Version 1.0
#   - the info comes from https://people.uta.fi/~jk54415/dx/pi-codes.html
#  =================================================

class piCodes(object):
    \"\"\"RDS PI codes from:
    - https://people.uta.fi/~jk54415/dx/pi-codes.html 
    - https://www.csa.fr/maradiofm/radiords_tableau
    \"\"\"
    def __init__(self):
        self.init()
        
    ## --------------------------------------------------------------
    ## Description : get station name
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 24-29-2019 17:29:31
    ## --------------------------------------------------------------
    def getStation (self,key):
        key = key.upper()
        print("looking for %s"%key)
        if key in self.PI:
            return self.PI[key][0]
        else:
            return "Unknown"

    ## --------------------------------------------------------------
    ## Description : define stations
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 24-29-2019 17:29:31
    ## --------------------------------------------------------------
    def init (self):
        self.PI={\n""")

for i in PI:
    fid.write("            \"%s\":[\"%s\"],\n"%(i,PI[i]))

fid.write("        }\n\n")

fid.write("""
""")
fid.close()

