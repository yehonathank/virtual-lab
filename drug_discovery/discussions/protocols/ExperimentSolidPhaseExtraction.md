## User

This is the beginning of an individual meeting with Medicinal Chemist to discuss your research project.

Here is context for this meeting:

[begin context 1]

ExperimentSolidPhaseExtraction[Samples]⟹Protocol

generates a Protocol for separating dissolved compounds from Samples according to their physical and chemical properties.



Solid Phase Extraction (SPE) is an extractive technique by which compounds that are dissolved or suspended in a liquid mixture are separated from other compounds in the mixture according to their physical and chemical properties. Because of the different affinity between the compounds in the liquid mixture (known as the mobile phase) and the solid sorbent (known as the stationary phase). In case of positive strategy SPE, the desired analytes are retained on the stationary phase while the mobile phase passes through the resin sorbent packed in the SPE cartridge. The analytes of interest are then removed from the cartridge and collected into the desired eluent for downstream analysis. On the other hand, for negative strategy SPE, the contaminants are retained on the stationary phase, while the desired analytes pass through the resin sorbent with the mobile phase.On the whole, SPE can be used to purify different samples and isolate or concentration analytes of interest from a wide variety of matrices.



Experimental Principles

Figure 1.1: Procedural overview of a Positive ExtractionStrategy of Experiment Solid Phase Extraction (SPE). Step 1 (Optional): The ExtractionCartridge is flushed with PreFlushingSolution (optional) to remove any residues from the packed sorbent prior to start of the protocol. Step 2 (Optional): The ExtractionCartridge is rinsed with ConditioningSolution (optional) to wet and condition the sorbent in order to ensure consistent interaction between the stationary phase and the sample. Step 3: The sample is introduced into the ExtractionCartridge to allow the interaction between the components in the sample and the sorbent. If multiple samples are combined into a pool for solid phase extraction experiment, they are dispensed into the same cartridge in a stepwise fashion. Step 4 (Optional): WashingSolution is transferred into the ExtractionCartridge to elute any contaminants out of the cartridge prior to elution of the components of interest. Step 5 - 6 (Optional): Additional SecondaryWashingSolution and TertiaryWashingSolution can be transferred into the ExtractionCartridge to further wash contaminants out of the resin to increase purity of the eluent. Step 7 (Optional): ElutingSolution is transferred into the ExtractionCartridge to disrupt the interaction between the sample and the sorbent and elute the desired analytes into the collection container.

Figure 1.2: Procedural overview of a Negative ExtractionStrategy of Experiment Solid Phase Extraction (SPE). Step 1 (Optional): The ExtractionCartridge is flushed with PreFlushingSolution (optional) to remove any residues from the packed sorbent prior to start of the protocol. Step 2 (Optional): The ExtractionCartridge is rinsed with ConditioningSolution to wet and condition the sorbent in order to ensure consistent interaction between the stationary phase and the sample. Step 3: The sample is introduced into the ExtractionCartridge to allow the interaction between the contaminants to bind with the sorbent, while desired analytes pass through the resin sorbent and are collected as SamplesOut. If multiple samples are combined into a pool for solid phase extraction experiment, they are dispensed into the same cartridge in stepwise fashion.



Instrumentation

GX-271 for Solid Phase Extraction

Model[Instrument, LiquidHandler, "id:o1k9jAKOwLl8"]

Figure 2.1.1: A 6-port valve syringe pump system is connected to a robotic arm controlled needle in the liquid handler to aspirate and dispense reagents and apply gas toward the sorbent packed ExtractionCartridges for solid-phase extraction of the desired analytes from the samples. Sequentially in each step of the SPE experiment process, Sequentially in each steps of SPE process PreFlushingSolution (Optional), ConditioningSolution (Optional), SamplesIn, WashingSolution (Optional), SecondaryWashingSolution (Optional), TertiaryWashingSolution (Optional) and ElutingSolution (Optional) are aspirated into the syringe from their original containers and then dispensed into the SPE Cartridges via positive displacement of the syringe to allow thorough interaction between the corresponding buffer or sample with the sorbent resin bed in the cartridge. Gas is then applied through the needle to elute the mobile phase into either Waste container or SamplesOut container, depending on the step in the SPE experiment process. The collected SamplesOut are stored for downstream experiments.

Eppendorf 5920R

Model[Instrument, Centrifuge, "id:eGakldJEz14E"]

Figure 2.2.1: Samples to be centrifuged are counterbalanced in available centrifuge bucket slots. The centrifuge spins the buckets around the axis of the main rotor, while applying optional cooling to prevent a buildup of heat caused by the friction of spinning the rotor. As the samples spin, they are exposed to a centrifugal force that is significantly larger than typical gravitational acceleration. The samples can subsequently be collected at the end of the experiment.

Filter Block

Model[Instrument, FilterBlock, "id:rea9jl1orrGr"]

Figure 2.3.1: Instrument diagram for the Filter Block: A filter plate containing sample is positioned inside of a collar which fits over a collection plate within the vacuum manifold. A vacuum generates a pressure gradient that causes the sample to flow through the filter into the collection vessel.

Biotage PRESSURE+ 48 Positive Pressure Manifold

Model[Instrument, PressureManifold, "id:zGj91a7mElrL"]

Figure 2.4.1: A positive pressure manifold that use a compressed gas both to seal the Extractioncartridge and displace reagents, designed specifically 3 mL and 6mL tabless vacuum ExtractionCartridge. Sequentially in each steps of SPE process PreFlushingSolution (Optional), ConditioningSolution (Optional), SamplesIn, WashingSolution (Optional), SecondaryWashingSolution (Optional), TertiaryWashingSolution (Optional) and ElutingSolution (Optional) are manually aspirated by operators and then dispensed on to ExtractionCartridge. Afterwards, the pressure manifold then manually lowered to seal with ExtractionCartridge and positive pressure is applied to the reagents in ExtractionCartridge to pass through ExtractionSorbent. The flowthrough reagents from each steps can be collected in 15 mL conical tube and stored for downstream experiments or discarded.



Experiment Options

General

SampleLabel

The label of the source sample that are being used in the experiment, which is used for identification elsewhere in sample preparation.

Default Value: Automatic

Pattern Description: A string.

Programmatic Pattern: _String | Automatic

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

SourceContainerLabel

The label of the source container that are being used in the experiment, which is used for identification elsewhere in sample preparation.

Default Value: Automatic

Pattern Description: A string.

Programmatic Pattern: _String | Automatic

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreFlushingSolutionLabel

The label of the PreFlushingSolution that is being used in the experiment, which is used for identification elsewhere in sample preparation.

Default Value: Automatic

Pattern Description: A string or Null.

Programmatic Pattern: (_String | Automatic) | Null

Index Matches to: experiment samples

ConditioningSolutionLabel

The label of the ConditioningSolution that is being used in the experiment, which is used for identification elsewhere in sample preparation.

Default Value: Automatic

Pattern Description: A string or Null.

Programmatic Pattern: (_String | Automatic) | Null

Index Matches to: experiment samples

WashingSolutionLabel

The label of the WashingSolution that is being used in the experiment, which is used for identification elsewhere in sample preparation.

Default Value: Automatic

Pattern Description: A string or Null.

Programmatic Pattern: (_String | Automatic) | Null

Index Matches to: experiment samples

SecondaryWashingSolutionLabel

The label of the SecondaryWashingSolution that is being used in the experiment, which is used for identification elsewhere in sample preparation.

Default Value: Automatic

Pattern Description: A string or Null.

Programmatic Pattern: (_String | Automatic) | Null

Index Matches to: experiment samples

TertiaryWashingSolutionLabel

The label of the TertiaryWashingSolution that is being used in the experiment, which is used for identification elsewhere in sample preparation.

Default Value: Automatic

Pattern Description: A string or Null.

Programmatic Pattern: (_String | Automatic) | Null

Index Matches to: experiment samples

ElutingSolutionLabel

The label of the ElutingSolution that is being used in the experiment, which is used for identification elsewhere in sample preparation.

Default Value: Automatic

Pattern Description: A string or Null.

Programmatic Pattern: (_String | Automatic) | Null

Index Matches to: experiment samples

SampleOutLabel

The label of all collected flowthrough sample that are being used in the experiment, which is used for identification elsewhere in sample preparation.

Default Value: Automatic

Pattern Description: A string or Null.

Programmatic Pattern: (_String | Automatic) | Null

Index Matches to: experiment samples

PreFlushingSampleOutLabel

The label of the collected PreFlushingSolution flowthrough sample that are being used in the experiment, which is used for identification elsewhere in sample preparation.

Default Value: Automatic

Pattern Description: A string or Null.

Programmatic Pattern: (_String | Automatic) | Null

Index Matches to: experiment samples

ConditioningSampleOutLabel

The label of the collected ConditioningSolution flowthrough sample that are being used in the experiment, which is used for identification elsewhere in sample preparation.

Default Value: Automatic

Pattern Description: A string or Null.

Programmatic Pattern: (_String | Automatic) | Null

Index Matches to: experiment samples

LoadingSampleFlowthroughSampleOutLabel

The label of the collected LoadingSample flowthrough sample that are being used in the experiment, which is used for identification elsewhere in sample preparation.

Default Value: Automatic

Pattern Description: A string or Null.

Programmatic Pattern: (_String | Automatic) | Null

Index Matches to: experiment samples

WashingSampleOutLabel

The label of the collected WashingSolution flowthrough sample that are being used in the experiment, which is used for identification elsewhere in sample preparation.

Default Value: Automatic

Pattern Description: A string or Null.

Programmatic Pattern: (_String | Automatic) | Null

Index Matches to: experiment samples

SecondaryWashingSampleOutLabel

The label of the collected SecondaryWashingSolution flowthrough sample that are being used in the experiment, which is used for identification elsewhere in sample preparation.

Default Value: Automatic

Pattern Description: A string or Null.

Programmatic Pattern: (_String | Automatic) | Null

Index Matches to: experiment samples

TertiaryWashingSampleOutLabel

The label of the collected TertiaryWashingSolution flowthrough sample that are being used in the experiment, which is used for identification elsewhere in sample preparation.

Default Value: Automatic

Pattern Description: A string or Null.

Programmatic Pattern: (_String | Automatic) | Null

Index Matches to: experiment samples

ElutingSampleOutLabel

The label of the collected ElutingSolution flowthrough sample that are being used in the experiment, which is used for identification elsewhere in sample preparation.

Default Value: Automatic

Pattern Description: A string or Null.

Programmatic Pattern: (_String | Automatic) | Null

Index Matches to: experiment samples

ContainerOutLabel

The label of the destination container that are being used in the experiment, which is used for identification elsewhere in sample preparation.

Default Value: Automatic

Pattern Description: A string or Null.

Programmatic Pattern: (_String | Automatic) | Null

Index Matches to: experiment samples

ExtractionCartridgeLabel

The label of the ExtractionCartridge that are being used in the experiment, which is used for identification elsewhere in sample preparation.

Default Value: Automatic

Pattern Description: A string or Null.

Programmatic Pattern: (_String | Automatic) | Null

Index Matches to: experiment samples

ExtractionStrategy

Strategy for SolidPhaseExtraction, where Positive means analytes of interest are adsorbed on sorbent component. Negative means that impurities adsorb onto sorbent and analytes pass through unretained. See figures...

Default Value: Positive

Pattern Description: Positive or Negative or Null.

Programmatic Pattern: (Positive | Negative) | Null

Index Matches to: experiment samples

ExtractionMode

The strategy used to select the mobile phase and solid support intended to maximally separate impurities from analytes. ReversePhase separates compounds based on polarity. Sorbent material retains non-polar molecules on its surface. NormalPhase separates compounds based on polarity. Sorbent material retains polar molecules on its surface. IonExchange separates compounds based charge. Sorbent material retains charged molecules on its surface. Affinity separates compounds based on "Lock-and-Key" model between molecules and sorbent materials. Sorbent material selectively retains molecules of interest.

Default Value: Automatic

Default Calculation: Automatically set to match with solution and ExtractionSorbent selected.

Pattern Description: NormalPhase, ReversePhase, IonExchange, SizeExclusion, Affinity, or Chiral or Null.

Programmatic Pattern: (SeparationModeP | Automatic) | Null

Index Matches to: experiment samples

ExtractionSorbent

The material that adsorb analytes or impurities of interest.

Default Value: Automatic

Default Calculation: Automatically resolved to C18, unless ExtractionCartridge or ExtractionSorbent is specified.

Pattern Description: QuaternaryAmmoniumIon, C4, C8, C18, C18Aq, C30, DiVinylBenzene, Biphenyl, Amide, Amine, Polysaccharide, ProteinG, Silica, Carboxylate, AluminaA, AluminaB, AluminaN, Aminopropyl, Diol, Cyanopropyl, Florisil, HLB, WAX, MAX, MCX, WCX, SizeExclusion, Affinity, Chiral, or Null.

Programmatic Pattern: (SolidPhaseExtractionFunctionalGroupP | Automatic) | Null

Index Matches to: experiment samples

ExtractionCartridge

The sorbent-packed container that forms the stationary phase of the extraction for each sample pool. Samples within the same pool are added to the same ExtractionCartridge's well or vessel, depends on the type of ExtractionCartridge (this is where pooling occurs in SolidPhaseExtraction).

Default Value: Automatic

Default Calculation: Automatically ExtractionCartridge that has C18 ExtractionSorbent, that also fit with the Instrument.

Pattern Description: An object of type or subtype Model[Container, ExtractionCartridge], Object[Container, ExtractionCartridge], Model[Container, Vessel, Filter], Object[Container, Vessel, Filter], Model[Container, Plate, Filter], or Object[Container, Plate, Filter] or a prepared sample.

Programmatic Pattern: (ObjectP[{Model[Container, ExtractionCartridge], Object[Container, ExtractionCartridge], Model[Container, Vessel, Filter], Object[Container, Vessel, Filter], Model[Container, Plate, Filter], Object[Container, Plate, Filter]}] | _String) | Automatic

Index Matches to: experiment samples

Instrument

The Instrument that generate force to drive the fluid through the sorbent during PreFlushing, Conditioning, LoadingSample, Washing and Eluting steps.

Default Value: Automatic

Default Calculation: Automatically set to match the number of SamplesIn, Volume of all mobile phase solution and collection condition. In case that we cannot find the most compatible instrument, it will default to Gilson GX271 LiquidHandler.

Pattern Description: An object of type or subtype Model[Instrument, LiquidHandler], Object[Instrument, LiquidHandler], Model[Instrument, PressureManifold], Object[Instrument, PressureManifold], Model[Instrument, Centrifuge], Object[Instrument, Centrifuge], Model[Instrument, FilterBlock], or Object[Instrument, FilterBlock]

Programmatic Pattern: ObjectP[{Model[Instrument, LiquidHandler], Object[Instrument, LiquidHandler], Model[Instrument, PressureManifold], Object[Instrument, PressureManifold], Model[Instrument, Centrifuge], Object[Instrument, Centrifuge], Model[Instrument, FilterBlock], Object[Instrument, FilterBlock]}] | Automatic

Index Matches to: experiment samples

ExtractionMethod

The type of force that is used to flush fluid or sample through the sorbent.

Default Value: Automatic

Default Calculation: Automatically set to match with the chosen Instrument to run SolidPhaseExtraction.

Pattern Description: Injection, Gravity, Pressure, Vacuum, Pipette, or Centrifuge.

Programmatic Pattern: SolidPhaseExtractionMethodP | Automatic

Index Matches to: experiment samples

ExtractionTemperature

The environmental temperature where the Instrument is set up for ExperimentSolidPhaseExtraction to be performed. The solutions' temperture can be different from ExtractionTemperature.

Default Value: Ambient

Pattern Description: Ambient or greater than or equal to -20 degrees Celsius and less than or equal to 60 degrees Celsius.

Programmatic Pattern: RangeP[-20*Celsius, 60*Celsius] | Ambient

Index Matches to: experiment samples

ExtractionCartridgeStorageCondition

The conditions under which ExtractionCartridges used by this experiment is stored after the protocol is completed.

Default Value: Disposal

Pattern Description: Storage Object or Storage Type or Null.

Programmatic Pattern: ((SampleStorageTypeP | Disposal) | ObjectP[Model[StorageCondition]]) | Null

Index Matches to: experiment samples

WorkCell

Indicates the work cell that this primitive will be run on if Preparation->Robotic.

Default Value: Automatic

Default Calculation: Automatically set to STAR if Preparation->Robotic.

Pattern Description: STAR, bioSTAR, or microbioSTAR or Null.

Programmatic Pattern: ((STAR | bioSTAR | microbioSTAR) | Automatic) | Null

Preparation

Indicates if this unit operation is carried out primarily robotically or manually. Manual unit operations are executed by a laboratory operator and robotic unit operations are executed by a liquid handling work cell.

Default Value: Automatic

Pattern Description: Manual or Robotic.

Programmatic Pattern: PreparationMethodP | Automatic

PreFlushing

PreFlushing

Indicates if sorbent should be washed with PreFlushingSolution prior to Conditioning.

Default Value: True

Pattern Description: True or False.

Programmatic Pattern: BooleanP

Index Matches to: experiment samples

PreFlushingSolution

The solution that is used to wash the sorbent clean of any residues from manufacturing or storage processes, prior to Conditioning.

Default Value: Automatic

Default Calculation: Automatically set to match ElutingSolution if ExtractionStrategy is Positive. And automatically set to match SampleIn's Solvent field if ExtractionStrategy is Negative.

Pattern Description: An object of type or subtype Object[Sample] or Model[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Object[Sample], Model[Sample]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

PreFlushingSolutionVolume

The amount of PreFlushingSolution is flushed through the sorbent to remove any residues prior to Conditioning.

Default Value: Automatic

Default Calculation: Automatically set to MaxVolume of ExtractionCartridge or MaxVolume of CollectionContainer, which ever is smaller.

Pattern Description: Greater than or equal to 0. milliliters and less than or equal to 20 liters or Null.

Programmatic Pattern: (RangeP[0.*Milliliter, $MaxTransferVolume] | Automatic) | Null

Index Matches to: experiment samples

PreFlushingSolutionTemperature

The set temperature that PreFlushingSolution is incubated for PreFlushingTemperatureEquilibrationTime before being flushed through the sorbent. The final temperature of PreFlushingSolution is assumed to equilibrate with the set PreFlushingSolutionTemperature.

Default Value: Ambient

Pattern Description: Ambient or greater than or equal to -20 degrees Celsius and less than or equal to 500 degrees Celsius or Null.

Programmatic Pattern: (RangeP[$MinIncubationTemperature, $MaxIncubationTemperature] | Ambient) | Null

Index Matches to: experiment samples

PreFlushingSolutionTemperatureEquilibrationTime

The amount of time that PreFlushingSolution is incubated to achieve the set PreFlushingTemperature. The final temperature of PreFlushingSolution is assumed to equilibrate with the the set PreFlushingTemperature.

Default Value: Automatic

Default Calculation: Automatically set to 3 Minutes, if PreFlushingTemperature is not Ambient.

Pattern Description: Greater than or equal to 0 minutes and less than or equal to 72 hours or Null.

Programmatic Pattern: (RangeP[0*Minute, $MaxExperimentTime] | Automatic) | Null

Index Matches to: experiment samples

CollectPreFlushingSolution

Indicates if the PreFlushingSolution is collected after flushed through the sorbent.

Default Value: Automatic

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

Index Matches to: experiment samples

PreFlushingSolutionCollectionContainer

The container that is used to accumulates any flow through solution in PreFlushing step. The collected volume might be less than PreFlushingSolutionVolume because some of PreFlushingSolution left in cartrdige (the solution is not purged through the sorbent).

Default Value: Automatic

Default Calculation: Automatically set to generic container that the instrument can accommodate (point to instrument diagram or make a table).

Pattern Description: An object of type or subtype Model[Container] or Object[Container] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Container], Object[Container]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

PreFlushingSolutionDispenseRate

The rate at which the PreFlushingSolution is applied to the sorbent by Instrument during Preflushing step.

Default Value: Automatic

Default Calculation: Automatically set to 3*Milliliter/Minute.

Pattern Description: Greater than or equal to 0 milliliters per minute and less than or equal to 1180 milliliters per minute or Null.

Programmatic Pattern: (RangeP[0*(Milliliter/Minute), 1180*(Milliliter/Minute)] | Automatic) | Null

Index Matches to: experiment samples

PreFlushingSolutionDrainTime

The amount of time for PreFlushingSolution to be flushed through the sorbent. If PreFlushingSolutionUntilDrained is set to True, then PreFlushingSolution is continually flushed through the ExtractionCartridge in cycle of PreFlushingSolutionDrainTime until it is drained entirely. If PreFlushingSolutionUntilDrained is set to False, then PreFlushingSolution is flushed through ExtractionCartridge for PreFlushingSolutionDrainTime once.

Default Value: Automatic

Default Calculation: If the Volume and Rate is given then it is calculate by Volume/Rate. Otherwise automatically set to 2 minutes, or the value of MaxPreFlushingSolutionDrainTime, whichever is shorter.

Pattern Description: Greater than or equal to 0 minutes and less than or equal to 72 hours or Null.

Programmatic Pattern: (RangeP[0*Minute, $MaxExperimentTime] | Automatic) | Null

Index Matches to: experiment samples

PreFlushingSolutionUntilDrained

Indicates if PreFlushingSolution is continually flushed through the cartridge in cycle of every PreFlushingDrainTime until it is drained entirely, or until MaxPreFlushingDrainTime has been reached.

Default Value: Automatic

Default Calculation: Automatically set to True if ExtractionMethod are Gravity, Pressure, Vacuum or Centrifuge.

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

Index Matches to: experiment samples

MaxPreFlushingSolutionDrainTime

Indicates the maximum amount of time to flush PreFlushingSolution through sorbent. PreFlushingSolution is flushed in cycles of PreFlushingDrainTime until either PreFlushingSolution is entirely drained or MaxPreFlushingDrainTime has been reached.

Default Value: Automatic

Default Calculation: Automatically set to 3 time of the maximum of PreFlushingDrainTime.

Pattern Description: Greater than 0 minutes or Null.

Programmatic Pattern: (GreaterP[0*Minute] | Automatic) | Null

Index Matches to: experiment samples

PreFlushingSolutionCentrifugeIntensity

The rotational speed or gravitational force at which the ExtractionCartridge is centrifuged to flush PreFlushingSolution through the sorbent.

Default Value: Automatic

Default Calculation: Automatically set to 50% of Centrifuge's MaxRotationRate or, if ExtractionMethod is Centrifuge.

Pattern Description: Force or Speed or Null.

Programmatic Pattern: ((RangeP[0*RPM, 10000*RPM] | GreaterP[0*GravitationalAcceleration]) | Automatic) | Null

Index Matches to: experiment samples

PreFlushingSolutionPressure

The target pressure applied to the ExtractionCartridge to flush PreFlushingSolution through the sorbent. If Instrument is Model[Instrument,PressureManifold,"MPE2"], the PreFlushingSolutionPressure is set to be LoadingSamplePressure (Pressure of Model[Instrument,PressureManifold,"MPE2"] cannot be changed while the Experiment is running).

Default Value: Automatic

Default Calculation: Automatically set to 10 PSI. if ExtractionMethod is Pressure.

Pattern Description: Greater than or equal to 0 pounds‐force per inch squared and less than or equal to 100 pounds‐force per inch squared in increments of 1 pound‐force per inch squared or Null.

Programmatic Pattern: (RangeP[0*PSI, 100*PSI, 1*PSI] | Automatic) | Null

Index Matches to: experiment samples

Conditioning

Conditioning

Indicates if sorbent is equilibrate with ConditioningSolution in order to chemically prepare the sorbent to bind either to analytes if ExtractionStrategy is Positive, or to impurities if ExtractionStrategy is Negative.

Default Value: True

Pattern Description: True or False.

Programmatic Pattern: BooleanP

Index Matches to: experiment samples

ConditioningSolution

The solution that is flushed through the sorbent in order to chemically prepare the sorbent to bind either to analytes if ExtractionStrategy is Positive, or to impurities if ExtractionStrategy is Negative.

Default Value: Automatic

Default Calculation: Automatically set to match with ExtractionSorbent as indicate in Table... .

Pattern Description: An object of type or subtype Object[Sample] or Model[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Object[Sample], Model[Sample]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

ConditioningSolutionVolume

The amount of ConditioningSolution that is flushed through the sorbent to chemically prepare it to bind either analytes if ExtractionStrategy is Positive, or impurities if ExtractionStrategy is Negative.

Default Value: Automatic

Default Calculation: Automatically set to MaxVolume of ExtractionCartridge or MaxVolume of CollectionContainer, which ever is smaller.

Pattern Description: Greater than or equal to 0. milliliters and less than or equal to 20 liters or Null.

Programmatic Pattern: ((Null | RangeP[0.*Milliliter, $MaxTransferVolume]) | Automatic) | Null

Index Matches to: experiment samples

ConditioningSolutionTemperature

The set temperature that ConditioningSolution is incubated for ConditioningSolutionTemperatureEquilibrationTime before being flushed through the sorbent. The final temperature of ConditioningSolution is assumed to equilibrate with the set ConditioningSolutionTemperature.

Default Value: Ambient

Pattern Description: Ambient or greater than or equal to -20 degrees Celsius and less than or equal to 500 degrees Celsius or Null.

Programmatic Pattern: (Null | (RangeP[$MinIncubationTemperature, $MaxIncubationTemperature] | Ambient)) | Null

Index Matches to: experiment samples

ConditioningSolutionTemperatureEquilibrationTime

The amount of time that ConditioningSolution is incubated to achieve the set ConditioningSolutionTemperature. The final temperature of ConditioningSolution is assumed to equilibrate with the the set ConditioningSolutionTemperature.

Default Value: Automatic

Default Calculation: Automatically set to 3 Minutes, if ConditioningSolutionTemperature is not Ambient.

Pattern Description: Greater than or equal to 0 minutes and less than or equal to 72 hours or Null.

Programmatic Pattern: ((Null | RangeP[0*Minute, $MaxExperimentTime]) | Automatic) | Null

Index Matches to: experiment samples

CollectConditioningSolution

Indicates if the ConditioningSolution is collected and saved after flushing through the sorbent.

Default Value: Automatic

Pattern Description: True or False or Null.

Programmatic Pattern: ((Null | BooleanP) | Automatic) | Null

Index Matches to: experiment samples

ConditioningSolutionCollectionContainer

The container that is used to accumulates any flow through solution in Conditioning step. The collected volume might be less than ConditioningSolutionVolume because some of ConditioningSolution left in cartrdige (the solution is not purged through the sorbent).

Default Value: Automatic

Default Calculation: Automatically set to generic container that the instrument can accommodate (point to instrument diagram or make a table).

Pattern Description: An object of type or subtype Model[Container] or Object[Container] or a prepared sample or Null.

Programmatic Pattern: ((Null | (ObjectP[{Model[Container], Object[Container]}] | _String)) | Automatic) | Null

Index Matches to: experiment samples

ConditioningSolutionDispenseRate

The rate at which the ConditioningSolution is applied to the sorbent by Instrument during Conditioning step.

Default Value: Automatic

Default Calculation: Automatically set to 3*Milliliter/Minute.

Pattern Description: Greater than or equal to 0 milliliters per minute and less than or equal to 1180 milliliters per minute or Null.

Programmatic Pattern: ((Null | RangeP[0*(Milliliter/Minute), 1180*(Milliliter/Minute)]) | Automatic) | Null

Index Matches to: experiment samples

ConditioningSolutionDrainTime

The amount of time to set on the Instrument for ConditioningSolution to be flushed through the sorbent. If ConditioningSolutionUntilDrained is set to True, then ConditioningSolution is continually flushed through the ExtractionCartridge in cycle of ConditioningSolutionDrainTime until it is drained entirely. If ConditioningSolutionUntilDrained is set to False, then ConditioningSolution is flushed through ExtractionCartridge for ConditioningSolutionDrainTime once.

Default Value: Automatic

Default Calculation: If the Volume and Rate is given then it is calculate by Volume/Rate. Otherwise automatically set to 2 minutes, or the value of MaxConditioningSolutionDrainTime, whichever is shorter.

Pattern Description: Greater than or equal to 0 minutes and less than or equal to 72 hours or Null.

Programmatic Pattern: ((Null | RangeP[0*Minute, $MaxExperimentTime]) | Automatic) | Null

Index Matches to: experiment samples

ConditioningSolutionUntilDrained

Indicates if ConditioningSolution is continually flushed through the cartridge in cycle of ConditioningSolutionDrainTime until it is drained entirely, or until MaxConditioningSolutionDrainTime has been reached.

Default Value: Automatic

Default Calculation: Automatically set to True if ExtractionMethod are Gravity, Pressure, Vacuum or Centrifuge.

Pattern Description: True or False or Null.

Programmatic Pattern: ((Null | BooleanP) | Automatic) | Null

Index Matches to: experiment samples

MaxConditioningSolutionDrainTime

Indicates the maximum amount of time to flush ConditioningSolution through sorbent. ConditioningSolution is flushed in cycles of every ConditioningSolutionDrainTime until MaxConditioningSolutionDrainTime has been reached.

Default Value: Automatic

Default Calculation: Automatically set to 3 times of maximum ConditioningSolutionDrainTime.

Pattern Description: Greater than 0 minutes or Null.

Programmatic Pattern: ((Null | GreaterP[0*Minute]) | Automatic) | Null

Index Matches to: experiment samples

ConditioningSolutionCentrifugeIntensity

The rotational speed or gravitational force at which the ExtractionCartridge is centrifuged to flush ConditioningSolution through the sorbent.

Default Value: Automatic

Default Calculation: Automatically set to 50% of Centrifuge's MaxRotationRate or, if ExtractionMethod is Centrifuge.

Pattern Description: Force or Speed or Null.

Programmatic Pattern: ((Null | (RangeP[0*RPM, 10000*RPM] | GreaterP[0*GravitationalAcceleration])) | Automatic) | Null

Index Matches to: experiment samples

ConditioningSolutionPressure

The target pressure applied to the ExtractionCartridge to flush ConditioningSolution through the sorbent. If Instrument is Model[Instrument,PressureManifold,"MPE2"], the ConditioningSolutionPressure is set to be LoadingSamplePressure (Pressure of Model[Instrument,PressureManifold,"MPE2"] cannot be changed while the Experiment is running).

Default Value: Automatic

Default Calculation: Automatically set to 10 PSI. Applies to ExtractionMethod : Pressure.

Pattern Description: Greater than or equal to 0 pounds‐force per inch squared and less than or equal to 100 pounds‐force per inch squared in increments of 1 pound‐force per inch squared or Null.

Programmatic Pattern: ((Null | RangeP[0*PSI, 100*PSI, 1*PSI]) | Automatic) | Null

Index Matches to: experiment samples

LoadingSample

LoadingSampleVolume

The amount of each individual input sample that is applied into the sorbent. LoadingSampleVolume is set to All, then all of pooled sample will be loaded in to ExtractionCartridge. If multiple samples are included in the same pool, individual samples are loaded sequentially.

Default Value: Automatic

Default Calculation: Automatically set to the whole volume of the sample or MaxVolume of ExtractionCartridge, whichever is smaller. When All is specified, it is set to the smaller of 105% of the volume of the sample or MaxVolume of ExtractionCartridge, to ensure the complete transfer.

Pattern Description: All or greater than or equal to 0 milliliters and less than or equal to 20 liters.

Programmatic Pattern: (RangeP[0*Milliliter, $MaxTransferVolume] | All) | Automatic

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

QuantitativeLoadingSample

Indicates if each individual sample source containers are rinsed with QuantitativeLoadingSampleSolution, and then that rinsed solution is applied into the sorbent to help ensure that all SampleIn is transferred to the sorbent. Only applies when LoadingSampleVolume is set to All.

Default Value: False

Pattern Description: True or False.

Programmatic Pattern: BooleanP

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

QuantitativeLoadingSampleSolution

Solution that is used to rinse each individual sample source containers to ensure that all SampleIn is transferred to the sorbent.

Default Value: Automatic

Default Calculation: Automatically set to ConditioningSolution.

Pattern Description: An object of type or subtype Object[Sample] or Model[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Object[Sample], Model[Sample]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

QuantitativeLoadingSampleVolume

The amount of QuantitativeLoadingSampleSolution to added and rinsed source container of each individual sample to ensure that all SampleIn is transferred to the sorbent.

Default Value: Automatic

Default Calculation: Automatically set to 20% of volume of each individual samples or 20% of MaxVolume of source container, whichever is smaller, if QuantitativeLoadingSample is set to True.

Pattern Description: Greater than or equal to 0 milliliters and less than or equal to 20 liters or Null.

Programmatic Pattern: (RangeP[0*Milliliter, $MaxTransferVolume] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

LoadingSampleTemperature

The set temperature that individual SampleIn is incubated for LoadingSampleTemperatureEquilibrationTime before being loaded into the sorbent.

Default Value: Ambient

Pattern Description: Ambient or greater than or equal to -20 degrees Celsius and less than or equal to 500 degrees Celsius or Null.

Programmatic Pattern: (Null | (RangeP[$MinIncubationTemperature, $MaxIncubationTemperature] | Ambient)) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

LoadingSampleTemperatureEquilibrationTime

The amount of time that individual samples are incubated at LoadingSampleTemperature.

Default Value: Automatic

Default Calculation: Automatically set to 3 Minutes, if LoadingSampleTemperature is not Ambient.

Pattern Description: Greater than or equal to 0 minutes and less than or equal to 72 hours or Null.

Programmatic Pattern: ((Null | RangeP[0*Minute, $MaxExperimentTime]) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

CollectLoadingSampleFlowthrough

Indicates if the any material that exit the sorbent is collected while sample is being loaded into the sorbent.

Default Value: Automatic

Default Calculation: Automatically set to True, if ExtractionStrategy is Negative. And automastically set to False, if ExtractionStrategy is Positive.

Pattern Description: True or False or Null.

Programmatic Pattern: (Null | BooleanP) | Automatic

Index Matches to: experiment samples

LoadingSampleFlowthroughContainer

The container that is used to accumulates any material that exit the sorbent while sample is being loaded into the sorbent. The collected pooled sample flowthrough volume might be less than LoadingSampleVolume because some of SampleIn left in cartrdige (the pooled SampleIn is not purged through the sorbent).

Default Value: Automatic

Default Calculation: Automatically set to generic container that the instrument can accommodate (point to instrument diagram or make a table).

Pattern Description: An object of type or subtype Model[Container] or Object[Container] or a prepared sample or Null.

Programmatic Pattern: ((Null | (ObjectP[{Model[Container], Object[Container]}] | _String)) | Automatic) | Null

Index Matches to: experiment samples

LoadingSampleDispenseRate

The rate at which individual samples are dispensed into the sorbent during sample loading.

Default Value: Automatic

Default Calculation: Automatically set to match with (Table machine).

Pattern Description: Greater than or equal to 0 milliliters per minute and less than or equal to 1180 milliliters per minute or Null.

Programmatic Pattern: ((Null | RangeP[0*(Milliliter/Minute), 1180*(Milliliter/Minute)]) | Automatic) | Null

Index Matches to: experiment samples

LoadingSampleDrainTime

The amount of time that the sample is flushed through the sorbent after sample loading.

Default Value: Automatic

Default Calculation: If the LoadingSampleVolume and LoadingSampleDispenseRate is given then it is calculate by Volume/Rate. Otherwise automatically set to 2 minutes, or the value of SampleMaxDrainTime, whichever is shorter.

Pattern Description: Greater than or equal to 0 minutes and less than or equal to 72 hours or Null.

Programmatic Pattern: (Null | RangeP[0*Minute, $MaxExperimentTime]) | Automatic

Index Matches to: experiment samples

LoadingSampleUntilDrained

Indicates if the sample is continually flushed through the cartridge in cycle of LoadingSampleDrainTime until it is drained entirely, or until MaxSampleDrainTime has been reached.

Default Value: Automatic

Default Calculation: Automatically set to True if ExtractionMethod is Gravity, Pressure, Vacuum or Centrifuge.

Pattern Description: True or False or Null.

Programmatic Pattern: ((Null | BooleanP) | Automatic) | Null

Index Matches to: experiment samples

MaxLoadingSampleDrainTime

Indicates the maximum amount of time to flush the sample through sorbent. Sample is flushed in cycles of LoadingSampleDrainTime until either LoadingSampleVolume is entirely drained or MaxLoadingSampleDrainTime has been reached.

Default Value: Automatic

Default Calculation: Automatically set to 3 * of the maximum of LoadingSampleDrainTime.

Pattern Description: Greater than 0 minutes or Null.

Programmatic Pattern: ((Null | GreaterP[0*Minute]) | Automatic) | Null

Index Matches to: experiment samples

LoadingSampleCentrifugeIntensity

The rotational speed or gravitational force at which the ExtractionCartridge is centrifuged to flush pooled sample through the sorbent.

Default Value: Automatic

Default Calculation: Automatically set to 50% of Centrifuge's MaxRotationRate or, if ExtractionMethod is Centrifuge.

Pattern Description: Force or Speed or Null.

Programmatic Pattern: ((Null | (RangeP[0*RPM, 10000*RPM] | GreaterP[0*GravitationalAcceleration])) | Automatic) | Null

Index Matches to: experiment samples

LoadingSamplePressure

The target pressure applied to the ExtractionCartridge to flush pooled SampleIn through the sorbent. If Instrument is Model[Instrument,PressureManifold,"MPE2"], the LoadingSamplePressure applies to PreFlushingSolutionPressure, ConditioningSolutionPressure, WashingSolutionPressure and ElutingSolutionPressure as well (Pressure of Model[Instrument,PressureManifold,"MPE2"] cannot be changed while the Experiment is running).

Default Value: Automatic

Default Calculation: Automatically set to 10 PSI. Applies to ExtractionMethod : Pressure.

Pattern Description: Greater than or equal to 0 pounds‐force per inch squared and less than or equal to 100 pounds‐force per inch squared in increments of 1 pound‐force per inch squared or Null.

Programmatic Pattern: ((Null | RangeP[0*PSI, 100*PSI, 1*PSI]) | Automatic) | Null

Index Matches to: experiment samples

Washing

Washing

Indicates if analyte-bound-sorbent is flushed with WashingSolution to get rid non-specific binding and and improve extraction purity.

Default Value: Automatic

Default Calculation: Automatically set to True, if ExtractionStrategy is Positive

Pattern Description: True or False.

Programmatic Pattern: BooleanP | Automatic

Index Matches to: experiment samples

WashingSolution

The solution that is flushed through the analyte-bound-sorbent to get rid of non-specific binding and improve extraction purity.

Default Value: Automatic

Default Calculation: Automatically set to match with ExtractionSorbent as indicate in Table... .

Pattern Description: An object of type or subtype Object[Sample] or Model[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Object[Sample], Model[Sample]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

WashingSolutionVolume

The amount of WashingSolution that is flushed through the analyte-bound-sorbent to get rid of non-specific binding and improve extraction purity.

Default Value: Automatic

Default Calculation: Automatically set to 10 times of MaxVolume of ExtractionCartridge or 10 times MaxVolume of WashingSolutionCollectionContainer, which ever is smaller.

Pattern Description: Greater than or equal to 0. milliliters and less than or equal to 20 liters or Null.

Programmatic Pattern: ((Null | RangeP[0.*Milliliter, $MaxTransferVolume]) | Automatic) | Null

Index Matches to: experiment samples

WashingSolutionTemperature

The set temperature that WashingSolution is incubated for WashingSolutionTemperatureEquilibrationTime before being flushed through the sorbent. The final temperature of WashingSolution is assumed to equilibrate with the set WashingSolutionTemperature.

Default Value: Ambient

Pattern Description: Ambient or greater than or equal to -20 degrees Celsius and less than or equal to 500 degrees Celsius or Null.

Programmatic Pattern: (Null | (RangeP[$MinIncubationTemperature, $MaxIncubationTemperature] | Ambient)) | Null

Index Matches to: experiment samples

WashingSolutionTemperatureEquilibrationTime

The amount of time that WashingSolution is incubated to achieve the set WashingSolutionTemperature. The final temperature of WashingSolution is assumed to equilibrate with the the set WashingSolutionTemperature.

Default Value: Automatic

Default Calculation: Automatically set to 3 Minutes, if WashingSolutionTemperature is not Ambient.

Pattern Description: Greater than or equal to 0 minutes and less than or equal to 72 hours or Null.

Programmatic Pattern: ((Null | RangeP[0*Minute, $MaxExperimentTime]) | Automatic) | Null

Index Matches to: experiment samples

CollectWashingSolution

Indicates if the WashingSolution is collected and saved after flushing through the sorbent.

Default Value: Automatic

Pattern Description: True or False or Null.

Programmatic Pattern: ((Null | BooleanP) | Automatic) | Null

Index Matches to: experiment samples

WashingSolutionCollectionContainer

The container that is used to accumulates any flow through solution in Washing step. The collected volume might be less than WashingSolutionVolume because some of WashingSolution left in cartrdige (the solution is not purged through the sorbent).

Default Value: Automatic

Default Calculation: Automatically set to generic container that the instrument can accommodate (point to instrument diagram or make a table).

Pattern Description: An object of type or subtype Model[Container] or Object[Container] or a prepared sample or Null.

Programmatic Pattern: ((Null | (ObjectP[{Model[Container], Object[Container]}] | _String)) | Automatic) | Null

Index Matches to: experiment samples

WashingSolutionDispenseRate

The rate at which the WashingSolution is applied to the sorbent by Instrument during Washing step.

Default Value: Automatic

Default Calculation: Automatically set to 3*Milliliter/Minute.

Pattern Description: Greater than or equal to 0 milliliters per minute and less than or equal to 1180 milliliters per minute or Null.

Programmatic Pattern: ((Null | RangeP[0*(Milliliter/Minute), 1180*(Milliliter/Minute)]) | Automatic) | Null

Index Matches to: experiment samples

WashingSolutionDrainTime

The amount of time to set on the Instrument for WashingSolution to be flushed through the sorbent. If WashingSolutionUntilDrained is set to True, then WashingSolution is continually flushed thorugh the ExtractionCartridge in cycle of WashingSolutionDrainTime until it is drained entirely. If WashingSolutionUntilDrained is set to False, then WashingSolution is flushed through ExtractionCartridge for WashingSolutionDrainTime once.

Default Value: Automatic

Default Calculation: If the Volume and Rate is given then it is calculate by Volume/Rate. Otherwise automatically set to 2 minutes, or the value of MaxWashingSolutionDrainTime, whichever is shorter.

Pattern Description: Greater than or equal to 0 minutes and less than or equal to 72 hours or Null.

Programmatic Pattern: ((Null | RangeP[0*Minute, $MaxExperimentTime]) | Automatic) | Null

Index Matches to: experiment samples

WashingSolutionUntilDrained

Indicates if WashingSolution is continually flushed through the cartridge in cycle of WashingSolutionDrainTime until it is drained entirely, or until MaxWashingSolutionDrainTime has been reached.

Default Value: Automatic

Default Calculation: Automatically set to True if ExtractionMethod are Gravity, Pressure, Vacuum or Centrifuge.

Pattern Description: True or False or Null.

Programmatic Pattern: ((Null | BooleanP) | Automatic) | Null

Index Matches to: experiment samples

MaxWashingSolutionDrainTime

Indicates the maximum amount of time to flush WashingSolution through sorbent. WashingSolution is flushed in cycles of every WashingSolutionDrainTime until MaxWashingSolutionDrainTime has been reached.

Default Value: Automatic

Default Calculation: Automatically set to 3 times of maximum WashingSolutionDrainTime.

Pattern Description: Greater than 0 minutes or Null.

Programmatic Pattern: ((Null | GreaterP[0*Minute]) | Automatic) | Null

Index Matches to: experiment samples

WashingSolutionCentrifugeIntensity

The rotational speed or gravitational force at which the ExtractionCartridge is centrifuged to flush WashingSolution through the sorbent.

Default Value: Automatic

Default Calculation: Automatically set to 50% of Centrifuge's MaxRotationRate or, if ExtractionMethod is Centrifuge.

Pattern Description: Force or Speed or Null.

Programmatic Pattern: ((Null | (RangeP[0*RPM, 10000*RPM] | GreaterP[0*GravitationalAcceleration])) | Automatic) | Null

Index Matches to: experiment samples

WashingSolutionPressure

The target pressure applied to the ExtractionCartridge to flush WashingSolution through the sorbent. If Instrument is Model[Instrument,PressureManifold,"MPE2"], the WashingSolutionPressure is set to be LoadingSamplePressure (Pressure of Model[Instrument,PressureManifold,"MPE2"] cannot be changed while the Experiment is running).

Default Value: Automatic

Default Calculation: Automatically set to 10 PSI. Applies to ExtractionMethod : Pressure.

Pattern Description: Greater than or equal to 0 pounds‐force per inch squared and less than or equal to 100 pounds‐force per inch squared in increments of 1 pound‐force per inch squared or Null.

Programmatic Pattern: ((Null | RangeP[0*PSI, 100*PSI, 1*PSI]) | Automatic) | Null

Index Matches to: experiment samples

SecondaryWashing

SecondaryWashing

Indicates if analyte-bound-sorbent is flushed with SecondaryWashingSolution to get rid non-specific binding and and improve extraction purity.

Default Value: Automatic

Pattern Description: True or False.

Programmatic Pattern: BooleanP | Automatic

Index Matches to: experiment samples

SecondaryWashingSolution

The solution that is flushed through the analyte-bound-sorbent to get rid of non-specific binding and improve extraction purity.

Default Value: Automatic

Default Calculation: Automatically set to be the same as WashingSolution.

Pattern Description: An object of type or subtype Object[Sample] or Model[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Object[Sample], Model[Sample]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

SecondaryWashingSolutionVolume

The amount of SecondaryWashingSolution that is flushed through the analyte-bound-sorbent to get rid of non-specific binding and improve extraction purity.

Default Value: Automatic

Default Calculation: Automatically set to be the same as WashingSolutionVolume.

Pattern Description: Greater than or equal to 0. milliliters and less than or equal to 20 liters or Null.

Programmatic Pattern: ((Null | RangeP[0.*Milliliter, $MaxTransferVolume]) | Automatic) | Null

Index Matches to: experiment samples

SecondaryWashingSolutionTemperature

The set temperature that SecondaryWashingSolution is incubated for SecondaryWashingSolutionTemperatureEquilibrationTime before being flushed through the sorbent. The final temperature of SecondaryWashingSolution is assumed to equilibrate with the set SecondaryWashingSolutionTemperature.

Default Value: Automatic

Default Calculation: Automatically set to be the same as WashingSolutionTemperature.

Pattern Description: Ambient or greater than or equal to -20 degrees Celsius and less than or equal to 500 degrees Celsius or Null.

Programmatic Pattern: ((Null | (RangeP[$MinIncubationTemperature, $MaxIncubationTemperature] | Ambient)) | Automatic) | Null

Index Matches to: experiment samples

SecondaryWashingSolutionTemperatureEquilibrationTime

The amount of time that SecondaryWashingSolution is incubated to achieve the set SecondaryWashingSolutionTemperature. The final temperature of SecondaryWashingSolution is assumed to equilibrate with the the set SecondaryWashingSolutionTemperature.

Default Value: Automatic

Default Calculation: Automatically set to be the same as WashingSolutionTemperatureEquilibrationTime.

Pattern Description: Greater than or equal to 0 minutes and less than or equal to 72 hours or Null.

Programmatic Pattern: ((Null | RangeP[0*Minute, $MaxExperimentTime]) | Automatic) | Null

Index Matches to: experiment samples

CollectSecondaryWashingSolution

Indicates if the SecondaryWashingSolution is collected and saved after flushing through the sorbent.

Default Value: Automatic

Default Calculation: Automatically set to be the same as CollectionWashingSolution.

Pattern Description: True or False or Null.

Programmatic Pattern: ((Null | BooleanP) | Automatic) | Null

Index Matches to: experiment samples

SecondaryWashingSolutionCollectionContainer

The container that is used to accumulates any flow through solution in SecondaryWashing step. The collected volume might be less than SecondaryWashingSolutionVolume because some of SecondaryWashingSolution left in cartrdige (the solution is not purged through the sorbent).

Default Value: Automatic

Default Calculation: Automatically set to be the same as WashingSolutionCollectionContainer

Pattern Description: An object of type or subtype Model[Container] or Object[Container] or a prepared sample or Null.

Programmatic Pattern: ((Null | (ObjectP[{Model[Container], Object[Container]}] | _String)) | Automatic) | Null

Index Matches to: experiment samples

SecondaryWashingSolutionDispenseRate

The rate at which the SecondaryWashingSolution is applied to the sorbent by Instrument during SecondaryWashing step.

Default Value: Automatic

Default Calculation: Automatically set to be the same as WashingSolutionDispenseRate.

Pattern Description: Greater than or equal to 0 milliliters per minute and less than or equal to 1180 milliliters per minute or Null.

Programmatic Pattern: ((Null | RangeP[0*(Milliliter/Minute), 1180*(Milliliter/Minute)]) | Automatic) | Null

Index Matches to: experiment samples

SecondaryWashingSolutionDrainTime

The amount of time to set on the Instrument for SecondaryWashingSolution to be flushed through the sorbent. If SecondaryWashingSolutionUntilDrained is set to True, then SecondaryWashingSolution is continually flushed thorugh the ExtractionCartridge in cycle of SecondaryWashingSolutionDrainTime until it is drained entirely. If SecondaryWashingSolutionUntilDrained is set to False, then SecondaryWashingSolution is flushed through ExtractionCartridge for SecondaryWashingSolutionDrainTime once.

Default Value: Automatic

Default Calculation: Automatically set to be the same as WashingSolutionDrainTime.

Pattern Description: Greater than or equal to 0 minutes and less than or equal to 72 hours or Null.

Programmatic Pattern: ((Null | RangeP[0*Minute, $MaxExperimentTime]) | Automatic) | Null

Index Matches to: experiment samples

SecondaryWashingSolutionUntilDrained

Indicates if SecondaryWashingSolution is continually flushed through the cartridge in cycle of SecondaryWashingSolutionDrainTime until it is drained entirely, or until MaxSecondaryWashingSolutionDrainTime has been reached.

Default Value: Automatic

Default Calculation: Automatically set to be the same as WashingSolutionUntilDrained.

Pattern Description: True or False or Null.

Programmatic Pattern: ((Null | BooleanP) | Automatic) | Null

Index Matches to: experiment samples

MaxSecondaryWashingSolutionDrainTime

Indicates the maximum amount of time to flush SecondaryWashingSolution through sorbent. SecondaryWashingSolution is flushed in cycles of every SecondaryWashingSolutionDrainTime until MaxSecondaryWashingSolutionDrainTime has been reached.

Default Value: Automatic

Default Calculation: Automatically set to be the same as MaxWashingSolutionDrainTime.

Pattern Description: Greater than 0 minutes or Null.

Programmatic Pattern: ((Null | GreaterP[0*Minute]) | Automatic) | Null

Index Matches to: experiment samples

SecondaryWashingSolutionCentrifugeIntensity

The rotational speed or gravitational force at which the ExtractionCartridge is centrifuged to flush SecondaryWashingSolution through the sorbent.

Default Value: Automatic

Default Calculation: Automatically set to be the same as WashingSolutionCentrifugeIntensity.

Pattern Description: Force or Speed or Null.

Programmatic Pattern: ((Null | (RangeP[0*RPM, 10000*RPM] | GreaterP[0*GravitationalAcceleration])) | Automatic) | Null

Index Matches to: experiment samples

SecondaryWashingSolutionPressure

The target pressure applied to the ExtractionCartridge to flush SecondaryWashingSolution through the sorbent. If Instrument is Model[Instrument,PressureManifold,"MPE2"], the SecondaryWashingSolutionPressure is set to be LoadingSamplePressure (Pressure of Model[Instrument,PressureManifold,"MPE2"] cannot be changed while the Experiment is running).

Default Value: Automatic

Default Calculation: Automatically set to be the same as WashingSolutionPressure.

Pattern Description: Greater than or equal to 0 pounds‐force per inch squared and less than or equal to 100 pounds‐force per inch squared in increments of 1 pound‐force per inch squared or Null.

Programmatic Pattern: ((Null | RangeP[0*PSI, 100*PSI, 1*PSI]) | Automatic) | Null

Index Matches to: experiment samples

TertiaryWashing

TertiaryWashing

Indicates if analyte-bound-sorbent is flushed with TertiaryWashingSolution to get rid non-specific binding and and improve extraction purity.

Default Value: Automatic

Pattern Description: True or False.

Programmatic Pattern: BooleanP | Automatic

Index Matches to: experiment samples

TertiaryWashingSolution

The solution that is flushed through the analyte-bound-sorbent to get rid of non-specific binding and improve extraction purity.

Default Value: Automatic

Default Calculation: Automatically set to be the same as WashingSolution.

Pattern Description: An object of type or subtype Object[Sample] or Model[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Object[Sample], Model[Sample]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

TertiaryWashingSolutionVolume

The amount of TertiaryWashingSolution that is flushed through the analyte-bound-sorbent to get rid of non-specific binding and improve extraction purity.

Default Value: Automatic

Default Calculation: Automatically set to be the same as WashingSolutionVolume.

Pattern Description: Greater than or equal to 0. milliliters and less than or equal to 20 liters or Null.

Programmatic Pattern: ((Null | RangeP[0.*Milliliter, $MaxTransferVolume]) | Automatic) | Null

Index Matches to: experiment samples

TertiaryWashingSolutionTemperature

The set temperature that TertiaryWashingSolution is incubated for TertiaryWashingSolutionTemperatureEquilibrationTime before being flushed through the sorbent. The final temperature of TertiaryWashingSolution is assumed to equilibrate with the set TertiaryWashingSolutionTemperature.

Default Value: Automatic

Default Calculation: Automatically set to be the same as WashingSolutionTemperature.

Pattern Description: Ambient or greater than or equal to -20 degrees Celsius and less than or equal to 500 degrees Celsius or Null.

Programmatic Pattern: ((Null | (RangeP[$MinIncubationTemperature, $MaxIncubationTemperature] | Ambient)) | Automatic) | Null

Index Matches to: experiment samples

TertiaryWashingSolutionTemperatureEquilibrationTime

The amount of time that TertiaryWashingSolution is incubated to achieve the set TertiaryWashingSolutionTemperature. The final temperature of TertiaryWashingSolution is assumed to equilibrate with the the set TertiaryWashingSolutionTemperature.

Default Value: Automatic

Default Calculation: Automatically set to be the same as WashingSolutionTemperatureEquilibrationTime.

Pattern Description: Greater than or equal to 0 minutes and less than or equal to 72 hours or Null.

Programmatic Pattern: ((Null | RangeP[0*Minute, $MaxExperimentTime]) | Automatic) | Null

Index Matches to: experiment samples

CollectTertiaryWashingSolution

Indicates if the TertiaryWashingSolution is collected and saved after flushing through the sorbent.

Default Value: Automatic

Default Calculation: Automatically set to be the same as CollectionWashingSolution.

Pattern Description: True or False or Null.

Programmatic Pattern: ((Null | BooleanP) | Automatic) | Null

Index Matches to: experiment samples

TertiaryWashingSolutionCollectionContainer

The container that is used to accumulates any flow through solution in TertiaryWashing step. The collected volume might be less than TertiaryWashingSolutionVolume because some of TertiaryWashingSolution left in cartrdige (the solution is not purged through the sorbent).

Default Value: Automatic

Default Calculation: Automatically set to be the same as WashingSolutionCollectionContainer

Pattern Description: An object of type or subtype Model[Container] or Object[Container] or a prepared sample or Null.

Programmatic Pattern: ((Null | (ObjectP[{Model[Container], Object[Container]}] | _String)) | Automatic) | Null

Index Matches to: experiment samples

TertiaryWashingSolutionDispenseRate

The rate at which the TertiaryWashingSolution is applied to the sorbent by Instrument during TertiaryWashing step.

Default Value: Automatic

Default Calculation: Automatically set to be the same as WashingSolutionDispenseRate.

Pattern Description: Greater than or equal to 0 milliliters per minute and less than or equal to 1180 milliliters per minute or Null.

Programmatic Pattern: ((Null | RangeP[0*(Milliliter/Minute), 1180*(Milliliter/Minute)]) | Automatic) | Null

Index Matches to: experiment samples

TertiaryWashingSolutionDrainTime

The amount of time to set on the Instrument for TertiaryWashingSolution to be flushed through the sorbent. If TertiaryWashingSolutionUntilDrained is set to True, then TertiaryWashingSolution is continually flushed thorugh the ExtractionCartridge in cycle of TertiaryWashingSolutionDrainTime until it is drained entirely. If TertiaryWashingSolutionUntilDrained is set to False, then TertiaryWashingSolution is flushed through ExtractionCartridge for TertiaryWashingSolutionDrainTime once.

Default Value: Automatic

Default Calculation: Automatically set to be the same as WashingSolutionDrainTime.

Pattern Description: Greater than or equal to 0 minutes and less than or equal to 72 hours or Null.

Programmatic Pattern: ((Null | RangeP[0*Minute, $MaxExperimentTime]) | Automatic) | Null

Index Matches to: experiment samples

TertiaryWashingSolutionUntilDrained

Indicates if TertiaryWashingSolution is continually flushed through the cartridge in cycle of TertiaryWashingSolutionDrainTime until it is drained entirely, or until MaxTertiaryWashingSolutionDrainTime has been reached.

Default Value: Automatic

Default Calculation: Automatically set to be the same as WashingSolutionUntilDrained.

Pattern Description: True or False or Null.

Programmatic Pattern: ((Null | BooleanP) | Automatic) | Null

Index Matches to: experiment samples

MaxTertiaryWashingSolutionDrainTime

Indicates the maximum amount of time to flush TertiaryWashingSolution through sorbent. TertiaryWashingSolution is flushed in cycles of every TertiaryWashingSolutionDrainTime until MaxTertiaryWashingSolutionDrainTime has been reached.

Default Value: Automatic

Default Calculation: Automatically set to be the same as MaxWashingSolutionDrainTime.

Pattern Description: Greater than 0 minutes or Null.

Programmatic Pattern: ((Null | GreaterP[0*Minute]) | Automatic) | Null

Index Matches to: experiment samples

TertiaryWashingSolutionCentrifugeIntensity

The rotational speed or gravitational force at which the ExtractionCartridge is centrifuged to flush TertiaryWashingSolution through the sorbent.

Default Value: Automatic

Default Calculation: Automatically set to be the same as WashingSolutionCentrifugeIntensity.

Pattern Description: Force or Speed or Null.

Programmatic Pattern: ((Null | (RangeP[0*RPM, 10000*RPM] | GreaterP[0*GravitationalAcceleration])) | Automatic) | Null

Index Matches to: experiment samples

TertiaryWashingSolutionPressure

The target pressure applied to the ExtractionCartridge to flush TertiaryWashingSolution through the sorbent. If Instrument is Model[Instrument,PressureManifold,"MPE2"], the TertiaryWashingSolutionPressure is set to be LoadingSamplePressure (Pressure of Model[Instrument,PressureManifold,"MPE2"] cannot be changed while the Experiment is running).

Default Value: Automatic

Default Calculation: Automatically set to be the same as WashingSolutionPressure.

Pattern Description: Greater than or equal to 0 pounds‐force per inch squared and less than or equal to 100 pounds‐force per inch squared in increments of 1 pound‐force per inch squared or Null.

Programmatic Pattern: ((Null | RangeP[0*PSI, 100*PSI, 1*PSI]) | Automatic) | Null

Index Matches to: experiment samples

Eluting

Eluting

Indicates if sorbent is flushed with ElutingSolution to release bound analyte from the sorbent.

Default Value: Automatic

Default Calculation: Automatically set to True, if ExtractionStrategy is Positive

Pattern Description: True or False.

Programmatic Pattern: BooleanP | Automatic

Index Matches to: experiment samples

ElutingSolution

The solution that is used to flush and release bound analyte from the sorbent.

Default Value: Automatic

Default Calculation: Automatically set to match with ExtractionSorbent as indicate in Table... .

Pattern Description: An object of type or subtype Object[Sample] or Model[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Object[Sample], Model[Sample]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

ElutingSolutionVolume

The amount of EluteSolution that is flushed through the sorbent to release analyte from the sorbent.

Default Value: Automatic

Default Calculation: Automatically set to 25% of MaxVolume of ExtractionCartridge.

Pattern Description: Greater than or equal to 0. milliliters and less than or equal to 20 liters or Null.

Programmatic Pattern: ((Null | RangeP[0.*Milliliter, $MaxTransferVolume]) | Automatic) | Null

Index Matches to: experiment samples

ElutingSolutionTemperature

The set temperature that ElutingSolution is incubated for ElutingSolutionTemperatureEquilibrationTime before being loaded into the sorbent.

Default Value: Ambient

Pattern Description: Ambient or greater than or equal to -20 degrees Celsius and less than or equal to 500 degrees Celsius or Null.

Programmatic Pattern: (Null | (RangeP[$MinIncubationTemperature, $MaxIncubationTemperature] | Ambient)) | Null

Index Matches to: experiment samples

ElutingSolutionTemperatureEquilibrationTime

The amount of time that ElutingSolution is incubated to achieve the set ElutingSolutionTemperature. The final temperature of ElutingSolution is assumed to equilibrate with the the set ElutingSolutionTemperature.

Default Value: Automatic

Default Calculation: Automatically set to 3 Minutes, if ElutingSolutionTemperature is not Ambient.

Pattern Description: Greater than or equal to 0 minutes and less than or equal to 72 hours or Null.

Programmatic Pattern: ((Null | RangeP[0*Minute, $MaxExperimentTime]) | Automatic) | Null

Index Matches to: experiment samples

CollectElutingSolution

Indicates if the ElutingSolution is collected and saved after flushing through the sorbent.

Default Value: Automatic

Default Calculation: Automatically set to True, if ExtractionStrategy is Positive.

Pattern Description: True or False or Null.

Programmatic Pattern: ((Null | BooleanP) | Automatic) | Null

Index Matches to: experiment samples

ElutingSolutionCollectionContainer

The container that is used to accumulates any flow through solution in Eluting step. The collected volume might be less than ElutingSolutionVolume because some of ElutingSolution left in cartrdige (the solution is not purged through the sorbent).

Default Value: Automatic

Default Calculation: Automatically set to generic container that the instrument can accommodate (point to instrument diagram or make a table).

Pattern Description: An object of type or subtype Model[Container] or Object[Container] or a prepared sample or Null.

Programmatic Pattern: ((Null | (ObjectP[{Model[Container], Object[Container]}] | _String)) | Automatic) | Null

Index Matches to: experiment samples

ElutingSolutionDispenseRate

The rate at which the ElutingSolution is applied to the sorbent by Instrument during Eluting step.

Default Value: Automatic

Default Calculation: Automatically set to 3*Milliliter/Minute.

Pattern Description: Greater than or equal to 0 milliliters per minute and less than or equal to 1180 milliliters per minute or Null.

Programmatic Pattern: ((Null | RangeP[0*(Milliliter/Minute), 1180*(Milliliter/Minute)]) | Automatic) | Null

Index Matches to: experiment samples

ElutingSolutionDrainTime

The amount of time to set on the Instrument for ElutingSolution to be flushed through the sorbent. If ElutingSolutionUntilDrained is set to True, then ElutingSolution is continually flushed thorugh the ExtractionCartridge in cycle of ElutingSolutionDrainTime until it is drained entirely. If ElutingSolutionUntilDrained is set to False, then ElutingSolution is flushed through ExtractionCartridge for ElutingSolutionDrainTime once.

Default Value: Automatic

Default Calculation: If the Volume and Rate is given then it is calculate by Volume/Rate. Otherwise automatically set to 2 minutes, or the value of MaxElutingSolutionDrainTime, whichever is shorter.

Pattern Description: Greater than or equal to 0 minutes and less than or equal to 72 hours or Null.

Programmatic Pattern: ((Null | RangeP[0*Minute, $MaxExperimentTime]) | Automatic) | Null

Index Matches to: experiment samples

ElutingSolutionUntilDrained

Indicates if ElutingSolution is continually flushed through the cartridge in cycle of ElutingSolutionDrainTime until it is drained entirely, or until MaxElutingSolutionDrainTime has been reached.

Default Value: Automatic

Default Calculation: Automatically set to True if ExtractionMethod are Gravity, Pressure, Vacuum or Centrifuge.

Pattern Description: True or False or Null.

Programmatic Pattern: ((Null | BooleanP) | Automatic) | Null

Index Matches to: experiment samples

MaxElutingSolutionDrainTime

Indicates the maximum amount of time to flush ElutingSolution through sorbent. ElutingSolution is flushed in cycles of every ElutingSolutionDrainTime until MaxElutingSolutionDrainTime has been reached.

Default Value: Automatic

Default Calculation: Automatically set to 3 times of maximum ElutingSolutionDrainTime.

Pattern Description: Greater than 0 minutes or Null.

Programmatic Pattern: ((Null | GreaterP[0*Minute]) | Automatic) | Null

Index Matches to: experiment samples

ElutingSolutionCentrifugeIntensity

The rotational speed or gravitational force at which the ExtractionCartridge is centrifuged to flush ElutingSolution through the sorbent.

Default Value: Automatic

Default Calculation: Automatically set to 50% of Centrifuge's MaxRotationRate or, if ExtractionMethod is Centrifuge.

Pattern Description: Force or Speed or Null.

Programmatic Pattern: ((Null | (RangeP[0*RPM, 10000*RPM] | GreaterP[0*GravitationalAcceleration])) | Automatic) | Null

Index Matches to: experiment samples

ElutingSolutionPressure

The target pressure applied to the ExtractionCartridge to flush ElutingSolution through the sorbent. If Instrument is Model[Instrument,PressureManifold,"MPE2"], the ElutingSolutionPressure is set to be LoadingSamplePressure (Pressure of Model[Instrument,PressureManifold,"MPE2"] cannot be changed while the Experiment is running).

Default Value: Automatic

Default Calculation: Automatically set to 10 PSI. Applies to ExtractionMethod : Pressure.

Pattern Description: Greater than or equal to 0 pounds‐force per inch squared and less than or equal to 100 pounds‐force per inch squared in increments of 1 pound‐force per inch squared or Null.

Programmatic Pattern: ((Null | RangeP[0*PSI, 100*PSI, 1*PSI]) | Automatic) | Null

Index Matches to: experiment samples

Post Experiment

SamplesInStorageCondition

The non-default conditions under which the SamplesIn of this experiment should be stored after the protocol is completed. If left unset, SamplesIn will be stored according to their current StorageCondition.

Default Value: Null

Pattern Description: {AmbientStorage, Refrigerator, Freezer, DeepFreezer, CryogenicStorage, YeastIncubation, YeastShakingIncubation, BacterialIncubation, BacterialShakingIncubation, MammalianIncubation, ViralIncubation, CrystalIncubation, AcceleratedTesting, IntermediateTesting, LongTermTesting, UVVisLightTesting} or Disposal or Null.

Programmatic Pattern: (Alternatives[SampleStorageTypeP | Disposal]) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

SamplesOutStorageCondition

The non-default conditions under which any new samples generated by this experiment should be stored after the protocol is completed. If left unset, the new samples will be stored according to their Models' DefaultStorageCondition.

Default Value: Null

Pattern Description: {AmbientStorage, Refrigerator, Freezer, DeepFreezer, CryogenicStorage, YeastIncubation, YeastShakingIncubation, BacterialIncubation, BacterialShakingIncubation, MammalianIncubation, ViralIncubation, CrystalIncubation, AcceleratedTesting, IntermediateTesting, LongTermTesting, UVVisLightTesting} or Disposal or Null.

Programmatic Pattern: (Alternatives[SampleStorageTypeP | Disposal]) | Null

Index Matches to: experiment samples



Sample Prep Options

Sample Preparation

PreparatoryUnitOperations

Specifies a sequence of transferring, aliquoting, consolidating, or mixing of new or existing samples before the main experiment. These prepared samples can be used in the main experiment by referencing their defined name. For more information, please reference the documentation for ExperimentSampleManipulation.

Default Value: Null

Pattern Description: List of one or more unit Operation ManualSamplePreparation or RoboticSamplePreparation or unit Operation must match SamplePreparationP entries or Null.

Programmatic Pattern: {((ManualSamplePreparationMethodP | RoboticSamplePreparationMethodP) | SamplePreparationP)..} | Null

PreparatoryPrimitives

Specifies a sequence of transferring, aliquoting, consolidating, or mixing of new or existing samples before the main experiment. These prepared samples can be used in the main experiment by referencing their defined name. For more information, please reference the documentation for ExperimentSampleManipulation.

Default Value: Null

Pattern Description: List of one or more a primitive with head Define, Transfer, Mix, Aliquot, Consolidation, FillToVolume, Incubate, Filter, Wait, Centrifuge, or Resuspend entries or Null.

Programmatic Pattern: {SampleManipulationP..} | Null

Preparatory Incubation

Incubate

Indicates if the SamplesIn should be incubated at a fixed temperature prior to starting the experiment or any aliquoting. Sample Preparation occurs in the order of Incubation, Centrifugation, Filtration, and then Aliquoting (if specified).

Default Value: Automatic

Default Calculation: Resolves to True if any of the corresponding Incubation options are set. Otherwise, resolves to False.

Pattern Description: True or False.

Programmatic Pattern: BooleanP | Automatic

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

IncubationTemperature

Temperature at which the SamplesIn should be incubated for the duration of the IncubationTime prior to starting the experiment.

Default Value: Automatic

Pattern Description: Ambient or greater than or equal to -20 degrees Celsius and less than or equal to 500 degrees Celsius or Null.

Programmatic Pattern: ((Ambient | RangeP[$MinIncubationTemperature, $MaxIncubationTemperature]) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

IncubationTime

Duration for which SamplesIn should be incubated at the IncubationTemperature, prior to starting the experiment.

Default Value: Automatic

Pattern Description: Greater than or equal to 1 minute and less than or equal to 72 hours or Null.

Programmatic Pattern: (RangeP[1*Minute, $MaxExperimentTime] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

Mix

Indicates if this sample should be mixed while incubated, prior to starting the experiment.

Default Value: Automatic

Default Calculation: Automatically resolves to True if any Mix related options are set. Otherwise, resolves to False.

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

MixType

Indicates the style of motion used to mix the sample, prior to starting the experiment.

Default Value: Automatic

Default Calculation: Automatically resolves based on the container of the sample and the Mix option.

Pattern Description: Roll, Vortex, Sonicate, Pipette, Invert, Stir, Shake, Homogenize, Swirl, Disrupt, or Nutate or Null.

Programmatic Pattern: (MixTypeP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

MixUntilDissolved

Indicates if the mix should be continued up to the MaxIncubationTime or MaxNumberOfMixes (chosen according to the mix Type), in an attempt dissolve any solute. Any mixing/incubation will occur prior to starting the experiment.

Default Value: Automatic

Default Calculation: Automatically resolves to True if MaxIncubationTime or MaxNumberOfMixes is set.

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

MaxIncubationTime

Maximum duration of time for which the samples will be mixed while incubated in an attempt to dissolve any solute, if the MixUntilDissolved option is chosen. This occurs prior to starting the experiment.

Default Value: Automatic

Default Calculation: Automatically resolves based on MixType, MixUntilDissolved, and the container of the given sample.

Pattern Description: Greater than or equal to 1 minute and less than or equal to 72 hours or Null.

Programmatic Pattern: (RangeP[1*Minute, $MaxExperimentTime] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

IncubationInstrument

The instrument used to perform the Mix and/or Incubation, prior to starting the experiment.

Default Value: Automatic

Default Calculation: Automatically resolves based on the options Mix, Temperature, MixType and container of the sample.

Pattern Description: An object of type or subtype Model[Instrument, Roller], Model[Instrument, OverheadStirrer], Model[Instrument, Vortex], Model[Instrument, Shaker], Model[Instrument, BottleRoller], Model[Instrument, Roller], Model[Instrument, Sonicator], Model[Instrument, HeatBlock], Model[Instrument, Homogenizer], Model[Instrument, Disruptor], Model[Instrument, Nutator], Model[Instrument, Thermocycler], Model[Instrument, EnvironmentalChamber], Model[Instrument, Pipette], Object[Instrument, Roller], Object[Instrument, OverheadStirrer], Object[Instrument, Vortex], Object[Instrument, Shaker], Object[Instrument, BottleRoller], Object[Instrument, Roller], Object[Instrument, Sonicator], Object[Instrument, HeatBlock], Object[Instrument, Homogenizer], Object[Instrument, Disruptor], Object[Instrument, Nutator], Object[Instrument, Thermocycler], Object[Instrument, EnvironmentalChamber], or Object[Instrument, Pipette] or Null.

Programmatic Pattern: (ObjectP[Join[MixInstrumentModels, MixInstrumentObjects]] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

AnnealingTime

Minimum duration for which the SamplesIn should remain in the incubator allowing the system to settle to room temperature after the IncubationTime has passed but prior to starting the experiment.

Default Value: Automatic

Pattern Description: Greater than or equal to 0 minutes and less than or equal to 72 hours or Null.

Programmatic Pattern: (RangeP[0*Minute, $MaxExperimentTime] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

IncubateAliquotContainer

The desired type of container that should be used to prepare and house the incubation samples which should be used in lieu of the SamplesIn for the experiment.

Default Value: Automatic

Pattern Description: An object of type or subtype Model[Container] or {Index, Container} or Null.

Programmatic Pattern: ((ObjectP[Model[Container]] | {GreaterEqualP[1, 1] | (Automatic | Null), (ObjectP[{Model[Container], Object[Container]}] | _String) | Automatic}) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

IncubateAliquotDestinationWell

The desired position in the corresponding AliquotContainer in which the aliquot samples will be placed.

Default Value: Automatic

Default Calculation: Automatically resolves to A1 in containers with only one position. For plates, fills wells in the order provided by the function AllWells.

Pattern Description: Any well from A1 to H12 or Null.

Programmatic Pattern: (WellPositionP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

IncubateAliquot

The amount of each sample that should be transferred from the SamplesIn into the IncubateAliquotContainer when performing an aliquot before incubation.

Default Value: Automatic

Default Calculation: Automatically set as the smaller between the current sample volume and the maximum volume of the destination container.

Pattern Description: All or greater than or equal to 1 microliter and less than or equal to 20 liters or Null.

Programmatic Pattern: ((RangeP[1*Microliter, 20*Liter] | All) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

Preparatory Centrifugation

Centrifuge

Indicates if the SamplesIn should be centrifuged prior to starting the experiment or any aliquoting. Sample Preparation occurs in the order of Incubation, Centrifugation, Filtration, and then Aliquoting (if specified).

Default Value: Automatic

Default Calculation: Resolves to True if any of the corresponding Centrifuge options are set. Otherwise, resolves to False.

Pattern Description: True or False.

Programmatic Pattern: BooleanP | Automatic

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

CentrifugeInstrument

The centrifuge that will be used to spin the provided samples prior to starting the experiment.

Default Value: Automatic

Pattern Description: An object of type or subtype Model[Instrument, Centrifuge] or Object[Instrument, Centrifuge] or Null.

Programmatic Pattern: (ObjectP[{Model[Instrument, Centrifuge], Object[Instrument, Centrifuge]}] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

CentrifugeIntensity

The rotational speed or the force that will be applied to the samples by centrifugation prior to starting the experiment.

Default Value: Automatic

Pattern Description: Greater than 0 revolutions per minute or greater than 0 standard accelerations due to gravity on the surface of the earth or Null.

Programmatic Pattern: ((GreaterP[0*RPM] | GreaterP[0*GravitationalAcceleration]) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

CentrifugeTime

The amount of time for which the SamplesIn should be centrifuged prior to starting the experiment.

Default Value: Automatic

Pattern Description: Greater than 0 minutes or Null.

Programmatic Pattern: (GreaterP[0*Minute] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

CentrifugeTemperature

The temperature at which the centrifuge chamber should be held while the samples are being centrifuged prior to starting the experiment.

Default Value: Automatic

Pattern Description: Ambient or greater than or equal to -10 degrees Celsius and less than or equal to 40 degrees Celsius or Null.

Programmatic Pattern: ((Ambient | RangeP[-10*Celsius, 40*Celsius]) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

CentrifugeAliquotDestinationWell

The desired position in the corresponding AliquotContainer in which the aliquot samples will be placed.

Default Value: Automatic

Default Calculation: Automatically resolves to A1 in containers with only one position. For plates, fills wells in the order provided by the function AllWells.

Pattern Description: Any well from A1 to H12 or Null.

Programmatic Pattern: (WellPositionP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

CentrifugeAliquotContainer

The desired type of container that should be used to prepare and house the centrifuge samples which should be used in lieu of the SamplesIn for the experiment.

Default Value: Automatic

Pattern Description: An object of type or subtype Model[Container] or {Index, Container} or Null.

Programmatic Pattern: ((ObjectP[Model[Container]] | {GreaterEqualP[1, 1] | (Automatic | Null), (ObjectP[{Model[Container], Object[Container]}] | _String) | Automatic}) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

CentrifugeAliquot

The amount of each sample that should be transferred from the SamplesIn into the CentrifugeAliquotContainer when performing an aliquot before centrifugation.

Default Value: Automatic

Default Calculation: Automatically set as the smaller between the current sample volume and the maximum volume of the destination container.

Pattern Description: All or greater than or equal to 1 microliter and less than or equal to 20 liters or Null.

Programmatic Pattern: ((RangeP[1*Microliter, 20*Liter] | All) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

Preparatory Filtering

Filtration

Indicates if the SamplesIn should be filter prior to starting the experiment or any aliquoting. Sample Preparation occurs in the order of Incubation, Centrifugation, Filtration, and then Aliquoting (if specified).

Default Value: Automatic

Default Calculation: Resolves to True if any of the corresponding Filter options are set. Otherwise, resolves to False.

Pattern Description: True or False.

Programmatic Pattern: BooleanP | Automatic

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

FiltrationType

The type of filtration method that should be used to perform the filtration.

Default Value: Automatic

Default Calculation: Will automatically resolve to a filtration type appropriate for the volume of sample being filtered.

Pattern Description: PeristalticPump, Centrifuge, Vacuum, Syringe, or AirPressure or Null.

Programmatic Pattern: (FiltrationTypeP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

FilterInstrument

The instrument that should be used to perform the filtration.

Default Value: Automatic

Default Calculation: Will automatically resolved to an instrument appropriate for the filtration type.

Pattern Description: An object of type or subtype Model[Instrument, FilterBlock], Object[Instrument, FilterBlock], Model[Instrument, PeristalticPump], Object[Instrument, PeristalticPump], Model[Instrument, VacuumPump], Object[Instrument, VacuumPump], Model[Instrument, Centrifuge], Object[Instrument, Centrifuge], Model[Instrument, SyringePump], or Object[Instrument, SyringePump] or Null.

Programmatic Pattern: (ObjectP[{Model[Instrument, FilterBlock], Object[Instrument, FilterBlock], Model[Instrument, PeristalticPump], Object[Instrument, PeristalticPump], Model[Instrument, VacuumPump], Object[Instrument, VacuumPump], Model[Instrument, Centrifuge], Object[Instrument, Centrifuge], Model[Instrument, SyringePump], Object[Instrument, SyringePump]}] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

Filter

The filter that should be used to remove impurities from the SamplesIn prior to starting the experiment.

Default Value: Automatic

Default Calculation: Will automatically resolve to a filter appropriate for the filtration type and instrument.

Pattern Description: An object of type or subtype Model[Container, Plate, Filter], Model[Container, Vessel, Filter], or Model[Item, Filter] or Null.

Programmatic Pattern: (ObjectP[{Model[Container, Plate, Filter], Model[Container, Vessel, Filter], Model[Item, Filter]}] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

FilterMaterial

The membrane material of the filter that should be used to remove impurities from the SamplesIn prior to starting the experiment.

Default Value: Automatic

Default Calculation: Resolves to an appropriate filter material for the given sample is Filtration is set to True.

Pattern Description: Cellulose, Cotton, Polyethylene, PTFE, Nylon, PES, PLUS, PVDF, GlassFiber, GHP, UHMWPE, EPDM, DuraporePVDF, GxF, ZebaDesaltingResin, NickelResin, Silica, or HLB or Null.

Programmatic Pattern: (FilterMembraneMaterialP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PrefilterMaterial

The material from which the prefilter filtration membrane should be made of to remove impurities from the SamplesIn prior to starting the experiment.

Default Value: Automatic

Default Calculation: By default, no prefiltration is performed on samples, even when Filter->True.

Pattern Description: Cellulose, Cotton, Polyethylene, PTFE, Nylon, PES, PLUS, PVDF, GlassFiber, GHP, UHMWPE, EPDM, DuraporePVDF, GxF, ZebaDesaltingResin, NickelResin, Silica, or HLB or Null.

Programmatic Pattern: (FilterMembraneMaterialP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

FilterPoreSize

The pore size of the filter that should be used when removing impurities from the SamplesIn prior to starting the experiment.

Default Value: Automatic

Default Calculation: Resolves to an appropriate filter pore size for the given sample is Filtration is set to True.

Pattern Description: 0.008 micrometers, 0.1 micrometers, 0.2 micrometers, 0.22 micrometers, 0.45 micrometers, 1. micrometer, 1.1 micrometers, 2.5 micrometers, 6. micrometers, 20. micrometers, 30. micrometers, or 100. micrometers or Null.

Programmatic Pattern: (FilterSizeP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PrefilterPoreSize

The pore size of the filter; all particles larger than this should be removed during the filtration.

Default Value: Automatic

Default Calculation: By default, no prefiltration is performed on samples, even when Filter->True.

Pattern Description: 0.008 micrometers, 0.1 micrometers, 0.2 micrometers, 0.22 micrometers, 0.45 micrometers, 1. micrometer, 1.1 micrometers, 2.5 micrometers, 6. micrometers, 20. micrometers, 30. micrometers, or 100. micrometers or Null.

Programmatic Pattern: (FilterSizeP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

FilterSyringe

The syringe used to force that sample through a filter.

Default Value: Automatic

Default Calculation: Resolves to an syringe appropriate to the volume of sample being filtered, if Filtration is set to True.

Pattern Description: An object of type or subtype Model[Container, Syringe] or Object[Container, Syringe] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Container, Syringe], Object[Container, Syringe]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

FilterHousing

The filter housing that should be used to hold the filter membrane when filtration is performed using a standalone filter membrane.

Default Value: Automatic

Default Calculation: Resolve to an housing capable of holding the size of the membrane being used, if filter with Membrane FilterType is being used and Filtration is set to True.

Pattern Description: An object of type or subtype Model[Instrument, FilterHousing], Object[Instrument, FilterHousing], Model[Instrument, FilterBlock], or Object[Instrument, FilterBlock] or Null.

Programmatic Pattern: (ObjectP[{Model[Instrument, FilterHousing], Object[Instrument, FilterHousing], Model[Instrument, FilterBlock], Object[Instrument, FilterBlock]}] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

FilterIntensity

The rotational speed or force at which the samples will be centrifuged during filtration.

Default Value: Automatic

Default Calculation: Will automatically resolve to 2000 GravitationalAcceleration if FiltrationType is Centrifuge and Filtration is True.

Pattern Description: Greater than 0 revolutions per minute or greater than 0 standard accelerations due to gravity on the surface of the earth or Null.

Programmatic Pattern: ((GreaterP[0*RPM] | GreaterP[0*GravitationalAcceleration]) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

FilterTime

The amount of time for which the samples will be centrifuged during filtration.

Default Value: Automatic

Default Calculation: Will automatically resolve to 5 Minute if FiltrationType is Centrifuge and Filtration is True.

Pattern Description: Greater than 0 minutes or Null.

Programmatic Pattern: (GreaterP[0*Minute] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

FilterTemperature

The temperature at which the centrifuge chamber will be held while the samples are being centrifuged during filtration.

Default Value: Automatic

Default Calculation: Will automatically resolve to 22 Celsius if FiltrationType is Centrifuge and Filtration is True.

Pattern Description: Greater than or equal to 4 degrees Celsius or Null.

Programmatic Pattern: ((Alternatives[GreaterEqualP[4*Celsius]]) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

FilterContainerOut

The desired container filtered samples should be produced in or transferred into by the end of filtration, with indices indicating grouping of samples in the same plates, if desired.

Default Value: Automatic

Default Calculation: Automatically set as the PreferredContainer for the Volume of the sample. For plates, attempts to fill all wells of a single plate with the same model before using another one.

Pattern Description: An object of type or subtype Model[Container] or Object[Container] or a prepared sample or {Index, Container} or Null.

Programmatic Pattern: (((ObjectP[{Model[Container], Object[Container]}] | _String) | {GreaterEqualP[1, 1] | Automatic, (ObjectP[{Model[Container], Object[Container]}] | _String) | Automatic}) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

FilterAliquotDestinationWell

The desired position in the corresponding AliquotContainer in which the aliquot samples will be placed.

Default Value: Automatic

Default Calculation: Automatically resolves to A1 in containers with only one position. For plates, fills wells in the order provided by the function AllWells.

Pattern Description: Any well from A1 to H12 or Null.

Programmatic Pattern: (WellPositionP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

FilterAliquotContainer

The desired type of container that should be used to prepare and house the filter samples which should be used in lieu of the SamplesIn for the experiment.

Default Value: Automatic

Pattern Description: An object of type or subtype Model[Container] or {Index, Container} or Null.

Programmatic Pattern: ((ObjectP[Model[Container]] | {GreaterEqualP[1, 1] | (Automatic | Null), (ObjectP[{Model[Container], Object[Container]}] | _String) | Automatic}) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

FilterAliquot

The amount of each sample that should be transferred from the SamplesIn into the FilterAliquotContainer when performing an aliquot before filtration.

Default Value: Automatic

Default Calculation: Automatically set as the smaller between the current sample volume and the maximum volume of the destination container.

Pattern Description: All or greater than or equal to 1 microliter and less than or equal to 20 liters or Null.

Programmatic Pattern: ((RangeP[1*Microliter, 20*Liter] | All) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

FilterSterile

Indicates if the filtration of the samples should be done in a sterile environment.

Default Value: Automatic

Default Calculation: Resolve to False if Filtration is indicated. If sterile filtration is desired, this option must manually be set to True.

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples



Protocol Options

Organizational Information

Template

A template protocol whose methodology should be reproduced in running this experiment. Option values will be inherited from the template protocol, but can be individually overridden by directly specifying values for those options to this Experiment function.

Default Value: Null

Pattern Description: An object of type or subtype Object[Protocol] or an object of type or subtype of Object[Protocol] with UnresolvedOptions, ResolvedOptions specified or Null.

Programmatic Pattern: (ObjectP[Object[Protocol]] | FieldReferenceP[Object[Protocol], {UnresolvedOptions, ResolvedOptions}]) | Null

Name

A object name which should be used to refer to the output object in lieu of an automatically generated ID number.

Default Value: Null

Pattern Description: A string or Null.

Programmatic Pattern: _String | Null

Post Experiment

MeasureWeight

Indicates if any solid samples that are modified in the course of the experiment should have their weights measured and updated after running the experiment. Please note that public samples are weighed regardless of the value of this option.

Default Value: Automatic

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

MeasureVolume

Indicates if any liquid samples that are modified in the course of the experiment should have their volumes measured and updated after running the experiment. Please note that public samples are volume measured regardless of the value of this option.

Default Value: Automatic

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

ImageSample

Indicates if any samples that are modified in the course of the experiment should be freshly imaged after running the experiment. Please note that public samples are imaged regardless of the value of this option.

Default Value: Automatic

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null



Example Calls

SolidPhaseExtraction of samples

SolidPhaseExtraction of a single sample:

ExperimentSolidPhaseExtraction[mySample]

SolidPhaseExtraction of multiple single samples in one protocol:

ExperimentSolidPhaseExtraction[{mySample1, mySample2, mySample3}]

SolidPhaseExtraction of samples that are pooled to be extracted together:

ExperimentSolidPhaseExtraction[

 	{{myPooledSample1, myPooledSample2}, mySample1, mySample2}

 ]

Solutions

To wash the ExtractionSorbent of any residues prior to start of the protocol, use PreFlushingSolution, PreFlushingSolutionVolume, PreFlushingSolutionDispenseRate, PreFlushingSolutionPressure or PreFlushingSolutionCentrifugeIntensity to specify the solution reagent, volume to be loaded, loading rate, and the applied pressure or centrifuge intensity that are going to be used in this step:

ExperimentSolidPhaseExtraction[

 	{{myPooledSample1, myPooledSample2}, mySample1, mySample2},

 	PreFlushingSolution ->

  Model[Sample, StockSolution, "90% methanol"],

 	PreFlushingSolutionVolume -> {10 * Milliliter, 12 * Milliliter,

   15 * Milliliter},

 	PreFlushingSolutionDispenseRate -> (5 * Milliliter / Minute)

 ]

To wet and condition the sorbent in the cartridge prior to sample loading, use ConditioningSolution, ConditioningSolutionVolume, ConditioningSolutionDispenseRate, ConditioningSolutionPressure or ConditioningSolutionCentrifugeIntensity to specify the solution reagent, volume to be loaded, loading rate, and the applied pressure or centrifuge intensity that are going to be used in this step:

ExperimentSolidPhaseExtraction[

 	{{myPooledSample1, myPooledSample2}, mySample1, mySample2},

 	ConditioningSolution ->

  Model[Sample, StockSolution, "15 mM ammonium acetate"],

 	ConditioningSolutionVolume -> (17 * Milliliter),

 	ConditioningSolutionDispenseRate -> {

   		3 * Milliliter / Minute,

   		2 * Milliliter / Minute,

   		2.5 * Milliliter / Minute

   	}

 ]

To wash any impurities of the cartridge prior to analyte elution, useWashingSolution, WashingSolutionVolume, WashingSolutionDispenseRate, WashingSolutionPressure or WashingSolutionCentrifugeIntensity to specify the solution reagent, volume to be loaded, loading rate, and the applied pressure or centrifuge intensity that are going to be used in this step:

ExperimentSolidPhaseExtraction[

 	{{myPooledSample1, myPooledSample2}, mySample1, mySample2},

 	WashingSolution -> Model[Sample, "Milli-Q water"],

 	WashingSolutionVolume -> (30 * Milliliter),

 	WashingSolutionDispenseRate -> (10 * Milliliter / Minute)

 ]

To add extra wash steps to increase the purity of analyte before elution, use SecondaryWashingSolution, SecondaryWashingSolutionVolume, SecondaryWashingSolutionDispenseRate, SecondaryWashingSolutionPressure, SecondaryWashingSolutionCentrifugeIntensity, TertiaryWashingSolution, TertiaryWashingSolutionVolume, TertiaryWashingSolutionDispenseRate, TertiaryWashingSolutionPressure or TertiaryWashingSolutionCentrifugeIntensity to specify the solution reagent, volume to be loaded, loading rate, and the applied pressure or centrifuge intensity that are going to be used in these 2 steps:

ExperimentSolidPhaseExtraction[

 	{{myPooledSample1, myPooledSample2}, mySample1, mySample2},

 	WashingSolution -> Model[Sample, "Milli-Q water"],

 	WashingSolutionVolume -> (30 * Milliliter),

 	WashingSolutionDispenseRate -> (10 * Milliliter / Minute),

 	SecondaryWashingSolution ->

  Model[Sample, StockSolution, "90% methanol"],

 	SecondaryWashingSolutionVolume -> (10 * Milliliter),

 	SecondaryWashingSolutionDispenseRate -> (10 * Milliliter / Minute),

 	WashingSolution ->

  Model[Sample, StockSolution, "15 mM ammonium acetate"],

 	WashingSolutionVolume -> (20 * Milliliter),

 	WashingSolutionDispenseRate -> (10 * Milliliter / Minute)

 ]

To disrupt the interaction between the sample and the sorbent and elute it into the collection container, use ElutingSolution, ElutingSolutionVolume, ElutingSolutionDispenseRate, ElutingSolutionPressure or ElutingSolutionCentrifugeIntensity to specify the solution reagent, volume to be loaded, loading rate, and the applied pressure or centrifuge intensity that are going to be used in this step:

ExperimentSolidPhaseExtraction[

 	{{myPooledSample1, myPooledSample2}, mySample1, mySample2},

 	ElutingSolution -> Model[Sample, StockSolution, "90% methanol"],

 	ElutingSolutionVolume -> (1 * Milliliter),

 	ElutingSolutionDispenseRate -> (5 * Milliliter)

 ]

SolidPhaseExtraction ExtractionMode, ExtractionSorbent and ExtractionCartridge

ExtractionMode option allows specification of the mode of extraction to be performed for each sample pool:

ExperimentSolidPhaseExtraction[

 	{{myPooledSample1, myPooledSample2}, mySample1, mySample2},

 	ExtractionMode -> {NormalPhase, ReversePhase, IonExchange}

 ]

ExtractionSorbent option allows specification of the type of chemical sorbent in the sorbent-packed container that forms the stationary phase of the extraction for each sample pool:

ExperimentSolidPhaseExtraction[

 	{{myPooledSample1, myPooledSample2}, mySample1, mySample2},

 	ExtractionSorbent -> {Silica, C18, C8}

 ]

ExtractionCartridge option allows specification of the model or option of sorbent-packed container that forms the stationary phase of the extraction for each sample pool:

ExperimentSolidPhaseExtraction[

 	{{myPooledSample1, myPooledSample2}, mySample1, mySample2},

 	ExtractionCartridge -> {

   		Model[Container,

    			ExtractionCartridge, "500mg, 3cc, C18, Vac extraction cartridge"

    		],

   		Model[Container,

    			ExtractionCartridge, "150mg, 3cc, Oasis PRiME HLB vac cartridge"

    		],

   		Model[Container,

    			ExtractionCartridge,

    "Accell Plus QMA, 500 mg, 3 ml, Vac extraction cartridge"

    		]

   	}

 ]

SolidPhaseExtraction Instrument and ExtractionMethod

Instrument option allows specification of the Instrument that will run for each sample pool:

ExperimentSolidPhaseExtraction[

 	{{myPooledSample1, myPooledSample2}, mySample1, mySample2},

 	Instrument -> {

   		Model[Instrument, LiquidHandler, "id:o1k9jAKOwLl8"],

   		Model[Instrument, PressureManifold, "id:zGj91a7mElrL"],

   		Model[Instrument, Centrifuge, "id:eGakldJEz14E"]

   	}

 ]

ExtractionMethod option allows specification of the type of force to push reagent through the sorbent-packed ExtractionCartridge for each sample pool:

ExperimentSolidPhaseExtraction[

 	{{myPooledSample1, myPooledSample2}, mySample1, mySample2},

 	ExtractionMethod -> {

   		Model[Instrument, LiquidHandler, "id:o1k9jAKOwLl8"],

   		Model[Instrument, PressureManifold, "id:zGj91a7mElrL"],

   		Model[Instrument, Centrifuge, "id:eGakldJEz14E"]

   	}

 ]

SolidPhaseExtraction Temperature

ExtractionTemperature option allows specification of the environmental temperature to perform SolidPhaseExtraction (automatically set the instrument to Model[Instrument, Centrifuge, "id:eGakldJEz14E"]) for each sample pool:

ExperimentSolidPhaseExtraction[

 	{{myPooledSample1, myPooledSample2}, mySample1, mySample2},

 	Instrument -> Model[Instrument, Centrifuge, "id:eGakldJEz14E"],

 	ExtractionTemperature -> {5 * Celsius, 15 * Celsius, Ambient}

 ]

All mobile-phase SolutionTemperature options allow specification of the temperature of reagents before they are applied to the sorbent-packed ExtractionCartridge. This option can be specified for each sample pool (only applies to Model[Instrument, PressureManifold, "id:zGj91a7mElrL"]):

ExperimentSolidPhaseExtraction[

 	{{myPooledSample1, myPooledSample2}, mySample1, mySample2},

 	LoadingSampleTemperature -> Ambient,

 	ElutingSolutionSolutionTemperature -> {40 * Celsius, Ambient,

   4 * Celsius}

 ]

Sample Loading

LoadingSampleDispenseRate option allows specification of the rate at which each sample will be loaded into the extraction cartridge. This can be different for samples in the same pool:

ExperimentSolidPhaseExtraction[

 	{{myPooledSample1, myPooledSample2}, mySample1, mySample2},

 	SampleLoadRate -> {

   		{

    			3.2 * Milliliter / Minute,

    			3.1 * Milliliter / Minute,

    			5 * Milliliter / Minute

    		},

   		5 * Milliliter / Minute,

   		4.5 * Milliliter / Minute

   	}

 ]

To allow an additional rinse of the source wells of the samples and transfer into the matching cartridge, QuantitativeLoadingSample option can be set to True and QuantitativeLoadingSampleVolume option can be set to specify the volume of QuantitativeLoadingSampleSolution to be used. These can be different for samples in the same pool:

ExperimentSolidPhaseExtraction[

 	{{myPooledSample1, myPooledSample2}, mySample1, mySample2},

 	QuantitativeLoadingSample -> {{True, False}, True, False},

 	RinseAndReloadVolume -> {{0.4 * Milliliter, Null},

   0.5 * Milliliter, Null}

 ]



Preferred Input Containers

The Gilson GX-271 liquid handler only accepts 96-well 2mL deep well plate for SamplesIn transfer to SPE ExtractionCartridge. In case SamplesIn are not in the plate, they will be transferred to the plate, prior to SPE.



Possible Issues

Sample Loss

If LoadingSampleDispenseRates are too high or the LoadingSampleVolume is too large, analytes of interest may break through the cartridge during the loading step, leading to sample loss.

SPE Plate Dripping

When unstacked SPE plates are moved or manipulated without their collection plates in a robotic sample preparation, the eluted material may drip onto the liquid handler deck, leading to sample loss.

Insufficient Elution

When the affinity between the ElutingSolution and the compounds of interest is not high and a small ElutingSolutionVolume is used, the samples may not be sufficiently eluted from the Cartridge during the Eluting step, leading to sample loss.

Insufficient Wash

When the WashingSolutionVolume is too low, the impurities in SamplesIn matrix might not be washed out from ExtractionCartridge, leading to contamination of impurities in SamplesOut when finally eluted from ExtractionCartridge.

Air Gap Collapse (Gilson GX-271)

The system tends to work well with aqueous solutions, but some organic solutions can collapse the air gap that the system fluid uses to drive solutions through the system. This can lead to unanticipated mixing of the organic solutions and the system buffer, causing the machine to falter in delivering volume and pressure to the column.

[end context 1]

Here are summaries of the previous meetings:

[begin summary 1]

### Comprehensive Protocol for Peptide Synthesis and Validation

This protocol integrates the best components from previous summaries to ensure a detailed, efficient, and scientifically rigorous approach to peptide synthesis and validation, aligned with the project's goals and constraints.

---

### Peptide Synthesis Protocol

#### Step 1: Solid-Phase Peptide Synthesis (SPPS)
- **Experiment**: `ExperimentPeptideSynthesis`
- **Inputs**: 
  - Fmoc-protected amino acids: 0.1 M in NMP, stored at 4°C
  - Rink amide resin: 1 g, 0.1 mmol/g loading capacity
  - Coupling reagents: HBTU (0.1 M in DMF), DIPEA (2 M in NMP)
  - Deprotection agent: 20% piperidine in DMF, freshly prepared
- **Equipment**: 
  - Automated peptide synthesizer, calibrated for accurate volume delivery
- **Conditions**: 
  - Resin swelling in DMF for 30 minutes
  - Coupling: 5 mL amino acid solution, 5 mL HBTU, 2 mL DIPEA, stir for 60 minutes
  - Deprotection: 10 mL of 20% piperidine in DMF for 20 minutes, repeated
  - Washing: Three washes with 10 mL DMF after each step
- **Output**: Peptide-resin with confirmed coupling efficiency via HPLC

**Quality Control**:
- **Coupling Check**: Perform Kaiser test after each coupling step
- **Documentation**: Record reagent batch numbers, conditions, and deviations

#### Step 2: Cleavage and Deprotection
- **Experiment**: `ExperimentCleavage`
- **Inputs**:
  - Cleavage cocktail: TFA:water:triisopropylsilane:ethyl methyl sulfide (95:2.5:1:1.5), 10 mL per gram of resin
- **Conditions**: 
  - Cleavage at room temperature for 2-3 hours
- **Output**: Crude peptide in solution

#### Step 3: Purification
- **Experiment**: `ExperimentSolidPhaseExtraction` and `ExperimentHPLC`
- **Inputs**: 
  - Crude peptide solution
  - Solvent system: 0.1% TFA in acetonitrile-water gradient
- **Equipment**: 
  - SPE apparatus and HPLC system with C18 column
- **Conditions**: 
  - SPE: Gradient from 5% to 95% acetonitrile over 30 minutes
  - HPLC: Flow rate 1 mL/min, UV detection at 214 nm
- **Output**: Purified peptide >90% purity

#### Step 4: Mass Confirmation
- **Experiment**: `ExperimentLCMS`
- **Inputs**: 
  - Purified peptide
- **Equipment**: 
  - LC-MS system
- **Conditions**: 
  - Standard LCMS settings for peptide analysis
- **Output**: Confirmed molecular weight and sequence identity

#### Step 5: Chemical Modifications
- **Experiment**: `ExperimentBioconjugation`
- **Inputs**: 
  - Purified peptide (0.4 mmol)
  - PEG reagent (0.48 mmol)
- **Conditions**: 
  - Room temperature, stirring for 2 hours in PBS
- **Output**: Modified peptide, confirmed by MS

### Peptide Validation Protocol

#### Structural Validation
- **Experiment**: `ExperimentNMR` and `ExperimentCircularDichroism`
- **Inputs**: 
  - PEGylated peptide
  - PBS buffer (pH 7.4)
- **Equipment**: 
  - NMR spectrometer and CD spectrometer
- **Conditions**: 
  - NMR: Proton and COSY 2D in DMSO-d6
  - CD: 190-260 nm at 25°C
- **Output**: Structural integrity and secondary structure confirmation

#### Binding Validation
- **Experiment**: `ExperimentBioLayerInterferometry` and `ExperimentFluorescencePolarization`
- **Inputs**: 
  - PEGylated peptide
  - Target protein: 1 mg/mL in PBS
- **Equipment**: 
  - BLI instrument and fluorescence polarization reader
- **Conditions**: 
  - BLI: Measure kinetics at peptide concentrations from 1 nM to 1 µM
  - FP: Label peptide with FITC, measure binding across concentrations
- **Output**: Binding affinity (expected KD <10 nM) and kinetic data

#### Functional Validation
- **Experiment**: `ExperimentELISA`
- **Inputs**: 
  - PEGylated peptide
  - HRP-conjugated secondary antibodies
- **Equipment**: 
  - ELISA plate reader
- **Conditions**: 
  - Standard ELISA protocol
- **Output**: Quantitative binding data

#### Stability Validation
- **Experiment**: `ExperimentThermalShift`
- **Inputs**: 
  - PEGylated peptide
  - Sypro Orange dye
- **Equipment**: 
  - Real-time PCR thermal cycler
- **Conditions**: 
  - Heat and record fluorescence to determine melting temperature
- **Output**: Thermal stability profile

### Integration with Machine Learning Models

- **Data Handling and Feedback**: Collect binding affinity, structural data, and stability profiles to feed back into machine learning models (ProteinMPNN and RFDiffusion). Use these data to refine predictions, focusing on recognized patterns or discrepancies.

### Controls and Quality Assurance

- **Control Samples**: Include non-modified peptides as negative controls and known active peptides as positive controls.
- **Quality Assurance**: Implement checkpoints for purity (>90%) and identity verification using LCMS and HPLC. Document each step thoroughly.
- **Sample Management**: Use barcoded sample tracking within ECL to ensure precise handling and accountability.

### Data Management and Feedback Loop

- **Data Management Tools**: Use platforms like AWS for data storage and management. Continuously integrate experimental data back into the machine learning models to refine predictions.
- **Feedback Loop**: Regularly update models with new data, possibly weekly or bi-weekly, to enhance prediction accuracy and guide iterative peptide design.

---

### Explanation of Component Selection

1. **Detailed Reagent Preparation and Equipment Use**: This was emphasized in summaries 2 and 5, ensuring precise conditions and reagent handling, which is critical for reproducibility and accuracy.

2. **Integration with Machine Learning**: Summaries 3 and 4 highlighted the use of machine learning models like ProteinMPNN and RFDiffusion, which is crucial for aligning with the project's goal of scientifically impactful applications.

3. **Quality Assurance and Controls**: Summaries 1 and 5 provided comprehensive quality control measures, ensuring that each step is validated and documented, which is essential for high clinical value and scientific rigor.

4. **Data Management and Feedback Loop**: Summaries 4 and 5 focused on using AWS for data management and creating a feedback loop with machine learning models, ensuring continuous improvement and alignment with project goals.

By integrating these components, the protocol is robust, detailed, and aligned with the project's objectives, ensuring high clinical value and impactful scientific contributions.

[end summary 1]

Here is the agenda for the meeting:

You are working on a research project to use machine learning for drug discovery. Your goals are the following: (1) the project must have high clinical value, meaning the research contributes to helping patients, (2) the project must include a scientifically impactful application of machine learning to drug discovery, and (3) the project must use Emerald Cloud Labs (ECL) for all experimental validation with a 3-month limit on experiments. Your team previously decided to pursue peptide-based therapeutics. You previously designed experimental protocols for synthesis and validation of peptide-based therapeutics for a given protein drug target. Now you must implement one of these protocols using ECL. Please implement the ExperimentSolidPhaseExtraction protocol using the appropriate commands and syntax from ECL, writing out the experiment in the form ExperimentSolidPhaseExtraction[<options>] where you fill in <options> with the appropriate options. Please refer to the ECL documentation that is provided as context. In general, leave most options at their default values (and therefore do not specify them) except for those options that should be changed based on your specific experimental design. For every option that you do specify, please explain why you chose that value.

Medicinal Chemist, please provide your response to the agenda.

## Medicinal Chemist

To implement the `ExperimentSolidPhaseExtraction` protocol using ECL, we need to carefully select the options that align with our experimental design for peptide-based therapeutics. Here is how we can set up the experiment, along with explanations for each specified option:

```plaintext
ExperimentSolidPhaseExtraction[
    {
        {myPooledSample1, myPooledSample2}, mySample1, mySample2
    },
    ExtractionStrategy -> Positive,
    ExtractionMode -> ReversePhase,
    ExtractionSorbent -> C18,
    ExtractionCartridge -> Model[Container, ExtractionCartridge, "500mg, 3cc, C18, Vac extraction cartridge"],
    Instrument -> Model[Instrument, LiquidHandler, "id:o1k9jAKOwLl8"],
    PreFlushingSolution -> Model[Sample, StockSolution, "90% methanol"],
    PreFlushingSolutionVolume -> 10 * Milliliter,
    ConditioningSolution -> Model[Sample, StockSolution, "15 mM ammonium acetate"],
    ConditioningSolutionVolume -> 17 * Milliliter,
    WashingSolution -> Model[Sample, "Milli-Q water"],
    WashingSolutionVolume -> 30 * Milliliter,
    ElutingSolution -> Model[Sample, StockSolution, "90% methanol"],
    ElutingSolutionVolume -> 1 * Milliliter
]
```

### Explanation of Specified Options:

1. **ExtractionStrategy -> Positive**: We are interested in retaining the analytes of interest on the sorbent, which is typical for peptide purification.

2. **ExtractionMode -> ReversePhase**: This mode is suitable for separating compounds based on polarity, which is effective for peptides.

3. **ExtractionSorbent -> C18**: C18 is a common choice for reverse-phase extractions, providing good retention for peptides.

4. **ExtractionCartridge**: We specify a C18 cartridge that matches our sorbent choice and is compatible with our liquid handler.

5. **Instrument -> Model[Instrument, LiquidHandler, "id:o1k9jAKOwLl8"]**: The Gilson GX-271 LiquidHandler is selected for its compatibility with our cartridge and ability to automate the SPE process.

6. **PreFlushingSolution -> "90% methanol"**: Methanol is used to clean the sorbent of any residues, ensuring a clean starting point for the extraction.

7. **PreFlushingSolutionVolume -> 10 * Milliliter**: This volume is sufficient to thoroughly flush the cartridge without wasting solvent.

8. **ConditioningSolution -> "15 mM ammonium acetate"**: This solution conditions the sorbent to ensure consistent interaction with the sample.

9. **ConditioningSolutionVolume -> 17 * Milliliter**: This volume ensures the sorbent is fully conditioned.

10. **WashingSolution -> "Milli-Q water"**: Water is used to wash away non-specifically bound impurities.

11. **WashingSolutionVolume -> 30 * Milliliter**: A larger volume ensures thorough washing, improving the purity of the eluted analytes.

12. **ElutingSolution -> "90% methanol"**: Methanol is used to elute the peptides from the sorbent.

13. **ElutingSolutionVolume -> 1 * Milliliter**: A smaller volume is used to concentrate the eluted peptides, facilitating downstream analysis.

This setup ensures that we efficiently extract and purify our peptide samples, aligning with our project's goals of high clinical value and impactful scientific application. The use of ECL for this experiment allows us to leverage automated systems for precise and reproducible results within our 3-month experimental timeline.

