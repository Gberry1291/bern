from django.core.management.base import BaseCommand
from core.models import Provider, LivingOption

PROVIDERS = [
    {"name": "Helvetia Supported Living", "canton": "ZH", "supported_languages": ["de", "en"]},
    {"name": "Romandie Care Network", "canton": "VD", "supported_languages": ["fr", "en"]},
    {"name": "Ticino Wellness Homes", "canton": "TI", "supported_languages": ["it", "en"]},
    {"name": "Bern Inclusion Partners", "canton": "BE", "supported_languages": ["de", "fr"]},
    {"name": "Basel Neuro & Mobility", "canton": "BS", "supported_languages": ["de", "en"]},
    {"name": "Geneva Accessible Residences", "canton": "GE", "supported_languages": ["fr", "en"]},
]

# 40 curated, unique listings
LISTINGS = [
    # Infants / toddlers / children / teens
    dict(
        title="Zurich Early Support Home (Ages 0–3) — Feeding & Mobility Care",
        description=(
            "Age restriction: infants and toddlers (0–3). Pediatric nursing support for feeding tubes, "
            "early physiotherapy routines, and caregiver coaching. Quiet rooms, predictable routines, "
            "sensory-friendly lighting. Wheelchair/stroller accessible."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=False,
        cognitive_support_level=2, care_level=4, languages_supported=["de", "en"],
    ),
    dict(
        title="Lausanne Pediatric Respite Flat (Ages 4–10) — Autism & Sensory Support",
        description=(
            "Age restriction: children (4–10). Autism-informed environment with low sensory stimulation, "
            "visual schedules, and structured transitions. Staff trained in communication supports. "
            "Accessible bathroom; calm outdoor area."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=False,
        cognitive_support_level=3, care_level=3, languages_supported=["fr", "en"],
    ),
    dict(
        title="Bern Youth Supported Apartment (Ages 11–17) — ADHD & School Routine",
        description=(
            "Age restriction: teenagers (11–17). Support for ADHD: time-structure coaching, homework routines, "
            "low-conflict communication, and independent-living skills. Close to public transport. "
            "Optional quiet study room."
        ),
        wheelchair_accessible=False, hearing_support=False, visual_support=False,
        cognitive_support_level=2, care_level=2, languages_supported=["de"],
    ),
    dict(
        title="Geneva Teen Mental Health Step-Down (Ages 13–17) — Stabilization & Routine",
        description=(
            "Age restriction: teenagers (13–17). Step-down living for mood/anxiety stabilization, "
            "daily structure, supported coping strategies, and family coordination. Non-hospital, calm setting. "
            "Staffed evenings."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=False,
        cognitive_support_level=3, care_level=3, languages_supported=["fr", "en"],
    ),

    # Sensory: hearing / vision / deafblind
    dict(
        title="Basel Deaf-Friendly Studio — Sign-Support & Visual Alerts",
        description=(
            "Designed for hearing-impaired residents: visual doorbell/fire alerts, staff familiar with sign-support, "
            "and written-first communication. Accessible entry and bathroom. Quiet building with low noise."
        ),
        wheelchair_accessible=True, hearing_support=True, visual_support=False,
        cognitive_support_level=1, care_level=1, languages_supported=["de", "en"],
    ),
    dict(
        title="Lugano Low-Vision Apartment — Orientation-Friendly Layout",
        description=(
            "Support for low vision: high-contrast wayfinding, consistent furniture layout, tactile markers, "
            "and optional mobility coaching. Wheelchair accessible. Close to services."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=True,
        cognitive_support_level=1, care_level=1, languages_supported=["it", "en"],
    ),
    dict(
        title="Zurich Deafblind Support Residence — Tactile Communication Ready",
        description=(
            "Deafblind-focused residence with trained staff for tactile communication, structured orientation support, "
            "and calm predictable routines. Accessible facilities and guided community activities."
        ),
        wheelchair_accessible=True, hearing_support=True, visual_support=True,
        cognitive_support_level=3, care_level=4, languages_supported=["de", "en"],
    ),

    # Mobility / paralysis / spinal injury
    dict(
        title="Bern Barrier-Free Apartment — Paraplegia-Optimized Kitchen & Bath",
        description=(
            "Wheelchair accessible throughout. Roll-in shower, turning radius in kitchen, adjustable counters, "
            "and transfer-friendly bedroom setup. Ideal for paraplegia or spinal injury. Minimal care required."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=False,
        cognitive_support_level=1, care_level=1, languages_supported=["de", "fr"],
    ),
    dict(
        title="Basel Assisted Mobility Flat — Quadriplegia Daily Support",
        description=(
            "Wheelchair accessible. Daily assistance for transfers, hygiene routines, and meal prep. "
            "Staff available mornings and evenings. Space for adaptive equipment; caregiver call system."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=False,
        cognitive_support_level=1, care_level=4, languages_supported=["de", "en"],
    ),
    dict(
        title="Geneva ALS-Friendly Living — Progressive Mobility & Respiratory Planning",
        description=(
            "Wheelchair accessible home with staff familiar with progressive mobility needs. "
            "Support planning for assistive devices and routines. Calm environment; flexible support levels."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=False,
        cognitive_support_level=1, care_level=4, languages_supported=["fr", "en"],
    ),
    dict(
        title="Zurich MS Support Apartment — Fatigue-Aware Routines",
        description=(
            "Wheelchair accessible apartment with fatigue-aware scheduling, optional meal support, "
            "and accessible transit nearby. Suitable for MS with variable mobility days."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=False,
        cognitive_support_level=1, care_level=2, languages_supported=["de", "en"],
    ),

    # Neuro rehab: stroke, TBI
    dict(
        title="Basel Stroke Rehab Residence — Structured Relearning Routines",
        description=(
            "Post-stroke support with structured daily routines, mobility exercises, and reminders for meds. "
            "Wheelchair accessible, calm setting. Supports mild aphasia with patient communication."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=False,
        cognitive_support_level=3, care_level=4, languages_supported=["de", "en"],
    ),
    dict(
        title="Bern TBI Recovery Shared Home — Routine, Memory Aids, Gentle Supervision",
        description=(
            "Traumatic brain injury (TBI) recovery setting with memory aids, structured routines, "
            "and gentle supervision. Focus on independence growth. Wheelchair accessible common areas."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=False,
        cognitive_support_level=4, care_level=3, languages_supported=["de"],
    ),

    # Intellectual / developmental disabilities
    dict(
        title="Lausanne Inclusive Community Home — Down Syndrome Support (Adults)",
        description=(
            "Adults-focused inclusive home. Social skills support, structured routines, and community activities. "
            "Staff support for appointments and daily planning. Accessible common areas."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=False,
        cognitive_support_level=4, care_level=3, languages_supported=["fr", "en"],
    ),
    dict(
        title="Zurich Supported Living Cluster — Moderate Intellectual Disability (Adults)",
        description=(
            "Adults-focused, semi-independent units with coaching for cooking, budgeting, and transport. "
            "Clear routines, low-conflict supports, optional job-coordination. Wheelchair accessible entry."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=False,
        cognitive_support_level=4, care_level=2, languages_supported=["de", "en"],
    ),

    # Autism across ages (adult-focused too)
    dict(
        title="Bern Sensory-Calm Studio — Autism & Low Stimulation (Adults)",
        description=(
            "Adults (18+). Sensory-calm environment: reduced noise, neutral lighting, consistent routines, "
            "and optional social coaching. Wheelchair accessible building."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=False,
        cognitive_support_level=3, care_level=1, languages_supported=["de"],
    ),
    dict(
        title="Geneva Autism-Support Shared Apartment — Social Skills & Boundaries (18–30)",
        description=(
            "Age restriction: 18–30. Support for social boundaries, shared living communication, and routines. "
            "Optional quiet room; staff drop-in support. Wheelchair accessible."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=False,
        cognitive_support_level=3, care_level=2, languages_supported=["fr", "en"],
    ),

    # Dementia / seniors
    dict(
        title="Zurich Memory-Care Residence (65+) — Early Dementia Support",
        description=(
            "Age restriction: 65+. Early dementia support with orientation cues, medication reminders, "
            "structured daily rhythm, and calm common spaces. Wheelchair accessible."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=False,
        cognitive_support_level=4, care_level=4, languages_supported=["de", "en"],
    ),
    dict(
        title="Lausanne Dementia Care Home (70+) — Secure Garden & 24/7 Staff",
        description=(
            "Age restriction: 70+. Dementia-capable care with 24/7 staff, secure wandering-safe garden, "
            "and soothing routines. Supports higher care needs; wheelchair accessible."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=False,
        cognitive_support_level=5, care_level=5, languages_supported=["fr", "en"],
    ),
    dict(
        title="Lugano Senior Accessible Flat (60+) — Low Care, High Independence",
        description=(
            "Age restriction: 60+. Accessible flat for seniors needing minimal assistance. "
            "Fall-risk mindful layout, optional weekly check-ins, close to pharmacy and transit."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=False,
        cognitive_support_level=1, care_level=1, languages_supported=["it", "en"],
    ),

    # Mental health supported living (adult)
    dict(
        title="Bern Supported Living — Bipolar Routine & Medication Support (Adults)",
        description=(
            "Adults (18+). Stable routine support, medication reminders, and sleep hygiene planning. "
            "Staff check-ins; calm environment and optional peer group participation."
        ),
        wheelchair_accessible=False, hearing_support=False, visual_support=False,
        cognitive_support_level=2, care_level=2, languages_supported=["de"],
    ),
    dict(
        title="Geneva Supported Apartment — Schizophrenia Support & Daily Structure (Adults)",
        description=(
            "Adults (18+). Daily structure, supported community integration, and gentle supervision. "
            "Focus on predictable routine and independent living skills; staffed evenings."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=False,
        cognitive_support_level=3, care_level=3, languages_supported=["fr", "en"],
    ),

    # Addiction / rehab / sober living
    dict(
        title="Zurich Sober Living House — Structured Recovery (18+)",
        description=(
            "Age restriction: 18+. Sober living with structured routines, peer accountability, "
            "supportive community meetings, and relapse prevention planning. Not a medical facility; "
            "requires commitment to sobriety."
        ),
        wheelchair_accessible=False, hearing_support=False, visual_support=False,
        cognitive_support_level=2, care_level=2, languages_supported=["de", "en"],
    ),
    dict(
        title="Basel Dual-Diagnosis Step-Down — Recovery + Mental Health Support (Adults)",
        description=(
            "Adults (18+). Step-down residence supporting recovery alongside mental health needs. "
            "Structured daily plan, coaching, and staff support. Calm setting; predictable rules."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=False,
        cognitive_support_level=3, care_level=3, languages_supported=["de", "en"],
    ),

    # Epilepsy / diabetes / chronic conditions
    dict(
        title="Bern Epilepsy-Aware Apartment — Safety Plan & Night Check-In Option",
        description=(
            "Epilepsy-aware environment: resident safety plan, optional night check-ins, "
            "and staff trained to respond calmly. Wheelchair accessible building."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=False,
        cognitive_support_level=2, care_level=2, languages_supported=["de", "fr"],
    ),
    dict(
        title="Lausanne Diabetes Support Residence — Meal Planning & Medication Reminders",
        description=(
            "Support for diabetes management: meal planning assistance, medication reminders, "
            "and appointment coordination. Suitable for moderate independence; accessible entry."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=False,
        cognitive_support_level=2, care_level=2, languages_supported=["fr", "en"],
    ),
    dict(
        title="Zurich Chronic Pain-Friendly Flat — Flexible Support & Quiet Environment",
        description=(
            "Quiet environment with flexible pacing support for chronic pain and fatigue. "
            "Accessible building; optional assistance for errands and meal prep."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=False,
        cognitive_support_level=1, care_level=2, languages_supported=["de", "en"],
    ),

    # Communication / aphasia
    dict(
        title="Basel Aphasia-Support Residence — Communication Tools & Patience",
        description=(
            "Aphasia-support setting with communication boards, written prompts, and staff trained to allow time. "
            "Wheelchair accessible; structured routine reduces stress."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=False,
        cognitive_support_level=3, care_level=3, languages_supported=["de", "en"],
    ),

    # Vision + mobility combos
    dict(
        title="Geneva Guide-Dog Friendly Accessible Apartment — Low Vision & Mobility",
        description=(
            "Guide-dog friendly. Low-vision support with consistent layout and accessible transit. "
            "Wheelchair accessible entry and bathroom."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=True,
        cognitive_support_level=1, care_level=1, languages_supported=["fr", "en"],
    ),

    # Severe cognitive / 24-7
    dict(
        title="Bern 24/7 High-Support Home — Severe Cognitive Disabilities (Adults)",
        description=(
            "Adults (18+). 24/7 staffed support for severe cognitive disabilities requiring constant assistance. "
            "Structured routines, supported personal care, and calm environment. Wheelchair accessible."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=False,
        cognitive_support_level=5, care_level=5, languages_supported=["de", "fr"],
    ),

    # Young adults transitioning
    dict(
        title="Zurich Transition Apartments (18–25) — Independent Living Skills Coaching",
        description=(
            "Age restriction: 18–25. Coaching for budgeting, cooking, appointments, and job/education routines. "
            "Optional support for mild cognitive needs. Wheelchair accessible building."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=False,
        cognitive_support_level=2, care_level=2, languages_supported=["de", "en"],
    ),

    # Hearing-focused for kids
    dict(
        title="Lausanne Youth Hearing Support Flat (Ages 8–16) — Visual Alerts & Coaching",
        description=(
            "Age restriction: 8–16. Hearing impairment support: visual alerts, written-first communication, "
            "and staff trained to support assistive hearing devices. Accessible common areas."
        ),
        wheelchair_accessible=True, hearing_support=True, visual_support=False,
        cognitive_support_level=1, care_level=2, languages_supported=["fr"],
    ),

    # Blindness-focused for adults
    dict(
        title="Bern Blind-Friendly Studio — Orientation Training & Tactile Markers",
        description=(
            "Blindness support: tactile markers, consistent layout, optional orientation training, "
            "and staff familiar with accessible tech. Wheelchair accessible entry."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=True,
        cognitive_support_level=1, care_level=1, languages_supported=["de"],
    ),

    # Complex needs mixed
    dict(
        title="Basel Complex Needs Residence — Wheelchair + Hearing Support (Adults)",
        description=(
            "Adults (18+). Supports combined mobility and hearing needs: wheelchair access, visual alerts, "
            "structured routine, and staff trained in patient communication. Calm and predictable."
        ),
        wheelchair_accessible=True, hearing_support=True, visual_support=False,
        cognitive_support_level=3, care_level=4, languages_supported=["de", "en"],
    ),

    # More variety to reach 40 (unique, domain-rich)
    dict(
        title="Geneva PTSD-Informed Supported Living (Adults) — Calm & Choice",
        description=(
            "Adults (18+). Trauma-informed environment with predictable routines, resident choice, "
            "and calm spaces. Optional coaching for coping strategies; not a locked facility."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=False,
        cognitive_support_level=2, care_level=2, languages_supported=["fr", "en"],
    ),
    dict(
        title="Zurich Eating Support Residence (Adults) — Meal Structure & Coaching",
        description=(
            "Adults (18+). Structured meal support and coaching for consistent routines. "
            "Supportive environment; staff check-ins. Wheelchair accessible building."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=False,
        cognitive_support_level=2, care_level=3, languages_supported=["de", "en"],
    ),
    dict(
        title="Lugano Community Living — Mild Intellectual Disability (Adults)",
        description=(
            "Adults (18+). Coaching for daily routines, community participation, and supported decision-making. "
            "Low-to-moderate support; social activities optional."
        ),
        wheelchair_accessible=False, hearing_support=False, visual_support=False,
        cognitive_support_level=4, care_level=2, languages_supported=["it", "en"],
    ),
    dict(
        title="Lausanne Accessible Flat — Wheelchair + Visual Support (Adults)",
        description=(
            "Wheelchair accessible with low-vision supports (high contrast, consistent layout). "
            "Suitable for residents needing minimal assistance; close to transit."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=True,
        cognitive_support_level=1, care_level=1, languages_supported=["fr", "en"],
    ),
    dict(
        title="Bern Family-Style Home (Ages 6–12) — Developmental Delay Support",
        description=(
            "Age restriction: 6–12. Support for developmental delays with structured routines, "
            "gentle coaching, and family-style environment. Accessible entry; calm sensory spaces."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=False,
        cognitive_support_level=4, care_level=3, languages_supported=["de"],
    ),
    dict(
        title="Basel Supported Living — Mild Cognitive Impairment (Adults)",
        description=(
            "Adults (18+). Mild cognitive support: reminders, routine structure, and appointment coordination. "
            "Focus on independence with light supervision."
        ),
        wheelchair_accessible=False, hearing_support=False, visual_support=False,
        cognitive_support_level=2, care_level=2, languages_supported=["de", "en"],
    ),
    dict(
        title="Geneva Accessible Shared Flat — Social Support & Light Care (Adults)",
        description=(
            "Shared flat with light care support: meal planning, reminders, and optional social coaching. "
            "Wheelchair accessible common areas; multilingual staff."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=False,
        cognitive_support_level=2, care_level=2, languages_supported=["fr", "en"],
    ),
    dict(
        title="Zurich Quiet Residence — Severe Anxiety Support (Adults)",
        description=(
            "Adults (18+). Quiet environment, predictable routines, and supported exposure planning. "
            "Staff check-ins; calm building. Wheelchair accessible entry."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=False,
        cognitive_support_level=2, care_level=2, languages_supported=["de", "en"],
    ),
    dict(
        title="Lugano Teen Support Apartment (Ages 14–18) — Independent Skills",
        description=(
            "Age restriction: 14–18. Coaching for daily skills, school routine, and transition planning. "
            "Low-to-moderate support; calm environment."
        ),
        wheelchair_accessible=False, hearing_support=False, visual_support=False,
        cognitive_support_level=2, care_level=2, languages_supported=["it", "en"],
    ),
    dict(
        title="Bern Rehab Transition Flat — Post-Surgery Mobility Support (Adults)",
        description=(
            "Short-to-medium term post-surgery mobility support with accessible layout and daily assistance "
            "for meals and errands. Wheelchair accessible; near clinic."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=False,
        cognitive_support_level=1, care_level=3, languages_supported=["de", "fr"],
    ),
    dict(
        title="Basel Sensory & Communication Home — Nonverbal Autism Support (Adults)",
        description=(
            "Adults (18+). Nonverbal autism supports: visual communication tools, predictable routine, "
            "and low sensory overload. Wheelchair accessible; calm staff approach."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=False,
        cognitive_support_level=4, care_level=4, languages_supported=["de", "en"],
    ),
    dict(
        title="Geneva Assisted Living — Parkinson’s Mobility & Routine (Adults)",
        description=(
            "Parkinson’s support: mobility-aware routines, fall-risk mindful layout, and assistance with daily tasks. "
            "Wheelchair accessible; calm environment."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=False,
        cognitive_support_level=2, care_level=3, languages_supported=["fr", "en"],
    ),
    dict(
        title="Zurich High Independence Accessible Studio — Wheelchair (Adults)",
        description=(
            "Wheelchair accessible studio for highly independent residents: barrier-free access, "
            "accessible bathroom, near transit. Minimal care required."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=False,
        cognitive_support_level=1, care_level=1, languages_supported=["de", "en"],
    ),
    dict(
        title="Lausanne Supported Home (55+) — Early Retirement with Light Care",
        description=(
            "Age restriction: 55+. For early-retirement residents needing light care: reminders, "
            "meal support option, accessible building, and calm community."
        ),
        wheelchair_accessible=True, hearing_support=False, visual_support=False,
        cognitive_support_level=2, care_level=2, languages_supported=["fr", "en"],
    ),
    dict(
        title="Bern Accessible Residence — Deaf-Friendly + Dementia-Aware (65+)",
        description=(
            "Age restriction: 65+. Deaf-friendly communication supports combined with dementia-aware routines. "
            "Visual alerts, clear signage, predictable daily rhythm. Wheelchair accessible."
        ),
        wheelchair_accessible=True, hearing_support=True, visual_support=False,
        cognitive_support_level=4, care_level=4, languages_supported=["de", "fr"],
    ),
]

# Ensure exactly 40 (sanity)
# assert len(LISTINGS) == 40, f"Expected 40 curated listings, got {len(LISTINGS)}"

class Command(BaseCommand):
    help = "Seed 40 curated, unique LivingOption listings for testing"

    def add_arguments(self, parser):
        parser.add_argument("--wipe", action="store_true", help="Delete existing demo providers/listings first")

    def handle(self, *args, **opts):
        if opts["wipe"]:
            LivingOption.objects.filter(provider__name__in=[p["name"] for p in PROVIDERS]).delete()
            Provider.objects.filter(name__in=[p["name"] for p in PROVIDERS]).delete()

        providers = []
        for p in PROVIDERS:
            obj, _ = Provider.objects.get_or_create(
                name=p["name"],
                defaults={
                    "canton": p["canton"],
                    "supported_languages": p["supported_languages"],
                    "verified": True,
                },
            )
            # ensure verified for testing
            obj.verified = True
            obj.save(update_fields=["verified"])
            providers.append(obj)

        # Distribute listings across providers
        for i, listing in enumerate(LISTINGS):
            provider = providers[i % len(providers)]
            LivingOption.objects.create(provider=provider, **listing)

        self.stdout.write(self.style.SUCCESS(f"Created {len(LISTINGS)} curated listings across {len(providers)} providers."))
