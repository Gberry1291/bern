# python manage.py sync_livingoptions
# python manage.py sync_livingoptions --apply
# python manage.py sync_livingoptions --apply --no-delete-missing
MODEL_DATA = [
    {'provider_idx': 0,
     'slug': 'bern-accessible-residence-deaf-friendly-dementia-aware-65',
     'care_level': 4,
     'cognitive_support_level': 4,
     'wheelchair_accessible': True,
     'hearing_support': True,
     'visual_support': False,
     'languages_supported': ['de', 'fr'],
     'min_age': 65,
     'max_age': 120,
     'translations': {'de': {'title': 'Bern Accessible Residence — Deaf-Friendly + Dementia-Aware '
                                      '(65+)',
                             'description': 'BESCHREIBUNG:\n'
                                            'Altersbeschränkung: 65+. Gehörfreundliche Kommunikation '
                                            'unterstützt durch demenzbewusste Routinen. Visuelle '
                                            'Warnungen, klare Beschilderung, vorhersehbarer '
                                            'Tagesablauf. Barrierefrei für Rollstühle.'},
                      'fr': {'title': 'Bern Accessible Residence — Deaf-Friendly + Dementia-Aware '
                                      '(65+)',
                             'description': 'DESCRIPTION :  \n'
                                            "Restriction d'âge : 65 ans et plus. Supports de "
                                            'communication adaptés aux malentendants combinés à des '
                                            'routines conscientes de la démence. Alertes visuelles, '
                                            'signalisation claire, rythme quotidien prévisible. '
                                            'Accessible en fauteuil roulant.'}},
     'provider_name': 'Helvetia Supported Living'},
    {'provider_idx': 0,
     'slug': 'bern-epilepsy-aware-apartment-safety-plan-night-check-in-option',
     'care_level': 2,
     'cognitive_support_level': 2,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de', 'fr'],
     'min_age': 0,
     'max_age': 120,
     'translations': {'de': {'title': 'Bern Epilepsy-Aware Apartment — Safety Plan & Night Check-In '
                                      'Option',
                             'description': 'Betriebsumfeld für Epilepsie: Sicherheitsplan für '
                                            'Bewohner, optionale nächtliche Kontrollen und geschultes '
                                            'Personal, das ruhig reagiert. Barrierefreies Gebäude.'},
                      'fr': {'title': 'Bern Epilepsy-Aware Apartment — Safety Plan & Night Check-In '
                                      'Option',
                             'description': 'DESCRIPTION :\n'
                                            "Environnement conscient de l'épilepsie : plan de sécurité "
                                            'pour les résidents, contrôles nocturnes optionnels et '
                                            'personnel formé à réagir calmement. Immeuble accessible '
                                            'aux fauteuils roulants.'}},
     'provider_name': 'Helvetia Supported Living'},
    {'provider_idx': 0,
     'slug': 'bern-tbi-recovery-shared-home-routine-memory-aids-gentle-supervision',
     'care_level': 3,
     'cognitive_support_level': 4,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de'],
     'min_age': 0,
     'max_age': 120,
     'translations': {'de': {'title': 'Bern TBI Recovery Shared Home — Routine, Memory Aids, Gentle '
                                      'Supervision',
                             'description': 'Beschreibung: \n'
                                            'Umgebung zur Genesung von traumatischen Hirnverletzungen '
                                            '(TBI) mit Gedächtnisstützen, strukturierten Abläufen und '
                                            'sanfter Aufsicht. Fokus auf das Wachstum der '
                                            'Unabhängigkeit. Rollstuhlgerechte '
                                            'Gemeinschaftsbereiche.'}},
     'provider_name': 'Helvetia Supported Living'},
    {'provider_idx': 0,
     'slug': 'lausanne-dementia-care-home-70-secure-garden-247-staff',
     'care_level': 5,
     'cognitive_support_level': 5,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de', 'fr'],
     'min_age': 70,
     'max_age': 120,
     'translations': {'de': {'title': 'Lausanne Dementia Care Home (70+) — Secure Garden & 24/7 Staff',
                             'description': 'Beschreibung: Altersbeschränkung: 70+. Demenzfähige '
                                            'Pflege mit 24/7-Personal, sicherem, wanderfreundlichem '
                                            'Garten und beruhigenden Abläufen. Unterstützt höhere '
                                            'Pflegebedürfnisse; rollstuhlgerecht.'},
                      'fr': {'title': 'Lausanne Dementia Care Home (70+) — Secure Garden & 24/7 Staff',
                             'description': 'DESCRIPTION :\n'
                                            "Restriction d'âge : 70 ans et plus. Soins adaptés à la "
                                            'démence avec personnel disponible 24/7, jardin sécurisé '
                                            'pour éviter les errances et routines apaisantes. Soutient '
                                            'des besoins de soins plus élevés ; accessible en fauteuil '
                                            'roulant.'}},
     'provider_name': 'Helvetia Supported Living'},
    {'provider_idx': 0,
     'slug': 'lugano-community-living-mild-intellectual-disability-adults',
     'care_level': 2,
     'cognitive_support_level': 4,
     'wheelchair_accessible': False,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de', 'it'],
     'min_age': 18,
     'max_age': 120,
     'translations': {'de': {'title': 'Lugano Community Living — Mild Intellectual Disability (Adults)',
                             'description': 'BESCHREIBUNG:\n'
                                            'Erwachsene (18+). Coaching für tägliche Routinen, '
                                            'Teilnahme an der Gemeinschaft und unterstützte '
                                            'Entscheidungsfindung. Niedrige bis moderate '
                                            'Unterstützung; soziale Aktivitäten optional.'},
                      'it': {'title': 'Lugano Community Living — Mild Intellectual Disability (Adults)',
                             'description': 'DESCRIZIONE:\n'
                                            'Adulti (18+). Coaching per routine quotidiane, '
                                            'partecipazione alla comunità e supporto nelle decisioni. '
                                            'Supporto da basso a moderato; attività sociali '
                                            'opzionali.'}},
     'provider_name': 'Helvetia Supported Living'},
    {'provider_idx': 0,
     'slug': 'lugano-teen-support-apartment-ages-1418-independent-skills',
     'care_level': 2,
     'cognitive_support_level': 2,
     'wheelchair_accessible': False,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de', 'it'],
     'min_age': 14,
     'max_age': 18,
     'translations': {'de': {'title': 'Lugano Teen Support Apartment (Ages 14–18) — Independent Skills',
                             'description': 'BESCHREIBUNG:\n'
                                            'Altersbeschränkung: 14–18. Coaching für '
                                            'Alltagsfähigkeiten, Schulroutine und Übergangsplanung. '
                                            'Geringe bis moderate Unterstützung; ruhige Umgebung.'},
                      'it': {'title': 'Lugano Teen Support Apartment (Ages 14–18) — Independent Skills',
                             'description': 'DESCRIZIONE:\n'
                                            'Restrizione di età: 14-18. Coaching per abilità '
                                            'quotidiane, routine scolastica e pianificazione della '
                                            'transizione. Supporto da basso a moderato; ambiente '
                                            'tranquillo.'}},
     'provider_name': 'Helvetia Supported Living'},
    {'provider_idx': 0,
     'slug': 'zurich-deafblind-support-residence-tactile-communication-ready',
     'care_level': 4,
     'cognitive_support_level': 3,
     'wheelchair_accessible': True,
     'hearing_support': True,
     'visual_support': True,
     'languages_supported': ['de'],
     'min_age': 0,
     'max_age': 120,
     'translations': {'de': {'title': 'Zurich Deafblind Support Residence — Tactile Communication '
                                      'Ready',
                             'description': 'Beschreibung:\n'
                                            'Wohnheim für taubblinde Menschen mit geschultem Personal '
                                            'für taktile Kommunikation, strukturierte '
                                            'Orientierungsunterstützung und ruhige, vorhersehbare '
                                            'Abläufe. Barrierefreie Einrichtungen und geführte '
                                            'Gemeinschaftsaktivitäten.'}},
     'provider_name': 'Helvetia Supported Living'},
    {'provider_idx': 0,
     'slug': 'zurich-early-support-home-ages-03-feeding-mobility-care',
     'care_level': 4,
     'cognitive_support_level': 2,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de'],
     'min_age': 0,
     'max_age': 3,
     'translations': {'de': {'title': 'Zurich Early Support Home (Ages 0–3) — Feeding & Mobility Care',
                             'description': 'BESCHREIBUNG:\n'
                                            'Altersbeschränkung: Säuglinge und Kleinkinder (0–3 '
                                            'Jahre). Pädiatrische Pflegeunterstützung für '
                                            'Ernährungssonden, frühe Physiotherapie-Routinen und '
                                            'Schulung von Betreuern. Ruhige Räume, vorhersehbare '
                                            'Abläufe, sensorfreundliche Beleuchtung. '
                                            'Rollstuhl-/Kinderwagenzugänglich.'}},
     'provider_name': 'Helvetia Supported Living'},
    {'provider_idx': 0,
     'slug': 'zurich-transition-apartments-1825-independent-living-skills-coaching',
     'care_level': 2,
     'cognitive_support_level': 2,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de'],
     'min_age': 18,
     'max_age': 25,
     'translations': {'de': {'title': 'Zurich Transition Apartments (18–25) — Independent Living '
                                      'Skills Coaching',
                             'description': 'BESCHREIBUNG:\n'
                                            'Altersbeschränkung: 18–25. Coaching für Budgetierung, '
                                            'Kochen, Termine und Arbeits-/Bildungsroutinen. Optionale '
                                            'Unterstützung bei leichten kognitiven Bedürfnissen. '
                                            'Barrierefreies Gebäude.'}},
     'provider_name': 'Helvetia Supported Living'},
    {'provider_idx': 1,
     'slug': 'bern-barrier-free-apartment-paraplegia-optimized-kitchen-bath',
     'care_level': 1,
     'cognitive_support_level': 1,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de', 'fr'],
     'min_age': 0,
     'max_age': 120,
     'translations': {'de': {'title': 'Bern Barrier-Free Apartment — Paraplegia-Optimized Kitchen & '
                                      'Bath',
                             'description': 'Rollstuhlgerecht im gesamten Bereich. Roll-in-Dusche, '
                                            'Wendekreis in der Küche, höhenverstellbare Arbeitsflächen '
                                            'und transferfreundliche Schlafzimmergestaltung. Ideal für '
                                            'Paraplegie oder Rückenmarksverletzungen. Minimale Pflege '
                                            'erforderlich.'},
                      'fr': {'title': 'Bern Barrier-Free Apartment — Paraplegia-Optimized Kitchen & '
                                      'Bath',
                             'description': 'ACCESSIBILITÉ :\n'
                                            "Accessible en fauteuil roulant dans tout l'espace. Douche "
                                            "à l'italienne, rayon de rotation dans la cuisine, "
                                            'comptoirs ajustables et aménagement de chambre adapté '
                                            'pour les transferts. Idéal pour les personnes '
                                            'paraplégiques ou ayant subi une blessure à la colonne '
                                            'vertébrale. Peu de soins nécessaires.'}},
     'provider_name': 'Romandie Care Network'},
    {'provider_idx': 1,
     'slug': 'bern-rehab-transition-flat-post-surgery-mobility-support-adults',
     'care_level': 3,
     'cognitive_support_level': 1,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de', 'fr'],
     'min_age': 0,
     'max_age': 120,
     'translations': {'de': {'title': 'Bern Rehab Transition Flat — Post-Surgery Mobility Support '
                                      '(Adults)',
                             'description': 'Bieten Sie kurzfristige bis mittelfristige '
                                            'Mobilitätsunterstützung nach einer Operation mit '
                                            'barrierefreiem Layout und täglicher Hilfe bei Mahlzeiten '
                                            'und Besorgungen. Rollstuhlgerecht; in der Nähe einer '
                                            'Klinik.'},
                      'fr': {'title': 'Bern Rehab Transition Flat — Post-Surgery Mobility Support '
                                      '(Adults)',
                             'description': 'DESCRIPTION :\n'
                                            'Soutien à la mobilité à court ou moyen terme après une '
                                            'chirurgie, avec un aménagement accessible et une '
                                            'assistance quotidienne pour les repas et les courses. '
                                            'Accessible en fauteuil roulant ; près de la clinique.'}},
     'provider_name': 'Romandie Care Network'},
    {'provider_idx': 1,
     'slug': 'lausanne-accessible-flat-wheelchair-visual-support-adults',
     'care_level': 1,
     'cognitive_support_level': 1,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': True,
     'languages_supported': ['de', 'fr'],
     'min_age': 0,
     'max_age': 120,
     'translations': {'de': {'title': 'Lausanne Accessible Flat — Wheelchair + Visual Support (Adults)',
                             'description': 'Rollstuhlgerecht mit Unterstützung für Menschen mit '
                                            'Sehbehinderungen (hoher Kontrast, konsistente Anordnung). '
                                            'Geeignet für Bewohner, die minimale Unterstützung '
                                            'benötigen; in der Nähe von Verkehrsanbindungen.'},
                      'fr': {'title': 'Lausanne Accessible Flat — Wheelchair + Visual Support (Adults)',
                             'description': 'Accessible aux fauteuils roulants avec des supports pour '
                                            'les personnes malvoyantes (fort contraste, agencement '
                                            'cohérent). Convient aux résidents nécessitant une '
                                            'assistance minimale ; proche des transports en commun.'}},
     'provider_name': 'Romandie Care Network'},
    {'provider_idx': 1,
     'slug': 'lausanne-diabetes-support-residence-meal-planning-medication-reminders',
     'care_level': 2,
     'cognitive_support_level': 2,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de', 'fr'],
     'min_age': 0,
     'max_age': 120,
     'translations': {'de': {'title': 'Lausanne Diabetes Support Residence — Meal Planning & '
                                      'Medication Reminders',
                             'description': 'Unterstützung bei der Diabetesverwaltung: Hilfe bei der '
                                            'Essensplanung, Erinnerungen an Medikamente und '
                                            'Koordination von Terminen. Geeignet für moderate '
                                            'Unabhängigkeit; barrierefreier Zugang.'},
                      'fr': {'title': 'Lausanne Diabetes Support Residence — Meal Planning & '
                                      'Medication Reminders',
                             'description': 'DESCRIPTION :\n'
                                            'Soutien à la gestion du diabète : assistance à la '
                                            'planification des repas, rappels de médicaments et '
                                            'coordination des rendez-vous. Convient pour une '
                                            'indépendance modérée ; entrée accessible.'}},
     'provider_name': 'Romandie Care Network'},
    {'provider_idx': 1,
     'slug': 'lausanne-inclusive-community-home-down-syndrome-support-adults',
     'care_level': 3,
     'cognitive_support_level': 4,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de', 'fr'],
     'min_age': 0,
     'max_age': 120,
     'translations': {'de': {'title': 'Lausanne Inclusive Community Home — Down Syndrome Support '
                                      '(Adults)',
                             'description': 'Beschreibung:\n'
                                            'Erwachsenenorientiertes inklusives Zuhause. Unterstützung '
                                            'bei sozialen Fähigkeiten, strukturierte Abläufe und '
                                            'Gemeinschaftsaktivitäten. Unterstützung durch das '
                                            'Personal bei Terminen und täglicher Planung. '
                                            'Barrierefreie Gemeinschaftsbereiche.'},
                      'fr': {'title': 'Lausanne Inclusive Community Home — Down Syndrome Support '
                                      '(Adults)',
                             'description': 'DESCRIPTION :\n'
                                            'Maison inclusive axée sur les adultes. Soutien aux '
                                            'compétences sociales, routines structurées et activités '
                                            'communautaires. Soutien du personnel pour les rendez-vous '
                                            'et la planification quotidienne. Espaces communs '
                                            'accessibles.'}},
     'provider_name': 'Romandie Care Network'},
    {'provider_idx': 1,
     'slug': 'lausanne-pediatric-respite-flat-ages-410-autism-sensory-support',
     'care_level': 3,
     'cognitive_support_level': 3,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de', 'fr'],
     'min_age': 4,
     'max_age': 10,
     'translations': {'de': {'title': 'Lausanne Pediatric Respite Flat (Ages 4–10) — Autism & Sensory '
                                      'Support',
                             'description': 'BESCHREIBUNG:\n'
                                            'Altersbeschränkung: Kinder (4–10). Autismusfreundliche '
                                            'Umgebung mit geringer sensorischer Stimulation, visuellen '
                                            'Zeitplänen und strukturierten Übergängen. Mitarbeiter '
                                            'geschult in Kommunikationsunterstützung. Barrierefreies '
                                            'Badezimmer; ruhiger Außenbereich.'},
                      'fr': {'title': 'Lausanne Pediatric Respite Flat (Ages 4–10) — Autism & Sensory '
                                      'Support',
                             'description': 'DESCRIPTION :\n'
                                            "Restriction d'âge : enfants (4–10 ans). Environnement "
                                            "informé sur l'autisme avec faible stimulation "
                                            'sensorielle, emplois du temps visuels et transitions '
                                            'structurées. Personnel formé aux supports de '
                                            'communication. Salle de bain accessible ; espace '
                                            'extérieur calme.'}},
     'provider_name': 'Romandie Care Network'},
    {'provider_idx': 1,
     'slug': 'lausanne-youth-hearing-support-flat-ages-816-visual-alerts-coaching',
     'care_level': 2,
     'cognitive_support_level': 1,
     'wheelchair_accessible': True,
     'hearing_support': True,
     'visual_support': False,
     'languages_supported': ['de', 'fr'],
     'min_age': 8,
     'max_age': 16,
     'translations': {'de': {'title': 'Lausanne Youth Hearing Support Flat (Ages 8–16) — Visual Alerts '
                                      '& Coaching',
                             'description': 'BESCHREIBUNG:\n'
                                            'Altersbeschränkung: 8–16. Unterstützung bei '
                                            'Hörbehinderungen: visuelle Signale, schriftliche '
                                            'Kommunikation zuerst und geschultes Personal zur '
                                            'Unterstützung von Hörhilfen. Barrierefreie '
                                            'Gemeinschaftsbereiche.'},
                      'fr': {'title': 'Lausanne Youth Hearing Support Flat (Ages 8–16) — Visual Alerts '
                                      '& Coaching',
                             'description': 'DESCRIPTION :\n'
                                            "Restriction d'âge : 8–16 ans. Soutien aux personnes "
                                            'malentendantes : alertes visuelles, communication écrite '
                                            'en priorité et personnel formé pour soutenir les '
                                            'appareils auditifs. Espaces communs accessibles.'}},
     'provider_name': 'Romandie Care Network'},
    {'provider_idx': 1,
     'slug': 'lugano-senior-accessible-flat-60-low-care-high-independence',
     'care_level': 1,
     'cognitive_support_level': 1,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de', 'it'],
     'min_age': 60,
     'max_age': 120,
     'translations': {'de': {'title': 'Lugano Senior Accessible Flat (60+) — Low Care, High '
                                      'Independence',
                             'description': 'BESCHREIBUNG:\n'
                                            'Altersbeschränkung: 60+. Barrierefreie Wohnung für '
                                            'Senioren, die minimale Unterstützung benötigen. '
                                            'Sturzrisiko-bewusste Anordnung, optionale wöchentliche '
                                            'Kontrollen, in der Nähe von Apotheke und '
                                            'Verkehrsanbindung.'},
                      'it': {'title': 'Lugano Senior Accessible Flat (60+) — Low Care, High '
                                      'Independence',
                             'description': 'DESCRIZIONE:\n'
                                            'Restrizione di età: 60+. Appartamento accessibile per '
                                            'anziani che necessitano di assistenza minima. Layout '
                                            'attento al rischio di cadute, controlli settimanali '
                                            'opzionali, vicino a farmacia e mezzi di trasporto.'}},
     'provider_name': 'Romandie Care Network'},
    {'provider_idx': 2,
     'slug': 'basel-assisted-mobility-flat-quadriplegia-daily-support',
     'care_level': 4,
     'cognitive_support_level': 1,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de'],
     'min_age': 0,
     'max_age': 120,
     'translations': {'de': {'title': 'Basel Assisted Mobility Flat — Quadriplegia Daily Support',
                             'description': 'Rollstuhlgerecht. Tägliche Unterstützung bei Transfers, '
                                            'Hygieneroutinen und Essensvorbereitung. Personal '
                                            'verfügbar morgens und abends. Platz für adaptive Geräte; '
                                            'Pflegekraft-Rufsystem.'}},
     'provider_name': 'Ticino Wellness Homes'},
    {'provider_idx': 2,
     'slug': 'basel-sensory-communication-home-nonverbal-autism-support-adults',
     'care_level': 4,
     'cognitive_support_level': 4,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de'],
     'min_age': 18,
     'max_age': 120,
     'translations': {'de': {'title': 'Basel Sensory & Communication Home — Nonverbal Autism Support '
                                      '(Adults)',
                             'description': 'BESCHREIBUNG:\n'
                                            'Erwachsene (18+). Unterstützung bei nonverbalem Autismus: '
                                            'visuelle Kommunikationshilfen, vorhersehbare Routinen und '
                                            'geringe sensorische Überlastung. Barrierefrei; ruhiger '
                                            'Umgang des Personals.'}},
     'provider_name': 'Ticino Wellness Homes'},
    {'provider_idx': 2,
     'slug': 'bern-blind-friendly-studio-orientation-training-tactile-markers',
     'care_level': 1,
     'cognitive_support_level': 1,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': True,
     'languages_supported': ['de'],
     'min_age': 0,
     'max_age': 120,
     'translations': {'de': {'title': 'Bern Blind-Friendly Studio — Orientation Training & Tactile '
                                      'Markers',
                             'description': 'Beschreibung:\n'
                                            'Unterstützung für Blinde: taktile Markierungen, '
                                            'konsistente Anordnung, optionale Orientierungs Schulungen '
                                            'und Personal, das mit barrierefreier Technik vertraut '
                                            'ist. Rollstuhlgerechter Eingang.'}},
     'provider_name': 'Ticino Wellness Homes'},
    {'provider_idx': 2,
     'slug': 'bern-family-style-home-ages-612-developmental-delay-support',
     'care_level': 3,
     'cognitive_support_level': 4,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de'],
     'min_age': 6,
     'max_age': 12,
     'translations': {'de': {'title': 'Bern Family-Style Home (Ages 6–12) — Developmental Delay '
                                      'Support',
                             'description': 'BESCHREIBUNG:\n'
                                            'Altersbeschränkung: 6–12. Unterstützung bei '
                                            'Entwicklungsverzögerungen durch strukturierte Abläufe, '
                                            'sanfte Anleitung und familiäre Umgebung. Barrierefreier '
                                            'Zugang; ruhige sensorische Räume.'}},
     'provider_name': 'Ticino Wellness Homes'},
    {'provider_idx': 2,
     'slug': 'bern-supported-living-bipolar-routine-medication-support-adults',
     'care_level': 2,
     'cognitive_support_level': 2,
     'wheelchair_accessible': False,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de'],
     'min_age': 18,
     'max_age': 120,
     'translations': {'de': {'title': 'Bern Supported Living — Bipolar Routine & Medication Support '
                                      '(Adults)',
                             'description': 'BESCHREIBUNG:\n'
                                            'Erwachsene (18+). Unterstützung bei stabilen Routinen, '
                                            'Erinnerungen an die Medikation und Planung der '
                                            'Schlafhygiene. Mitarbeiter-Kontrollen; ruhige Umgebung '
                                            'und optionale Teilnahme an Peer-Gruppen.'}},
     'provider_name': 'Ticino Wellness Homes'},
    {'provider_idx': 2,
     'slug': 'bern-youth-supported-apartment-ages-1117-adhd-school-routine',
     'care_level': 2,
     'cognitive_support_level': 2,
     'wheelchair_accessible': False,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de'],
     'min_age': 11,
     'max_age': 17,
     'translations': {'de': {'title': 'Bern Youth Supported Apartment (Ages 11–17) — ADHD & School '
                                      'Routine',
                             'description': 'BESCHREIBUNG:\n'
                                            'Altersbeschränkung: Jugendliche (11–17 Jahre). '
                                            'Unterstützung bei ADHS: Zeitstruktur-Coaching, '
                                            'Hausaufgabenroutinen, konfliktfreie Kommunikation und '
                                            'Fähigkeiten für ein selbstständiges Leben. In der Nähe '
                                            'von öffentlichen Verkehrsmitteln. Optional ruhiger '
                                            'Studienraum.'}},
     'provider_name': 'Ticino Wellness Homes'},
    {'provider_idx': 2,
     'slug': 'zurich-chronic-pain-friendly-flat-flexible-support-quiet-environment',
     'care_level': 2,
     'cognitive_support_level': 1,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de'],
     'min_age': 0,
     'max_age': 120,
     'translations': {'de': {'title': 'Zurich Chronic Pain-Friendly Flat — Flexible Support & Quiet '
                                      'Environment',
                             'description': 'Beschreibung:\n'
                                            'Ruhige Umgebung mit flexibler Unterstützung für '
                                            'chronische Schmerzen und Müdigkeit. Barrierefreies '
                                            'Gebäude; optionale Hilfe bei Besorgungen und der '
                                            'Zubereitung von Mahlzeiten.'}},
     'provider_name': 'Ticino Wellness Homes'},
    {'provider_idx': 2,
     'slug': 'zurich-supported-living-cluster-moderate-intellectual-disability-adults',
     'care_level': 2,
     'cognitive_support_level': 4,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de'],
     'min_age': 0,
     'max_age': 120,
     'translations': {'de': {'title': 'Zurich Supported Living Cluster — Moderate Intellectual '
                                      'Disability (Adults)',
                             'description': 'Beschreibung:\n'
                                            'Erwachsenenorientierte, semi-unabhängige Einheiten mit '
                                            'Coaching für Kochen, Budgetierung und Transport. Klare '
                                            'Routinen, konfliktarme Unterstützung, optionale '
                                            'Jobkoordination. Rollstuhlgerechter Eingang.'}},
     'provider_name': 'Ticino Wellness Homes'},
    {'provider_idx': 3,
     'slug': 'basel-aphasia-support-residence-communication-tools-patience',
     'care_level': 3,
     'cognitive_support_level': 3,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de'],
     'min_age': 0,
     'max_age': 120,
     'translations': {'de': {'title': 'Basel Aphasia-Support Residence — Communication Tools & '
                                      'Patience',
                             'description': 'Aphasie-Unterstützungsumgebung mit Kommunikationsboards, '
                                            'schriftlichen Aufforderungen und geschultem Personal, das '
                                            'Zeit einräumt. Rollstuhlgerecht; strukturierte Routine '
                                            'reduziert Stress.'}},
     'provider_name': 'Bern Inclusion Partners'},
    {'provider_idx': 3,
     'slug': 'basel-complex-needs-residence-wheelchair-hearing-support-adults',
     'care_level': 4,
     'cognitive_support_level': 3,
     'wheelchair_accessible': True,
     'hearing_support': True,
     'visual_support': False,
     'languages_supported': ['de'],
     'min_age': 18,
     'max_age': 120,
     'translations': {'de': {'title': 'Basel Complex Needs Residence — Wheelchair + Hearing Support '
                                      '(Adults)',
                             'description': 'BESCHREIBUNG:\n'
                                            'Erwachsene (18+). Unterstützt kombinierte Mobilitäts- und '
                                            'Hörbedürfnisse: barrierefreier Zugang, visuelle Signale, '
                                            'strukturierte Routine und geschultes Personal in der '
                                            'Patientenkommunikation. Ruhig und vorhersehbar.'}},
     'provider_name': 'Bern Inclusion Partners'},
    {'provider_idx': 3,
     'slug': 'basel-supported-living-mild-cognitive-impairment-adults',
     'care_level': 2,
     'cognitive_support_level': 2,
     'wheelchair_accessible': False,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de'],
     'min_age': 18,
     'max_age': 120,
     'translations': {'de': {'title': 'Basel Supported Living — Mild Cognitive Impairment (Adults)',
                             'description': 'BESCHREIBUNG:\n'
                                            'Erwachsene (18+). Leichte kognitive Unterstützung: '
                                            'Erinnerungen, Strukturierung von Routinen und '
                                            'Terminkoordination. Fokus auf Unabhängigkeit mit leichter '
                                            'Aufsicht.'}},
     'provider_name': 'Bern Inclusion Partners'},
    {'provider_idx': 3,
     'slug': 'bern-sensory-calm-studio-autism-low-stimulation-adults',
     'care_level': 1,
     'cognitive_support_level': 3,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de'],
     'min_age': 18,
     'max_age': 120,
     'translations': {'de': {'title': 'Bern Sensory-Calm Studio — Autism & Low Stimulation (Adults)',
                             'description': 'BESCHREIBUNG:\n'
                                            'Erwachsene (18+). Sinnesberuhigende Umgebung: reduzierte '
                                            'Geräuschkulisse, neutrales Licht, konsistente Routinen '
                                            'und optionale soziale Unterstützung. Barrierefreies '
                                            'Gebäude.'}},
     'provider_name': 'Bern Inclusion Partners'},
    {'provider_idx': 3,
     'slug': 'geneva-als-friendly-living-progressive-mobility-respiratory-planning',
     'care_level': 4,
     'cognitive_support_level': 1,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de', 'fr'],
     'min_age': 0,
     'max_age': 120,
     'translations': {'de': {'title': 'Geneva ALS-Friendly Living — Progressive Mobility & Respiratory '
                                      'Planning',
                             'description': 'Rollstuhlgerechtes Zuhause mit Personal, das mit '
                                            'fortschreitenden Mobilitätsbedürfnissen vertraut ist. '
                                            'Unterstützung bei der Planung von Hilfsmitteln und '
                                            'Routinen. Ruhige Umgebung; flexible '
                                            'Unterstützungsniveaus.'},
                      'fr': {'title': 'Geneva ALS-Friendly Living — Progressive Mobility & Respiratory '
                                      'Planning',
                             'description': 'Maison accessible aux fauteuils roulants avec du '
                                            'personnel familiarisé avec les besoins de mobilité '
                                            'progressive. Planification de soutien pour les '
                                            "dispositifs d'assistance et les routines. Environnement "
                                            'calme ; niveaux de soutien flexibles.'}},
     'provider_name': 'Bern Inclusion Partners'},
    {'provider_idx': 3,
     'slug': 'geneva-assisted-living-parkinsons-mobility-routine-adults',
     'care_level': 3,
     'cognitive_support_level': 2,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de', 'fr'],
     'min_age': 0,
     'max_age': 120,
     'translations': {'de': {'title': 'Geneva Assisted Living — Parkinson’s Mobility & Routine '
                                      '(Adults)',
                             'description': 'Beschreibung:\n'
                                            'Unterstützung bei Parkinson: mobilitätsbewusste Routinen, '
                                            'sturzrisikobewusste Gestaltung und Hilfe bei täglichen '
                                            'Aufgaben. Rollstuhlgerecht; ruhige Umgebung.'},
                      'fr': {'title': 'Geneva Assisted Living — Parkinson’s Mobility & Routine '
                                      '(Adults)',
                             'description': 'DESCRIPTION :\n'
                                            'Soutien pour la maladie de Parkinson : routines adaptées '
                                            'à la mobilité, aménagement tenant compte du risque de '
                                            'chute et aide aux tâches quotidiennes. Accessible en '
                                            'fauteuil roulant ; environnement calme.'}},
     'provider_name': 'Bern Inclusion Partners'},
    {'provider_idx': 3,
     'slug': 'geneva-supported-apartment-schizophrenia-support-daily-structure-adults',
     'care_level': 3,
     'cognitive_support_level': 3,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de', 'fr'],
     'min_age': 18,
     'max_age': 120,
     'translations': {'de': {'title': 'Geneva Supported Apartment — Schizophrenia Support & Daily '
                                      'Structure (Adults)',
                             'description': 'BESCHREIBUNG:\n'
                                            'Erwachsene (18+). Tägliche Struktur, unterstützte '
                                            'Gemeinschaftsintegration und sanfte Aufsicht. Fokus auf '
                                            'vorhersehbare Routine und Fähigkeiten zum selbständigen '
                                            'Leben; abends Personal vorhanden.'},
                      'fr': {'title': 'Geneva Supported Apartment — Schizophrenia Support & Daily '
                                      'Structure (Adults)',
                             'description': 'DESCRIPTION :\n'
                                            'Adultes (18 ans et plus). Structure quotidienne, '
                                            'intégration communautaire soutenue et supervision douce. '
                                            'Accent sur une routine prévisible et les compétences de '
                                            'vie autonome ; personnel présent en soirée.'}},
     'provider_name': 'Bern Inclusion Partners'},
    {'provider_idx': 3,
     'slug': 'geneva-teen-mental-health-step-down-ages-1317-stabilization-routine',
     'care_level': 3,
     'cognitive_support_level': 3,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de', 'fr'],
     'min_age': 13,
     'max_age': 17,
     'translations': {'de': {'title': 'Geneva Teen Mental Health Step-Down (Ages 13–17) — '
                                      'Stabilization & Routine',
                             'description': 'BESCHREIBUNG:  \n'
                                            'Altersbeschränkung: Jugendliche (13–17). Stufenweise '
                                            'Betreuung zur Stabilisierung von Stimmung/Angst, tägliche '
                                            'Struktur, unterstützte Bewältigungsstrategien und '
                                            'Familienkoordination. Nicht-klinische, ruhige Umgebung. '
                                            'Abends besetzt.'},
                      'fr': {'title': 'Geneva Teen Mental Health Step-Down (Ages 13–17) — '
                                      'Stabilization & Routine',
                             'description': 'DESCRIPTION :\n'
                                            "Restriction d'âge : adolescents (13-17 ans). Vie en "
                                            'milieu encadré pour la stabilisation de '
                                            "l'humeur/l'anxiété, structure quotidienne, stratégies de "
                                            'coping soutenues et coordination familiale. Cadre calme, '
                                            'non hospitalier. Personnel présent en soirée.'}},
     'provider_name': 'Bern Inclusion Partners'},
    {'provider_idx': 4,
     'slug': 'basel-deaf-friendly-studio-sign-support-visual-alerts',
     'care_level': 1,
     'cognitive_support_level': 1,
     'wheelchair_accessible': True,
     'hearing_support': True,
     'visual_support': False,
     'languages_supported': ['de'],
     'min_age': 0,
     'max_age': 120,
     'translations': {'de': {'title': 'Basel Deaf-Friendly Studio — Sign-Support & Visual Alerts',
                             'description': 'BESCHREIBUNG:\n'
                                            'Für hörgeschädigte Bewohner konzipiert: visuelle '
                                            'Türklingel/Feueralarme, Personal mit Kenntnissen in '
                                            'Gebärdensprache und schriftlicher Kommunikation. '
                                            'Barrierefreier Eingang und Badezimmer. Ruhiges Gebäude '
                                            'mit geringer Lärmbelastung.'}},
     'provider_name': 'Basel Neuro & Mobility'},
    {'provider_idx': 4,
     'slug': 'geneva-accessible-shared-flat-social-support-light-care-adults',
     'care_level': 2,
     'cognitive_support_level': 2,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de', 'fr'],
     'min_age': 0,
     'max_age': 120,
     'translations': {'de': {'title': 'Geneva Accessible Shared Flat — Social Support & Light Care '
                                      '(Adults)',
                             'description': 'WG mit leichter Pflegeunterstützung: Essensplanung, '
                                            'Erinnerungen und optionales soziales Coaching. '
                                            'Rollstuhlgerechte Gemeinschaftsbereiche; mehrsprachiges '
                                            'Personal.'},
                      'fr': {'title': 'Geneva Accessible Shared Flat — Social Support & Light Care '
                                      '(Adults)',
                             'description': 'DESCRIPTION :\n'
                                            'Appartement partagé avec soutien léger : planification '
                                            'des repas, rappels et coaching social optionnel. Espaces '
                                            'communs accessibles en fauteuil roulant ; personnel '
                                            'multilingue.'}},
     'provider_name': 'Basel Neuro & Mobility'},
    {'provider_idx': 4,
     'slug': 'geneva-autism-support-shared-apartment-social-skills-boundaries-1830',
     'care_level': 2,
     'cognitive_support_level': 3,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de', 'fr'],
     'min_age': 18,
     'max_age': 30,
     'translations': {'de': {'title': 'Geneva Autism-Support Shared Apartment — Social Skills & '
                                      'Boundaries (18–30)',
                             'description': 'BESCHREIBUNG:\n'
                                            'Altersbeschränkung: 18–30. Unterstützung für soziale '
                                            'Grenzen, Kommunikation im gemeinschaftlichen Wohnen und '
                                            'Routinen. Optionaler Ruheraum; Unterstützung durch das '
                                            'Personal bei Bedarf. Barrierefrei.'},
                      'fr': {'title': 'Geneva Autism-Support Shared Apartment — Social Skills & '
                                      'Boundaries (18–30)',
                             'description': 'DESCRIPTION :\n'
                                            "Restriction d'âge : 18-30 ans. Soutien pour les limites "
                                            'sociales, communication en colocation et routines. '
                                            'Chambre calme optionnelle ; soutien du personnel en cas '
                                            'de besoin. Accessible aux fauteuils roulants.'}},
     'provider_name': 'Basel Neuro & Mobility'},
    {'provider_idx': 4,
     'slug': 'geneva-guide-dog-friendly-accessible-apartment-low-vision-mobility',
     'care_level': 1,
     'cognitive_support_level': 1,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': True,
     'languages_supported': ['de', 'fr'],
     'min_age': 0,
     'max_age': 120,
     'translations': {'de': {'title': 'Geneva Guide-Dog Friendly Accessible Apartment — Low Vision & '
                                      'Mobility',
                             'description': 'Führhundfreundlich. Unterstützung für Menschen mit '
                                            'Sehbehinderung durch konsistente Raumaufteilung und '
                                            'barrierefreien Verkehr. Rollstuhlgerechter Eingang und '
                                            'Badezimmer.'},
                      'fr': {'title': 'Geneva Guide-Dog Friendly Accessible Apartment — Low Vision & '
                                      'Mobility',
                             'description': 'DESCRIPTION :\n'
                                            'Acceptant les chiens-guides. Soutien pour les personnes '
                                            'malvoyantes avec un aménagement cohérent et des '
                                            'transports accessibles. Entrée et salle de bain '
                                            'accessibles aux fauteuils roulants.'}},
     'provider_name': 'Basel Neuro & Mobility'},
    {'provider_idx': 4,
     'slug': 'geneva-ptsd-informed-supported-living-adults-calm-choice',
     'care_level': 2,
     'cognitive_support_level': 2,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de', 'fr'],
     'min_age': 18,
     'max_age': 120,
     'translations': {'de': {'title': 'Geneva PTSD-Informed Supported Living (Adults) — Calm & Choice',
                             'description': 'BESCHREIBUNG:\n'
                                            'Erwachsene (18+). Trauma-informierte Umgebung mit '
                                            'vorhersehbaren Abläufen, Wahlmöglichkeiten für die '
                                            'Bewohner und ruhigen Räumen. Optionale Unterstützung für '
                                            'Bewältigungsstrategien; keine geschlossene Einrichtung.'},
                      'fr': {'title': 'Geneva PTSD-Informed Supported Living (Adults) — Calm & Choice',
                             'description': 'DESCRIPTION :\n'
                                            'Adultes (18+). Environnement informé sur les traumatismes '
                                            'avec des routines prévisibles, choix des résidents et '
                                            'espaces calmes. Coaching optionnel pour des stratégies '
                                            "d'adaptation ; pas d'établissement fermé."}},
     'provider_name': 'Basel Neuro & Mobility'},
    {'provider_idx': 4,
     'slug': 'zurich-high-independence-accessible-studio-wheelchair-adults',
     'care_level': 1,
     'cognitive_support_level': 1,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de'],
     'min_age': 0,
     'max_age': 120,
     'translations': {'de': {'title': 'Zurich High Independence Accessible Studio — Wheelchair '
                                      '(Adults)',
                             'description': 'Rollstuhlgerechtes Studio für hochgradig unabhängige '
                                            'Bewohner: barrierefreier Zugang, zugängliches Badezimmer, '
                                            'in der Nähe von Verkehrsanbindungen. Minimale Pflege '
                                            'erforderlich.'}},
     'provider_name': 'Basel Neuro & Mobility'},
    {'provider_idx': 4,
     'slug': 'zurich-ms-support-apartment-fatigue-aware-routines',
     'care_level': 2,
     'cognitive_support_level': 1,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de'],
     'min_age': 0,
     'max_age': 120,
     'translations': {'de': {'title': 'Zurich MS Support Apartment — Fatigue-Aware Routines',
                             'description': 'Rollstuhlgerechte Wohnung mit ermüdungsbewusster '
                                            'Terminplanung, optionaler Essensunterstützung und '
                                            'barrierefreiem Nahverkehr in der Nähe. Geeignet für MS '
                                            'mit variablen Mobilitätstagen.'}},
     'provider_name': 'Basel Neuro & Mobility'},
    {'provider_idx': 4,
     'slug': 'zurich-sober-living-house-structured-recovery-18',
     'care_level': 2,
     'cognitive_support_level': 2,
     'wheelchair_accessible': False,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de'],
     'min_age': 18,
     'max_age': 120,
     'translations': {'de': {'title': 'Zurich Sober Living House — Structured Recovery (18+)',
                             'description': 'BESCHREIBUNG:\n'
                                            'Altersbeschränkung: 18+. Nüchternes Wohnen mit '
                                            'strukturierten Routinen, gegenseitiger Verantwortung, '
                                            'unterstützenden Gemeinschaftsversammlungen und '
                                            'Rückfallpräventionsplanung. Keine medizinische '
                                            'Einrichtung; erfordert Engagement für Nüchternheit.'}},
     'provider_name': 'Basel Neuro & Mobility'},
    {'provider_idx': 5,
     'slug': 'basel-dual-diagnosis-step-down-recovery-mental-health-support-adults',
     'care_level': 3,
     'cognitive_support_level': 3,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de'],
     'min_age': 18,
     'max_age': 120,
     'translations': {'de': {'title': 'Basel Dual-Diagnosis Step-Down — Recovery + Mental Health '
                                      'Support (Adults)',
                             'description': 'BESCHREIBUNG:\n'
                                            'Erwachsene (18+). Wohnheim zur Unterstützung der Genesung '
                                            'in Verbindung mit psychischen Gesundheitsbedürfnissen. '
                                            'Strukturierter Tagesablauf, Coaching und Unterstützung '
                                            'durch das Personal. Ruhige Umgebung; vorhersehbare '
                                            'Regeln.'}},
     'provider_name': 'Geneva Accessible Residences'},
    {'provider_idx': 5,
     'slug': 'basel-stroke-rehab-residence-structured-relearning-routines',
     'care_level': 4,
     'cognitive_support_level': 3,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de'],
     'min_age': 0,
     'max_age': 120,
     'translations': {'de': {'title': 'Basel Stroke Rehab Residence — Structured Relearning Routines',
                             'description': 'Betriebsunterstützung nach Schlaganfall mit '
                                            'strukturierten täglichen Abläufen, Mobilitätsübungen und '
                                            'Erinnerungen für Medikamente. Rollstuhlgerecht, ruhige '
                                            'Umgebung. Unterstützt leichte Aphasie mit '
                                            'patientenorientierter Kommunikation.'}},
     'provider_name': 'Geneva Accessible Residences'},
    {'provider_idx': 5,
     'slug': 'bern-247-high-support-home-severe-cognitive-disabilities-adults',
     'care_level': 5,
     'cognitive_support_level': 5,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de', 'fr'],
     'min_age': 18,
     'max_age': 120,
     'translations': {'de': {'title': 'Bern 24/7 High-Support Home — Severe Cognitive Disabilities '
                                      '(Adults)',
                             'description': 'BESCHREIBUNG:\n'
                                            'Erwachsene (18+). Rund-um-die-Uhr betreute Unterstützung '
                                            'für schwere kognitive Behinderungen, die ständige Hilfe '
                                            'erfordern. Strukturierte Abläufe, unterstützte '
                                            'persönliche Pflege und ruhige Umgebung. '
                                            'Rollstuhlgerecht.'},
                      'fr': {'title': 'Bern 24/7 High-Support Home — Severe Cognitive Disabilities '
                                      '(Adults)',
                             'description': 'DESCRIPTION :\n'
                                            'Adultes (18+). Soutien 24/7 pour des handicaps cognitifs '
                                            'sévères nécessitant une assistance constante. Routines '
                                            'structurées, soins personnels assistés et environnement '
                                            'calme. Accessible en fauteuil roulant.'}},
     'provider_name': 'Geneva Accessible Residences'},
    {'provider_idx': 5,
     'slug': 'lausanne-supported-home-55-early-retirement-with-light-care',
     'care_level': 2,
     'cognitive_support_level': 2,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de', 'fr'],
     'min_age': 55,
     'max_age': 120,
     'translations': {'de': {'title': 'Lausanne Supported Home (55+) — Early Retirement with Light '
                                      'Care',
                             'description': 'Beschreibung: Altersbeschränkung: 55+. Für '
                                            'Frühruheständler, die leichte Unterstützung benötigen: '
                                            'Erinnerungen, Essensunterstützungsoption, barrierefreies '
                                            'Gebäude und ruhige Gemeinschaft.'},
                      'fr': {'title': 'Lausanne Supported Home (55+) — Early Retirement with Light '
                                      'Care',
                             'description': 'DESCRIPTION :\n'
                                            "Restriction d'âge : 55 ans et plus. Pour les résidents en "
                                            'pré-retraite ayant besoin de soins légers : rappels, '
                                            'option de soutien aux repas, bâtiment accessible et '
                                            'communauté calme.'}},
     'provider_name': 'Geneva Accessible Residences'},
    {'provider_idx': 5,
     'slug': 'lugano-low-vision-apartment-orientation-friendly-layout',
     'care_level': 1,
     'cognitive_support_level': 1,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': True,
     'languages_supported': ['de', 'it'],
     'min_age': 0,
     'max_age': 120,
     'translations': {'de': {'title': 'Lugano Low-Vision Apartment — Orientation-Friendly Layout',
                             'description': 'B Unterstützung für Menschen mit Sehbehinderung: '
                                            'hochkontrastierende Wegführung, konsistente Möblierung, '
                                            'taktile Markierungen und optionale Mobilitätsschulung. '
                                            'Barrierefrei. In der Nähe von Dienstleistungen.'},
                      'it': {'title': 'Lugano Low-Vision Apartment — Orientation-Friendly Layout',
                             'description': 'DESCRIZIONE:\n'
                                            'Supporto per persone con visione ridotta: segnaletica ad '
                                            'alto contrasto, disposizione dei mobili coerente, '
                                            'marcatori tattili e coaching per la mobilità opzionale. '
                                            'Accessibile in sedia a rotelle. Vicino ai servizi.'}},
     'provider_name': 'Geneva Accessible Residences'},
    {'provider_idx': 5,
     'slug': 'zurich-eating-support-residence-adults-meal-structure-coaching',
     'care_level': 3,
     'cognitive_support_level': 2,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de'],
     'min_age': 18,
     'max_age': 120,
     'translations': {'de': {'title': 'Zurich Eating Support Residence (Adults) — Meal Structure & '
                                      'Coaching',
                             'description': 'BESCHREIBUNG:\n'
                                            'Erwachsene (18+). Strukturierte Essensunterstützung und '
                                            'Coaching für konsistente Routinen. Unterstützende '
                                            'Umgebung; Mitarbeiter-Check-ins. Rollstuhlgerechtes '
                                            'Gebäude.'}},
     'provider_name': 'Geneva Accessible Residences'},
    {'provider_idx': 5,
     'slug': 'zurich-memory-care-residence-65-early-dementia-support',
     'care_level': 4,
     'cognitive_support_level': 4,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de'],
     'min_age': 65,
     'max_age': 120,
     'translations': {'de': {'title': 'Zurich Memory-Care Residence (65+) — Early Dementia Support',
                             'description': 'BESCHREIBUNG:\n'
                                            'Altersbeschränkung: 65+. Unterstützung bei leichter '
                                            'Demenz mit Orientierungshilfen, Medikamentenerinnerungen, '
                                            'strukturiertem Tagesablauf und ruhigen '
                                            'Gemeinschaftsräumen. Barrierefrei.'}},
     'provider_name': 'Geneva Accessible Residences'},
    {'provider_idx': 5,
     'slug': 'zurich-quiet-residence-severe-anxiety-support-adults',
     'care_level': 2,
     'cognitive_support_level': 2,
     'wheelchair_accessible': True,
     'hearing_support': False,
     'visual_support': False,
     'languages_supported': ['de'],
     'min_age': 18,
     'max_age': 120,
     'translations': {'de': {'title': 'Zurich Quiet Residence — Severe Anxiety Support (Adults)',
                             'description': 'BESCHREIBUNG:\n'
                                            'Erwachsene (18+). Ruhige Umgebung, vorhersehbare Abläufe '
                                            'und unterstützte Expositionsplanung. Personal-Kontrollen; '
                                            'ruhiges Gebäude. Rollstuhlgerechter Eingang.'}},
     'provider_name': 'Geneva Accessible Residences'},
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "bern-barrierefreies-studio-balkon-18plus",
        "care_level": 2,
        "cognitive_support_level": 0,
        "wheelchair_accessible": True,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 120,
        "translations": {
            "de": {
                "title": "Bern Barrierefreies Studio mit Balkon (18+)",
                "description": "BESCHREIBUNG:\nRollstuhlgängiges Studio mit schwellenlosen Türen, unterfahrbarer Küche und bodenebener Dusche. Großer Balkon mit breiter Schiebetür. Ruhige Lage, ÖV-nah; ideal bei Mobilitätseinschränkung."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "zuerich-autismusfreundliche-wg-reizarm-18plus",
        "care_level": 2,
        "cognitive_support_level": 2,
        "wheelchair_accessible": False,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 55,
        "translations": {
            "de": {
                "title": "Zürich Autismusfreundliche WG (reizarm, 18+)",
                "description": "BESCHREIBUNG:\nReizarmes WG-Setting mit klaren Regeln, ruhigen Gemeinschaftsbereichen (gedimmtes Licht, leise Geräte) und Rückzugsraum. Planbare Wochenroutine; geeignet bei Autismus-Spektrum und sensorischer Überlastung."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "basel-adhs-apartment-struktur-coaching-18plus",
        "care_level": 2,
        "cognitive_support_level": 1,
        "wheelchair_accessible": False,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 45,
        "translations": {
            "de": {
                "title": "Basel Apartment mit Strukturhilfe (ADHS, 18+)",
                "description": "BESCHREIBUNG:\nKompaktes Apartment mit optionalem Struktur-Coaching (Alltag, Termine, Budget) und ruhiger Arbeitsnische. Gute Schallschutzfenster und einfache Ablagesysteme; passend für Menschen mit ADHS."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "luzern-demenz-wohngruppe-65plus",
        "care_level": 4,
        "cognitive_support_level": 3,
        "wheelchair_accessible": True,
        "hearing_support": False,
        "visual_support": True,
        "languages_supported": ["de"],
        "min_age": 65,
        "max_age": 120,
        "translations": {
            "de": {
                "title": "Luzern Demenz-Wohngruppe (65+)",
                "description": "BESCHREIBUNG:\nKleine Wohngruppe mit demenzbewussten Routinen, gut lesbarer Beschilderung und sicherer Wegeführung. Barrierefrei, rutschhemmende Böden und gute Ausleuchtung zur Orientierung. Betreuung bis 24/7 möglich."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "winterthur-wohnung-hoerunterstuetzung-18plus",
        "care_level": 1,
        "cognitive_support_level": 0,
        "wheelchair_accessible": False,
        "hearing_support": True,
        "visual_support": True,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 120,
        "translations": {
            "de": {
                "title": "Winterthur Wohnung mit Hör-Unterstützung (18+)",
                "description": "BESCHREIBUNG:\nLichtklingel und visuelle Alarmoptionen, gute Beleuchtung für Lippenlesen/Gebärden. Übersichtliche Raumaufteilung und ruhiges Haus. Geeignet bei Schwerhörigkeit oder Gehörlosigkeit."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "stgallen-wohnung-sehbehinderung-kontraste-18plus",
        "care_level": 1,
        "cognitive_support_level": 0,
        "wheelchair_accessible": False,
        "hearing_support": False,
        "visual_support": True,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 120,
        "translations": {
            "de": {
                "title": "St. Gallen Wohnung für Sehbehinderung (18+)",
                "description": "BESCHREIBUNG:\nBlendfreie Beleuchtung, kontrastreiche Markierungen und klare Wegeführung. Optional taktile Markierungen an Türen/Küche. Geeignet bei Sehbehinderung oder Blindheit."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "bern-epilepsie-apartment-notfallplan-18plus",
        "care_level": 2,
        "cognitive_support_level": 1,
        "wheelchair_accessible": True,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 120,
        "translations": {
            "de": {
                "title": "Bern Epilepsie-Apartment (Notfallplan, 18+)",
                "description": "BESCHREIBUNG:\nEpilepsie-bewusstes Umfeld: individueller Notfallplan, optional Nacht-Check-in und geschultes Personal. Barrierefrei, rutschhemmende Böden und sichere Badgestaltung."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "thun-traumasensible-wg-ptbs-18plus",
        "care_level": 2,
        "cognitive_support_level": 1,
        "wheelchair_accessible": False,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 65,
        "translations": {
            "de": {
                "title": "Thun Traumasensible WG (PTBS, 18+)",
                "description": "BESCHREIBUNG:\nRuhige WG mit traumasensiblen Absprachen (klare Besucherregeln, vorhersehbare Abläufe, Rückzugsoption). Geeignet bei PTBS/Traumafolgen und Angst. Optional: Stabilisierungsgespräche."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "biel-suchtfreie-uebergangswohnung-18plus",
        "care_level": 3,
        "cognitive_support_level": 1,
        "wheelchair_accessible": True,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 70,
        "translations": {
            "de": {
                "title": "Biel Suchtfreie Übergangswohnung (18+)",
                "description": "BESCHREIBUNG:\nSubstanzfreie Wohnform mit klaren Regeln, Unterstützung bei Tagesstruktur und Anbindung an Therapie/Sozialarbeit. Barrierefrei. Für Menschen in Stabilisierung nach Abhängigkeitserkrankung."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "zug-wohnung-bipolar-krisenplan-18plus",
        "care_level": 2,
        "cognitive_support_level": 1,
        "wheelchair_accessible": False,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 65,
        "translations": {
            "de": {
                "title": "Zug Wohnung mit Krisenplan (Bipolar, 18+)",
                "description": "BESCHREIBUNG:\nEinzelwohnung mit optionalem Krisen- und Medikamentenplan sowie regelmäßigen Check-ins. Ruhige Umgebung, gut erreichbar. Geeignet für Menschen mit bipolarer Störung, die ein Sicherheitsnetz wünschen."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "solothurn-unterstuetztes-wohnen-psychose-18plus",
        "care_level": 3,
        "cognitive_support_level": 2,
        "wheelchair_accessible": False,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 70,
        "translations": {
            "de": {
                "title": "Solothurn Unterstütztes Wohnen (Psychose, 18+)",
                "description": "BESCHREIBUNG:\nStabilitätsorientiertes Setting mit klarer Tagesstruktur, Deeskalation und optionaler Unterstützung bei Medikamentenroutine. Reizarme Umgebung, private Rückzugsmöglichkeiten. Für Menschen mit Psychose-Erfahrungen."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "aarau-wohngruppe-intellektuelle-beeintraechtigung-18plus",
        "care_level": 3,
        "cognitive_support_level": 2,
        "wheelchair_accessible": True,
        "hearing_support": False,
        "visual_support": True,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 80,
        "translations": {
            "de": {
                "title": "Aarau Wohngruppe (kognitiv, 18+)",
                "description": "BESCHREIBUNG:\nKleine Wohngruppe mit Unterstützung bei Haushalt, Kochen und Terminen. Barrierefreier Zugang, visuelle Orientierung (Piktogramme) und klare Abläufe. Geeignet bei intellektueller Beeinträchtigung/Lernschwierigkeiten."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "schaffhausen-ms-wohnung-barrierefrei-18plus",
        "care_level": 2,
        "cognitive_support_level": 1,
        "wheelchair_accessible": True,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 75,
        "translations": {
            "de": {
                "title": "Schaffhausen MS-freundliche Wohnung (18+)",
                "description": "BESCHREIBUNG:\nLift, breite Türen, Haltegriffe und bodenebene Dusche. Geeignet bei Multipler Sklerose oder wechselnder Mobilität. Platz für Rollator/Rollstuhl und ruhiger Hausflur."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "fribourg-wohnen-nach-schlaganfall-40plus",
        "care_level": 3,
        "cognitive_support_level": 2,
        "wheelchair_accessible": True,
        "hearing_support": False,
        "visual_support": True,
        "languages_supported": ["de"],
        "min_age": 40,
        "max_age": 120,
        "translations": {
            "de": {
                "title": "Fribourg Wohnen nach Schlaganfall (40+)",
                "description": "BESCHREIBUNG:\nBarrierefreie Wohnung nahe Therapiepraxen. Gute Beleuchtung, Kontraste zur Orientierung und sichere Badgestaltung. Optional Unterstützung bei Tagesstruktur. Geeignet nach Schlaganfall/neurologischer Reha."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "chur-wohnung-parkinson-lift-55plus",
        "care_level": 3,
        "cognitive_support_level": 1,
        "wheelchair_accessible": True,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["de"],
        "min_age": 55,
        "max_age": 120,
        "translations": {
            "de": {
                "title": "Chur Wohnung für Parkinson (Lift, 55+)",
                "description": "BESCHREIBUNG:\nLift, rutschhemmende Böden, stabile Handläufe und ruhige Umgebung. Küche mit gut greifbaren Griffen. Geeignet bei Parkinson oder Tremor, optional mit Alltagsunterstützung."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "bern-kinderwohngruppe-autismus-8bis12",
        "care_level": 4,
        "cognitive_support_level": 2,
        "wheelchair_accessible": True,
        "hearing_support": False,
        "visual_support": True,
        "languages_supported": ["de"],
        "min_age": 8,
        "max_age": 12,
        "translations": {
            "de": {
                "title": "Bern Kinder-Wohngruppe (Autismus, 8–12)",
                "description": "BESCHREIBUNG:\nKinderwohngruppe mit visuellen Tagesplänen, reizarmen Rückzugsräumen und sicheren Außenflächen. Barrierefrei. Team mit Erfahrung bei Autismus und Entwicklungsverzögerung; enge Zusammenarbeit mit Schule/Therapie."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "zuerich-jugendwohnen-adhs-13bis17",
        "care_level": 4,
        "cognitive_support_level": 2,
        "wheelchair_accessible": False,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["de"],
        "min_age": 13,
        "max_age": 17,
        "translations": {
            "de": {
                "title": "Zürich Jugendwohnen (ADHS, 13–17)",
                "description": "BESCHREIBUNG:\nJugendwohnen mit Lernzeiten, Unterstützung bei Schulorganisation und sozialem Miteinander. Ruhige Zimmer, klare Regeln und verlässliche Betreuung. Geeignet für Jugendliche mit ADHS."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "basel-jugendwohnen-angst-14bis17",
        "care_level": 4,
        "cognitive_support_level": 2,
        "wheelchair_accessible": False,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["de"],
        "min_age": 14,
        "max_age": 17,
        "translations": {
            "de": {
                "title": "Basel Jugendwohnen bei Angst (14–17)",
                "description": "BESCHREIBUNG:\nSicherer Rahmen mit vorhersehbaren Abläufen, Rückzugsoption und Unterstützung bei Schule/Alltag. Geeignet bei Angststörung, Panik oder sozialer Überforderung."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "bern-inklusive-familienwohnung-barrierefrei-0plus",
        "care_level": 3,
        "cognitive_support_level": 1,
        "wheelchair_accessible": True,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["de"],
        "min_age": 0,
        "max_age": 120,
        "translations": {
            "de": {
                "title": "Bern Inklusive Familienwohnung (barrierefrei)",
                "description": "BESCHREIBUNG:\nGroße Wohnung mit Lift, breiten Türen und ebenerdiger Dusche. Platz für Hilfsmittel (z.B. Rollstuhl, Stehgerät). Balkon, Abstellraum und kinderfreundliche Umgebung. Geeignet für Familien mit Kind mit Behinderung."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "bern-moebliertes-apartment-chronische-schmerzen-18plus",
        "care_level": 2,
        "cognitive_support_level": 0,
        "wheelchair_accessible": True,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 120,
        "translations": {
            "de": {
                "title": "Bern Möbliertes Apartment (chronische Schmerzen, 18+)",
                "description": "BESCHREIBUNG:\nErgonomisch möbliert (gute Matratze, höhenverstellbarer Tisch), Lift und barrierefreies Bad. Ruhige Lage, kurze Wege. Geeignet bei chronischen Schmerzen, Fibromyalgie oder EDS; optional Reinigungsservice."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "interlaken-barrierefrei-cerebralparese-16plus",
        "care_level": 3,
        "cognitive_support_level": 1,
        "wheelchair_accessible": True,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["de"],
        "min_age": 16,
        "max_age": 70,
        "translations": {
            "de": {
                "title": "Interlaken Barrierefreies Wohnen (Cerebralparese, 16+)",
                "description": "BESCHREIBUNG:\nSchwellenlos, breite Türen, ausreichend Wendeflächen und Bad mit Haltegriffen. Balkon ebenerdig zugänglich. Geeignet bei Cerebralparese oder neuromuskulären Einschränkungen; Assistenzkoordination möglich."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "olten-uebergangswohnung-nach-klinik-18plus",
        "care_level": 3,
        "cognitive_support_level": 2,
        "wheelchair_accessible": False,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 65,
        "translations": {
            "de": {
                "title": "Olten Übergangswohnung nach Klinik (18+)",
                "description": "BESCHREIBUNG:\nÜbergangswohnung zur Stabilisierung nach psychiatrischem Aufenthalt. Regelmäßige Check-ins, Krisenplan und Unterstützung bei Terminen/Alltag. Geeignet bei Depression, Angst oder Erschöpfung."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "bern-wohngruppe-down-syndrom-18plus",
        "care_level": 3,
        "cognitive_support_level": 2,
        "wheelchair_accessible": True,
        "hearing_support": True,
        "visual_support": False,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 70,
        "translations": {
            "de": {
                "title": "Bern Wohngruppe (Down-Syndrom, 18+)",
                "description": "BESCHREIBUNG:\nWohngruppe mit Unterstützung bei Alltag, Gesundheitsterminen und Kommunikation. Barrierefrei, großzügige Gemeinschaftsräume. Geeignet bei Down-Syndrom, auch bei begleitendem Hörverlust."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "zuerich-stabilisierungswohnung-essstoerung-16plus",
        "care_level": 3,
        "cognitive_support_level": 2,
        "wheelchair_accessible": False,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["de"],
        "min_age": 16,
        "max_age": 40,
        "translations": {
            "de": {
                "title": "Zürich Stabilisierungswohnung (Essstörung, 16+)",
                "description": "BESCHREIBUNG:\nUnterstütztes Wohnen mit Fokus auf Alltagsstruktur und ruhigem Umfeld. Essensplanung/Absprachen in Koordination mit Behandlung möglich. Rückzugsräume und klare Regeln; für Jugendliche und junge Erwachsene."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "basel-wohnung-gehoerlos-visuelle-alarme-18plus",
        "care_level": 1,
        "cognitive_support_level": 0,
        "wheelchair_accessible": False,
        "hearing_support": True,
        "visual_support": True,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 120,
        "translations": {
            "de": {
                "title": "Basel Wohnung für Gehörlose (18+)",
                "description": "BESCHREIBUNG:\nVisuelle Klingel-/Alarmoptionen, gute Beleuchtung und klare Sichtachsen für Gebärdenkommunikation. Ruhiges Haus, gut erreichbar. Geeignet für gehörlose oder stark schwerhörige Personen."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "bern-blindenfreundliches-apartment-taktil-18plus",
        "care_level": 2,
        "cognitive_support_level": 0,
        "wheelchair_accessible": True,
        "hearing_support": False,
        "visual_support": True,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 120,
        "translations": {
            "de": {
                "title": "Bern Blindenfreundliches Apartment (18+)",
                "description": "BESCHREIBUNG:\nTaktile Markierungen, klare Wegeführung und sichere Bad-/Küchenanordnung. Barrierefreier Zugang und genügend Platz für Hilfsmittel. Geeignet bei Blindheit oder starker Sehbehinderung."
            }
        },
    },

    # --- additional DE entries to reach 48 (wide disability + age spread) ---
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "basel-reizarme-wohnung-migraene-18plus",
        "care_level": 1,
        "cognitive_support_level": 0,
        "wheelchair_accessible": False,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 65,
        "translations": {"de": {"title": "Basel Reizarme Wohnung (Migräne, 18+)", "description": "BESCHREIBUNG:\nVerdunkelung, ruhige Lage und wenig Flackerlicht. Geeignet bei Migräne/Photophobie oder sensorischer Sensitivität. Optional: flexible Alltagsunterstützung an schlechten Tagen."}},
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "bern-wohnung-angst-agoraphobie-18plus",
        "care_level": 2,
        "cognitive_support_level": 1,
        "wheelchair_accessible": False,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 70,
        "translations": {"de": {"title": "Bern Geschütztes Wohnen (Agoraphobie, 18+)", "description": "BESCHREIBUNG:\nSehr ruhiges Haus mit wenig Publikumsverkehr. Klare Besucherregeln und optional begleitete Wege nach draußen. Für Menschen mit Agoraphobie oder starker sozialer Angst."}},
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "zuerich-wohnung-zwang-struktur-18plus",
        "care_level": 2,
        "cognitive_support_level": 1,
        "wheelchair_accessible": False,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 65,
        "translations": {"de": {"title": "Zürich Wohnung mit Struktur (Zwang, 18+)", "description": "BESCHREIBUNG:\nÜbersichtliche Raumaufteilung und klare Ablagebereiche (nach Wunsch). Unterstützende Begleitung kann an Therapieziele angepasst werden. Geeignet bei Zwangsstörung."}},
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "bern-wohnen-schaedelhirntrauma-18plus",
        "care_level": 3,
        "cognitive_support_level": 2,
        "wheelchair_accessible": True,
        "hearing_support": False,
        "visual_support": True,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 75,
        "translations": {"de": {"title": "Bern Wohnen nach SHT (18+)", "description": "BESCHREIBUNG:\nUnterstütztes Wohnen mit Gedächtnis-/Alltagsstrategien, klarer Beschilderung und sicherer Umgebung. Barrierefrei, gute Beleuchtung. Geeignet nach Schädelhirntrauma mit kognitiven Folgen."}},
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "basel-dbt-orientiert-wohnen-18plus",
        "care_level": 3,
        "cognitive_support_level": 2,
        "wheelchair_accessible": False,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 50,
        "translations": {"de": {"title": "Basel Unterstütztes Wohnen (DBT, 18+)", "description": "BESCHREIBUNG:\nKrisenplan, Skills-Unterstützung (DBT-orientiert), verlässliche Check-ins und Rückzugsraum. Geeignet bei emotionaler Instabilität und Bedarf an Stabilitätsstrukturen."}},
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "bern-seniorenwohnung-rollator-balkon-70plus",
        "care_level": 3,
        "cognitive_support_level": 1,
        "wheelchair_accessible": True,
        "hearing_support": False,
        "visual_support": True,
        "languages_supported": ["de"],
        "min_age": 70,
        "max_age": 120,
        "translations": {"de": {"title": "Bern Seniorenwohnung rollatorfreundlich (70+)", "description": "BESCHREIBUNG:\nLift, breite Türen, bodenebene Dusche und gute Beleuchtung. Balkon mit sicherem Geländer. Optional Notruf und Alltagshilfe; geeignet bei eingeschränkter Mobilität."}},
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "zuerich-inklusive-wg-barrierefrei-18plus",
        "care_level": 2,
        "cognitive_support_level": 1,
        "wheelchair_accessible": True,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 65,
        "translations": {"de": {"title": "Zürich Barrierefreie Inklusive WG (18+)", "description": "BESCHREIBUNG:\nGroßes Zimmer mit Platz für Hilfsmittel, stufenloser Zugang und breite Küche. Gemeinschaftliches Wohnen mit klaren Absprachen; geeignet bei körperlicher Behinderung."}},
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "bern-kurzzeit-studio-pflegebett-18plus",
        "care_level": 4,
        "cognitive_support_level": 1,
        "wheelchair_accessible": True,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 120,
        "translations": {"de": {"title": "Bern Möbliertes Kurzzeit-Studio (18+)", "description": "BESCHREIBUNG:\nMöbliertes Studio für Übergang nach OP/Reha. Barrierefrei, Pflegebett optional, bodenebene Dusche. Ideal bei vorübergehender Mobilitätseinschränkung."}},
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "basel-wohnung-autismus-lichtlaermkontrolle-18plus",
        "care_level": 1,
        "cognitive_support_level": 2,
        "wheelchair_accessible": False,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 60,
        "translations": {"de": {"title": "Basel Wohnung mit Reizkontrolle (Autismus, 18+)", "description": "BESCHREIBUNG:\nVerdunkelung, ruhige Geräte, klare Raumaufteilung und Rückzugsoption. Geeignet bei Autismus-Spektrum oder sensorischer Empfindlichkeit; optional Unterstützungsplan für Alltag."}},
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "bern-wohnung-hirnverletzung-orientierung-18plus",
        "care_level": 3,
        "cognitive_support_level": 3,
        "wheelchair_accessible": True,
        "hearing_support": False,
        "visual_support": True,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 80,
        "translations": {"de": {"title": "Bern Wohnung mit Orientierungshilfen (18+)", "description": "BESCHREIBUNG:\nVisuelle Checklisten, klare Beschriftung und sichere Wege. Barrierefrei, wenig Stolperfallen. Geeignet bei erworbener Hirnverletzung mit Gedächtnis-/Orientierungsproblemen."}},
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "zuerich-wohnung-psychose-fruehwarnplan-18plus",
        "care_level": 3,
        "cognitive_support_level": 2,
        "wheelchair_accessible": False,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 65,
        "translations": {"de": {"title": "Zürich Wohnen mit Frühwarn-Plan (18+)", "description": "BESCHREIBUNG:\nFrühwarnzeichen-Plan, regelmäßige Check-ins und Krisenkontaktkette. Reizarme Umgebung und planbare Struktur; geeignet bei Psychose-Erfahrungen."}},
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "bern-barrierefrei-rampe-dusche-18plus",
        "care_level": 2,
        "cognitive_support_level": 0,
        "wheelchair_accessible": True,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 120,
        "translations": {"de": {"title": "Bern Barrierefreie Wohnung mit Rampe (18+)", "description": "BESCHREIBUNG:\nStufenloser Zugang via Rampe, Lift und bodenebene Dusche. Genügend Wendefläche, Haltegriffe möglich. Geeignet bei Querschnitt, Muskelerkrankung oder allgemeiner Mobilitätseinschränkung."}},
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "basel-uebergangswohnen-autismus-16bis20",
        "care_level": 4,
        "cognitive_support_level": 2,
        "wheelchair_accessible": False,
        "hearing_support": False,
        "visual_support": True,
        "languages_supported": ["de"],
        "min_age": 16,
        "max_age": 20,
        "translations": {"de": {"title": "Basel Übergangswohnen (Autismus, 16–20)", "description": "BESCHREIBUNG:\nÜbergang in die Selbstständigkeit mit visuellen Plänen, Reizreduktion und Begleitung bei Ausbildung/Jobsuche. Für Jugendliche/junge Erwachsene im Autismus-Spektrum."}},
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "bern-wohnplatz-kinder-entwicklungsverzoegerung-6bis10",
        "care_level": 5,
        "cognitive_support_level": 3,
        "wheelchair_accessible": True,
        "hearing_support": True,
        "visual_support": True,
        "languages_supported": ["de"],
        "min_age": 6,
        "max_age": 10,
        "translations": {"de": {"title": "Bern Wohnplatz für Kinder (6–10)", "description": "BESCHREIBUNG:\nIntensives Setting für Kinder mit Entwicklungsverzögerung/komplexen Bedürfnissen. Barrierefrei, sichere Spielzone, visuelle Struktur. Zusammenarbeit mit Physio/Logo/Ergo."}},
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "thun-kurzzeit-krisenintervention-18plus",
        "care_level": 4,
        "cognitive_support_level": 2,
        "wheelchair_accessible": True,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 65,
        "translations": {"de": {"title": "Thun Kurzzeitwohnung Krisenintervention (18+)", "description": "BESCHREIBUNG:\nKurzzeit-Setting mit intensiveren Check-ins, Krisenplan und ruhiger Umgebung. Barrierefrei. Geeignet bei akuter psychischer Belastung, wenn ein stabiler Übergangsraum benötigt wird."}},
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "bern-wohnung-fatigue-energiearm-18plus",
        "care_level": 2,
        "cognitive_support_level": 0,
        "wheelchair_accessible": True,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 120,
        "translations": {"de": {"title": "Bern Ruhiges Wohnen bei Fatigue (18+)", "description": "BESCHREIBUNG:\nLift, kurze Wege und barrierearme Umgebung. Unterstützung bei Energie-Management (Einkauf/Termine) möglich. Geeignet bei ME/CFS, Fatigue nach Krankheit oder chronischer Erschöpfung."}},
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "basel-wohnung-kognitive-hilfen-arbeitsnische-18plus",
        "care_level": 2,
        "cognitive_support_level": 2,
        "wheelchair_accessible": False,
        "hearing_support": False,
        "visual_support": True,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 60,
        "translations": {"de": {"title": "Basel Wohnung mit kognitiven Hilfen (18+)", "description": "BESCHREIBUNG:\nVisuelle Planung (Whiteboard/Checklisten), ruhige Arbeitsnische und Unterstützung bei Tagesstruktur. Geeignet bei kognitiven Einschränkungen (z.B. nach Unfall) und Wiedereinstieg in Ausbildung/Arbeit."}},
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "bern-seniorenwohnung-hoerverlust-75plus",
        "care_level": 3,
        "cognitive_support_level": 1,
        "wheelchair_accessible": True,
        "hearing_support": True,
        "visual_support": True,
        "languages_supported": ["de"],
        "min_age": 75,
        "max_age": 120,
        "translations": {"de": {"title": "Bern Seniorenwohnung mit Hör-Unterstützung (75+)", "description": "BESCHREIBUNG:\nBarrierefrei, Lift und Licht-/Alarmoptionen. Gute Beleuchtung und kontrastreiche Orientierung. Optional Alltagsunterstützung und Notruf; geeignet bei Hörverlust."}},
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "zuerich-demenz-fruehphase-70plus",
        "care_level": 4,
        "cognitive_support_level": 3,
        "wheelchair_accessible": True,
        "hearing_support": False,
        "visual_support": True,
        "languages_supported": ["de"],
        "min_age": 70,
        "max_age": 120,
        "translations": {"de": {"title": "Zürich Demenz-Wohnen (Frühphase, 70+)", "description": "BESCHREIBUNG:\nOrientierungshilfen, klare Routine und sichere Wege. Barrierefrei, gut ausgeleuchtet, wenig Stolperfallen. Geeignet bei Demenz in der Frühphase, mit anpassbarer Betreuungsintensität."}},
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "bern-sturzsichere-wohnung-schwindel-40plus",
        "care_level": 2,
        "cognitive_support_level": 0,
        "wheelchair_accessible": True,
        "hearing_support": True,
        "visual_support": True,
        "languages_supported": ["de"],
        "min_age": 40,
        "max_age": 120,
        "translations": {"de": {"title": "Bern Sturzsichere Wohnung (Schwindel, 40+)", "description": "BESCHREIBUNG:\nSturzprävention: rutschhemmende Böden, Haltegriffe, gute Beleuchtung und klare Kontraste. Barrierefrei. Geeignet bei Gleichgewichtsproblemen oder vestibulären Störungen."}},
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "basel-wohnung-unterstuetzte-kommunikation-18plus",
        "care_level": 3,
        "cognitive_support_level": 2,
        "wheelchair_accessible": True,
        "hearing_support": True,
        "visual_support": True,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 80,
        "translations": {"de": {"title": "Basel Wohnen mit Unterstützter Kommunikation (18+)", "description": "BESCHREIBUNG:\nUnterstützte Kommunikation (leichte Sprache, visuelle Hinweise) möglich. Barrierefrei, ruhige Gesprächszonen. Geeignet bei Sprach-/Kommunikationsbeeinträchtigung (z.B. nach Schlaganfall) oder kognitiven Einschränkungen."}},
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "bern-rollstuhlwohnung-ov-nah-18plus",
        "care_level": 2,
        "cognitive_support_level": 0,
        "wheelchair_accessible": True,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 120,
        "translations": {"de": {"title": "Bern Rollstuhlwohnung nahe ÖV (18+)", "description": "BESCHREIBUNG:\nGroße Wendeflächen, unterfahrbare Küche und barrierefreies Bad. Platz für Assistenz/Spitex-Absprachen. Sehr gute ÖV-Anbindung. Ideal bei dauerhafter Rollstuhlnutzung."}},
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "zuerich-wohnung-assistenzhund-option-18plus",
        "care_level": 2,
        "cognitive_support_level": 1,
        "wheelchair_accessible": False,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 65,
        "translations": {"de": {"title": "Zürich Wohnung mit Assistenzhund-Option (18+)", "description": "BESCHREIBUNG:\nTierfreundlich nach Absprache (Assistenz-/Therapietier). Ruhiges Haus, klare Besucherregeln. Geeignet, wenn ein Tier stabilisierend wirkt (z.B. bei Angst/Trauma). Check-ins optional."}},
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "bern-demenz-und-hoerverlust-70plus",
        "care_level": 4,
        "cognitive_support_level": 3,
        "wheelchair_accessible": True,
        "hearing_support": True,
        "visual_support": True,
        "languages_supported": ["de"],
        "min_age": 70,
        "max_age": 120,
        "translations": {"de": {"title": "Bern Demenz-Wohnen mit Hör-Unterstützung (70+)", "description": "BESCHREIBUNG:\nDemenzbewusste Routine, klare Beschilderung und hörfreundliche Gesprächszonen. Barrierefrei, gut ausgeleuchtet. Geeignet für Senior:innen mit Demenz und Hörbeeinträchtigung."}},
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "basel-wg-junge-erwachsene-18bis25",
        "care_level": 3,
        "cognitive_support_level": 2,
        "wheelchair_accessible": False,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 25,
        "translations": {"de": {"title": "Basel WG für junge Erwachsene (18–25)", "description": "BESCHREIBUNG:\nWG mit Unterstützung in Alltag, Ausbildung/Arbeit und sozialen Themen. Verlässliche Bezugspersonen, klare Regeln und Krisenplan. Geeignet bei psychosozialer Beeinträchtigung."}},
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "bern-ruhiges-studio-balkon-stabilisierung-18plus",
        "care_level": 2,
        "cognitive_support_level": 1,
        "wheelchair_accessible": False,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 65,
        "translations": {"de": {"title": "Bern Ruhiges Studio mit Balkon (18+)", "description": "BESCHREIBUNG:\nStudio mit Balkon als Rückzugsort, helle Räume und ruhige Umgebung. Optional unterstützende Check-ins zur Stabilisierung bei Depression/Angst. Einkauf/ÖV gut erreichbar."}},
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "zuerich-wohnung-kognitiv-begleitet-18plus",
        "care_level": 2,
        "cognitive_support_level": 2,
        "wheelchair_accessible": True,
        "hearing_support": False,
        "visual_support": True,
        "languages_supported": ["de"],
        "min_age": 18,
        "max_age": 75,
        "translations": {"de": {"title": "Zürich Begleitetes Wohnen (kognitiv, 18+)", "description": "BESCHREIBUNG:\nEinzelwohnung mit Unterstützung bei Planung/Haushalt (Checklisten, visuelle Hinweise). Barrierefrei, ruhiges Umfeld. Geeignet bei kognitiver Beeinträchtigung oder nach neurologischem Ereignis."}},
    },

    # 20 more DE entries (to reach 48)
    {
        "provider_idx": 0, "provider_name": "Helvetia Supported Living",
        "slug": "bern-wg-rollstuhl-grosses-zimmer-18plus",
        "care_level": 2, "cognitive_support_level": 0, "wheelchair_accessible": True,
        "hearing_support": False, "visual_support": False, "languages_supported": ["de"],
        "min_age": 18, "max_age": 120,
        "translations": {"de": {"title": "Bern Rollstuhl-WG mit großem Zimmer (18+)", "description": "BESCHREIBUNG:\nBarrierefreie WG, großes Zimmer mit Platz für Hilfsmittel und bodenebene Dusche. Gemeinschaftsküche mit unterfahrbarem Bereich. Geeignet bei dauerhafter Rollstuhlnutzung."}},
    },
    {
        "provider_idx": 0, "provider_name": "Helvetia Supported Living",
        "slug": "zuerich-apartment-soziale-phobie-18plus",
        "care_level": 2, "cognitive_support_level": 1, "wheelchair_accessible": False,
        "hearing_support": False, "visual_support": False, "languages_supported": ["de"],
        "min_age": 18, "max_age": 60,
        "translations": {"de": {"title": "Zürich Apartment bei sozialer Phobie (18+)", "description": "BESCHREIBUNG:\nRuhiges Apartment mit klaren Besucherregeln und gut planbarer Hausumgebung. Optional begleitete Schritte in Richtung Ausbildung/Arbeit. Geeignet bei sozialer Angst/Überforderung."}},
    },
    {
        "provider_idx": 0, "provider_name": "Helvetia Supported Living",
        "slug": "basel-wohnung-ptbs-ruhezone-18plus",
        "care_level": 3, "cognitive_support_level": 2, "wheelchair_accessible": False,
        "hearing_support": False, "visual_support": False, "languages_supported": ["de"],
        "min_age": 18, "max_age": 65,
        "translations": {"de": {"title": "Basel Wohnen mit Ruhezone (PTBS, 18+)", "description": "BESCHREIBUNG:\nWohnung mit separater Rückzugsnische, vorhersehbaren Absprachen und Krisenplan. Geeignet bei PTBS/Traumafolgen; optionale regelmäßige Check-ins zur Stabilisierung."}},
    },
    {
        "provider_idx": 0, "provider_name": "Helvetia Supported Living",
        "slug": "bern-wohnung-depression-tageslicht-18plus",
        "care_level": 2, "cognitive_support_level": 1, "wheelchair_accessible": False,
        "hearing_support": False, "visual_support": False, "languages_supported": ["de"],
        "min_age": 18, "max_age": 70,
        "translations": {"de": {"title": "Bern Helle Wohnung (Depression, 18+)", "description": "BESCHREIBUNG:\nSehr helle Wohnung mit großen Fenstern und ruhiger Lage. Optional: Tagesstruktur-Unterstützung und kurze Wege zu Therapieangeboten. Für Menschen mit Depression oder Erschöpfung."}},
    },
    {
        "provider_idx": 0, "provider_name": "Helvetia Supported Living",
        "slug": "zuerich-wohnung-burnout-erschöpfung-25plus",
        "care_level": 2, "cognitive_support_level": 1, "wheelchair_accessible": False,
        "hearing_support": False, "visual_support": False, "languages_supported": ["de"],
        "min_age": 25, "max_age": 65,
        "translations": {"de": {"title": "Zürich Ruhiges Wohnen bei Burnout (25+)", "description": "BESCHREIBUNG:\nRuhige Wohnung mit einfacher Alltagslogistik (naher Einkauf/ÖV). Optionale Unterstützung beim Wiedereinstieg in Arbeit/Alltag. Geeignet bei Burnout, Erschöpfung oder Stressfolgen."}},
    },
    {
        "provider_idx": 0, "provider_name": "Helvetia Supported Living",
        "slug": "bern-wohnung-chronische-atemnot-copd-40plus",
        "care_level": 2, "cognitive_support_level": 0, "wheelchair_accessible": True,
        "hearing_support": False, "visual_support": False, "languages_supported": ["de"],
        "min_age": 40, "max_age": 120,
        "translations": {"de": {"title": "Bern Barrierearme Wohnung bei COPD (40+)", "description": "BESCHREIBUNG:\nLift, kurze Wege und stufenloser Zugang. Geeignet bei COPD/chronischer Atemnot oder eingeschränkter Belastbarkeit. Optional: Unterstützung bei Einkäufen und Terminen."}},
    },
    {
        "provider_idx": 0, "provider_name": "Helvetia Supported Living",
        "slug": "basel-wohnung-diabetes-selbstmanagement-18plus",
        "care_level": 1, "cognitive_support_level": 0, "wheelchair_accessible": False,
        "hearing_support": False, "visual_support": False, "languages_supported": ["de"],
        "min_age": 18, "max_age": 120,
        "translations": {"de": {"title": "Basel Wohnung mit Selbstmanagement-Support (18+)", "description": "BESCHREIBUNG:\nWohnung mit optionaler Unterstützung bei Terminplanung/Medikationsroutine (nach Wunsch). Ruhige Umgebung, einfache Wege zu Gesundheitsdiensten. Geeignet bei chronischer Erkrankung mit Organisationsbedarf."}},
    },
    {
        "provider_idx": 0, "provider_name": "Helvetia Supported Living",
        "slug": "zuerich-wohnung-leichte-sprache-18plus",
        "care_level": 3, "cognitive_support_level": 2, "wheelchair_accessible": False,
        "hearing_support": False, "visual_support": True, "languages_supported": ["de"],
        "min_age": 18, "max_age": 80,
        "translations": {"de": {"title": "Zürich Wohnen mit leichter Sprache (18+)", "description": "BESCHREIBUNG:\nUnterstützung in leichter Sprache möglich, klare Beschriftung und visuelle Hinweise. Geeignet bei Lernschwierigkeiten oder kognitiver Beeinträchtigung; Begleitung bei Alltag/Terminen verfügbar."}},
    },
    {
        "provider_idx": 0, "provider_name": "Helvetia Supported Living",
        "slug": "bern-wohnung-hypersensibilitaet-reizarm-18plus",
        "care_level": 1, "cognitive_support_level": 1, "wheelchair_accessible": False,
        "hearing_support": False, "visual_support": False, "languages_supported": ["de"],
        "min_age": 18, "max_age": 60,
        "translations": {"de": {"title": "Bern Reizarme Wohnung (Hochsensibilität, 18+)", "description": "BESCHREIBUNG:\nGute Schalldämmung, ruhiger Innenhof und sanfte Beleuchtung. Wenig wechselnde Reize im Treppenhaus. Geeignet bei Hochsensibilität, sensorischer Überforderung oder Migräne."}},
    },
    {
        "provider_idx": 0, "provider_name": "Helvetia Supported Living",
        "slug": "basel-wohnung-arthritis-handlaeufe-55plus",
        "care_level": 2, "cognitive_support_level": 0, "wheelchair_accessible": True,
        "hearing_support": False, "visual_support": False, "languages_supported": ["de"],
        "min_age": 55, "max_age": 120,
        "translations": {"de": {"title": "Basel Barrierearme Wohnung (Arthritis, 55+)", "description": "BESCHREIBUNG:\nHandläufe, rutschhemmende Böden und bodenebene Dusche. Lift vorhanden. Geeignet bei Arthritis/Rheuma oder eingeschränkter Kraft; kurze Wege im Haus."}},
    },
    {
        "provider_idx": 0, "provider_name": "Helvetia Supported Living",
        "slug": "zuerich-wg-jugend-trauma-15bis18",
        "care_level": 4, "cognitive_support_level": 2, "wheelchair_accessible": False,
        "hearing_support": False, "visual_support": False, "languages_supported": ["de"],
        "min_age": 15, "max_age": 18,
        "translations": {"de": {"title": "Zürich Jugend-WG (Trauma, 15–18)", "description": "BESCHREIBUNG:\nJugend-WG mit stabilen Bezugspersonen, klaren Grenzen und Rückzugsoption. Unterstützung bei Schule/Alltag. Geeignet bei Traumafolgen und emotionaler Belastung."}},
    },
    {
        "provider_idx": 0, "provider_name": "Helvetia Supported Living",
        "slug": "bern-wohnung-entwicklung-teen-12bis15",
        "care_level": 4, "cognitive_support_level": 2, "wheelchair_accessible": True,
        "hearing_support": False, "visual_support": True, "languages_supported": ["de"],
        "min_age": 12, "max_age": 15,
        "translations": {"de": {"title": "Bern Betreutes Jugendwohnen (12–15)", "description": "BESCHREIBUNG:\nBetreutes Setting für Jugendliche mit Entwicklungs- oder Lernschwierigkeiten. Barrierefrei, visuelle Struktur und sichere Umgebung. Unterstützung bei Schule, Alltag und sozialen Kompetenzen."}},
    },
    {
        "provider_idx": 0, "provider_name": "Helvetia Supported Living",
        "slug": "basel-wohnung-schlafstoerung-ruhig-18plus",
        "care_level": 1, "cognitive_support_level": 0, "wheelchair_accessible": False,
        "hearing_support": False, "visual_support": False, "languages_supported": ["de"],
        "min_age": 18, "max_age": 70,
        "translations": {"de": {"title": "Basel Ruhige Wohnung bei Schlafstörung (18+)", "description": "BESCHREIBUNG:\nSchlaf-freundliche Lage (wenig Straßenlärm), Verdunkelung und klare Hausruhezeiten. Geeignet bei Schlafstörung, Reizüberlastung oder Erholung nach Krisenphasen."}},
    },
    {
        "provider_idx": 0, "provider_name": "Helvetia Supported Living",
        "slug": "bern-wohnung-hohe-pflege-24-7-18plus",
        "care_level": 5, "cognitive_support_level": 2, "wheelchair_accessible": True,
        "hearing_support": False, "visual_support": False, "languages_supported": ["de"],
        "min_age": 18, "max_age": 120,
        "translations": {"de": {"title": "Bern Wohnangebot mit 24/7 Pflege (18+)", "description": "BESCHREIBUNG:\nIntensives Pflege-/Assistenzsetting bis 24/7 möglich. Voll barrierefrei, Pflegebad und Platz für Hilfsmittel. Geeignet bei hohem Unterstützungsbedarf (körperlich/neurologisch)."}},
    },
    {
        "provider_idx": 0, "provider_name": "Helvetia Supported Living",
        "slug": "zuerich-wohnung-psychische-stabilisierung-checkins-18plus",
        "care_level": 3, "cognitive_support_level": 2, "wheelchair_accessible": False,
        "hearing_support": False, "visual_support": False, "languages_supported": ["de"],
        "min_age": 18, "max_age": 70,
        "translations": {"de": {"title": "Zürich Stabilisierungswohnung mit Check-ins (18+)", "description": "BESCHREIBUNG:\nRegelmäßige Check-ins, Krisenplan und Unterstützung bei Behörden/Terminen. Reizarme Umgebung, klare Tagesstruktur möglich. Geeignet bei psychischer Erkrankung nach Klinik oder in instabilen Phasen."}},
    },
    {
        "provider_idx": 0, "provider_name": "Helvetia Supported Living",
        "slug": "basel-wohnung-seh-und-gehbeeintraechtigung-60plus",
        "care_level": 3, "cognitive_support_level": 1, "wheelchair_accessible": True,
        "hearing_support": False, "visual_support": True, "languages_supported": ["de"],
        "min_age": 60, "max_age": 120,
        "translations": {"de": {"title": "Basel Barrierefrei mit Seh-Orientierung (60+)", "description": "BESCHREIBUNG:\nBarrierefrei mit guter Beleuchtung, Kontrastmarkierungen und sicheren Wegen. Geeignet bei kombinierter Seh- und Mobilitätseinschränkung. Balkon, Lift und bodenebene Dusche vorhanden."}},
    },
    {
        "provider_idx": 0, "provider_name": "Helvetia Supported Living",
        "slug": "bern-wohnung-taubblind-visuell-taktil-18plus",
        "care_level": 3, "cognitive_support_level": 1, "wheelchair_accessible": True,
        "hearing_support": True, "visual_support": True, "languages_supported": ["de"],
        "min_age": 18, "max_age": 120,
        "translations": {"de": {"title": "Bern Wohnen mit taktilen/visuellen Hilfen (18+)", "description": "BESCHREIBUNG:\nKombinierte Unterstützungen: visuelle Alarmoptionen, taktile Markierungen und sichere Wegeführung. Barrierefrei. Geeignet bei komplexen Sinnesbeeinträchtigungen (z.B. taubblind) je nach Bedarf."}},
    },

    # =========================================================
    # FR (9) — French-only entries
    # =========================================================
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "lausanne-studio-accessible-balcon-18plus",
        "care_level": 2,
        "cognitive_support_level": 0,
        "wheelchair_accessible": True,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["fr"],
        "min_age": 18,
        "max_age": 120,
        "translations": {
            "fr": {
                "title": "Lausanne Studio accessible avec balcon (18+)",
                "description": "DESCRIPTION :\nStudio sans marches, portes larges, douche à l’italienne et cuisine partiellement accessible. Balcon spacieux, quartier calme et proche des transports. Convient aux personnes à mobilité réduite."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "geneve-colocation-autisme-reizarm-18plus",
        "care_level": 2,
        "cognitive_support_level": 2,
        "wheelchair_accessible": False,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["fr"],
        "min_age": 18,
        "max_age": 55,
        "translations": {
            "fr": {
                "title": "Genève Colocation adaptée à l’autisme (18+)",
                "description": "DESCRIPTION :\nColocation avec règles claires, espaces de retrait et faible stimulation (bruit limité, lumière douce). Routine prévisible. Convient aux personnes sur le spectre autistique."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "fribourg-appartement-epilepsie-plan-securite-18plus",
        "care_level": 2,
        "cognitive_support_level": 1,
        "wheelchair_accessible": True,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["fr"],
        "min_age": 18,
        "max_age": 120,
        "translations": {
            "fr": {
                "title": "Fribourg Appartement conscient de l’épilepsie (18+)",
                "description": "DESCRIPTION :\nPlan de sécurité personnalisé, option de contrôles nocturnes et environnement calme. Accès fauteuil roulant, sols antidérapants et salle de bain sécurisée."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "neuchatel-studio-lumineux-depression-18plus",
        "care_level": 2,
        "cognitive_support_level": 1,
        "wheelchair_accessible": False,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["fr"],
        "min_age": 18,
        "max_age": 70,
        "translations": {
            "fr": {
                "title": "Neuchâtel Studio lumineux (dépression, 18+)",
                "description": "DESCRIPTION :\nStudio très lumineux, quartier calme, cadre simple et stable. Check-ins optionnels et proximité des services de soins. Convient en cas de dépression ou fatigue psychique."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "geneve-logement-trauma-informe-ptsd-18plus",
        "care_level": 3,
        "cognitive_support_level": 2,
        "wheelchair_accessible": False,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["fr"],
        "min_age": 18,
        "max_age": 65,
        "translations": {
            "fr": {
                "title": "Genève Logement trauma-informé (PTSD, 18+)",
                "description": "DESCRIPTION :\nCadre prévisible, règles de visiteurs claires, espaces de retrait et plan de crise. Convient aux personnes avec PTSD/trauma et besoin d’un contexte stable."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "lausanne-logement-deficience-visuelle-18plus",
        "care_level": 1,
        "cognitive_support_level": 0,
        "wheelchair_accessible": False,
        "hearing_support": False,
        "visual_support": True,
        "languages_supported": ["fr"],
        "min_age": 18,
        "max_age": 120,
        "translations": {
            "fr": {
                "title": "Lausanne Logement malvoyance/contrastes (18+)",
                "description": "DESCRIPTION :\nÉclairage homogène, marquages contrastés et cheminement clair. Repères tactiles possibles. Convient aux personnes malvoyantes ou aveugles."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "fribourg-logement-soutenu-cognitif-18plus",
        "care_level": 3,
        "cognitive_support_level": 3,
        "wheelchair_accessible": True,
        "hearing_support": False,
        "visual_support": True,
        "languages_supported": ["fr"],
        "min_age": 18,
        "max_age": 80,
        "translations": {
            "fr": {
                "title": "Fribourg Logement soutenu (cognitif, 18+)",
                "description": "DESCRIPTION :\nAides visuelles (pictogrammes, listes), signalisation claire et environnement sécurisé. Accès fauteuil roulant. Convient après lésion cérébrale ou troubles cognitifs."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "geneve-logement-jeunes-anxiete-14a17",
        "care_level": 4,
        "cognitive_support_level": 2,
        "wheelchair_accessible": False,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["fr"],
        "min_age": 14,
        "max_age": 17,
        "translations": {
            "fr": {
                "title": "Genève Logement jeunesse (anxiété, 14–17)",
                "description": "DESCRIPTION :\nCadre sécurisant, routine stable, accompagnement scolaire et espaces de retrait. Convient aux adolescents avec anxiété, panique ou surcharge sociale."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "lausanne-residence-dementia-65plus",
        "care_level": 4,
        "cognitive_support_level": 3,
        "wheelchair_accessible": True,
        "hearing_support": False,
        "visual_support": True,
        "languages_supported": ["fr"],
        "min_age": 65,
        "max_age": 120,
        "translations": {
            "fr": {
                "title": "Lausanne Résidence sensible à la démence (65+)",
                "description": "DESCRIPTION :\nPetite unité de vie avec routines prévisibles, repères visuels, éclairage renforcé et accès fauteuil roulant. Encadrement adaptable jusqu’à 24/7."
            }
        },
    },

    # =========================================================
    # IT (3) — Italian-only entries
    # =========================================================
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "lugano-monolocale-accessibile-arredato-18plus",
        "care_level": 2,
        "cognitive_support_level": 0,
        "wheelchair_accessible": True,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["it"],
        "min_age": 18,
        "max_age": 120,
        "translations": {
            "it": {
                "title": "Lugano Monolocale accessibile arredato (18+)",
                "description": "DESCRIZIONE:\nMonolocale senza barriere: ingresso a livello, porte larghe, doccia a filo pavimento e cucina parzialmente accessibile. Arredato, ambiente tranquillo e vicino ai mezzi pubblici."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "locarno-appartamento-autismo-ambiente-calmo-18plus",
        "care_level": 2,
        "cognitive_support_level": 2,
        "wheelchair_accessible": False,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["it"],
        "min_age": 18,
        "max_age": 55,
        "translations": {
            "it": {
                "title": "Locarno Appartamento per autismo (18+)",
                "description": "DESCRIZIONE:\nAmbiente a bassa stimolazione (rumore ridotto, luce morbida), regole chiare e possibilità di spazio di ritiro. Routine prevedibile; adatto a sensibilità sensoriale."
            }
        },
    },
    {
        "provider_idx": 0,
        "provider_name": "Helvetia Supported Living",
        "slug": "bellinzona-alloggio-trauma-informed-ptsd-18plus",
        "care_level": 3,
        "cognitive_support_level": 2,
        "wheelchair_accessible": True,
        "hearing_support": False,
        "visual_support": False,
        "languages_supported": ["it"],
        "min_age": 18,
        "max_age": 65,
        "translations": {
            "it": {
                "title": "Bellinzona Alloggio trauma-informed (PTSD, 18+)",
                "description": "DESCRIZIONE:\nRoutine prevedibile, piano di crisi e check-in regolari. Accesso senza barriere e ambiente tranquillo. Adatto a persone con PTSD/trauma che cercano stabilità e sicurezza."
            }
        },
    },
]
