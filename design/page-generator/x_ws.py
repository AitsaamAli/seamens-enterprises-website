X = {}
X['fc-3020'] = dict(
 how=['An A/C plant\'s condenser water loop is open to the air at the cooling tower. Water evaporates, minerals concentrate, airborne dust enters and warm, aerated water encourages microbial growth. Left alone, the loop drifts toward scale, corrosion and slime within weeks.',
      'Water Safe FC-3020 is the recirculating-system product in the Seamens A/C plant programme. It is dosed into the loop against your water analysis and kept in range by regular testing, so the circulating water stays in a condition that protects the plant.'],
 bens=[('Lower chiller power use','Clean condenser tubes transfer heat efficiently, so compressors work less for the same cooling output.'),
       ('Protects heat exchangers','Holding the loop in a controlled condition guards tubes and pipework against deposits and corrosion.'),
       ('Programme built on your water','Dosing is set from your own make-up and circulating water analysis, not a generic chart.'),
       ('Fewer unplanned shutdowns','A controlled loop reduces the emergency cleaning that interrupts cooling.'),
       ('Longer equipment life','Protected exchangers, pumps and piping last longer before replacement.'),
       ('Regular follow-up','Seamens reviews the loop on visits and adjusts the programme as conditions change.')],
 probs=[('Rising condenser approach temperature','Fouled condenser tubes','Controlled recirculating water'),('High chiller power bills','Poor heat transfer','Cleaner heat-transfer surfaces'),('Frequent manual cleaning','Uncontrolled loop chemistry','Programme kept in range'),('Corroded loop pipework','Aggressive circulating water','Treatment held in range by testing')],
 checks=[('Loop water chemistry','Conductivity, pH, hardness and alkalinity at each visit','ashrae12'),('Heat-exchanger performance','Condenser approach temperature trend','ahri550'),('Microbial control','Routine microbial checks as part of a water management plan','ashrae188')],
 faq2=[('How often is the loop tested?','At follow-up visits agreed in your programme, more often during start-up.'),('Can FC-3020 be used with other Water Safe products?','Yes. It is part of an A/C plant programme with products such as FC-120Q and FC-30B.'),('Does Seamens train our operators?','Seamens explains the testing and dosing routine to your team as part of the programme.')],
 refs=['ashrae12','ashrae188','ahri550'])

X['fc-120q'] = dict(
 how=['Scale and corrosion attack A/C plants from opposite directions. Hard water deposits minerals on hot surfaces, while oxygen and dissolved salts eat into steel and copper. Inhibitors work by adsorbing on surfaces and holding minerals in solution so neither process takes hold.',
      'Water Safe FC-120Q combines anti-scale and anti-corrosion inhibition for A/C plant water. It is dosed to a target level and checked at visits so protection does not lapse.'],
 bens=[('Two protections in one product','Scale inhibition and corrosion inhibition together simplify the programme.'),
       ('Lower energy use','Scale-free tubes keep heat transfer and chiller efficiency high.'),
       ('Fewer tube failures','Corrosion inhibition protects copper and steel from pitting and leaks.'),
       ('Longer cleaning intervals','Less deposit means less frequent mechanical or chemical cleaning.'),
       ('Lower repair costs','Avoided leaks and tube replacements save significant maintenance spend.'),
       ('Controlled by testing','Residual checks keep inhibitor levels where they work.')],
 probs=[('Scale on condenser tubes','Hard, concentrated water','Scale inhibition'),('Pinhole leaks','Corrosion of tubes','Corrosion inhibition'),('Rising energy bills','Fouled surfaces','Clean heat transfer'),('Short equipment life','Combined scale and corrosion','Dual protection')],
 checks=[('Corrosion rate','Corrosion coupons or probes in the loop','ashrae12'),('Scaling tendency','Calcium hardness, alkalinity and saturation index from water analysis','bs2486'),('Plant efficiency','Condenser approach and chiller performance','ahri550')],
 faq2=[('Is FC-120Q safe for copper?','It is used in A/C plant circuits with copper and steel; suitability is confirmed for your system.'),('How is protection verified?','With water analysis, inhibitor residual checks and corrosion coupons where installed.'),('Can FC-120Q be used in closed loops?','Closed loops normally use Water Safe BR-999; Seamens recommends per system.')],
 refs=['ashrae12','bs2486','ahri550'])

X['fc-30b'] = dict(
 how=['Hardness is the calcium and magnesium dissolved in water. When water is heated or concentrated by evaporation, these minerals come out as scale. Reducing hardness reduces the raw material for scale.',
      'Water Safe FC-30B is the softening product in the A/C plant range. It works alongside inhibitors to lower the scale-forming load in systems fed with hard groundwater.'],
 bens=[('Less scale formation','Lower hardness means less mineral available to deposit.'),
       ('Supports inhibitor performance','A lower scale load makes the rest of the programme more effective.'),
       ('Cleaner heat exchangers','Less deposit keeps tubes efficient between cleanings.'),
       ('Suited to hard Punjab water','Built for systems fed from hard local groundwater.'),
       ('Lower cleaning costs','Fewer descaling jobs over the year.'),
       ('Part of a tested programme','Used where water analysis shows softening is worthwhile.')],
 probs=[('Rapid scale build-up','Very hard make-up water','Reduces hardness'),('Inhibitor overwhelmed','High scale load','Lowers the load'),('Frequent descaling','Hardness deposits','Less deposit formation'),('Inefficient A/C plant','Scaled exchangers','Cleaner surfaces')],
 checks=[('Hardness','Total and calcium hardness of make-up and loop water','bs2486'),('Scaling tendency','Saturation index from full water analysis','ashrae12'),('Exchanger condition','Approach temperature and inspection at overhaul','ahri550')],
 faq2=[('Do all A/C plants need FC-30B?','No. It is used where water analysis shows softening is worthwhile.'),('Can FC-30B replace a softener plant?','Seamens assesses your water and system before recommending the approach.'),('How is the effect measured?','By hardness tests on make-up and circulating water.')],
 refs=['bs2486','ashrae12','ahri550'])

X['fc-7090'] = dict(
 how=['Once scale has formed inside a chiller or A/C heat exchanger, it must be dissolved. FC-7090 is an organic de-scaler with two-way action designed to work while the system keeps running, so cooling does not stop.',
      'Because it is safe for copper and aluminium heat exchangers, it can be used on the mixed-metal equipment common in A/C plants. Seamens plans the dosing and monitors the system during descaling.'],
 bens=[('No shutdown needed','Descale while the plant keeps cooling, avoiding lost production or comfort.'),
       ('Safe for copper and aluminium','Suitable for the metals used in chiller and A/C heat exchangers.'),
       ('Restores efficiency','Removing scale brings back heat transfer and lowers power use.'),
       ('Organic chemistry','An organic de-scaler, gentler than harsh mineral acid cleaning.'),
       ('Certified for CONAIR and Luwa equipment','Seamens water treatment chemicals are certified by CONAIR and Luwa-Nederman for use in their equipment.'),
       ('Supervised application','Seamens plans dosing and checks progress during descaling.')],
 probs=[('Scaled chiller tubes','Hardness deposits','Online organic descaling'),('Cannot afford shutdown','Continuous cooling demand','No shutdown needed'),('Mixed metals at risk','Harsh acid cleaners','Safe for copper and aluminium'),('High power consumption','Poor heat transfer','Efficiency restored')],
 checks=[('Chiller efficiency','Condenser approach and kW/TR before and after descaling','ahri550'),('Water chemistry during descaling','Hardness and pH trends showing scale dissolution','bs2486'),('Metal protection','Corrosion coupons where installed','ashrae12')],
 faq2=[('How long does online descaling take?','It depends on scale thickness and system size; Seamens plans and monitors it.'),('What is FC-70/90?','Another name used for Water Safe FC-7090.'),('Is follow-up treatment needed?','Yes. After descaling, an inhibitor programme keeps scale from returning.')],
 refs=['ahri550','bs2486','ashrae12'])

X['br-111'] = dict(
 how=['Feed water carries hardness into the boiler. As water turns to steam, the hardness concentrates and deposits on hot tubes. An anti-scalant changes how these minerals behave so they stay suspended as a removable sludge instead of a hard scale.',
      'Water Safe BR-111 provides that anti-scale protection for fire-tube and water-tube boilers. The dose is set from feed water analysis and boiler pressure, and blowdown removes the conditioned solids.'],
 bens=[('Lower fuel bills','Scale-free tubes transfer heat efficiently, so less fuel raises the same steam.'),
       ('Protects tubes from overheating','Without insulating scale, tube metal stays cooler and safer.'),
       ('Longer boiler life','Less scale and overheating reduce tube failures and repairs.'),
       ('Fewer acid cleanings','Prevention reduces the need for disruptive descaling.'),
       ('Programme based on your water','Dosed from feed water and boiler water analysis.'),
       ('For fire-tube and water-tube boilers','Covers the boiler types used across Pakistani industry.')],
 probs=[('Rising fuel consumption','Scale on tubes','Scale prevention'),('Tube bulging or failure','Overheating under scale','Cooler, clean tubes'),('Frequent descaling shutdowns','Uncontrolled hardness','Conditioned, removable sludge'),('Unstable steam output','Fouled heat transfer','Clean heating surfaces')],
 checks=[('Boiler water chemistry','TDS, alkalinity and hardness of feed and boiler water','bs2486'),('Operating practice','Feed water and boiler water targets for your pressure','asmefw'),('Fuel efficiency','Fuel used per tonne of steam over time','iso50001')],
 faq2=[('Is BR-111 enough on its own?','It is usually used with an oxygen scavenger such as BR-555 as part of a full programme.'),('Does blowdown matter?','Yes. Blowdown removes the conditioned solids; Seamens helps set the blowdown rate.'),('Can BR-111 be used in high-pressure boilers?','The programme is set for your boiler type and pressure.')],
 refs=['bs2486','asmefw','iso50001'])

X['br-555'] = dict(
 how=['Water exposed to air holds dissolved oxygen. Inside a hot boiler, that oxygen attacks steel in concentrated spots, creating deep pits that can perforate tubes. Deaeration removes most oxygen; a chemical scavenger removes the rest.',
      'Water Safe BR-555 is that scavenger. Dosed to the deaerator or feed line, it reacts with residual oxygen before the water enters the boiler, and a small residual is maintained to protect against oxygen ingress.'],
 bens=[('Prevents pitting corrosion','Removing oxygen stops the most damaging form of boiler corrosion.'),
       ('Protects feed lines and economisers','Scavenging starts before the boiler, protecting the whole feed system.'),
       ('Longer tube life','Fewer pits mean fewer leaks and tube replacements.'),
       ('Safer operation','Sound tubes reduce the risk of sudden failures.'),
       ('Lower maintenance costs','Avoided corrosion damage saves repair spend and downtime.'),
       ('Residual control','A measured residual confirms protection at each check.')],
 probs=[('Pitting on boiler tubes','Dissolved oxygen','Oxygen scavenging'),('Leaks in feed lines','Oxygen corrosion upstream','Dosing at deaerator or feed line'),('Rust in boiler water','Corrosion products','Oxygen removed'),('Short tube life','Ongoing corrosion','Protected metal')],
 checks=[('Scavenger residual','Residual in boiler water at each visit','bs2486'),('Dissolved oxygen','Feed water oxygen after the deaerator','asmefw'),('Iron levels','Iron in boiler water as a corrosion indicator','bs2486')],
 faq2=[('Why use a scavenger if we have a deaerator?','Deaerators remove most oxygen; a scavenger removes the remainder.'),('Is BR-555 hydrazine?','BR-555 is the Water Safe oxygen scavenger; ask Seamens for its data sheet for your application.'),('How is the dose checked?','By measuring the scavenger residual in boiler water.')],
 refs=['bs2486','asmefw'])

X['ct-9080'] = dict(
 how=['Every cycle of evaporation in a cooling tower leaves its minerals behind. The ratio between circulating and make-up water concentration, the cycles of concentration, decides how close the water is to scaling.',
      'Water Safe CT-9080 is a scale inhibitor that keeps those minerals in solution at higher cycles. Running at higher cycles means less blowdown and less make-up water, so the tower saves water and chemical as well as staying clean.'],
 bens=[('Saves water','Higher cycles of concentration cut blowdown and make-up volumes.'),
       ('Keeps fill clean','Prevents the scale that clogs fill and cuts cooling capacity.'),
       ('Protects exchangers','Clean exchangers hold process temperatures and lower energy use.'),
       ('Lower chemical and water bills','Less blowdown means less water and treatment lost to drain.'),
       ('Stable tower performance','Design cooling is held through the season.'),
       ('Programme set from your water','Dose and cycles calculated from make-up analysis.')],
 probs=[('Scaled fill packs','Mineral deposition','Scale inhibition'),('High water consumption','Low cycles of concentration','Supports higher cycles'),('Hot process returns','Fouled exchangers','Clean heat transfer'),('Frequent fill replacement','Clogging deposits','Protected fill')],
 checks=[('Cycles of concentration','Conductivity of circulating versus make-up water','epaws'),('Scaling tendency','Saturation index from water analysis','ashrae12'),('Tower performance','Cold water temperature against design','cti105')],
 faq2=[('How many cycles can my tower run?','It depends on make-up water quality; Seamens calculates it from analysis.'),('Does CT-9080 control algae?','No. Biological control uses Water Safe BC-1000.'),('Will it reduce my water bill?','Higher cycles reduce blowdown and make-up, which lowers water use.')],
 refs=['epaws','ashrae12','cti105'])

X['dc-1020'] = dict(
 how=['A cooling tower is an air scrubber as well as a cooler. Dust, pollen and process contaminants wash into the water and, with biological slime, form deposits in low-flow areas and on exchanger surfaces.',
      'Water Safe DC-1020 disperses these solids, keeping them in suspension so they leave with blowdown. It also helps control scale and biological fouling, keeping exchangers clean and extending fill life.'],
 bens=[('Cleaner heat exchangers','Suspended solids pass through instead of settling on tubes.'),
       ('Longer fill life','Less fouling keeps fill open and efficient for longer.'),
       ('Better cooling performance','Clean fill and exchangers hold design temperatures.'),
       ('Fewer basin clean-outs','Less settled sludge in the tower basin.'),
       ('Helps control biological fouling','Disperses slime so biocides work more effectively.'),
       ('Works with the full programme','Combines with scale inhibitor and biocide.')],
 probs=[('Sludge in tower basin','Settling solids','Dispersion keeps solids moving'),('Clogged fill','Dirt and slime deposits','Dispersant action'),('Fouled exchangers','Deposited solids','Solids leave with blowdown'),('Biocide not working well','Slime protected by deposits','Dispersed deposits')],
 checks=[('Suspended solids and turbidity','Circulating water clarity at visits','ashrae12'),('Tower performance','Approach to design cold water temperature','cti105'),('Deposit inspection','Fill and basin inspection at shutdowns','ashrae188')],
 faq2=[('Is DC-1020 a biocide?','No. It is a dispersant that helps control fouling; BC-1000 is the biocide.'),('Where is DC-1020 dosed?','Into the circulating water, at a rate set from your tower.'),('Does it help with Legionella?','Clean systems support Legionella control, which also needs a biocide and a water management plan.')],
 refs=['ashrae12','ashrae188','cti105'])

X['bc-1000'] = dict(
 how=['Cooling towers are ideal habitats for microbes: warm water, oxygen, sunlight and nutrients. Algae, bacteria and fungi form slime that fouls surfaces and can harbour harmful organisms.',
      'Water Safe BC-1000 is the biocide in the Seamens cooling tower programme. It is dosed on a planned schedule set from tower size and conditions, alongside cleaning and dispersant treatment, as part of a water management plan.'],
 bens=[('Controls algae and slime','Keeps fill, basins and distribution decks cleaner.'),
       ('Protects heat transfer','Slime-free surfaces transfer heat efficiently.'),
       ('Supports Legionella risk management','Biological control is a key part of a water management plan.'),
       ('Prevents under-deposit corrosion','Removing biofilm reduces corrosion beneath deposits.'),
       ('Planned dosing','Scheduled treatment matched to your tower.'),
       ('Healthier site','Better biological control supports safer working conditions.')],
 probs=[('Green algae on deck and fill','Sunlight and nutrients','Algae control'),('Slimy exchanger surfaces','Bacterial growth','Biocide treatment'),('Odour from tower','Microbial growth','Biological control'),('Health risk concerns','Uncontrolled bacteria','Part of a water management plan')],
 checks=[('Microbial counts','Routine bacterial counts in circulating water','ashrae188'),('Legionella risk management','Water management plan and periodic testing','cdcleg'),('Visual condition','Deck, fill and basin inspection','ashrae12')],
 faq2=[('How often is BC-1000 dosed?','On a schedule set from tower size, water and operating conditions.'),('Is BC-1000 enough for Legionella control?','It is one part; a full water management plan includes cleaning, monitoring and records.'),('Can BC-1000 be used in RO plants?','RO plants use Water Safe RD-4050.')],
 refs=['ashrae188','cdcleg','ashrae12'])

X['br-999'] = dict(
 how=['A closed loop, such as chilled water circulating between a chiller and air handlers, loses very little water. With no evaporation, scaling is minor, but corrosion and sludge can still build up over years if the water is untreated.',
      'Water Safe BR-999 treats closed circuits. Because so little water is lost, a correct treatment level lasts a long time and is maintained with periodic tests and small top-ups.'],
 bens=[('Long-lasting protection','Treatment stays in the loop because little water is lost.'),
       ('Low running cost','Small top-ups maintain protection after the initial dose.'),
       ('Protects mixed metals','Guards steel and copper components in the loop.'),
       ('Cleaner coils and strainers','Reduces sludge that blocks coils and valves.'),
       ('Stable chilled water temperatures','Clean loops deliver design capacity to air handlers.'),
       ('Simple monitoring','Periodic tests confirm protection.')],
 probs=[('Black sludge in strainers','Corrosion products','Corrosion protection'),('Blocked fan-coil units','Deposits in loop','Cleaner circuit'),('Leaking pipes','Long-term corrosion','Maintained inhibitor level'),('Loss of cooling at terminals','Fouled coils','Clean heat transfer')],
 checks=[('Inhibitor level','Treatment residual at each check','ashrae12'),('Corrosion indicators','Iron and copper levels in loop water','ashrae12'),('System performance','Chilled water delivery temperatures','ahri550')],
 faq2=[('How often should the loop be checked?','Periodically, at intervals agreed in your programme.'),('What if the loop is topped up often?','Frequent make-up suggests a leak, which should be found and repaired.'),('Is BR-999 for cooling towers?','No. It is for closed circuits; open towers use CT-9080, DC-1020 and BC-1000.')],
 refs=['ashrae12','ahri550'])

X['rc-1030'] = dict(
 how=['In an RO system, pure water passes through the membrane and salts stay behind. Toward the end of each vessel, those salts concentrate past their solubility limit and start to precipitate on the membrane surface.',
      'Water Safe RC-1030 is dosed into the feed before the membranes. It delays crystal formation so concentrated salts stay in solution and leave with the reject stream, protecting the membrane surface.'],
 bens=[('Longer membrane life','Less scaling means membranes last longer before replacement.'),
       ('Stable permeate output','Clean membranes hold their design flow.'),
       ('Lower operating pressure','Unfouled membranes need less pressure, saving pump energy.'),
       ('Fewer chemical cleanings','Prevention reduces how often membranes need cleaning.'),
       ('Higher recovery potential','Scale control can allow the plant to run at the recovery it was designed for.'),
       ('Dose from lab analysis','Calculated from your feed water chemistry.')],
 probs=[('Falling permeate flow','Scale on membranes','Anti-scalant protection'),('Rising feed pressure','Fouled membranes','Cleaner membranes'),('Frequent membrane cleaning','Ongoing scaling','Scale prevention'),('Early membrane replacement','Irreversible scaling','Longer membrane life')],
 checks=[('Normalised performance','Normalised permeate flow and salt passage','astm4516'),('Feed water quality','Silt Density Index before the membranes','astm4189'),('Feed chemistry','Full feed water analysis for dose calculation','who')],
 faq2=[('How is RC-1030 dosed?','Continuously into the RO feed, at a dose calculated from feed analysis.'),('Does RC-1030 clean membranes?','No. It prevents scaling; cleaning uses membrane cleaners.'),('Can it be used with RD-4050?','Yes. RO programmes often combine an anti-scalant with biological control.')],
 refs=['astm4516','astm4189','who'])

X['rd-4050'] = dict(
 how=['Bacteria in RO feed water attach to membrane surfaces and spacers, producing a slimy biofilm. Unlike scale, biofilm grows, so fouling accelerates once it starts.',
      'Water Safe RD-4050 is a biocide for RO plants, used as part of an RO programme to control biological growth. Its use is planned around your membrane type and plant design.'],
 bens=[('Controls biofouling','Keeps biological growth on membranes down.'),
       ('Longer cleaning intervals','Less biofilm means membranes run longer between cleans.'),
       ('Stable pressure drop','Prevents the rising differential pressure caused by biofilm.'),
       ('Protects membrane investment','Reduces the irreversible fouling that shortens membrane life.'),
       ('Complements the anti-scalant','Covers biological fouling while RC-1030 covers scaling.'),
       ('Planned for your plant','Programme set from membrane type and plant design.')],
 probs=[('Rising differential pressure','Biofilm on membranes and spacers','Biological control'),('Slimy membrane surfaces','Bacterial growth','Biocide programme'),('Cleaning becoming less effective','Mature biofilm','Earlier control'),('Short membrane life','Repeated biofouling','Protected membranes')],
 checks=[('Normalised performance','Normalised flow and differential pressure','astm4516'),('Feed water quality','SDI and microbial checks on feed','astm4189'),('Membrane autopsy (if needed)','Inspection of a membrane element','astm4516')],
 faq2=[('Is RD-4050 dosed continuously?','The dosing approach is planned for your plant and membrane type.'),('Can RD-4050 be used on all membranes?','Membrane compatibility is checked before use.'),('What else helps prevent biofouling?','Good pre-treatment, regular monitoring and timely cleaning.')],
 refs=['astm4516','astm4189'])
