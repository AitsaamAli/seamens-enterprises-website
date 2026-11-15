Y = {}
S = {}
def a(slug, tips, pk, faq3, scen): Y[slug] = dict(tips=tips, pk=pk, faq3=faq3); S[slug] = scen

a('fc-3020',
 ['Log condenser approach temperature weekly; a rising approach is the earliest sign of fouling.','Test circulating water hardness, conductivity and pH at the same point every time.','Keep make-up and blow-down meters working so cycles of concentration are known, not guessed.','Inspect the tower basin each month for sludge and algae.','Review results with Seamens each quarter and adjust the programme to the season.'],
 'Lahore and Karachi summers push A/C plants to full load for months, while municipal and borehole make-up water can carry high hardness and dissolved solids. A programme product like FC-3020, set up for local water and checked through the season, keeps condensers clean when cooling demand and electricity tariffs are both at their highest.',
 [('Is FC-3020 used on its own?','It is part of a programme Seamens sets up for the plant; other products may be added depending on the water.'),('When should treatment start?','Ideally before the cooling season, so condensers start clean and stay clean.')],
 [('Shopping mall and hotel A/C plants','Large commercial plants run long hours with high public expectations. Keeping the circulating water treated protects comfort cooling and avoids peak-season breakdowns.'),
  ('Hospital central cooling','Hospitals cannot tolerate cooling interruptions in theatres and wards. A managed water programme supports reliable, hygienic plant operation.'),
  ('Factory process and comfort cooling','Textile and food plants use A/C for both process and staff comfort. Clean condensers keep energy use and humidity control on target.')])
a('fc-120q',
 ['Test hardness and corrosion indicators monthly.','Install corrosion coupons to see metal loss directly.','Keep dosing continuous; gaps allow scale and corrosion to restart.','Check that blow-down is controlled to the target cycles.','Record chiller condenser pressures to spot fouling early.'],
 'Many Pakistani A/C plants use mixed metallurgy, with copper tubes, steel pipework and galvanised tower components in one circuit. A combined anti-scale and corrosion inhibitor protects these metals together, which is simpler than managing separate chemicals on a busy site.',
 [('Does FC-120Q protect copper tubes?','It is a corrosion inhibitor for A/C plant water; metallurgy is reviewed when the programme is set.'),('How is corrosion checked?','Corrosion coupons measured by weight loss show the actual rate.')],
 [('Office tower chilled water plants','Commercial towers want low running cost and long chiller life. Preventing scale and corrosion protects both.'),
  ('Older plants with corrosion history','Plants that have suffered leaks benefit from a controlled inhibitor programme with coupon monitoring.'),
  ('Plants with variable make-up water','When water quality shifts between borehole and municipal supply, a combined inhibitor gives a stable baseline.')])
a('fc-30b',
 ['Test make-up hardness before and after softening.','Regenerate or service softening equipment on schedule.','Combine softening with inhibitor treatment for full protection.','Check condenser approach temperatures for scale signs.','Keep records of hardness readings for audits.'],
 'Borehole water in many parts of Punjab is hard. For A/C plants using it as make-up, softening the water is often the first and most effective step against scale.',
 [('Does softening remove the need for inhibitors?','Softening reduces scale load; inhibitors are often still used for corrosion and remaining scaling risk.'),('Is Water Safe FC-30B used in boilers or A/C plants?','FC-30B is a water softener product for A/C plants; boiler programmes use the BR range.')],
 [('Plants on hard borehole water','Where make-up hardness is high, softening reduces the scale that forms on condensers.'),
  ('Plants with repeated descaling','Sites that descale often can reduce how often they need to by softening first.'),
  ('New installations','Starting with softened water protects new heat exchangers from the first day.')])
a('fc-7090',
 ['Isolate and circulate the descaler through the heat exchanger as advised.','Monitor the solution during cleaning to judge progress.','Flush thoroughly after descaling.','Restart with a proper inhibitor programme to stop scale returning.','Record approach temperature before and after to show the gain.'],
 'After a hot Pakistani summer, many chiller condensers are scaled and running inefficiently. An organic descaler that is safe for copper and aluminium allows a clean-up before the next season without risking the tubes.',
 [('How do I know descaling worked?','Compare condenser approach and pressures before and after cleaning.'),('What should follow descaling?','A treatment programme to stop new scale forming.')],
 [('Pre-season chiller clean-up','Descaling before summer starts the season with clean, efficient condensers.'),
  ('Aluminium and copper heat exchangers','Sensitive metals need a descaler safe for them; FC-7090 is designed for that.'),
  ('Plants with high head pressure','Rising head pressure often signals scale; descaling restores performance.')])
a('br-111',
 ['Test feed water hardness daily.','Keep blow-down regular to control dissolved solids.','Inspect tubes during annual shutdown.','Record fuel use per tonne of steam.','Combine with oxygen scavenging as advised.'],
 'Pakistan\'s textile and food factories rely heavily on gas and coal-fired boilers, and fuel cost is a major line item. Preventing scale keeps heat transfer efficient and fuel bills lower.',
 [('Can BR-111 remove existing scale?','It is an anti-scalant to prevent scale; existing heavy scale may need cleaning first.'),('How often is dosing checked?','Regularly, alongside boiler water testing.')],
 [('Textile mill process boilers','Mills running boilers around the clock gain the most from keeping tubes clean.'),
  ('Food and beverage plants','Clean, efficient steam supports cooking, sterilising and cleaning.'),
  ('Boilers on hard feed water','Where softening is limited, an anti-scalant adds protection.')])
a('br-555',
 ['Test residual scavenger in boiler water regularly.','Keep the deaerator or feed tank at the right temperature.','Minimise air leaks in the condensate system.','Inspect for pitting during shutdowns.','Dose continuously, not in batches.'],
 'Many smaller boiler houses in Pakistan run without full deaeration, which makes dissolved oxygen a common cause of pitting. A chemical oxygen scavenger fills that gap.',
 [('Do I need BR-555 if I have a deaerator?','A scavenger removes the remaining oxygen after mechanical deaeration.'),('Where is it dosed?','Usually into the feed water; Seamens advises the point.')],
 [('Boilers without deaerators','Chemical scavenging is especially important where oxygen removal is limited.'),
  ('Plants with high make-up rates','Fresh make-up water brings oxygen; scavenging protects against it.'),
  ('Older boilers with pitting history','Controlling oxygen helps slow further damage.')])
a('ct-9080',
 ['Measure cycles of concentration regularly.','Control blow-down to target.','Inspect fill and basin for scale.','Check heat exchanger approach temperatures.','Adjust dose with season and load.'],
 'Cooling towers in Pakistan\'s hot climate evaporate large volumes of water, concentrating minerals quickly. A scale inhibitor allows higher cycles while protecting heat exchangers.',
 [('Can higher cycles save water?','Running higher cycles with good inhibition can reduce make-up water and blow-down.'),('Is CT-9080 a biocide?','No, it is a scale inhibitor; biocide treatment is separate.')],
 [('Industrial process cooling','Plants with process heat exchangers benefit from scale control.'),
  ('Power and captive generation','Engine and condenser cooling need clean exchangers.'),
  ('High-evaporation summer months','Peak summer raises concentration; inhibition keeps scale in check.')])
a('dc-1020',
 ['Inspect fill and basin for deposits.','Monitor biological growth with dip slides.','Combine with biocide treatment.','Check heat exchanger approach.','Clean basins on schedule.'],
 'Dust storms and airborne debris in Pakistani cities load cooling towers with dirt. A dispersant keeps that dirt moving so it is removed in blow-down instead of settling.',
 [('Is DC-1020 used with a biocide?','Yes, dispersants and biocides work together.'),('Does it help with dust?','It keeps particles dispersed so they do not settle.')],
 [('Towers near roads or construction','Airborne dust settles in towers; dispersion helps keep it moving.'),
  ('Towers with slime problems','Dispersants help biocides penetrate and remove slime.'),
  ('Plants with fouled exchangers','Keeping deposits dispersed protects heat transfer.')])
a('bc-1000',
 ['Monitor bacteria with dip slides.','Alternate biocides if advised.','Keep tower covers in place to reduce sunlight.','Clean basins regularly.','Keep records for hygiene audits.'],
 'Strong sunlight and warm temperatures in Pakistan create ideal conditions for algae in cooling towers. A biocide programme protects both hygiene and performance.',
 [('Does BC-1000 control Legionella?','It is a cooling tower biocide; Legionella risk is managed with a full programme following recognised guidance.'),('How often is it dosed?','Seamens sets the dosing schedule for your tower.')],
 [('Hospitals and hotels','Hygiene matters most where people are vulnerable.'),
  ('Open, sunlit towers','Algae grow fastest in sunlight; biocide keeps it under control.'),
  ('Towers near air intakes','Controlling growth supports healthier surroundings.')])
a('br-999',
 ['Test treatment level in the loop regularly.','Find and fix leaks that cause make-up.','Check for corrosion products in the water.','Keep records of top-ups.','Review annually.'],
 'Many large buildings in Pakistan run chilled water loops for years with little attention. Correct closed-circuit treatment protects pipework that is expensive and disruptive to replace.',
 [('How often is a closed loop treated?','Closed loops lose little water; treatment level is checked and topped up as needed.'),('Does BR-999 suit hot water loops?','Ask Seamens for your loop type.')],
 [('Chilled water loops','Protecting pipework avoids leaks and costly replacements.'),
  ('Process closed circuits','Machine cooling circuits benefit from controlled treatment.'),
  ('After loop repairs','Re-treating after draining protects the system.')])
a('rc-1030',
 ['Track normalised permeate flow.','Monitor differential pressure.','Test feed water regularly.','Clean membranes when indicators call for it.','Keep dosing continuous.'],
 'RO plants are common in Pakistani industry because groundwater dissolved solids are high. Anti-scalant dosing protects membranes that are costly to replace.',
 [('How do I know it is working?','Stable normalised flow and pressure show the anti-scalant is protecting the membranes.'),('Is RC-1030 a cleaner?','No, it prevents scaling; cleaning uses separate products.')],
 [('Boiler feed RO','Protecting membranes supports reliable boiler feed water.'),
  ('Drinking and process water RO','Steady permeate output supports production.'),
  ('High-TDS borehole water','High dissolved solids raise scaling risk; anti-scalant counters it.')])
a('rd-4050',
 ['Monitor differential pressure for biofouling signs.','Keep pre-treatment clean.','Dose as scheduled.','Clean membranes when needed.','Check feed water bacteria.'],
 'Warm feed water in Pakistan encourages bacterial growth in RO systems. A biocide programme protects membranes from biofouling.',
 [('Is RD-4050 safe for membranes?','It is a biocide for RO plants; use follows Seamens\' advice for your membranes.'),('Can biofouling be prevented?','Good pre-treatment and biocide dosing reduce it.')],
 [('Plants with warm feed water','Warm water speeds bacterial growth; biocide control helps.'),
  ('Plants with rising pressure drop','Biofouling raises pressure; controlling it restores performance.'),
  ('Food and beverage RO','Hygiene is important where water touches product.')])

from ws_new import Y_NEW as _YN, S_NEW as _SN
Y.update(_YN); S.update(_SN)
