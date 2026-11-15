H = {}
def h(slug, *ps): H[slug] = list(ps)
# cleaning
h('ro-membrane-cleaner',
 ('Identifying the foulant first','Membrane fouling comes in several forms: organic matter, biofilm, silt and colloids, metal oxides and mineral scale. Alkaline cleaners are most effective on organic, biological and silt fouling, while mineral scale usually needs an acid clean. Reviewing feed water analysis, the stage where performance has dropped and, if possible, a membrane autopsy shows which clean is needed, so chemical and downtime are not wasted.'),
 ('A typical cleaning sequence','Cleaning normally follows a set order: flush the system with permeate, prepare the cleaning solution at the right pH and temperature, recirculate at low pressure, allow a soak period, recirculate again and then flush thoroughly before returning to service. Cleaning each stage separately often gives better results than cleaning the whole array together.'),
 ('Protecting membrane warranty','Membrane manufacturers publish pH and temperature limits for cleaning. Staying inside those limits protects both the membranes and any warranty. Seamens sets the cleaning conditions with those limits in mind.'))
h('floor-surface-cleaner',
 ('Matching dilution to the soil','Light dust in offices needs only a weak solution, while oily workshop floors and loading bays need a stronger mix and some dwell time. Using the right dilution for each area saves chemical, avoids sticky residues and gives a cleaner result. Seamens provides a simple dilution chart for each zone of your site.'),
 ('Food and pharma floors','In food and pharmaceutical plants, floors are part of the hygiene programme. Cleaning removes soils so disinfection can work, and floor drains should be cleaned on the same schedule.'),
 ('Lower long-term cost','Regular cleaning protects floor coatings and reduces the need for expensive resurfacing.'))
h('disinfectant-sanitiser',
 ('Choosing the right product for the area','Food-contact surfaces, medical areas, washrooms and clean rooms each have different needs. Food areas need products and rinsing practices suited to food contact, clean rooms need low-residue products, and washrooms need broad action against common bacteria. Seamens recommends the product and routine for each area of your site.'),
 ('Training staff','Disinfection only works when staff dilute correctly, cover the surface and wait for the contact time. Short training with clear wall charts makes the routine consistent.'),
 ('Storage and shelf life','Store disinfectants as labelled, away from heat and direct sunlight, and use diluted solutions within the stated time.'))
h('heavy-duty-degreaser',
 ('Why a heavy-duty grade','Generator rooms, compressor houses, engine bays and workshop floors collect carbonised oil and baked-on grease that general cleaners cannot shift. A heavy-duty degreaser contains stronger surfactants and solvency to penetrate these layers, cutting cleaning time and labour.'),
 ('Better maintenance visibility','Clean machines show oil leaks, cracks and loose fittings that dirt hides. Many plants find faults early simply because equipment is clean enough to inspect.'),
 ('Fire risk reduction','Oil-soaked dust near hot surfaces is a fire hazard. Regular degreasing reduces this risk in engine rooms and boiler houses.'))
h('cooling-tower-descaler',
 ('Signs a tower needs descaling','White or brown scale on fill and basin walls, higher return water temperature, reduced airflow and rising condenser approach on connected equipment all suggest that scale has built up. Weighing a section of fill or inspecting heat exchanger tubes confirms how severe it is.'),
 ('Clean, then control','Descaling recovers performance, but scale will return if the water is not treated. A scale inhibitor programme with controlled blow-down should restart as soon as the tower is refilled.'),
 ('Planning the work','Cleaning is timed around production load and weather, often before the summer peak.'))
h('washroom-cleaner-descaler',
 ('Choosing an acidic descaler safely','Descaling products for washrooms are mildly acidic, which is why they dissolve scale. That also means they should not be mixed with bleach or chlorine products, and staff should rinse surfaces after use. Clear labelling and training make this simple.'),
 ('Saving water and fittings','Scale in cisterns, taps and urinal outlets wastes water and damages fittings. Regular descaling keeps them working and reduces repairs.'),
 ('Hostels and staff colonies','Large residential facilities benefit from a single product for cleaning and descaling.'))
h('alkaline-cip-cleaner',
 ('Why CIP needs control','Clean-in-place relies on circulating solutions through tanks, pipes and heat exchangers without dismantling. If the concentration is weak, the temperature low, contact time short or flow too slow, soils remain inside the system where they cannot be seen. Controlling all four factors and recording them for each cycle is what makes CIP reliable.'),
 ('Verification','Visual inspection, ATP swabs and microbiological tests verify that cleaning has worked. Recognised hygienic design and cleaning guidance from EHEDG and 3-A supports this approach.'),
 ('Reducing water and energy','A correctly set CIP programme avoids over-long cycles, saving water, heat and time.'))
h('textile-machine-cleaner',
 ('Size kitchens and sizing machines','Hardened size on cylinders, size boxes and squeeze rollers affects add-on and yarn quality. Cleaning these surfaces regularly helps keep sizing consistent.'),
 ('Stenter chains and frames','Deposits on stenter chains and clips can mark fabric edges and cause width variation. Cleaning during planned stops keeps finishing quality high.'),
 ('Lower fire risk','Oily fly accumulations in weaving and finishing halls are a known fire risk; clean machines reduce it.'))
h('drain-pipe-unclogger',
 ('Understanding grease build-up','In canteens and food areas, warm greasy water flows into drains and cools, leaving fat on pipe walls. Over weeks, these layers grow and trap food particles and soap. Regular treatment and grease trap cleaning prevent the gradual narrowing that leads to blockages.'),
 ('After clearing','Flush the line well with water after treatment and inspect any traps or chambers for remaining solids.'))
h('biofilm-remover',
 ('Process pipelines','Pipelines carrying water, syrups or dilute chemicals can host biofilm that sheds bacteria into product. Periodic removal is part of a good hygiene programme.'),
 ('Flushing and monitoring','After treatment, flush systems thoroughly and monitor with swabs or dip slides to confirm results.'))
h('grease-oil-remover',
 ('Saving labour time','Fast-acting emulsification cuts the time technicians spend scraping and wiping parts, freeing them for actual maintenance work.'),
 ('Better inspection','Clean parts reveal wear, cracks and damage that grease hides, improving maintenance decisions.'))
h('metal-passivator',
 ('Linking with water treatment','After passivation, starting the correct water treatment programme quickly helps keep surfaces protected in service.'),
 ('Documenting the work','Recording cleaning and passivation steps helps future inspections and audits.'))
h('glass-surface-cleaner',
 ('Indoor air and comfort','A low-residue product used with good ventilation keeps offices pleasant for staff while cleaning.'))
# water safe
h('fc-30b',
 ('What softening achieves','Water softening exchanges calcium and magnesium for ions that do not form scale. With less hardness in the make-up water, an A/C plant can run more cycles with lower scaling risk.'),
 ('Keeping the softener effective','Softening performance falls when regeneration or servicing is missed. Regular hardness checks on the outlet show when service is due.'),
 ('Reducing descaling frequency','Plants that soften make-up water usually need less frequent condenser descaling, saving downtime.'))
h('ct-9080',
 ('Why scale forms in towers','Calcium carbonate becomes less soluble as water warms and concentrates, so it deposits on hot heat exchanger surfaces first. An inhibitor keeps it in solution or as soft, non-adherent particles.'),
 ('Energy cost of scale','Scale on condensers and process exchangers increases approach temperature and chiller or compressor power.'),
 ('Testing to recognised methods','Hardness, alkalinity and conductivity are measured with standard ASTM methods.'))
h('br-555',
 ('Pitting is hard to see','Oxygen pitting often attacks tubes from inside where it cannot be seen until a leak appears. Prevention through scavenging is far cheaper than tube replacement.'),
 ('Condensate systems','Air leaks in condensate systems bring oxygen back. Finding them improves protection.'),
 ('Shutdown protection','Idle boilers can corrode quickly; correct lay-up protects them.'))
h('br-999',
 ('Mixed metals in loops','Closed loops often contain steel, copper and brass. Treatment protects all of them.'),
 ('Annual review','A yearly water test and review keeps the loop protected.'))
h('dc-1020',
 ('Slime and biofilm','Dispersants help loosen slime so biocides work better.'),
 ('Approach temperature','Rising approach shows fouling.'))
h('fc-7090',
 ('Why organic descalers','Organic descalers are designed to remove scale with less risk to sensitive metals than strong mineral acids.'),
 ('Restoring efficiency','Clean condensers lower head pressure and power.'))
h('br-111',
 ('Feed water hardness','Testing feed water hardness daily shows when softening or anti-scalant dosing needs attention.'),
 ('Tube life','Preventing scale prevents overheating that can damage tubes.'))
h('bc-1000',
 ('Dip slide monitoring','Dip slides give a simple, regular check on bacteria levels.'),
 ('Cleaning schedule','Physical basin cleaning complements biocide.'))
h('rc-1030',
 ('Higher recovery','Anti-scalant allows higher recovery, saving feed water.'),
 ('Lower cleaning frequency','Controlled scaling means fewer membrane cleans.'))
h('fc-120q',
 ('Corrosion coupons','Coupons show actual metal loss and confirm protection.'),
 ('Continuous dosing','Steady dosing keeps protection constant.'))
h('rd-4050',
 ('Pre-treatment hygiene','Clean filters and tanks reduce bacteria entering the RO.'))
# eco
h('ecolevel-lv',
 ('Why shades go uneven','Uneven shades come from dye rushing onto fabric too fast, poor circulation or temperature differences. A levelling agent slows initial uptake so dye spreads evenly before fixing.'),
 ('First-time-right dyeing','Fewer re-dyes save water, steam, chemicals and time.'),
 ('Lab to bulk','Comparing lab and bulk shades helps transfer recipes reliably.'))
h('ecopva-gs',
 ('Adhesion to synthetics','Polyester and other synthetic fibres have smooth surfaces where starch adheres poorly. PVA bonds well and forms a flexible film.'),
 ('Lower breaks on fine counts','Strong, flexible films protect fine yarns from abrasion at the loom.'),
 ('Consistent cooking','Consistent cooking and viscosity keep add-on steady.'))
h('ecowet-det',
 ('Quicker wetting','Fast wetting allows chemicals to reach fibres quickly, especially on continuous ranges with short dwell times.'),
 ('Soil suspension','Detergency keeps soils suspended so they rinse away.'),
 ('Store simplification','Holding fewer products simplifies stores.'))
h('ecoshield-wp',
 ('Durability through washing','Repellency is tested after the washes the buyer specifies.'),
 ('Breathability','Repellent finishes keep fabric breathable.'),
 ('Export orders','Repellency supports outerwear export orders.'))
h('eco-silsoftner-glazer',
 ('Weaving efficiency','Fewer breaks raise loom efficiency and output.'),
 ('Cleaner sheds','Smooth yarns separate cleanly at shed opening.'),
 ('Less fly','Less fly keeps halls and fabric cleaner.'))
h('eco-silsoftner-hydrophobic',
 ('Value-added finishing','A premium hand helps fabrics command better prices.'),
 ('Buyer approval','Matching the approved sample builds buyer trust.'))
h('ecoguard-fp',
 ('Documentation','Test reports support safety inspections.'),
 ('Treatment suitability','Fabric type is checked first.'))
h('ecofix-fb',
 ('Buyer compliance','Checking RSL limits protects orders.'),
 ('Wet fastness','Better wet fastness reduces complaints.'))
h('ecostab-hs',
 ('Fewer pinholes','Stable peroxide reduces catalytic damage.'),
 ('Consistent whiteness','Steady bleaching gives even whiteness.'))
h('ecodesize-ez',
 ('Matching size type','Starch and PVA need different desizing.'),
 ('Gentle on fabric','Controlled conditions protect strength.'))
h('ecoscour-sca-30',
 ('Even dyeing','Clean fabric dyes evenly.'),
 ('Whiteness','Good scouring supports whiteness.'))
h('eco-silsoftner-hydrophilic',
 ('Towel exports','Soft, absorbent towels support export orders.'))
h('ecodye-lev-series',
 ('Fewer re-dyes','Even shades reduce re-processing cost.'))
# services
h('boiler-upgrades-maintenance',
 ('Why older boilers lose efficiency','Over years of service, boilers develop soot on firesides, scale on watersides, leaking refractory and burners that drift out of adjustment. Each fault wastes a little fuel, and together they can add a significant amount to the fuel bill. An overhaul with tuning tackles all of them at once.'),
 ('Flue gas analysis','Measuring oxygen, carbon monoxide and stack temperature shows how well the burner is set. Adjusting air-fuel ratio to the right range saves fuel without making combustion unsafe.'),
 ('Safety devices','Overhauls include checks of safety valves, low-water cut-outs and controls.'))
h('industrial-air-humidification',
 ('Measuring the right conditions','Spinning and weaving halls typically aim for a target relative humidity set for the fibre and process. Measuring at several points shows where humidity is uneven.'),
 ('Energy and maintenance','Well-designed systems use less energy and need simple maintenance, such as nozzle cleaning and water treatment.'),
 ('Static and fly','Correct humidity reduces static, fly and dust in halls.'))
h('cooling-tower-supply-erection',
 ('Material selection','FRP towers resist corrosion and suit many industrial duties.'),
 ('Access and safety','Ladders, platforms and guards make maintenance safe.'),
 ('Performance test','Testing to recognised CTI methods confirms the tower meets design.'))
h('industrial-chiller-systems',
 ('Part-load efficiency','Most chillers spend most of their time at part load, so part-load efficiency matters as much as full-load ratings.'),
 ('Rating standards','Chiller performance is rated to recognised AHRI methods.'),
 ('Refrigerant safety','Installations follow recognised refrigeration safety practice.'))
h('monitoring-controls',
 ('Saving blow-down water','TDS-controlled blow-down discharges only when needed.'),
 ('Shift consistency','Automation removes variation between shifts.'),
 ('Data for audits','Logged data supports energy and water audits.'))
h('reverse-osmosis-ro-plants',
 ('Materials of construction','Pressure vessels, pipework and skids are selected for the water and duty.'),
 ('Operator training','Operators learn daily logging and cleaning triggers.'),
 ('After-sales support','Chemicals and servicing support long-term performance.'))
h('textile-machinery-parts',
 ('Healds and reeds','Correct healds and reeds reduce warp abrasion and reed marks.'),
 ('Picker sticks','Good picker sticks keep shuttle and projectile looms running.'),
 ('Spinning parts','Frame parts affect yarn evenness and breaks.'))
h('plant-erection-installation',
 ('Safety on site','Lifting plans, permits and supervision keep erection safe.'),
 ('Documentation','Records of alignment and tests support handover.'),
 ('Single coordination','One team for mechanical and piping reduces gaps.'))
h('captive-power-plant-support',
 ('Steam purity','Monitoring silica and conductivity in steam limits turbine deposits.'),
 ('Condenser performance','Clean condensers maintain vacuum and output.'),
 ('Outage planning','Inspection during outages guides water treatment.'))
h('industrial-spare-parts',
 ('Faster delivery','Local supply reduces waiting time.'),
 ('Correct materials','Seals and impellers are matched to the fluid.'))
h('erection-commissioning',
 ('Punch lists','Open items are recorded and closed before handover.'),
 ('Safety checks','Safety systems are tested before start-up.'))
h('custom-fabrication',
 ('Design support','Seamens can prepare drawings from your requirements.'),
 ('Coatings','Protective coatings extend life.'))
h('mechanical-maintenance-contracts',
 ('Recognised standards','Condition monitoring follows ISO 20816 and ISO 18436 practice.'))
h('plant-upgradations',
 ('Energy management','ISO 50001 principles guide energy upgrades.'))
h('steam-boiler-supply-erection',
 ('Safety and codes','Boilers are installed with safety valves and controls to recognised practice.'))
