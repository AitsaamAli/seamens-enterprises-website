G = {}
G['rd-4050'] = [
 ('Why biofouling is the most common RO problem','Bacteria enter an RO plant with the feed water and settle on membrane surfaces and spacers. There they multiply and form biofilm, which narrows feed channels, raises differential pressure and lowers permeate flow. Because biofilm grows continuously, it returns after each cleaning unless the cause is controlled.'),
 ('Where a biocide fits','A biocide programme reduces the number of active bacteria reaching and growing on the membranes. Combined with good pre-treatment and timely cleaning, it slows biofouling so cleaning intervals become longer and membrane life improves.'),
 ('Membrane compatibility','Many RO membranes are damaged by strong oxidising chemicals such as free chlorine. That is why biocide choice and dosing method matter. Seamens advises dosing for your membrane type and operating mode.'),
 ('Reading the warning signs','A rise in differential pressure across the first stage, together with a fall in normalised flow, is a typical sign of biofouling. Logging these figures daily shows the trend early.'),
 ('Linking with cleaning','When cleaning is needed, an alkaline membrane cleaner removes biofilm, and biocide treatment then helps keep membranes clean longer.')]
G['bc-1000'] = [
 ('Why towers need biocide','Open cooling towers are warm, wet, aerated and often exposed to sunlight, ideal conditions for algae, bacteria and slime. Biological growth blocks fill and nozzles, reduces heat transfer, increases corrosion under deposits and creates hygiene risks.'),
 ('A managed programme','Biocide is most effective as part of a programme: regular dosing, monitoring with dip slides, physical cleaning of basins and, where advised, use of complementary biocides to prevent resistance.'),
 ('Hygiene and Legionella awareness','Recognised guidance such as ASHRAE 188 and CDC toolkits describe how building owners manage Legionella risk in cooling towers. Biocide treatment is one part of that risk management.'),
 ('Working with dispersants','Dispersants help biocides reach organisms inside deposits.')]
G['rc-1030'] = [
 ('How scaling happens in RO','As water passes through an RO plant, pure water goes through the membrane and salts are concentrated in the reject stream. In the last stage, salts such as calcium carbonate, calcium sulphate and silica can exceed their solubility and form scale on the membrane surface.'),
 ('What an anti-scalant does','An anti-scalant interferes with crystal formation and growth so minerals stay in solution long enough to leave with the concentrate. This allows higher recovery without scaling.'),
 ('Dose based on analysis','The dose depends on feed water analysis and recovery. Seamens reviews the water to set it.'),
 ('Monitoring','Stable normalised flow and pressure in the last stage show scaling is controlled.')]
G['br-999'] = [
 ('Why closed loops still need treatment','Closed chilled and hot water loops lose little water, but the water inside stays in contact with steel, copper and other metals for years. Without treatment, corrosion produces sludge, blocks strainers and leads to leaks.'),
 ('Treatment levels','Treatment level is tested and topped up after any water loss.'),
 ('Finding leaks','High make-up shows leaks that bring in fresh, untreated water.'),
 ('Sludge and strainers','Clean strainers and clear water indicate a healthy loop.')]
G['dc-1020'] = [
 ('What a dispersant does','A dispersant keeps fine particles, silt and organic matter suspended in the circulating water so they leave the system with blow-down rather than settling on fill and heat exchangers.'),
 ('Fouling and heat transfer','Even thin deposits reduce heat transfer and raise approach temperatures.'),
 ('Combined approach','Dispersants work with scale inhibitors and biocides in a full programme.'),
 ('Basin cleaning','Regular basin cleaning removes what settles.')]
G['ct-9080'] = [
 ('Cycles of concentration','As water evaporates, minerals concentrate. Cycles of concentration compare circulating water to make-up water.'),
 ('Saving water','Good inhibition allows higher cycles, reducing make-up and blow-down.'),
 ('Monitoring','Conductivity and hardness tests track cycles.'),
 ('Season changes','Dose adjusts with summer and winter load.')]
G['fc-30b'] = [
 ('Hardness and scale','Calcium and magnesium hardness form scale when water heats or concentrates.'),
 ('Softening first','Reducing hardness lowers scale load on condensers.'),
 ('Testing','Simple hardness tests confirm softening.'),
 ('Combined programmes','Softening works with inhibitors.')]
G['br-555'] = [
 ('How oxygen corrodes boilers','Dissolved oxygen attacks steel and forms pits that penetrate tubes.'),
 ('Residual testing','A small scavenger residual shows oxygen is removed.'),
 ('Feed tank temperature','Hot feed water holds less oxygen.')]
G['fc-7090'] = [
 ('Two-way action','The descaler is designed to act on scale while being safe for copper and aluminium.'),
 ('Flushing','Flush thoroughly after descaling.')]
G['br-111'] = [
 ('Scale costs fuel','Scale insulates tubes so more fuel is needed for the same steam.'),
 ('Blow-down','Blow-down removes concentrated solids.')]
G['fc-120q'] = [
 ('Two problems, one product','Scale and corrosion are the two main threats to A/C plant water systems.')]

from ws_new import G_NEW as _GN
G.update(_GN)

from ws_fix import G_FIX as _GF
G.update(_GF)
