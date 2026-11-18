"""Owner update (Nov 18, 2026): Water Safe FC-120Q is an anti-scale and corrosion inhibitor for air humidification plants,
also used for de-scaling and cleaning of eliminator plates, nozzles, SS caps, tiles, showering pipes, SS clamps and intake grills,
for the long life of A/C plants against scaling, sludge, algae, micro short cotton dust and industrial problems.
Imported at the end of each data module; replaces the earlier FC-120Q wording."""

WS_FIX = {'fc-120q': dict(
  system='Air humidification and A/C plants', role='Anti-scale and corrosion inhibitor, de-scaler and cleaner',
  imgalt='Air humidification plant in a textile mill',
  title='Water Safe FC-120Q | Air Humidification Plant Anti-Scale & Cleaner',
  meta='Water Safe FC-120Q: anti-scale and corrosion inhibitor for air humidification plants, also used to de-scale and clean eliminators, nozzles and grills. 60, 250, 1,000 KG.',
  h1='Water Safe FC-120Q: Anti-Scale and Corrosion Inhibitor for Air Humidification Plants',
  lead='Water Safe FC-120Q is an anti-scale and corrosion inhibitor for air humidification plants. It is also used for de-scaling and cleaning eliminator plates, nozzles, SS caps, tiles, showering pipes, SS clamps and intake grills, so A/C plants last longer and stay free of scaling, sludge, algae, micro short cotton dust and other industrial problems.',
  body=[('Why humidification plants need protection', ['An air washer or humidification plant sprays recirculating water through nozzles and draws air across wet eliminator plates. Hardness in the water leaves scale on nozzles and plates, sludge collects in the tank and on the tiles, and warm, wet surfaces encourage algae.', 'In textile mills the plant also pulls in fine cotton fly and micro short cotton dust. That lint sticks to wet scale and sludge, blocks nozzles and intake grills, and cuts both airflow and humidity control.']),
        ('Protection plus cleaning', ['FC-120Q is dosed into the recirculating water to inhibit scale and corrosion, and it is also used during cleaning to de-scale eliminator plates, nozzles, SS caps, tiles, showering pipes, SS clamps and intake grills. Seamens sets the dose and the cleaning routine for your plant.'])],
  benefits=['Inhibits scale and corrosion in air humidification water', 'De-scales and cleans eliminators, nozzles, grills and pipes', 'Fights sludge, algae and micro short cotton dust build-up'],
  apps=['Air washers and humidification plants in textile mills', 'Eliminator plates, nozzles, SS caps and showering pipes', 'Tiles, SS clamps and intake grills of A/C plants'],
  faqs=[('What does Water Safe FC-120Q do?', 'It is an anti-scale and corrosion inhibitor for air humidification plants, and it is also used to de-scale and clean eliminator plates, nozzles, SS caps, tiles, showering pipes, SS clamps and intake grills.'),
        ('Which problems does FC-120Q help control?', 'Scaling, sludge, algae, micro short cotton dust build-up and the general fouling that shortens the life of A/C and humidification plants.'),
        ('What pack sizes are available?', '60, 250 and 1,000 KG packs.')],
  related=['fc-3020', 'fc-7090', 'fc-30b'])}

X_FIX = {'fc-120q': dict(
  how=['In an air humidification plant, a pump lifts water from the tank to banks of nozzles that spray it into the passing air. Eliminator plates downstream catch the droplets and return them to the tank. Because water keeps evaporating, the minerals it carries concentrate with every hour of running, and they come out as hard scale on nozzles, SS caps, showering pipes and eliminator plates.',
       'Water Safe FC-120Q works on two fronts. Dosed into the recirculating water, it inhibits scale and protects metal parts against corrosion. Used as a cleaning product, it helps de-scale and clean the parts that foul first, so the plant goes back into service with open nozzles, clean plates and clear intake grills.'],
  bens=[('Open, even spray', 'Nozzles and SS caps free of scale give a fine, even spray and steady humidity in the hall.'),
        ('Clean eliminator plates', 'De-scaled plates let air pass freely and catch droplets properly, so water is not carried into ducts.'),
        ('Less sludge in tanks and on tiles', 'Cleaner tanks and tiles mean fewer blocked strainers and less manual scraping.'),
        ('Algae kept down', 'Clean, scale-free surfaces give algae less to cling to between cleanings.'),
        ('Cotton dust does not cake', 'Micro short cotton dust has less wet scale and sludge to stick to, so grills and nozzles stay clearer.'),
        ('Longer plant life', 'Inhibiting scale and corrosion protects SS clamps, showering pipes and pump parts for many seasons.')],
  probs=[('Blocked or uneven nozzles', 'Scale on nozzles and SS caps', 'De-scaling and scale inhibition'),
         ('Water carry-over into ducts', 'Fouled eliminator plates', 'Clean eliminators'),
         ('Sludge and slime in the tank', 'Settled solids, algae and lint', 'Regular cleaning with FC-120Q'),
         ('Choked intake grills', 'Micro short cotton dust on wet deposits', 'Clean grills and surfaces'),
         ('Rusting clamps and fittings', 'Corrosive recirculating water', 'Corrosion inhibition')],
  checks=[('Spray quality', 'Visual check of nozzle spray pattern at each bank', 'ashrae12'),
          ('Water condition', 'Hardness, conductivity and clarity of the tank water', 'bs2486'),
          ('Hall conditions', 'Relative humidity and temperature in the department', 'ashrae188')],
  faq2=[('Can FC-120Q clean eliminator plates?', 'Yes. It is used for de-scaling and cleaning eliminator plates along with nozzles, SS caps, tiles, showering pipes, SS clamps and intake grills.'),
        ('Is FC-120Q only for textile mills?', 'Textile humidification plants are the main use, but any air washer or A/C plant with the same scaling and fouling problems can use it.'),
        ('How often should a humidification plant be cleaned?', 'Seamens sets a routine from your water quality, running hours and lint load, usually reviewed season by season.')],
  refs=['ashrae12', 'ashrae188', 'bs2486'])}

Y_FIX = {'fc-120q': dict(
  tips=['Inspect nozzles bank by bank and clean any that spray unevenly.', 'De-scale eliminator plates before scale bridges the gaps between blades.', 'Drain, clean and rinse the tank and tiles on a fixed routine.', 'Keep intake grills free of cotton fly so airflow stays steady.', 'Keep the inhibitor dose steady between cleanings.'],
  pk='Pakistani spinning and weaving mills run humidification plants almost all year, often on hard borehole water and in air loaded with cotton fly. Scale, sludge, algae and micro short cotton dust build up quickly in this climate, so a product that both protects the water and cleans the plant parts saves downtime and keeps humidity steady in production halls.',
  faq3=[('Does FC-120Q help with algae?', 'Keeping surfaces clean and free of scale and sludge gives algae less to grow on; Seamens adds biocide control where a plant needs it.'),
        ('Can it be used on stainless steel parts?', 'Yes. SS caps, SS clamps and showering pipes are among the parts it is used to clean; the routine is confirmed for your plant.')])}
S_FIX = {'fc-120q': [('Spinning and weaving halls', 'Mills that need tight humidity control rely on open nozzles and clean eliminators, which FC-120Q helps keep in working order.'),
                     ('Plants with heavy cotton fly', 'Where micro short cotton dust is drawn into the air washer, cleaner grills and plates stop lint from caking on wet deposits.'),
                     ('Plants on hard borehole water', 'Hard water scales nozzles and SS caps fastest; scale inhibition plus regular de-scaling keeps the spray even.')]}
G_FIX = {'fc-120q': [('Where scale and dust collect first', 'In an air washer the first parts to foul are the nozzles, SS caps and eliminator plates, followed by the tank tiles and intake grills. Checking these in a fixed order shows quickly whether the plant needs a clean.'),
                     ('A cleaning routine that works', 'Most plants combine a steady inhibitor dose in the water with planned cleaning stops. During a stop, nozzles, eliminators, showering pipes and grills are de-scaled and rinsed, and the tank is drained and cleaned before refilling.')]}
H_FIX = {'fc-120q': [('Nozzle checks', 'A quick walk past each nozzle bank shows blocked or dripping nozzles before humidity drifts.'), ('Planned cleaning stops', 'Cleaning on a fixed routine is faster and cheaper than waiting for a breakdown.')]}
Q_FIX = {'fc-120q': ('What a well-kept plant looks like', 'An even spray from every nozzle, clean eliminator plates, clear intake grills, a clean tank and steady humidity in the hall show that scale, sludge, algae and cotton dust are under control.')}
Z_FIX = {'fc-120q': [('Seasonal review', 'Seamens reviews the dose and the cleaning routine before and after the summer peak.')]}
