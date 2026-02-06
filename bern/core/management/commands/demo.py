DEMO_LISTINGS = [
  {
    "provider_name": "Stiftung Aare Wohnen (Bern)",
    "translations": {
      "de": {
        "title": "Bern Wohntraining (18–25) — Selbstständigkeit & Coaching #01",
        "description": "Betreutes Wohntraining für junge Erwachsene (18–25) mit leichtem Unterstützungsbedarf. Fokus: Alltag strukturieren, Budget/Behörden, Ausbildung/Job-Coaching. Ruhige, zentral gelegene Wohngemeinschaft. Keine medizinische Pflege, aber regelmäßige Check-ins.",
      }
    },
    "wheelchair_accessible": False,
    "hearing_support": False,
    "visual_support": False,
    "cognitive_support_level": 1,
    "care_level": 2,
    "languages_supported": ["de"],
  },

  {
    "provider_name": "Basel SignalHaus",
    "translations": {
      "en": {
        "title": "Basel Deaf-Friendly Studio — Visual Alerts & Clear Communication #02",
        "description": "Compact studio with visual doorbell/fire alerts and staff trained in clear communication. Optional sign-support appointments, written routines, and low-noise environment. Great for Deaf or hard-of-hearing residents seeking independence with light support.",
      }
    },
    "wheelchair_accessible": True,
    "hearing_support": True,
    "visual_support": False,
    "cognitive_support_level": 0,
    "care_level": 1,
    "languages_supported": ["en"],
  },

  {
    "provider_name": "Maison Rive Gauche (Genève)",
    "translations": {
      "fr": {
        "title": "Genève — Logement avec accompagnement (Parkinson) #03",
        "description": "Appartement accompagné pour personnes avec Parkinson: routines stables, aide à l’organisation, coordination des rendez-vous, et supervision légère. Espaces dégagés pour la mobilité et prévention des chutes. Personnel présent en journée.",
      }
    },
    "wheelchair_accessible": False,
    "hearing_support": False,
    "visual_support": False,
    "cognitive_support_level": 1,
    "care_level": 3,
    "languages_supported": ["fr"],
  },

  {
    "provider_name": "Casa Ticino Supporto (Lugano)",
    "translations": {
      "it": {
        "title": "Lugano — Appartamento accessibile (60+) autonomia con supporto leggero #04",
        "description": "Appartamento per persone 60+ con autonomia parziale. Supporto per routine, spesa, farmaci (promemoria), e gestione quotidiana. Spazi senza barriere principali e bagno comodo. Nessuna assistenza medica intensiva.",
      }
    },
    "wheelchair_accessible": True,
    "hearing_support": False,
    "visual_support": False,
    "cognitive_support_level": 1,
    "care_level": 2,
    "languages_supported": ["it"],
  },

  # --- Mixed-language (DE+EN) ---
  {
    "provider_name": "Zürich KlarWohnen",
    "translations": {
      "de": {
        "title": "Zürich Ruhige Wohnung — Depression & Tagesstruktur #05",
        "description": "Ruhiges Setting für Erwachsene mit Depression/Angst. Unterstützung bei Tagesstruktur, Terminen und Selbstfürsorge. Keine stationäre Klinik: Fokus auf Stabilität, Privatsphäre und planbare Check-ins. Nähe ÖV, reizarm.",
      },
      "en": {
        "title": "Zurich Quiet Flat — Depression & Daily Structure #05",
        "description": "Quiet setting for adults living with depression/anxiety. Support with routines, appointments, and self-care. Not an inpatient clinic—focus on stability, privacy, and predictable check-ins. Low-stimulus environment near transit.",
      },
    },
    "wheelchair_accessible": False,
    "hearing_support": False,
    "visual_support": False,
    "cognitive_support_level": 1,
    "care_level": 2,
    "languages_supported": ["de", "en"],
  },

  {
    "provider_name": "Stiftung SehenPlus (St. Gallen)",
    "translations": {
      "de": {
        "title": "St. Gallen Low-Vision Apartment — Orientierung & Kontrast #06",
        "description": "Wohnung mit kontrastreichen Markierungen, klarer Wegführung und blendarmem Licht. Unterstützung bei Orientierung im Haus, Alltagshilfen und sicheren Routinen. Ideal bei Sehbehinderung oder Low Vision, auch kombiniert mit leichter Betreuung.",
      },
      "en": {
        "title": "St. Gallen Low-Vision Apartment — Orientation & Contrast #06",
        "description": "High-contrast cues, clear navigation, and glare-reduced lighting. Support for orientation at home, daily living aids, and safety routines. Designed for low vision/visual impairment with optional light supervision.",
      },
    },
    "wheelchair_accessible": True,
    "hearing_support": False,
    "visual_support": True,
    "cognitive_support_level": 0,
    "care_level": 2,
    "languages_supported": ["de", "en"],
  },

  # --- Autism / sensory profiles ---
  {
    "provider_name": "Autismus Wohnen Winterthur",
    "translations": {
      "de": {
        "title": "Winterthur Reizarme WG — Autismus (16+) Struktur & Rückzug #07",
        "description": "Reizarme Wohngemeinschaft für Autist:innen (ab 16). Klare Regeln, visuelle Tagespläne, ruhige Zimmer, sensorikfreundliche Beleuchtung. Unterstützung bei sozialen Situationen, Einkaufen und Behörden. Keine medizinische Pflege.",
      }
    },
    "wheelchair_accessible": False,
    "hearing_support": False,
    "visual_support": False,
    "cognitive_support_level": 2,
    "care_level": 3,
    "languages_supported": ["de"],
  },

  {
    "provider_name": "Autism Support Home (Zurich)",
    "translations": {
      "en": {
        "title": "Zurich Sensory-Friendly Flat — Autism (18+) Visual Schedules #08",
        "description": "Sensory-friendly apartment for autistic adults. Visual schedules, predictable check-ins, support for executive function and daily planning. Quiet neighbors policy and low-stimulation common areas. Best for moderate support needs.",
      }
    },
    "wheelchair_accessible": False,
    "hearing_support": False,
    "visual_support": False,
    "cognitive_support_level": 2,
    "care_level": 3,
    "languages_supported": ["en"],
  },

  # --- Aphasia / communication supports ---
  {
    "provider_name": "Basel KommunikationsHaus",
    "translations": {
      "de": {
        "title": "Basel Aphasie-Unterstützung — Kommunikationshilfen & Geduld #09",
        "description": "Wohnangebot für Menschen mit Aphasie nach Schlaganfall. Team mit Geduld, visuellen Kommunikationskarten und unterstützter Kommunikation. Fokus auf Selbstständigkeit im Alltag und stressarme Gespräche. Regelmäßige Unterstützung, keine Intensivpflege.",
      }
    },
    "wheelchair_accessible": True,
    "hearing_support": False,
    "visual_support": False,
    "cognitive_support_level": 2,
    "care_level": 3,
    "languages_supported": ["de"],
  },

  # --- Dementia / memory care ---
  {
    "provider_name": "MemoryGarden (Bern)",
    "translations": {
      "en": {
        "title": "Bern Memory-Support Residence (65+) — Structured Days & Safety #10",
        "description": "For older adults (65+) with moderate memory impairment. Safe layout, gentle supervision, structured daytime activities, and support for routines. Calm environment; staff available day and evening with overnight on-call.",
      }
    },
    "wheelchair_accessible": True,
    "hearing_support": False,
    "visual_support": False,
    "cognitive_support_level": 3,
    "care_level": 4,
    "languages_supported": ["en", "de"],
  },

  {
    "provider_name": "Résidence Mémoire (Lausanne)",
    "translations": {
      "fr": {
        "title": "Lausanne — Résidence mémoire (70+) sécurité & repères #11",
        "description": "Pour personnes 70+ avec troubles cognitifs modérés à sévères. Repères visuels, supervision, activités adaptées, prévention de l’errance. Personnel présent 24/7. Environnement rassurant et calme.",
      }
    },
    "wheelchair_accessible": True,
    "hearing_support": False,
    "visual_support": False,
    "cognitive_support_level": 3,
    "care_level": 5,
    "languages_supported": ["fr"],
  },

  # --- Spinal injury / wheelchair optimized ---
  {
    "provider_name": "Bern Mobility Living",
    "translations": {
      "de": {
        "title": "Bern Barrierefreie Wohnung — Paraplegie-optimiert #12",
        "description": "Rollstuhlgängige Wohnung mit breiten Türen, unterfahrbarer Küche, barrierefreiem Bad. Fokus auf Autonomie bei Paraplegie/Querschnitt. Optional: Unterstützung bei Haushalt/Organisation (keine 24/7-Pflege).",
      },
      "en": {
        "title": "Bern Accessible Apartment — Optimized for Paraplegia #12",
        "description": "Wheelchair-optimized apartment with wide doors, roll-under kitchen, and accessible bathroom. Focus on autonomy for spinal cord injury. Optional help with household/organization (not 24/7 nursing care).",
      },
    },
    "wheelchair_accessible": True,
    "hearing_support": False,
    "visual_support": False,
    "cognitive_support_level": 0,
    "care_level": 2,
    "languages_supported": ["de", "en"],
  },

  # --- Substance recovery ---
  {
    "provider_name": "RecoveryHaus (Zürich)",
    "translations": {
      "de": {
        "title": "Zürich Übergangswohnen — Sucht-Rehabilitation & Stabilität #13",
        "description": "Strukturiertes Übergangswohnen nach Entzug/Therapie. Nüchternes Umfeld, klare Regeln, Unterstützung bei Rückfallprävention, Terminen und Tagesstruktur. Gruppenangebote optional. Keine medizinische Akutversorgung.",
      }
    },
    "wheelchair_accessible": False,
    "hearing_support": False,
    "visual_support": False,
    "cognitive_support_level": 1,
    "care_level": 3,
    "languages_supported": ["de", "en"],
  },

  {
    "provider_name": "CuraRipresa (Lugano)",
    "translations": {
      "it": {
        "title": "Lugano — Alloggio di transizione per recupero dipendenze #14",
        "description": "Alloggio strutturato dopo trattamento per dipendenze. Regole chiare, sostegno per routine, gestione stress e prevenzione ricadute. Ambiente sobrio e tranquillo. Supporto regolare, non clinico.",
      }
    },
    "wheelchair_accessible": False,
    "hearing_support": False,
    "visual_support": False,
    "cognitive_support_level": 1,
    "care_level": 3,
    "languages_supported": ["it"],
  },

  # --- Teen mental health ---
  {
    "provider_name": "Jugendhaus Thun",
    "translations": {
      "de": {
        "title": "Thun Jugendwohnen (13–17) — Emotionale Stabilisierung #15",
        "description": "Kleines Setting für Jugendliche 13–17 mit Angst/Depression/Schulverweigerung. Strukturierter Alltag, Bezugspersonen, Unterstützung bei Schule/Lehre. Krisenplan vorhanden. Kein geschlossenes Setting.",
      }
    },
    "wheelchair_accessible": False,
    "hearing_support": False,
    "visual_support": False,
    "cognitive_support_level": 1,
    "care_level": 4,
    "languages_supported": ["de"],
  },

  # --- Children / developmental ---
  {
    "provider_name": "KinderWohnen Luzern",
    "translations": {
      "de": {
        "title": "Luzern Kinderwohnen (6–12) — Entwicklungsförderung & Alltag #16",
        "description": "Wohnangebot für Kinder 6–12 mit Entwicklungsverzögerungen oder ADHS/Autismus. Unterstützte Routinen, spielerische Förderung, enge Zusammenarbeit mit Schule/Therapien. 24/7 Betreuung, familiennahe Einbindung.",
      }
    },
    "wheelchair_accessible": True,
    "hearing_support": False,
    "visual_support": False,
    "cognitive_support_level": 2,
    "care_level": 5,
    "languages_supported": ["de"],
  },

  # --- Infant / medically light but constant supervision ---
  {
    "provider_name": "FamilienEntlastung Bern",
    "translations": {
      "de": {
        "title": "Bern Kurzzeitplatz für Säuglinge — Entlastung & 24/7 Aufsicht #17",
        "description": "Kurzzeitbetreuung für Säuglinge (0–2) mit erhöhtem Betreuungsbedarf (z.B. Frühgeburt, Regulationsstörungen). Fokus auf Sicherheit, Schlaf-/Fütterungsroutinen und Entlastung der Familie. 24/7 Aufsicht (keine Intensivstation).",
      }
    },
    "wheelchair_accessible": True,
    "hearing_support": False,
    "visual_support": False,
    "cognitive_support_level": 3,
    "care_level": 5,
    "languages_supported": ["de", "fr"],
  },

  # --- Mixed DE+FR: bilingual region ---
  {
    "provider_name": "Fribourg PontLangues",
    "translations": {
      "de": {
        "title": "Fribourg Zweisprachige WG — DE/FR Alltag & Begleitung #18",
        "description": "WG in Freiburg mit zweisprachigem Team (Deutsch/Französisch). Unterstützung bei Alltag, Terminen und Integration. Ideal für Personen, die zwischen Sprachen wechseln oder neu in der Region sind.",
      },
      "fr": {
        "title": "Fribourg — Colocation bilingue DE/FR accompagnement du quotidien #18",
        "description": "Colocation à Fribourg avec équipe bilingue (allemand/français). Aide pour l’organisation, rendez-vous, et intégration. Idéal pour personnes bilingues ou en transition linguistique.",
      },
    },
    "wheelchair_accessible": False,
    "hearing_support": False,
    "visual_support": False,
    "cognitive_support_level": 1,
    "care_level": 2,
    "languages_supported": ["de", "fr"],
  },

  # --- Hearing + visual combined ---
  {
    "provider_name": "Zug DualSupport Living",
    "translations": {
      "en": {
        "title": "Zug Dual-Sensory Support Flat — Hearing + Low Vision #19",
        "description": "Apartment for residents with combined hearing and low-vision needs. Visual alerts, high-contrast cues, simplified signage, and staff trained in clear written communication. Light daily support and safety routines.",
      }
    },
    "wheelchair_accessible": True,
    "hearing_support": True,
    "visual_support": True,
    "cognitive_support_level": 1,
    "care_level": 3,
    "languages_supported": ["en", "de"],
  },

  # --- TBI / executive function ---
  {
    "provider_name": "NeuroWohnen Zürich",
    "translations": {
      "de": {
        "title": "Zürich Neuro-WG — Schädel-Hirn-Trauma & Exekutive Funktionen #20",
        "description": "Für Erwachsene nach Schädel-Hirn-Trauma: Unterstützung bei Planung, Impulskontrolle, Terminen und sicheren Routinen. Struktur, Erinnerungsstrategien, Coaching. Regelmäßige Betreuung, keine Intensivpflege.",
      }
    },
    "wheelchair_accessible": False,
    "hearing_support": False,
    "visual_support": False,
    "cognitive_support_level": 2,
    "care_level": 4,
    "languages_supported": ["de", "en"],
  },

  # --- Intellectual disability / supported employment ---
  {
    "provider_name": "WerkWohnen Aarau",
    "translations": {
      "de": {
        "title": "Aarau Begleitetes Wohnen — Arbeitstraining & Alltag #21",
        "description": "Begleitetes Wohnen für Erwachsene mit leichter bis moderater geistiger Beeinträchtigung. Unterstützung bei Haushalt, Kochen, Geld, und begleitetem Arbeitstraining. Klare Strukturen, wertschätzendes Umfeld.",
      },
      "en": {
        "title": "Aarau Supported Living — Work Training & Daily Skills #21",
        "description": "Supported living for adults with mild to moderate intellectual disability. Help with cooking, budgeting, and daily routines plus supported employment coaching. Structured but autonomy-focused.",
      },
    },
    "wheelchair_accessible": False,
    "hearing_support": False,
    "visual_support": False,
    "cognitive_support_level": 2,
    "care_level": 3,
    "languages_supported": ["de", "en"],
  },

  # --- 24/7 high care ---
  {
    "provider_name": "Pflegehaus Alpenblick (Interlaken)",
    "translations": {
      "de": {
        "title": "Interlaken 24/7 Betreuung — Hoher Pflege- & Unterstützungsbedarf #22",
        "description": "Für Personen mit hohem Unterstützungsbedarf (z.B. schwere kognitive Einschränkungen oder kombinierte Beeinträchtigungen). 24/7 Präsenz, strukturierte Tagesabläufe, sichere Umgebung. Geeignet bei care_level 5.",
      }
    },
    "wheelchair_accessible": True,
    "hearing_support": False,
    "visual_support": True,
    "cognitive_support_level": 3,
    "care_level": 5,
    "languages_supported": ["de"],
  },

  # --- Add 38 more entries (same quality level) ---
]

# NOTE: I’ve provided 22 fully detailed entries here to keep this message usable.
# If you want, I can continue immediately with entries #23–#60 in the same format.
