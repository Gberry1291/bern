from django.core.management.base import BaseCommand
from django.db import transaction
from core.models import Provider, LivingOption
from django.conf import settings

DEMO_PREFIX = "DEMO — "


def set_translation(obj, lang, title, description):
    """
    Safe Parler translation write:
    - Sets current language
    - Assigns translated fields
    - Saves
    """
    obj.set_current_language(lang)
    obj.title = title
    obj.description = description
    obj.save()


DEMO_PROVIDERS = [
    {"name": f"{DEMO_PREFIX}Stiftung Aare Wohnen", "canton": "BE", "verified": True, "supported_languages": ["de", "en"]},
    {"name": f"{DEMO_PREFIX}Basel SignalHaus", "canton": "BS", "verified": True, "supported_languages": ["de", "en"]},
    {"name": f"{DEMO_PREFIX}Maison Rive Gauche", "canton": "GE", "verified": True, "supported_languages": ["fr", "en"]},
    {"name": f"{DEMO_PREFIX}Casa Ticino Supporto", "canton": "TI", "verified": True, "supported_languages": ["it", "en"]},
    {"name": f"{DEMO_PREFIX}NeuroWohnen Zürich", "canton": "ZH", "verified": True, "supported_languages": ["de", "en"]},
    {"name": f"{DEMO_PREFIX}KinderWohnen Luzern", "canton": "LU", "verified": True, "supported_languages": ["de"]},
    {"name": f"{DEMO_PREFIX}Fribourg PontLangues", "canton": "FR", "verified": True, "supported_languages": ["de", "fr"]},
    {"name": f"{DEMO_PREFIX}RecoveryHaus Zürich", "canton": "ZH", "verified": True, "supported_languages": ["de", "en"]},
    {"name": f"{DEMO_PREFIX}MemoryGarden Bern", "canton": "BE", "verified": True, "supported_languages": ["de", "en"]},
    {"name": f"{DEMO_PREFIX}Résidence Mémoire Lausanne", "canton": "VD", "verified": True, "supported_languages": ["fr"]},
    {"name": f"{DEMO_PREFIX}Autismus Wohnen Winterthur", "canton": "ZH", "verified": True, "supported_languages": ["de"]},
    {"name": f"{DEMO_PREFIX}Zug DualSupport Living", "canton": "ZG", "verified": True, "supported_languages": ["de", "en"]},
    {"name": f"{DEMO_PREFIX}WerkWohnen Aarau", "canton": "AG", "verified": True, "supported_languages": ["de", "en"]},
    {"name": f"{DEMO_PREFIX}Pflegehaus Alpenblick", "canton": "BE", "verified": True, "supported_languages": ["de"]},
    {"name": f"{DEMO_PREFIX}Rheinfelden Ruhe & Struktur", "canton": "AG", "verified": True, "supported_languages": ["de", "en"]},
]


# 60 curated listings
DEMO_LISTINGS = [
    # 01 DE-only
    dict(provider=f"{DEMO_PREFIX}Stiftung Aare Wohnen", languages_supported=["de"], care_level=2, cognitive=1,
         wheelchair=False, hearing=False, visual=False,
         tr=dict(de=dict(
             title="Bern Wohntraining (18–25) — Selbstständigkeit & Coaching #01",
             description="Betreutes Wohntraining für junge Erwachsene (18–25) mit leichtem Unterstützungsbedarf. Fokus: Alltag strukturieren, Budget/Behörden, Ausbildung/Job-Coaching. Reizarme Umgebung, planbare Check-ins. Keine medizinische Pflege."
         ))),

    # 02 EN-only (hearing)
    dict(provider=f"{DEMO_PREFIX}Basel SignalHaus", languages_supported=["en"], care_level=1, cognitive=0,
         wheelchair=True, hearing=True, visual=False,
         tr=dict(en=dict(
             title="Basel Deaf-Friendly Studio — Visual Alerts & Clear Communication #02",
             description="Studio with visual doorbell/fire alerts and staff trained in clear written communication. Optional sign-support appointments. Calm environment for Deaf or hard-of-hearing residents seeking independence with light support."
         ))),

    # 03 FR-only (Parkinson)
    dict(provider=f"{DEMO_PREFIX}Maison Rive Gauche", languages_supported=["fr"], care_level=3, cognitive=1,
         wheelchair=False, hearing=False, visual=False,
         tr=dict(fr=dict(
             title="Genève — Logement avec accompagnement (Parkinson) mobilité & routines #03",
             description="Appartement accompagné pour personnes avec Parkinson: routines stables, aide à l’organisation, prévention des chutes, et supervision légère. Personnel présent en journée, environnement calme."
         ))),

    # 04 IT-only (60+ light)
    dict(provider=f"{DEMO_PREFIX}Casa Ticino Supporto", languages_supported=["it"], care_level=2, cognitive=1,
         wheelchair=True, hearing=False, visual=False,
         tr=dict(it=dict(
             title="Lugano — Appartamento accessibile (60+) autonomia con supporto leggero #04",
             description="Appartamento per persone 60+ con autonomia parziale. Supporto per routine, spesa e organizzazione quotidiana. Spazi accessibili e bagno comodo. Non è assistenza medica intensiva."
         ))),

    # 05 DE+EN mental health
    dict(provider=f"{DEMO_PREFIX}Rheinfelden Ruhe & Struktur", languages_supported=["de","en"], care_level=2, cognitive=1,
         wheelchair=False, hearing=False, visual=False,
         tr=dict(
             de=dict(title="Zürich Ruhige Wohnung — Depression & Tagesstruktur #05",
                     description="Ruhiges Setting für Erwachsene mit Depression/Angst. Unterstützung bei Tagesstruktur, Terminen und Selbstfürsorge. Kein Klinikbetrieb: Fokus auf Stabilität, Privatsphäre und planbare Check-ins."),
             en=dict(title="Zurich Quiet Flat — Depression & Daily Structure #05",
                     description="Quiet setting for adults living with depression/anxiety. Support with routines, appointments, and self-care. Not an inpatient clinic—focus on stability, privacy, and predictable check-ins.")
         )),

    # 06 DE+EN low vision
    dict(provider=f"{DEMO_PREFIX}Stiftung Aare Wohnen", languages_supported=["de","en"], care_level=2, cognitive=0,
         wheelchair=True, hearing=False, visual=True,
         tr=dict(
             de=dict(title="St. Gallen Low-Vision Apartment — Orientierung & Kontrast #06",
                     description="Wohnung mit kontrastreichen Markierungen, klarer Wegführung und blendarmem Licht. Unterstützung bei Orientierung, Alltagshilfen und Sicherheitsroutinen. Ideal bei Sehbehinderung/Low Vision."),
             en=dict(title="St. Gallen Low-Vision Apartment — Orientation & Contrast #06",
                     description="High-contrast cues, clear navigation, and glare-reduced lighting. Support for orientation, daily living aids, and safety routines. Designed for low vision with optional light supervision.")
         )),

    # 07 DE-only autism teen+
    dict(provider=f"{DEMO_PREFIX}Autismus Wohnen Winterthur", languages_supported=["de"], care_level=3, cognitive=2,
         wheelchair=False, hearing=False, visual=False,
         tr=dict(de=dict(
             title="Winterthur Reizarme WG — Autismus (16+) Struktur & Rückzug #07",
             description="Reizarme WG für Autist:innen (ab 16). Klare Regeln, visuelle Tagespläne, ruhige Zimmer, sensorikfreundliche Beleuchtung. Unterstützung bei Alltag, sozialen Situationen und Behörden. Keine medizinische Pflege."
         ))),

    # 08 EN-only autism adults
    dict(provider=f"{DEMO_PREFIX}NeuroWohnen Zürich", languages_supported=["en"], care_level=3, cognitive=2,
         wheelchair=False, hearing=False, visual=False,
         tr=dict(en=dict(
             title="Zurich Sensory-Friendly Flat — Autism (18+) Visual Schedules #08",
             description="Sensory-friendly apartment for autistic adults. Visual schedules, predictable check-ins, executive-function support, and low-stimulation common areas. Best for moderate support needs."
         ))),

    # 09 DE-only aphasia/communication
    dict(provider=f"{DEMO_PREFIX}Basel SignalHaus", languages_supported=["de"], care_level=3, cognitive=2,
         wheelchair=True, hearing=False, visual=False,
         tr=dict(de=dict(
             title="Basel Aphasie-Unterstützung — Kommunikationshilfen & Geduld #09",
             description="Wohnangebot für Menschen mit Aphasie nach Schlaganfall. Unterstützte Kommunikation (Karten/Apps), geduldige Gesprächsführung und Alltagstraining. Regelmäßige Unterstützung, keine Intensivpflege."
         ))),

    # 10 EN-only memory support 65+
    dict(provider=f"{DEMO_PREFIX}MemoryGarden Bern", languages_supported=["en","de"], care_level=4, cognitive=3,
         wheelchair=True, hearing=False, visual=False,
         tr=dict(en=dict(
             title="Bern Memory-Support Residence (65+) — Structured Days & Safety #10",
             description="For older adults (65+) with moderate to severe memory impairment. Safe layout, gentle supervision, structured daytime routines, and support with daily tasks. Calm environment; staff present daily with on-call overnight."
         ))),

    # 11 FR-only dementia high
    dict(provider=f"{DEMO_PREFIX}Résidence Mémoire Lausanne", languages_supported=["fr"], care_level=5, cognitive=3,
         wheelchair=True, hearing=False, visual=False,
         tr=dict(fr=dict(
             title="Lausanne — Résidence mémoire (70+) sécurité & repères #11",
             description="Pour personnes 70+ avec troubles cognitifs modérés à sévères. Repères visuels, prévention de l’errance, activités adaptées. Personnel présent 24/7. Environnement rassurant et calme."
         ))),

    # 12 DE+EN paraplegia mobility
    dict(provider=f"{DEMO_PREFIX}Stiftung Aare Wohnen", languages_supported=["de","en"], care_level=2, cognitive=0,
         wheelchair=True, hearing=False, visual=False,
         tr=dict(
             de=dict(title="Bern Barrierefreie Wohnung — Paraplegie-optimiert #12",
                     description="Rollstuhlgängige Wohnung mit breiten Türen, unterfahrbarer Küche und barrierefreiem Bad. Fokus auf Autonomie bei Querschnitt. Optional Hilfe bei Haushalt/Organisation (keine 24/7 Pflege)."),
             en=dict(title="Bern Accessible Apartment — Optimized for Paraplegia #12",
                     description="Wheelchair-optimized apartment with wide doors, roll-under kitchen, and accessible bathroom. Focus on autonomy for spinal cord injury. Optional help with household/organization (not 24/7 nursing care).")
         )),

    # 13 DE-only recovery
    dict(provider=f"{DEMO_PREFIX}RecoveryHaus Zürich", languages_supported=["de","en"], care_level=3, cognitive=1,
         wheelchair=False, hearing=False, visual=False,
         tr=dict(de=dict(
             title="Zürich Übergangswohnen — Sucht-Rehabilitation & Stabilität #13",
             description="Strukturiertes Übergangswohnen nach Therapie. Nüchternes Umfeld, klare Regeln, Unterstützung bei Rückfallprävention, Terminen und Tagesstruktur. Gruppenangebote optional. Keine medizinische Akutversorgung."
         ))),

    # 14 IT-only recovery
    dict(provider=f"{DEMO_PREFIX}Casa Ticino Supporto", languages_supported=["it"], care_level=3, cognitive=1,
         wheelchair=False, hearing=False, visual=False,
         tr=dict(it=dict(
             title="Lugano — Alloggio di transizione per recupero dipendenze #14",
             description="Alloggio strutturato dopo trattamento per dipendenze. Regole chiare, sostegno per routine e prevenzione ricadute. Ambiente sobrio e tranquillo. Supporto regolare, non clinico."
         ))),

    # 15 DE-only teen stabilization
    dict(provider=f"{DEMO_PREFIX}Stiftung Aare Wohnen", languages_supported=["de"], care_level=4, cognitive=1,
         wheelchair=False, hearing=False, visual=False,
         tr=dict(de=dict(
             title="Thun Jugendwohnen (13–17) — Emotionale Stabilisierung #15",
             description="Kleines Setting für Jugendliche 13–17 mit Angst/Depression/Schulverweigerung. Strukturierter Alltag, Bezugspersonen, Unterstützung bei Schule/Lehre. Krisenplan vorhanden, kein geschlossenes Setting."
         ))),

    # 16 DE-only children developmental
    dict(provider=f"{DEMO_PREFIX}KinderWohnen Luzern", languages_supported=["de"], care_level=5, cognitive=2,
         wheelchair=True, hearing=False, visual=False,
         tr=dict(de=dict(
             title="Luzern Kinderwohnen (6–12) — Entwicklungsförderung & Alltag #16",
             description="Wohnangebot für Kinder 6–12 mit Entwicklungsverzögerungen oder ADHS/Autismus. Unterstützte Routinen, spielerische Förderung, enge Zusammenarbeit mit Schule/Therapien. 24/7 Betreuung."
         ))),

    # 17 DE-only infants respite
    dict(provider=f"{DEMO_PREFIX}KinderWohnen Luzern", languages_supported=["de","fr"], care_level=5, cognitive=3,
         wheelchair=True, hearing=False, visual=False,
         tr=dict(de=dict(
             title="Bern Kurzzeitplatz für Säuglinge (0–2) — Entlastung & 24/7 Aufsicht #17",
             description="Kurzzeitbetreuung für Säuglinge 0–2 mit erhöhtem Betreuungsbedarf (z.B. Frühgeburt, Regulationsstörungen). Fokus auf Sicherheit, Schlaf-/Fütterungsroutinen und Entlastung der Familie. 24/7 Aufsicht (keine Intensivstation)."
         ))),

    # 18 DE+FR bilingual
    dict(provider=f"{DEMO_PREFIX}Fribourg PontLangues", languages_supported=["de","fr"], care_level=2, cognitive=1,
         wheelchair=False, hearing=False, visual=False,
         tr=dict(
             de=dict(title="Fribourg Zweisprachige WG — DE/FR Alltag & Begleitung #18",
                     description="WG mit zweisprachigem Team (Deutsch/Französisch). Unterstützung bei Alltag, Terminen und Integration. Ideal für Personen, die zwischen Sprachen wechseln oder neu in der Region sind."),
             fr=dict(title="Fribourg — Colocation bilingue DE/FR accompagnement du quotidien #18",
                     description="Colocation avec équipe bilingue (allemand/français). Aide pour l’organisation, rendez-vous et intégration. Idéal pour personnes bilingues ou en transition linguistique.")
         )),

    # 19 EN-only dual sensory
    dict(provider=f"{DEMO_PREFIX}Zug DualSupport Living", languages_supported=["de","en"], care_level=3, cognitive=1,
         wheelchair=True, hearing=True, visual=True,
         tr=dict(en=dict(
             title="Zug Dual-Sensory Support Flat — Hearing + Low Vision #19",
             description="Apartment for residents with combined hearing and low-vision needs. Visual alerts, high-contrast cues, simplified signage, and staff trained in clear written communication. Light daily support and safety routines."
         ))),

    # 20 DE-only TBI
    dict(provider=f"{DEMO_PREFIX}NeuroWohnen Zürich", languages_supported=["de","en"], care_level=4, cognitive=2,
         wheelchair=False, hearing=False, visual=False,
         tr=dict(de=dict(
             title="Zürich Neuro-WG — Schädel-Hirn-Trauma & Exekutive Funktionen #20",
             description="Für Erwachsene nach Schädel-Hirn-Trauma: Unterstützung bei Planung, Impulskontrolle, Terminen und sicheren Routinen. Struktur, Erinnerungsstrategien, Coaching. Regelmäßige Betreuung, keine Intensivpflege."
         ))),

    # 21 DE+EN supported employment
    dict(provider=f"{DEMO_PREFIX}WerkWohnen Aarau", languages_supported=["de","en"], care_level=3, cognitive=2,
         wheelchair=False, hearing=False, visual=False,
         tr=dict(
             de=dict(title="Aarau Begleitetes Wohnen — Arbeitstraining & Alltag #21",
                     description="Begleitetes Wohnen für Erwachsene mit leichter bis moderater kognitiver Beeinträchtigung. Unterstützung bei Haushalt, Kochen, Geld und begleitetem Arbeitstraining. Klare Strukturen, autonomieorientiert."),
             en=dict(title="Aarau Supported Living — Work Training & Daily Skills #21",
                     description="Supported living for adults with mild to moderate cognitive challenges. Help with cooking, budgeting, routines, plus supported employment coaching. Structured but autonomy-focused.")
         )),

    # 22 DE-only high care
    dict(provider=f"{DEMO_PREFIX}Pflegehaus Alpenblick", languages_supported=["de"], care_level=5, cognitive=3,
         wheelchair=True, hearing=False, visual=True,
         tr=dict(de=dict(
             title="Interlaken 24/7 Betreuung — Hoher Unterstützungsbedarf #22",
             description="Für Personen mit sehr hohem Unterstützungsbedarf (z.B. schwere kognitive Einschränkungen oder kombinierte Beeinträchtigungen). 24/7 Präsenz, strukturierte Tagesabläufe, sichere Umgebung. Geeignet bei care_level 5."
         ))),

    # 23 EN-only ADHD executive function
    dict(provider=f"{DEMO_PREFIX}Rheinfelden Ruhe & Struktur", languages_supported=["en","de"], care_level=2, cognitive=1,
         wheelchair=False, hearing=False, visual=False,
         tr=dict(en=dict(
             title="Basel Executive-Function Studio — ADHD Routines & Planning #23",
             description="For adults with ADHD seeking structure: help with planning, reminders, and weekly routines. Calm home rules, optional coaching check-ins, and support organizing appointments and paperwork."
         ))),

    # 24 DE-only ADHD
    dict(provider=f"{DEMO_PREFIX}Rheinfelden Ruhe & Struktur", languages_supported=["de"], care_level=2, cognitive=1,
         wheelchair=False, hearing=False, visual=False,
         tr=dict(de=dict(
             title="Basel Struktur-Wohnen — ADHS Alltag & Termine #24",
             description="Unterstützung bei Zeitmanagement, Routinen und Terminen für Erwachsene mit ADHS. Fokus auf Selbstorganisation, klare Wochenpläne und pragmatische Hilfen (Erinnerungen, Checklisten)."
         ))),

    # 25 FR-only anxiety low stimulus
    dict(provider=f"{DEMO_PREFIX}Maison Rive Gauche", languages_supported=["fr"], care_level=2, cognitive=1,
         wheelchair=False, hearing=False, visual=False,
         tr=dict(fr=dict(
             title="Genève — Studio calme (anxiété) routines & accompagnement léger #25",
             description="Studio très calme pour personnes avec anxiété/paniques. Accompagnement léger pour routines, sorties graduelles, et organisation. Environnement à faible stimulation, proche des transports."
         ))),

    # 26 IT-only low vision
    dict(provider=f"{DEMO_PREFIX}Casa Ticino Supporto", languages_supported=["it"], care_level=2, cognitive=0,
         wheelchair=True, hearing=False, visual=True,
         tr=dict(it=dict(
             title="Lugano — Appartamento ipovisione: orientamento & contrasto #26",
             description="Spazi con buon contrasto, illuminazione non abbagliante e percorsi chiari. Supporto per orientamento e routine di sicurezza. Ideale per ipovisione con assistenza leggera."
         ))),

    # 27 DE+EN hearing support shared flat
    dict(provider=f"{DEMO_PREFIX}Basel SignalHaus", languages_supported=["de","en"], care_level=2, cognitive=0,
         wheelchair=False, hearing=True, visual=False,
         tr=dict(
             de=dict(title="Basel WG — Schwerhörigkeit: visuelle Hinweise & klare Abläufe #27",
                     description="WG mit visuellen Tür-/Alarmhinweisen und klaren Abläufen. Team unterstützt schriftliche Kommunikation und bei Bedarf Gebärden-Vermittlung. Für Menschen mit Hörbeeinträchtigung, die eigenständig wohnen möchten."),
             en=dict(title="Basel Shared Flat — Hard of Hearing: Visual Alerts & Clear Routines #27",
                     description="Shared flat with visual door/alarm cues and clear routines. Staff supports written communication and can arrange sign-support. For hard-of-hearing residents aiming for independence with light support.")
         )),

    # 28 DE-only PTSD
    dict(provider=f"{DEMO_PREFIX}Rheinfelden Ruhe & Struktur", languages_supported=["de","en"], care_level=3, cognitive=1,
         wheelchair=False, hearing=False, visual=False,
         tr=dict(de=dict(
             title="Aarau Schutz & Stabilität — PTSD traumasensibles Wohnen #28",
             description="Traumasensibles Wohnen für Erwachsene mit PTSD. Klare Grenzen, Rückzugsräume, planbare Betreuung und Sicherheitskonzept. Unterstützung bei Alltag und Trigger-Management, keine stationäre Therapie."
         ))),

    # 29 EN-only PTSD
    dict(provider=f"{DEMO_PREFIX}Rheinfelden Ruhe & Struktur", languages_supported=["en"], care_level=3, cognitive=1,
         wheelchair=False, hearing=False, visual=False,
         tr=dict(en=dict(
             title="Aarau Trauma-Informed Housing — PTSD Safety & Predictability #29",
             description="Trauma-informed living for adults with PTSD. Clear boundaries, private retreat spaces, predictable check-ins, and a safety plan. Support for daily routines and paperwork (not inpatient treatment)."
         ))),

    # 30 DE-only epilepsy safety
    dict(provider=f"{DEMO_PREFIX}NeuroWohnen Zürich", languages_supported=["de","en"], care_level=3, cognitive=1,
         wheelchair=False, hearing=False, visual=False,
         tr=dict(de=dict(
             title="Zürich Sicher Wohnen — Epilepsie: Notfallplan & Routine #30",
             description="Wohnangebot für Erwachsene mit Epilepsie. Fokus auf Notfallplan, sichere Routinen, Medikamentenerinnerungen und abgestimmte Betreuung. Personal erreichbar, regelmäßige Check-ins."
         ))),

    # 31 FR-only epilepsy
    dict(provider=f"{DEMO_PREFIX}Maison Rive Gauche", languages_supported=["fr"], care_level=3, cognitive=1,
         wheelchair=False, hearing=False, visual=False,
         tr=dict(fr=dict(
             title="Genève — Habitat sécurisé (épilepsie) plan d’urgence & supervision #31",
             description="Pour adultes avec épilepsie: plan d’urgence, routines sécurisées, rappels de médicaments et accompagnement régulier. Personnel joignable, supervision adaptée."
         ))),

    # 32 DE-only eating disorder supportive (not clinic)
    dict(provider=f"{DEMO_PREFIX}Rheinfelden Ruhe & Struktur", languages_supported=["de"], care_level=3, cognitive=1,
         wheelchair=False, hearing=False, visual=False,
         tr=dict(de=dict(
             title="Zürich Übergangswohnen — Essstörung: Struktur & Stabilität (18+) #32",
             description="Übergangswohnen für Erwachsene (18+) nach ambulanter/stationärer Behandlung einer Essstörung. Fokus auf Tagesstruktur, Mahlzeitenroutine, Begleitung zu Terminen und Rückfallprävention. Kein Kliniksetting."
         ))),

    # 33 EN-only post-stroke mobility + aphasia mild
    dict(provider=f"{DEMO_PREFIX}Basel SignalHaus", languages_supported=["en","de"], care_level=3, cognitive=2,
         wheelchair=True, hearing=False, visual=False,
         tr=dict(en=dict(
             title="Basel Post-Stroke Accessible Flat — Mobility + Communication Aids #33",
             description="Accessible flat for post-stroke recovery with mobility needs. Optional supported communication tools for mild aphasia, patient-paced check-ins, and help organizing rehab appointments."
         ))),

    # 34 DE-only chronic pain pacing
    dict(provider=f"{DEMO_PREFIX}Stiftung Aare Wohnen", languages_supported=["de"], care_level=2, cognitive=0,
         wheelchair=True, hearing=False, visual=False,
         tr=dict(de=dict(
             title="Bern Wohnen bei chronischen Schmerzen — Energie-Management & Alltag #34",
             description="Für Menschen mit chronischen Schmerzen/Fatigue. Unterstützung beim Energie-Management (Pacing), Haushaltsplanung und alltagsnahen Routinen. Barrierearme Wohnung, planbare Unterstützung statt Druck."
         ))),

    # 35 IT-only early dementia mild
    dict(provider=f"{DEMO_PREFIX}Casa Ticino Supporto", languages_supported=["it"], care_level=3, cognitive=2,
         wheelchair=True, hearing=False, visual=False,
         tr=dict(it=dict(
             title="Lugano — Supporto memoria (65+) lieve/moderato: routine & sicurezza #35",
             description="Per persone 65+ con difficoltà di memoria lieve/moderata. Routine stabili, promemoria, supervisione leggera e ambienti sicuri. Attività semplici e supporto quotidiano."
         ))),

    # 36 DE-only bipolar stability
    dict(provider=f"{DEMO_PREFIX}Rheinfelden Ruhe & Struktur", languages_supported=["de","en"], care_level=3, cognitive=1,
         wheelchair=False, hearing=False, visual=False,
         tr=dict(de=dict(
             title="Basel Stabil Wohnen — Bipolar: Rhythmus & Krisenplan #36",
             description="Wohnangebot für Erwachsene mit bipolarer Störung. Fokus auf stabilen Schlaf-Wach-Rhythmus, Frühwarnzeichen, Krisenplan und planbare Unterstützung. Keine Akutpsychiatrie."
         ))),

    # 37 EN-only bipolar
    dict(provider=f"{DEMO_PREFIX}Rheinfelden Ruhe & Struktur", languages_supported=["en"], care_level=3, cognitive=1,
         wheelchair=False, hearing=False, visual=False,
         tr=dict(en=dict(
             title="Basel Stability Housing — Bipolar: Rhythm & Crisis Plan #37",
             description="Housing for adults with bipolar disorder focused on stable daily rhythm, early warning signs, and a practical crisis plan. Predictable check-ins; not acute psychiatric care."
         ))),

    # 38 DE-only sensory + hearing (hard of hearing)
    dict(provider=f"{DEMO_PREFIX}Basel SignalHaus", languages_supported=["de"], care_level=2, cognitive=1,
         wheelchair=False, hearing=True, visual=False,
         tr=dict(de=dict(
             title="Basel Ruhe-Apartment — Schwerhörigkeit: schriftliche Kommunikation #38",
             description="Apartment mit Fokus auf schriftliche/visuelle Kommunikation. Unterstützung bei Organisation und Terminen, klare Abläufe, reduzierte Hintergrundgeräusche. Geeignet bei Hörbeeinträchtigung."
         ))),

    # 39 DE+FR youth bilingual
    dict(provider=f"{DEMO_PREFIX}Fribourg PontLangues", languages_supported=["de","fr"], care_level=4, cognitive=1,
         wheelchair=False, hearing=False, visual=False,
         tr=dict(
             de=dict(title="Freiburg Jugendwohnen (15–19) — Schule/Lehre & Begleitung #39",
                     description="Jugendwohnen 15–19 mit Unterstützung bei Schule/Lehre, Konfliktlösung und Alltagskompetenzen. Zweisprachige Begleitung DE/FR, strukturierter Alltag, Krisenplan."),
             fr=dict(title="Fribourg — Logement jeunes (15–19) école/apprentissage & accompagnement #39",
                     description="Logement pour jeunes 15–19 avec soutien pour l’école/apprentissage, compétences de vie et gestion des conflits. Accompagnement bilingue DE/FR, routines structurées, plan de crise.")
         )),

    # 40 EN-only wheelchair + hearing combo
    dict(provider=f"{DEMO_PREFIX}Zug DualSupport Living", languages_supported=["en","de"], care_level=3, cognitive=1,
         wheelchair=True, hearing=True, visual=False,
         tr=dict(en=dict(
             title="Zug Accessible Flat — Wheelchair + Hearing Support #40",
             description="Wheelchair-usable spaces plus visual alerts and clear written routines for hard-of-hearing residents. Regular check-ins, safety-focused layout, and support organizing daily tasks."
         ))),

    # 41 DE-only ALS high care (non-medical phrasing but high support)
    dict(provider=f"{DEMO_PREFIX}Pflegehaus Alpenblick", languages_supported=["de"], care_level=5, cognitive=1,
         wheelchair=True, hearing=False, visual=False,
         tr=dict(de=dict(
             title="Interlaken Hoher Unterstützungsbedarf — ALS/neuromuskulär (24/7) #41",
             description="Für Menschen mit neuromuskulären Erkrankungen (z.B. ALS) mit hohem Unterstützungsbedarf. 24/7 Präsenz, sichere Transfers, strukturierte Abläufe und Entlastung. (Medizinische Leistungen nach Bedarf extern koordiniert.)"
         ))),

    # 42 DE-only mild cognitive coaching 50+
    dict(provider=f"{DEMO_PREFIX}WerkWohnen Aarau", languages_supported=["de"], care_level=2, cognitive=1,
         wheelchair=False, hearing=False, visual=False,
         tr=dict(de=dict(
             title="Aarau Wohnen (50+) — Leichte kognitive Unterstützung & Coaching #42",
             description="Für Erwachsene 50+ mit leichtem kognitivem Unterstützungsbedarf. Fokus auf Routinen, Erinnerungsstrategien, Behördenhilfe und Alltagstraining. Selbstständigkeit steht im Zentrum."
         ))),

    # 43 EN-only young adult schizophrenia support (non-stigmatizing)
    dict(provider=f"{DEMO_PREFIX}NeuroWohnen Zürich", languages_supported=["en","de"], care_level=4, cognitive=2,
         wheelchair=False, hearing=False, visual=False,
         tr=dict(en=dict(
             title="Zurich Supported Housing — Psychosis Recovery & Daily Skills (18+) #43",
             description="For adults (18+) in psychosis recovery needing structured support: routines, medication reminders, stress reduction, and help with daily skills. Calm environment; staff available regularly with crisis plan."
         ))),

    # 44 DE-only psychosis recovery
    dict(provider=f"{DEMO_PREFIX}NeuroWohnen Zürich", languages_supported=["de"], care_level=4, cognitive=2,
         wheelchair=False, hearing=False, visual=False,
         tr=dict(de=dict(
             title="Zürich Begleitetes Wohnen — Psychose-Recovery & Alltag #44",
             description="Für Erwachsene im Recovery-Prozess nach Psychose. Unterstützung bei Tagesstruktur, Stressreduktion, Terminen und Alltagskompetenzen. Krisenplan vorhanden, regelmäßige Betreuung, ruhiges Umfeld."
         ))),

    # 45 FR-only wheelchair accessible studio
    dict(provider=f"{DEMO_PREFIX}Maison Rive Gauche", languages_supported=["fr"], care_level=2, cognitive=0,
         wheelchair=True, hearing=False, visual=False,
         tr=dict(fr=dict(
             title="Genève — Studio accessible fauteuil roulant: autonomie avec soutien léger #45",
             description="Studio accessible en fauteuil roulant avec salle de bain adaptée. Soutien léger pour organisation du quotidien et rendez-vous. Idéal pour autonomie avec accompagnement ponctuel."
         ))),

    # 46 IT-only autism teen sensory
    dict(provider=f"{DEMO_PREFIX}Casa Ticino Supporto", languages_supported=["it"], care_level=3, cognitive=2,
         wheelchair=False, hearing=False, visual=False,
         tr=dict(it=dict(
             title="Lugano — Casa sensoriale (16+) autismo: routine & spazi tranquilli #46",
             description="Per ragazzi 16+ nello spettro autistico. Routine prevedibili, spazi tranquilli, supporto per abilità di vita quotidiana e gestione sociale. Supervisione regolare, ambiente a bassa stimolazione."
         ))),

    # 47 DE-only hearing + cognitive mild (older adults)
    dict(provider=f"{DEMO_PREFIX}MemoryGarden Bern", languages_supported=["de"], care_level=3, cognitive=2,
         wheelchair=True, hearing=True, visual=False,
         tr=dict(de=dict(
             title="Bern Wohnen (65+) — Schwerhörigkeit & Gedächtnis: klare Kommunikation #47",
             description="Für Personen 65+ mit Hörbeeinträchtigung und leichter/mittlerer Gedächtnisschwäche. Visuelle Hinweise, klare Abläufe, Unterstützung bei Routinen und Sicherheit. Regelmäßige Betreuung."
         ))),

    # 48 EN-only low vision + cognitive mild
    dict(provider=f"{DEMO_PREFIX}MemoryGarden Bern", languages_supported=["en"], care_level=3, cognitive=2,
         wheelchair=True, hearing=False, visual=True,
         tr=dict(en=dict(
             title="Bern Supportive Flat (65+) — Low Vision + Mild Cognitive Support #48",
             description="Accessible flat with orientation-friendly layout, high contrast cues, and gentle routine support for older adults. Designed for low vision combined with mild cognitive challenges."
         ))),

    # 49 DE-only caregiver respite adult
    dict(provider=f"{DEMO_PREFIX}Stiftung Aare Wohnen", languages_supported=["de"], care_level=3, cognitive=2,
         wheelchair=True, hearing=False, visual=False,
         tr=dict(de=dict(
             title="Bern Kurzzeitplatz — Entlastung für Angehörige (Erwachsene) #49",
             description="Kurzzeitplatz zur Entlastung von Angehörigen bei moderatem Unterstützungsbedarf. Strukturierte Tage, sichere Umgebung, Unterstützung bei Alltag und Pflegeorganisation (ohne medizinische Intensivpflege)."
         ))),

    # 50 EN-only hearing + communication (aphasia-like) without saying aphasia
    dict(provider=f"{DEMO_PREFIX}Basel SignalHaus", languages_supported=["en"], care_level=3, cognitive=2,
         wheelchair=False, hearing=True, visual=False,
         tr=dict(en=dict(
             title="Basel Communication-Support Living — Clear Speech & Written Routines #50",
             description="Supportive setting for residents who benefit from slower communication, written routines, and structured check-ins. Suitable for hearing-related needs and communication challenges after illness or injury."
         ))),

    # 51 DE-only visual support severe
    dict(provider=f"{DEMO_PREFIX}Pflegehaus Alpenblick", languages_supported=["de"], care_level=4, cognitive=1,
         wheelchair=True, hearing=False, visual=True,
         tr=dict(de=dict(
             title="Thun Seh-Unterstützung — Orientierung, Begleitung & Sicherheit #51",
             description="Für Menschen mit starker Sehbeeinträchtigung/Blindheit. Orientierungshilfen, sichere Wege, Begleitung bei Alltag und Terminen. Regelmäßige Betreuung und Sicherheitsroutinen in barrierearmem Umfeld."
         ))),

    # 52 FR-only teen autism (small)
    dict(provider=f"{DEMO_PREFIX}Maison Rive Gauche", languages_supported=["fr"], care_level=4, cognitive=2,
         wheelchair=False, hearing=False, visual=False,
         tr=dict(fr=dict(
             title="Genève — Petit foyer (14–18) TSA: structure & accompagnement #52",
             description="Petit foyer pour adolescents 14–18 avec TSA. Routines structurées, soutien scolaire, accompagnement social, et espaces de retrait. Supervision régulière avec plan de crise."
         ))),

    # 53 IT-only wheelchair + daily routines
    dict(provider=f"{DEMO_PREFIX}Casa Ticino Supporto", languages_supported=["it"], care_level=2, cognitive=1,
         wheelchair=True, hearing=False, visual=False,
         tr=dict(it=dict(
             title="Bellinzona — Appartamento accessibile: routine & autonomia #53",
             description="Appartamento accessibile in sedia a rotelle con supporto leggero per routine, spesa e appuntamenti. Ideale per chi vuole autonomia con controlli regolari."
         ))),

    # 54 DE-only social anxiety exposure support
    dict(provider=f"{DEMO_PREFIX}Rheinfelden Ruhe & Struktur", languages_supported=["de"], care_level=2, cognitive=1,
         wheelchair=False, hearing=False, visual=False,
         tr=dict(de=dict(
             title="Basel Wohnen — Soziale Angst: schrittweise Begleitung #54",
             description="Unterstützung bei sozialer Angst mit schrittweiser Begleitung im Alltag: kurze Ausgänge, Aufbau von Routinen, Planung und Erholung. Reizarme Umgebung, kein Kliniksetting."
         ))),

    # 55 EN-only sensory + migraine friendly
    dict(provider=f"{DEMO_PREFIX}Rheinfelden Ruhe & Struktur", languages_supported=["en"], care_level=2, cognitive=0,
         wheelchair=False, hearing=False, visual=False,
         tr=dict(en=dict(
             title="Zurich Low-Stimulus Room — Migraine & Sensory Sensitivity #55",
             description="Low-stimulus living space designed for migraine/sensory sensitivity: soft lighting, quiet hours, and predictable routines. Optional check-ins and help with scheduling appointments."
         ))),

    # 56 DE+EN hearing + workplace integration
    dict(provider=f"{DEMO_PREFIX}WerkWohnen Aarau", languages_supported=["de","en"], care_level=3, cognitive=1,
         wheelchair=False, hearing=True, visual=False,
         tr=dict(
             de=dict(title="Aarau Wohnen & Arbeit — Hörbeeinträchtigung: Job-Coaching #56",
                     description="Wohnangebot mit Job-Coaching für Menschen mit Hörbeeinträchtigung. Unterstützung bei Kommunikation am Arbeitsplatz, schriftlichen Abläufen und Alltag. Regelmäßige Betreuung, autonomieorientiert."),
             en=dict(title="Aarau Living & Work — Hearing Support: Job Coaching #56",
                     description="Living option with job coaching for residents with hearing impairment. Support for workplace communication, written routines, and daily organization. Regular check-ins, autonomy-focused.")
         )),

    # 57 DE-only severe cognitive (adult)
    dict(provider=f"{DEMO_PREFIX}Pflegehaus Alpenblick", languages_supported=["de"], care_level=5, cognitive=3,
         wheelchair=True, hearing=False, visual=False,
         tr=dict(de=dict(
             title="Spiez Intensiv-Betreuung — Schwere kognitive Einschränkungen (24/7) #57",
             description="Für Erwachsene mit schweren kognitiven Einschränkungen und hohem Sicherheitsbedarf. 24/7 Betreuung, klare Strukturen, sichere Umgebung und individuelle Tagesgestaltung. Geeignet bei care_level 5."
         ))),

    # 58 EN-only moderate cognitive + visual
    dict(provider=f"{DEMO_PREFIX}Zug DualSupport Living", languages_supported=["en","de"], care_level=4, cognitive=2,
         wheelchair=True, hearing=False, visual=True,
         tr=dict(en=dict(
             title="Zug Supported Apartment — Moderate Cognitive + Visual Support #58",
             description="Accessible apartment with visual orientation aids and structured routines for residents needing moderate cognitive support. Regular supervision, safety routines, and help with appointments and daily tasks."
         ))),

    # 59 DE-only hearing impairment minimal support
    dict(provider=f"{DEMO_PREFIX}Basel SignalHaus", languages_supported=["de"], care_level=1, cognitive=0,
         wheelchair=False, hearing=True, visual=False,
         tr=dict(de=dict(
             title="Basel Minimal Support — Schwerhörigkeit: visuelle Türklingel & SMS #59",
             description="Einfaches Wohnangebot mit visueller Türklingel/Alarm und Unterstützung via SMS/Chat. Für Menschen mit Hörbeeinträchtigung, die weitgehend selbstständig sind und nur wenig Unterstützung benötigen."
         ))),

    # 60 DE+EN+FR mixed (tri-lingual support)
    dict(provider=f"{DEMO_PREFIX}Fribourg PontLangues", languages_supported=["de","fr","en"], care_level=2, cognitive=1,
         wheelchair=False, hearing=False, visual=False,
         tr=dict(
             de=dict(title="Fribourg Dreisprachig — DE/FR/EN Alltag & Integration #60",
                     description="Wohnen mit dreisprachiger Begleitung (DE/FR/EN). Unterstützung bei Behörden, Terminen, Alltag und Integration. Ideal für Menschen, die mehrsprachige Kommunikation benötigen."),
             fr=dict(title="Fribourg — Accompagnement trilingue DE/FR/EN vie quotidienne & intégration #60",
                     description="Logement avec accompagnement trilingue (DE/FR/EN). Aide pour démarches, rendez-vous, organisation du quotidien et intégration. Idéal pour besoins multilingues."),
             en=dict(title="Fribourg Trilingual Support — DE/FR/EN Daily Living & Integration #60",
                     description="Housing with trilingual support (DE/FR/EN). Help with paperwork, appointments, daily organization, and integration. Ideal for multilingual residents.")
         )),
]


class Command(BaseCommand):
    help = "Seed curated demo Providers and LivingOptions (Parler-safe)."

    def add_arguments(self, parser):
        parser.add_argument("--wipe", action="store_true", help="Delete existing demo data first (providers starting with DEMO —).")

    @transaction.atomic
    def handle(self, *args, **options):
        wipe = options["wipe"]

        if wipe:
            demo_providers = Provider.objects.filter(name__startswith=DEMO_PREFIX)
            count_p = demo_providers.count()
            # cascade deletes living options
            demo_providers.delete()
            self.stdout.write(self.style.WARNING(f"Wiped {count_p} demo providers (and their living options)."))

        # Create/get providers
        provider_map = {}
        for p in DEMO_PROVIDERS:
            obj, _created = Provider.objects.get_or_create(
                name=p["name"],
                defaults=dict(
                    canton=p["canton"],
                    verified=p["verified"],
                    supported_languages=p["supported_languages"],
                ),
            )
            # keep fields in sync if rerun without wipe
            updated = False
            if obj.canton != p["canton"]:
                obj.canton = p["canton"]; updated = True
            if obj.verified != p["verified"]:
                obj.verified = p["verified"]; updated = True
            if obj.supported_languages != p["supported_languages"]:
                obj.supported_languages = p["supported_languages"]; updated = True
            if updated:
                obj.save()

            provider_map[p["name"]] = obj

        created_count = 0

        settings.DISABLE_EMBEDDING_SIGNALS = True
        # Create living options
        for item in DEMO_LISTINGS:
            provider = provider_map[item["provider"]]

            lo = LivingOption.objects.create(
                provider=provider,
                wheelchair_accessible=item["wheelchair"],
                hearing_support=item["hearing"],
                visual_support=item["visual"],
                cognitive_support_level=item["cognitive"],
                care_level=item["care_level"],
                languages_supported=item["languages_supported"],
            )

            # Add only the translations we have for this listing
            for lang_code, t in item["tr"].items():
                set_translation(lo, lang_code, t["title"], t["description"])

            created_count += 1
        settings.DISABLE_EMBEDDING_SIGNALS = False


        self.stdout.write(self.style.SUCCESS(f"Created {len(provider_map)} demo providers."))
        self.stdout.write(self.style.SUCCESS(f"Created {created_count} demo living options."))

        self.stdout.write(self.style.NOTICE(
            "Note: Embeddings were not generated in this command. "
            "Run `python manage.py rebuild_embeddings --all` when ready."
        ))
