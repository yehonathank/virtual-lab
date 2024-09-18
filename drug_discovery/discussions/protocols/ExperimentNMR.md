## User

This is the beginning of an individual meeting with Medicinal Chemist to discuss your research project.

Here is context for this meeting:

[begin context 1]

ExperimentNMR[Samples]⟹Protocol

generates a Protocol object for measuring the nuclear magnetic resonance (NMR) spectrum of provided Samples.



Nuclear magnetic resonance (NMR) is a spectroscopic technique used to identify and characterize the chemical structure of compounds. A sample is inserted into a magnetic field, which causes select nuclei (most commonly 1H and 13C) to absorb radio-frequency radiation. The frequency at which this occurs, and the intensity of this absorption, is proportional to the magnetic field around each nucleus. This magnetic field is heavily dependent on the chemical environment, and so each nucleus will give a characteristic signal depending on its surroundings. This produces a spectrum that allows identification of known molecules or the characterization of the structure of unknown ones.



Experimental Principles

Figure 1.1: Step 1: Sample is dissolved in specified NMRSolvent. Step 2: Samples are transferred into NMR tubes. Step 3: The tubes are loaded onto the NMR instrument. Step 4: The spectrum is collected for each of the samples. Step 5 (optional): The data is assessed using AnalyzePeaks.



Instrumentation

Ascend 500

Model[Instrument, NMR, "id:6V0npvK61r8q"]

Figure 2.1.1: Samples in NMR tubes are lowered into the bore of the NMR instrument. A superconducting magnet cooled by liquid helium generates a strong magnetic field (11.7 T) that surrounds the sample and aligns the spin states of its nuclei. A radio-frequency pulse is applied to the sample which excites the nuclear spin states of the desired nucleus. Once the pulse is turned off, the excited spins emit a decaying rf signal known as a free induction decay (FID) as they return to equilibrium. Because the environment of each nucleus differs, the nature of this FID allows for the characterization of the structure of the provided sample.



Experiment Options

Sample Parameters

Nucleus

The nucleus whose spins will be recorded in this experiment.

Default Value: 1H

Pattern Description: 1H, 13C, 19F, or 31P.

Programmatic Pattern: Nucleus1DP

Index Matches to: experiment samples

DeuteratedSolvent

The deuterated solvent in which the provided samples will be dissolved in prior to taking their spectra (or, if the samples are already in the NMR tube, what solvent was used to dissolve them).

Default Value: Automatic

Default Calculation: Automatically set to Model[Sample, "Milli-Q water"] if UseExternalStandard is True, otherwise set to Model[Sample, "Deuterium oxide"].

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Water, Chloroform, DMSO, Benzene, Acetone, Acetonitrile, or Methanol.

Programmatic Pattern: (DeuteratedSolventP | (ObjectP[{Model[Sample], Object[Sample]}] | _String)) | Automatic

Index Matches to: experiment samples

UseExternalStandard

Indicate if an external standard is used in this experiment. For example, in an NMR experiment, an external standard is stored separately in a coaxial insert (sealed or not) inserted into the NMR tube. The external standard helps lock the magnetic field if not using a deuterated solvent for the experiment or helps quantify the sample amount. For now, we only support one sealed coaxial insert: Model[Container,Vessel,"3mm NMR Sealed Coaxial Insert with 3-(Trimethylsilyl)propionic-2,2,3,3-d4 in Deuterium Oxide"].

Default Value: Automatic

Default Calculation: Automatically set to True if SealedCoaxialInsert is specified. Else set to False.

Pattern Description: True or False.

Programmatic Pattern: BooleanP | Automatic

Index Matches to: experiment samples

SealedCoaxialInsert

The sealed coaxial insert that used as an external standards during the experiment.

Default Value: Automatic

Default Calculation: Automatically set to Null if UseExternalStandard is False. Else set to Model[Container, Vessel, "3mm NMR Sealed Coaxial Insert with 3-(Trimethylsilyl)propionic-2,2,3,3-d4 in Deuterium Oxide"]

Pattern Description: An object of type or subtype Model[Container, Vessel] or Null.

Programmatic Pattern: (ObjectP[{Model[Container, Vessel]}] | Automatic) | Null

Index Matches to: experiment samples

SolventVolume

The amount of the specified DeuteratedSolvent to add to the sample, the combination of which will be read in the NMR spectrometer. If directly set to 0 uL then neat sample will itself be added to an NMR tube.

Default Value: Automatic

Default Calculation: Automatically set to Null if the sample is already in an NMR tube, or a volume such that SampleAmount + SolventVolume = 700 uL if it is not.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 1000 microliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 1000*Microliter] | Automatic) | Null

Index Matches to: experiment samples

SampleAmount

The amount of sample (after aliquoting, if applicable) that will be dissolved in the specified DeuteratedSolvent.

Default Value: Automatic

Default Calculation: Automatically set to Null if the sample is already in an NMR tube, or if not, to the smaller of 5 Milligram or the full mass of the sample if a solid, the smaller or 10 Microliter or the full volume of the sample if a liquid, or 1 unit if a counted sample.

Pattern Description: Count or Count or Mass or Volume or Null.

Programmatic Pattern: ((RangeP[1*Microliter, 1000*Microliter] | RangeP[1*Milligram, 3*Gram] | GreaterP[0*Unit, 1*Unit] | GreaterP[0., 1.]) | Automatic) | Null

Index Matches to: experiment samples

SampleTemperature

The temperature at which the sample will be held prior to and during data collection.

Default Value: Ambient

Pattern Description: Ambient or greater than or equal to -50 degrees Celsius and less than or equal to 60 degrees Celsius or Null.

Programmatic Pattern: (Ambient | RangeP[-50*Celsius, 60*Celsius]) | Null

Index Matches to: experiment samples

NMRTube

The model of NMR tube in which the provided input sample will be placed prior to data collection.

Default Value: Model[Container, Vessel, NMR Tube, 5 mm x 103.5 mm]

Pattern Description: An object of type or subtype Model[Container, Vessel]

Programmatic Pattern: ObjectP[{Model[Container, Vessel]}]

Index Matches to: experiment samples

Data Acquisition

NumberOfScans

The number of pulse and read cycles that will be averaged together that are applied to each sample.

Default Value: Automatic

Default Calculation: Automatically set to 16 if Nucleus -> 1H or 19F, 1024 if Nucleus -> 13C, and 32 if Nucleus -> 31P.

Pattern Description: Greater than or equal to 1 and less than or equal to 500000 in increments of 1.

Programmatic Pattern: RangeP[1, 500000, 1] | Automatic

Index Matches to: experiment samples

NumberOfDummyScans

The number of scans performed before the receiver is turned on and data is collected for each sample.

Default Value: Automatic

Default Calculation: Automatically set to 2 if Nucleus -> 1H, and 4 if Nucleus -> 13C, 19F, or 31P.

Pattern Description: 1 or Multiple of 2.

Programmatic Pattern: (RangeP[1, 1] | RangeP[2, 128, 2]) | Automatic

Index Matches to: experiment samples

AcquisitionTime

Length of time during which the NMR signal is sampled and digitized per scan.

Default Value: Automatic

Default Calculation: Automatically set to 4 Second if Nucleus -> 1H, 1.1 Second if Nucleus -> 13C, 0.6 Second if Nucleus -> 19F, and 0.4 Second if Nucleus -> 31P

Pattern Description: Greater than or equal to 0.1 seconds and less than or equal to 30 seconds.

Programmatic Pattern: RangeP[0.1*Second, 30*Second] | Automatic

Index Matches to: experiment samples

RelaxationDelay

Length of time before the beginning of the PulseWidth of a given scan. In effect, this is also the length of time after the AcquisitionTime before the next scan begins.

Default Value: Automatic

Default Calculation: Automatically set to 1 Second if Nucleus -> 1H or 19F, and 2 Second if Nucleus -> 13C or 31P.

Pattern Description: Greater than or equal to 0.1 seconds and less than or equal to 30 seconds.

Programmatic Pattern: RangeP[0.1*Second, 30*Second] | Automatic

Index Matches to: experiment samples

PulseWidth

Length of time during which the radio frequency pulse is turned on and the sample is irradiated per scan, assuming a 90 degree pulse. Note that for Nucleus -> 1H | 13C | 31P, the experiment is run with a 30 degree pulse, and so the specified pulse width is actually divided by 3. Although this lowers sensitivity per scan, it allows faster accumulation of data such that sensitivity is increased overall.

Default Value: Automatic

Default Calculation: Automatically set to 10 Microsecond if Nucleus -> 1H or 13C, 15 Microsecond if Nucleus -> 19F, and 14 Microsecond if Nucleus -> 31P.

Pattern Description: Greater than or equal to 1 microsecond and less than or equal to 60 microseconds.

Programmatic Pattern: RangeP[1*Microsecond, 60*Microsecond] | Automatic

Index Matches to: experiment samples

FlipAngle

Angle of rotation for the first radio-frequency pulse

Default Value: Automatic

Default Calculation: Automatically set to 90 AngularDegree if Nucleus -> 19F, or if WaterSuppression is set to anything but None. All other cases set to 30 AngularDegree.

Pattern Description: 30 degrees or 90 degrees.

Programmatic Pattern: (30*AngularDegree | 90*AngularDegree) | Automatic

Index Matches to: experiment samples

SpectralDomain

The range of the observed frequencies for a given spectrum.

Default Value: Automatic

Default Calculation: Automatically set to Span[-4 PPM, 16 PPM] if Nucleus -> 1H, Span[-20 PPM, 220 PPM] if Nucleus -> if 13C, Span[-220 PPM, 20 PPM] if Nucleus -> 19F, and Span[-250 PPM, 150 PPM] if Nucleus -> 31P.

Pattern Description: A span from anything greater than or equal to -200 parts per million and less than or equal to 600 parts per million to anything greater than or equal to -200 parts per million and less than or equal to 600 parts per million.

Programmatic Pattern: RangeP[-200*PPM, 600*PPM] ;; RangeP[-200*PPM, 600*PPM] | Automatic

Index Matches to: experiment samples

WaterSuppression

Indicates the method of eliminating a water signal from the spectrum. Note that this may only be set if Nucleus -> 1H.

Default Value: None

Pattern Description: {Presaturation, WATERGATE, ExcitationSculpting} or None.

Programmatic Pattern: WaterSuppressionMethodP | None

Index Matches to: experiment samples

Kinetic Data Acquisition

TimeCourse

Indicates if multiple spectra should be collected over time.

Default Value: Automatic

Default Calculation: Automatically set to True if TimeInterval, NumberOfTimedScans, are specified, or False otherwise.

Pattern Description: True or False.

Programmatic Pattern: BooleanP | Automatic

Index Matches to: experiment samples

TimeInterval

Indicates the length of time between the start of scans of the same sample when TimeCourse -> True.

Default Value: Automatic

Default Calculation: Automatically set to length of time for one scan + 1 Minute if TimeCourse is True, or Null otherwise.

Pattern Description: Greater than 0 seconds or Null.

Programmatic Pattern: (GreaterP[0*Second] | Automatic) | Null

Index Matches to: experiment samples

NumberOfTimeIntervals

Indicates the number of spectra to be collected of the input sample when TimeCourse -> True.

Default Value: Automatic

Default Calculation: Automatically set to Floor[TotalTimeCourse / TimeInterval] + 1 if TotalTimeCourse is set, or 10 if TimeCourse is otherwise True, or Null otherwise.

Pattern Description: Greater than or equal to 1 and less than or equal to 1000 in increments of 1 or Null.

Programmatic Pattern: (RangeP[1, 1000, 1] | Automatic) | Null

Index Matches to: experiment samples

TotalTimeCourse

Indicates the total duration of time during which scans are taken according to the TimeInterval.

Default Value: Automatic

Default Calculation: Automatically set to TimeInterval * NumberOfTimeIntervals if TimeCourse -> True, or Null otherwise.

Pattern Description: Greater than 0 seconds or Null.

Programmatic Pattern: (GreaterP[0*Second] | Automatic) | Null

Index Matches to: experiment samples

General

Instrument

The NMR instrument used for this experiment.

Default Value: Model[Instrument, NMR, Ascend 500]

Pattern Description: An object of type or subtype Model[Instrument, NMR] or Object[Instrument, NMR]

Programmatic Pattern: ObjectP[{Model[Instrument, NMR], Object[Instrument, NMR]}]

Protocol

NumberOfReplicates

The number of times to repeat NMR reading on each provided sample. If Aliquot -> True, this also indicates the number of times each provided sample will be aliquoted.

Default Value: Null

Pattern Description: Greater than or equal to 2 in increments of 1 or Null.

Programmatic Pattern: GreaterEqualP[2, 1] | Null

Post Experiment

SamplesInStorageCondition

The non-default conditions under which the SamplesIn of this experiment should be stored after the protocol is completed. If left unset, SamplesIn will be stored according to their current StorageCondition.

Default Value: Null

Pattern Description: {AmbientStorage, Refrigerator, Freezer, DeepFreezer, CryogenicStorage, YeastIncubation, YeastShakingIncubation, BacterialIncubation, BacterialShakingIncubation, MammalianIncubation, ViralIncubation, CrystalIncubation, AcceleratedTesting, IntermediateTesting, LongTermTesting, UVVisLightTesting} or Disposal or Null.

Programmatic Pattern: (Alternatives[SampleStorageTypeP | Disposal]) | Null

Index Matches to: experiment samples

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

IncubationTemperature

Temperature at which the SamplesIn should be incubated for the duration of the IncubationTime prior to starting the experiment.

Default Value: Automatic

Pattern Description: Ambient or greater than or equal to -20 degrees Celsius and less than or equal to 500 degrees Celsius or Null.

Programmatic Pattern: ((Ambient | RangeP[$MinIncubationTemperature, $MaxIncubationTemperature]) | Automatic) | Null

Index Matches to: experiment samples

IncubationTime

Duration for which SamplesIn should be incubated at the IncubationTemperature, prior to starting the experiment.

Default Value: Automatic

Pattern Description: Greater than or equal to 1 minute and less than or equal to 72 hours or Null.

Programmatic Pattern: (RangeP[1*Minute, $MaxExperimentTime] | Automatic) | Null

Index Matches to: experiment samples

Mix

Indicates if this sample should be mixed while incubated, prior to starting the experiment.

Default Value: Automatic

Default Calculation: Automatically resolves to True if any Mix related options are set. Otherwise, resolves to False.

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

Index Matches to: experiment samples

MixType

Indicates the style of motion used to mix the sample, prior to starting the experiment.

Default Value: Automatic

Default Calculation: Automatically resolves based on the container of the sample and the Mix option.

Pattern Description: Roll, Vortex, Sonicate, Pipette, Invert, Stir, Shake, Homogenize, Swirl, Disrupt, or Nutate or Null.

Programmatic Pattern: (MixTypeP | Automatic) | Null

Index Matches to: experiment samples

MixUntilDissolved

Indicates if the mix should be continued up to the MaxIncubationTime or MaxNumberOfMixes (chosen according to the mix Type), in an attempt dissolve any solute. Any mixing/incubation will occur prior to starting the experiment.

Default Value: Automatic

Default Calculation: Automatically resolves to True if MaxIncubationTime or MaxNumberOfMixes is set.

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

Index Matches to: experiment samples

MaxIncubationTime

Maximum duration of time for which the samples will be mixed while incubated in an attempt to dissolve any solute, if the MixUntilDissolved option is chosen. This occurs prior to starting the experiment.

Default Value: Automatic

Default Calculation: Automatically resolves based on MixType, MixUntilDissolved, and the container of the given sample.

Pattern Description: Greater than or equal to 1 minute and less than or equal to 72 hours or Null.

Programmatic Pattern: (RangeP[1*Minute, $MaxExperimentTime] | Automatic) | Null

Index Matches to: experiment samples

IncubationInstrument

The instrument used to perform the Mix and/or Incubation, prior to starting the experiment.

Default Value: Automatic

Default Calculation: Automatically resolves based on the options Mix, Temperature, MixType and container of the sample.

Pattern Description: An object of type or subtype Model[Instrument, Roller], Model[Instrument, OverheadStirrer], Model[Instrument, Vortex], Model[Instrument, Shaker], Model[Instrument, BottleRoller], Model[Instrument, Roller], Model[Instrument, Sonicator], Model[Instrument, HeatBlock], Model[Instrument, Homogenizer], Model[Instrument, Disruptor], Model[Instrument, Nutator], Model[Instrument, Thermocycler], Model[Instrument, EnvironmentalChamber], Model[Instrument, Pipette], Object[Instrument, Roller], Object[Instrument, OverheadStirrer], Object[Instrument, Vortex], Object[Instrument, Shaker], Object[Instrument, BottleRoller], Object[Instrument, Roller], Object[Instrument, Sonicator], Object[Instrument, HeatBlock], Object[Instrument, Homogenizer], Object[Instrument, Disruptor], Object[Instrument, Nutator], Object[Instrument, Thermocycler], Object[Instrument, EnvironmentalChamber], or Object[Instrument, Pipette] or Null.

Programmatic Pattern: (ObjectP[Join[MixInstrumentModels, MixInstrumentObjects]] | Automatic) | Null

Index Matches to: experiment samples

AnnealingTime

Minimum duration for which the SamplesIn should remain in the incubator allowing the system to settle to room temperature after the IncubationTime has passed but prior to starting the experiment.

Default Value: Automatic

Pattern Description: Greater than or equal to 0 minutes and less than or equal to 72 hours or Null.

Programmatic Pattern: (RangeP[0*Minute, $MaxExperimentTime] | Automatic) | Null

Index Matches to: experiment samples

IncubateAliquotContainer

The desired type of container that should be used to prepare and house the incubation samples which should be used in lieu of the SamplesIn for the experiment.

Default Value: Automatic

Pattern Description: An object of type or subtype Model[Container] or {Index, Container} or Null.

Programmatic Pattern: ((ObjectP[Model[Container]] | {GreaterEqualP[1, 1] | (Automatic | Null), (ObjectP[{Model[Container], Object[Container]}] | _String) | Automatic}) | Automatic) | Null

Index Matches to: experiment samples

IncubateAliquotDestinationWell

The desired position in the corresponding IncubateAliquotContainer in which the aliquot samples will be placed.

Default Value: Automatic

Default Calculation: Automatically resolves to A1 in containers with only one position. For plates, fills wells in the order provided by the function AllWells.

Pattern Description: Any well from A1 to H12 or Null.

Programmatic Pattern: (WellPositionP | Automatic) | Null

Index Matches to: experiment samples

IncubateAliquot

The amount of each sample that should be transferred from the SamplesIn into the IncubateAliquotContainer when performing an aliquot before incubation.

Default Value: Automatic

Default Calculation: Automatically set as the smaller between the current sample volume and the maximum volume of the destination container.

Pattern Description: All or greater than or equal to 1 microliter and less than or equal to 20 liters or Null.

Programmatic Pattern: ((RangeP[1*Microliter, 20*Liter] | All) | Automatic) | Null

Index Matches to: experiment samples

Preparatory Centrifugation

Centrifuge

Indicates if the SamplesIn should be centrifuged prior to starting the experiment or any aliquoting. Sample Preparation occurs in the order of Incubation, Centrifugation, Filtration, and then Aliquoting (if specified).

Default Value: Automatic

Default Calculation: Resolves to True if any of the corresponding Centrifuge options are set. Otherwise, resolves to False.

Pattern Description: True or False.

Programmatic Pattern: BooleanP | Automatic

Index Matches to: experiment samples

CentrifugeInstrument

The centrifuge that will be used to spin the provided samples prior to starting the experiment.

Default Value: Automatic

Pattern Description: An object of type or subtype Model[Instrument, Centrifuge] or Object[Instrument, Centrifuge] or Null.

Programmatic Pattern: (ObjectP[{Model[Instrument, Centrifuge], Object[Instrument, Centrifuge]}] | Automatic) | Null

Index Matches to: experiment samples

CentrifugeIntensity

The rotational speed or the force that will be applied to the samples by centrifugation prior to starting the experiment.

Default Value: Automatic

Pattern Description: Greater than 0 revolutions per minute or greater than 0 standard accelerations due to gravity on the surface of the earth or Null.

Programmatic Pattern: ((GreaterP[0*RPM] | GreaterP[0*GravitationalAcceleration]) | Automatic) | Null

Index Matches to: experiment samples

CentrifugeTime

The amount of time for which the SamplesIn should be centrifuged prior to starting the experiment.

Default Value: Automatic

Pattern Description: Greater than 0 minutes or Null.

Programmatic Pattern: (GreaterP[0*Minute] | Automatic) | Null

Index Matches to: experiment samples

CentrifugeTemperature

The temperature at which the centrifuge chamber should be held while the samples are being centrifuged prior to starting the experiment.

Default Value: Automatic

Pattern Description: Ambient or greater than or equal to -10 degrees Celsius and less than or equal to 40 degrees Celsius or Null.

Programmatic Pattern: ((Ambient | RangeP[-10*Celsius, 40*Celsius]) | Automatic) | Null

Index Matches to: experiment samples

CentrifugeAliquotContainer

The desired type of container that should be used to prepare and house the centrifuge samples which should be used in lieu of the SamplesIn for the experiment.

Default Value: Automatic

Pattern Description: An object of type or subtype Model[Container] or {Index, Container} or Null.

Programmatic Pattern: ((ObjectP[Model[Container]] | {GreaterEqualP[1, 1] | (Automatic | Null), (ObjectP[{Model[Container], Object[Container]}] | _String) | Automatic}) | Automatic) | Null

Index Matches to: experiment samples

CentrifugeAliquotDestinationWell

The desired position in the corresponding AliquotContainer in which the aliquot samples will be placed.

Default Value: Automatic

Default Calculation: Automatically resolves to A1 in containers with only one position. For plates, fills wells in the order provided by the function AllWells.

Pattern Description: Any well from A1 to H12 or Null.

Programmatic Pattern: (WellPositionP | Automatic) | Null

Index Matches to: experiment samples

CentrifugeAliquot

The amount of each sample that should be transferred from the SamplesIn into the CentrifugeAliquotContainer when performing an aliquot before centrifugation.

Default Value: Automatic

Default Calculation: Automatically set as the smaller between the current sample volume and the maximum volume of the destination container.

Pattern Description: All or greater than or equal to 1 microliter and less than or equal to 20 liters or Null.

Programmatic Pattern: ((RangeP[1*Microliter, 20*Liter] | All) | Automatic) | Null

Index Matches to: experiment samples

Preparatory Filtering

Filtration

Indicates if the SamplesIn should be filter prior to starting the experiment or any aliquoting. Sample Preparation occurs in the order of Incubation, Centrifugation, Filtration, and then Aliquoting (if specified).

Default Value: Automatic

Default Calculation: Resolves to True if any of the corresponding Filter options are set. Otherwise, resolves to False.

Pattern Description: True or False.

Programmatic Pattern: BooleanP | Automatic

Index Matches to: experiment samples

FiltrationType

The type of filtration method that should be used to perform the filtration.

Default Value: Automatic

Default Calculation: Will automatically resolve to a filtration type appropriate for the volume of sample being filtered.

Pattern Description: PeristalticPump, Centrifuge, Vacuum, Syringe, or AirPressure or Null.

Programmatic Pattern: (FiltrationTypeP | Automatic) | Null

Index Matches to: experiment samples

FilterInstrument

The instrument that should be used to perform the filtration.

Default Value: Automatic

Default Calculation: Will automatically resolved to an instrument appropriate for the filtration type.

Pattern Description: An object of type or subtype Model[Instrument, FilterBlock], Object[Instrument, FilterBlock], Model[Instrument, PeristalticPump], Object[Instrument, PeristalticPump], Model[Instrument, VacuumPump], Object[Instrument, VacuumPump], Model[Instrument, Centrifuge], Object[Instrument, Centrifuge], Model[Instrument, SyringePump], or Object[Instrument, SyringePump] or Null.

Programmatic Pattern: (ObjectP[{Model[Instrument, FilterBlock], Object[Instrument, FilterBlock], Model[Instrument, PeristalticPump], Object[Instrument, PeristalticPump], Model[Instrument, VacuumPump], Object[Instrument, VacuumPump], Model[Instrument, Centrifuge], Object[Instrument, Centrifuge], Model[Instrument, SyringePump], Object[Instrument, SyringePump]}] | Automatic) | Null

Index Matches to: experiment samples

Filter

The filter that should be used to remove impurities from the SamplesIn prior to starting the experiment.

Default Value: Automatic

Default Calculation: Will automatically resolve to a filter appropriate for the filtration type and instrument.

Pattern Description: An object of type or subtype Model[Container, Plate, Filter], Model[Container, Vessel, Filter], or Model[Item, Filter] or Null.

Programmatic Pattern: (ObjectP[{Model[Container, Plate, Filter], Model[Container, Vessel, Filter], Model[Item, Filter]}] | Automatic) | Null

Index Matches to: experiment samples

FilterMaterial

The membrane material of the filter that should be used to remove impurities from the SamplesIn prior to starting the experiment.

Default Value: Automatic

Default Calculation: Resolves to an appropriate filter material for the given sample is Filtration is set to True.

Pattern Description: Cellulose, Cotton, Polyethylene, Polypropylene, PTFE, Nylon, PES, PLUS, PVDF, GlassFiber, GHP, UHMWPE, EPDM, DuraporePVDF, GxF, ZebaDesaltingResin, NickelResin, Silica, or HLB or Null.

Programmatic Pattern: (FilterMembraneMaterialP | Automatic) | Null

Index Matches to: experiment samples

PrefilterMaterial

The material from which the prefilter filtration membrane should be made of to remove impurities from the SamplesIn prior to starting the experiment.

Default Value: Automatic

Default Calculation: By default, no prefiltration is performed on samples, even when Filter->True.

Pattern Description: Cellulose, Cotton, Polyethylene, Polypropylene, PTFE, Nylon, PES, PLUS, PVDF, GlassFiber, GHP, UHMWPE, EPDM, DuraporePVDF, GxF, ZebaDesaltingResin, NickelResin, Silica, or HLB or Null.

Programmatic Pattern: (FilterMembraneMaterialP | Automatic) | Null

Index Matches to: experiment samples

FilterPoreSize

The pore size of the filter that should be used when removing impurities from the SamplesIn prior to starting the experiment.

Default Value: Automatic

Default Calculation: Resolves to an appropriate filter pore size for the given sample is Filtration is set to True.

Pattern Description: 0.008 micrometers, 0.1 micrometers, 0.2 micrometers, 0.22 micrometers, 0.45 micrometers, 1. micrometer, 1.1 micrometers, 2.5 micrometers, 6. micrometers, 20. micrometers, 30. micrometers, or 100. micrometers or Null.

Programmatic Pattern: (FilterSizeP | Automatic) | Null

Index Matches to: experiment samples

PrefilterPoreSize

The pore size of the filter; all particles larger than this should be removed during the filtration.

Default Value: Automatic

Default Calculation: By default, no prefiltration is performed on samples, even when Filter->True.

Pattern Description: 0.008 micrometers, 0.1 micrometers, 0.2 micrometers, 0.22 micrometers, 0.45 micrometers, 1. micrometer, 1.1 micrometers, 2.5 micrometers, 6. micrometers, 20. micrometers, 30. micrometers, or 100. micrometers or Null.

Programmatic Pattern: (FilterSizeP | Automatic) | Null

Index Matches to: experiment samples

FilterSyringe

The syringe used to force that sample through a filter.

Default Value: Automatic

Default Calculation: Resolves to an syringe appropriate to the volume of sample being filtered, if Filtration is set to True.

Pattern Description: An object of type or subtype Model[Container, Syringe] or Object[Container, Syringe] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Container, Syringe], Object[Container, Syringe]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

FilterHousing

The filter housing that should be used to hold the filter membrane when filtration is performed using a standalone filter membrane.

Default Value: Automatic

Default Calculation: Resolve to an housing capable of holding the size of the membrane being used, if filter with Membrane FilterType is being used and Filtration is set to True.

Pattern Description: An object of type or subtype Model[Instrument, FilterHousing], Object[Instrument, FilterHousing], Model[Instrument, FilterBlock], or Object[Instrument, FilterBlock] or Null.

Programmatic Pattern: (ObjectP[{Model[Instrument, FilterHousing], Object[Instrument, FilterHousing], Model[Instrument, FilterBlock], Object[Instrument, FilterBlock]}] | Automatic) | Null

Index Matches to: experiment samples

FilterIntensity

The rotational speed or force at which the samples will be centrifuged during filtration.

Default Value: Automatic

Default Calculation: Will automatically resolve to 2000 GravitationalAcceleration if FiltrationType is Centrifuge and Filtration is True.

Pattern Description: Greater than 0 revolutions per minute or greater than 0 standard accelerations due to gravity on the surface of the earth or Null.

Programmatic Pattern: ((GreaterP[0*RPM] | GreaterP[0*GravitationalAcceleration]) | Automatic) | Null

Index Matches to: experiment samples

FilterTime

The amount of time for which the samples will be centrifuged during filtration.

Default Value: Automatic

Default Calculation: Will automatically resolve to 5 Minute if FiltrationType is Centrifuge and Filtration is True.

Pattern Description: Greater than 0 minutes or Null.

Programmatic Pattern: (GreaterP[0*Minute] | Automatic) | Null

Index Matches to: experiment samples

FilterTemperature

The temperature at which the centrifuge chamber will be held while the samples are being centrifuged during filtration.

Default Value: Automatic

Default Calculation: Will automatically resolve to 22 Celsius if FiltrationType is Centrifuge and Filtration is True.

Pattern Description: Greater than or equal to 4 degrees Celsius or Null.

Programmatic Pattern: ((Alternatives[GreaterEqualP[4*Celsius]]) | Automatic) | Null

Index Matches to: experiment samples

FilterContainerOut

The desired container filtered samples should be produced in or transferred into by the end of filtration, with indices indicating grouping of samples in the same plates, if desired.

Default Value: Automatic

Default Calculation: Automatically set as the PreferredContainer for the Volume of the sample. For plates, attempts to fill all wells of a single plate with the same model before using another one.

Pattern Description: An object of type or subtype Model[Container] or Object[Container] or a prepared sample or {Index, Container} or Null.

Programmatic Pattern: (((ObjectP[{Model[Container], Object[Container]}] | _String) | {GreaterEqualP[1, 1] | Automatic, (ObjectP[{Model[Container], Object[Container]}] | _String) | Automatic}) | Automatic) | Null

Index Matches to: experiment samples

FilterAliquotDestinationWell

The desired position in the corresponding AliquotContainer in which the aliquot samples will be placed.

Default Value: Automatic

Default Calculation: Automatically resolves to A1 in containers with only one position. For plates, fills wells in the order provided by the function AllWells.

Pattern Description: Any well from A1 to H12 or Null.

Programmatic Pattern: (WellPositionP | Automatic) | Null

Index Matches to: experiment samples

FilterAliquotContainer

The desired type of container that should be used to prepare and house the filter samples which should be used in lieu of the SamplesIn for the experiment.

Default Value: Automatic

Pattern Description: An object of type or subtype Model[Container] or {Index, Container} or Null.

Programmatic Pattern: ((ObjectP[Model[Container]] | {GreaterEqualP[1, 1] | (Automatic | Null), (ObjectP[{Model[Container], Object[Container]}] | _String) | Automatic}) | Automatic) | Null

Index Matches to: experiment samples

FilterAliquot

The amount of each sample that should be transferred from the SamplesIn into the FilterAliquotContainer when performing an aliquot before filtration.

Default Value: Automatic

Default Calculation: Automatically set as the smaller between the current sample volume and the maximum volume of the destination container.

Pattern Description: All or greater than or equal to 1 microliter and less than or equal to 20 liters or Null.

Programmatic Pattern: ((RangeP[1*Microliter, 20*Liter] | All) | Automatic) | Null

Index Matches to: experiment samples

FilterSterile

Indicates if the filtration of the samples should be done in a sterile environment.

Default Value: Automatic

Default Calculation: Resolve to False if Filtration is indicated. If sterile filtration is desired, this option must manually be set to True.

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

Index Matches to: experiment samples

Aliquoting

Aliquot

Indicates if aliquots should be taken from the SamplesIn and transferred into new AliquotSamples used in lieu of the SamplesIn for the experiment. Note that if NumberOfReplicates is specified this indicates that the input samples will also be aliquoted that number of times. Note that Aliquoting (if specified) occurs after any Sample Preparation (if specified).

Default Value: Automatic

Pattern Description: True or False.

Programmatic Pattern: BooleanP | Automatic

Index Matches to: experiment samples

AliquotAmount

The amount of a sample that should be transferred from the input samples into aliquots.

Default Value: Automatic

Default Calculation: Automatically set as the smaller between the current sample volume and the maximum volume of the destination container if a liquid, or the current Mass or Count if a solid or counted item, respectively.

Pattern Description: All or Count or Count or Mass or Volume or Null.

Programmatic Pattern: ((RangeP[1*Microliter, 20*Liter] | RangeP[1*Milligram, 20*Kilogram] | GreaterP[0*Unit, 1*Unit] | GreaterP[0., 1.] | All) | Automatic) | Null

Index Matches to: experiment samples

TargetConcentration

The desired final concentration of analyte in the AliquotSamples after dilution of aliquots of SamplesIn with the ConcentratedBuffer and BufferDiluent which should be used in lieu of the SamplesIn for the experiment.

Default Value: Automatic

Default Calculation: Automatically calculated based on aliquot and buffer volumes.

Pattern Description: Greater than 0 molar or greater than 0 grams per liter or Null.

Programmatic Pattern: ((GreaterP[0*Molar] | GreaterP[0*(Gram/Liter)]) | Automatic) | Null

Index Matches to: experiment samples

TargetConcentrationAnalyte

The substance whose final concentration is attained with the TargetConcentration option.

Default Value: Automatic

Default Calculation: Automatically set to the first value in the Analytes field of the input sample, or, if not populated, to the first analyte in the Composition field of the input sample, or if none exist, the first identity model of any kind in the Composition field.

Pattern Description: An object of type or subtype Model[Molecule], Model[Molecule, cDNA], Model[Molecule, Oligomer], Model[Molecule, Transcript], Model[Molecule, Protein], Model[Molecule, Protein, Antibody], Model[Molecule, Carbohydrate], Model[Molecule, Polymer], Model[Resin], Model[Resin, SolidPhaseSupport], Model[Lysate], Model[ProprietaryFormulation], Model[Virus], Model[Cell], Model[Cell, Mammalian], Model[Cell, Bacteria], Model[Cell, Yeast], Model[Tissue], Model[Material], or Model[Species] or Null.

Programmatic Pattern: (ObjectP[IdentityModelTypes] | Automatic) | Null

Index Matches to: experiment samples

AssayVolume

The desired total volume of the aliquoted sample plus dilution buffer.

Default Value: Automatic

Default Calculation: Automatically determined based on Volume and TargetConcentration option values.

Pattern Description: Greater than or equal to 1 microliter and less than or equal to 20 liters or Null.

Programmatic Pattern: (RangeP[1*Microliter, 20*Liter] | Automatic) | Null

Index Matches to: experiment samples

ConcentratedBuffer

The concentrated buffer which should be diluted by the BufferDilutionFactor in the final solution (i.e., the combination of the sample, ConcentratedBuffer, and BufferDiluent). The ConcentratedBuffer and BufferDiluent will be combined and then mixed with the sample, where the combined volume of these buffers is the difference between the AliquotAmount and the total AssayVolume.

Default Value: Automatic

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

BufferDilutionFactor

The dilution factor by which the concentrated buffer should be diluted in the final solution (i.e., the combination of the sample, ConcentratedBuffer, and BufferDiluent). The ConcentratedBuffer and BufferDiluent will be combined and then mixed with the sample, where the combined volume of these buffers is the difference between the AliquotAmount and the total AssayVolume.

Default Value: Automatic

Default Calculation: If ConcentratedBuffer is specified, automatically set to the ConcentratedBufferDilutionFactor of that sample; otherwise, set to Null.

Pattern Description: Greater than or equal to 1 or Null.

Programmatic Pattern: (GreaterEqualP[1] | Automatic) | Null

Index Matches to: experiment samples

BufferDiluent

The buffer used to dilute the aliquot sample such that ConcentratedBuffer is diluted by BufferDilutionFactor in the final solution. The ConcentratedBuffer and BufferDiluent will be combined and then mixed with the sample, where the combined volume of these buffers is the difference between the AliquotAmount and the total AssayVolume.

Default Value: Automatic

Default Calculation: Automatically resolves to Model[Sample, "Milli-Q water"] if ConcentratedBuffer is specified; otherwise, resolves to Null.

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

AssayBuffer

The buffer that should be added to any aliquots requiring dilution, where the volume of this buffer added is the difference between the AliquotAmount and the total AssayVolume.

Default Value: Automatic

Default Calculation: Automatically resolves to Model[Sample, "Milli-Q water"] if ConcentratedBuffer is not specified; otherwise, resolves to Null.

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

AliquotSampleStorageCondition

The non-default conditions under which any aliquot samples generated by this experiment should be stored after the protocol is completed.

Default Value: Automatic

Pattern Description: {AmbientStorage, Refrigerator, Freezer, DeepFreezer, CryogenicStorage, YeastIncubation, YeastShakingIncubation, BacterialIncubation, BacterialShakingIncubation, MammalianIncubation, ViralIncubation, CrystalIncubation, AcceleratedTesting, IntermediateTesting, LongTermTesting, UVVisLightTesting} or Disposal or Null.

Programmatic Pattern: ((SampleStorageTypeP | Disposal) | Automatic) | Null

Index Matches to: experiment samples

DestinationWell

The desired position in the corresponding AliquotContainer in which the aliquot samples will be placed.

Default Value: Automatic

Default Calculation: Automatically resolves to A1 in containers with only one position. For plates, fills wells in the order provided by the function AllWells.

Pattern Description: Any well from A1 to H12 or list of one or more any well from A1 to H12 or any well from A1 to H12 entries or Null.

Programmatic Pattern: ((WellPositionP | {((Automatic | Null) | WellPositionP)..}) | Automatic) | Null

AliquotContainer

The desired type of container that should be used to prepare and house the aliquot samples, with indices indicating grouping of samples in the same plates, if desired. This option will resolve to be the length of the SamplesIn * NumberOfReplicates.

Default Value: Automatic

Default Calculation: Automatically set as the PreferredContainer for the AssayVolume of the sample. For plates, attempts to fill all wells of a single plate with the same model before aliquoting into the next.

Pattern Description: An object of type or subtype Model[Container] or Object[Container] or a prepared sample or Automatic or Null or {Index, Container} or list of one or more an object of type or subtype Model[Container] or Object[Container] or a prepared sample or Automatic or Null entries or list of one or more Automatic or Null or {Index, Container} entries.

Programmatic Pattern: (((ObjectP[{Model[Container], Object[Container]}] | _String) | (Automatic | Null) | {GreaterEqualP[1, 1] | (Automatic | Null), (ObjectP[{Model[Container], Object[Container]}] | _String) | (Automatic | Null)} | {((ObjectP[{Model[Container], Object[Container]}] | _String) | (Automatic | Null))..} | {({GreaterEqualP[1, 1] | (Automatic | Null), (ObjectP[{Model[Container], Object[Container]}] | _String) | (Automatic | Null)} | (Automatic | Null))..}) | Automatic) | Null

AliquotPreparation

Indicates the desired scale at which liquid handling used to generate aliquots will occur.

Default Value: Automatic

Default Calculation: Automatic resolution will occur based on manipulation volumes and container types.

Pattern Description: Manual or Robotic or Null.

Programmatic Pattern: (PreparationMethodP | Automatic) | Null

ConsolidateAliquots

Indicates if identical aliquots should be prepared in the same container/position.

Default Value: Automatic

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null



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



Example Results

A simple 1D NMR of glucose in D_2O

protocol = ExperimentNMR[

    Object[Sample,"id:qdkmxzkjOvWa"],

    Nucleus -> "1H",

    AcquisitionTime -> 4 Second,

    NumberOfScans -> 16,

    DeuteratedSolvent -> Water,

    SampleAmounts -> 5 Milligram,

    SolventVolumes -> 700 Microliter

]

The results of this protocol reveal a clean spectrum with sharp peaks

data = Download[Object[Protocol, NMR, "id:dORYzZRj664R"], Data]

PlotNMR[data, PlotRange -> {{2.5 , 7.5}, Automatic}]

Multiple spectra with different parameters can be performed on the same sample, including different nuclei

Note that the DeuteratedSolvent must be specified; otherwise, it will default to Deuterium Oxide, which may not be the desired solvent.

Download[{Object[Sample, "id:n0k9mG80j7p1"],

  Object[Sample, "id:n0k9mG80j7p1"]}, Model]

protocol = ExperimentNMR[

    {Object[Sample,"id:n0k9mG80j7p1"], Object[Sample,"id:n0k9mG80j7p1"]},

    Nucleus -> {"1H", "13C"},

    NumberOfScans -> {64, 2048},

    DeuteratedSolvent -> Chloroform

]

ConfirmProtocol[protocol]

Download[Object[Protocol, NMR, "id:1ZA60vA1k75q"], Data]

AnalyzePeaks[Object[Data, NMR, "id:M8n3rxnbbp5O"]]

AnalyzePeaks for this ^1H spectrum identifies the expected peaks for caffeine, the residual CDCl3 peak (~7.26 ppm), and evidence of trace water (~1.6 ppm)

PlotNMR@Object[Data, NMR, "id:M8n3rxnbbp5O"]

For ^(13)C spectra, thresholds may need to be specified manually because signal is intrinscally much lower and peaks are extremely sharp.

AnalyzePeaks[Object[Data, NMR, "id:WNa4Zjanne5E"],

 WidthThreshold -> 0.01, RelativeThreshold -> 100000,

 AbsoluteThreshold -> 100000]

PlotNMR[Object[Data, NMR, "id:WNa4Zjanne5E"]]



Example Calls

Specify the nucleus of interest. Currently 1H, 13C, 19F, and 31P are supported.

To control which nucleus is read during the experiment, specify the Nucleus option:

ExperimentNMR[mySamples, Nucleus -> "13C"]

To set more than one nucleus for a single sample, list that sample multiple times:

ExperimentNMR[{mySample1, mySample1, mySample1, mySample2},

 	Nucleus -> {"1H", "13C", "19F", "1H"}

 ]

Acquisition parameters

Specific acquisition parameters may be provided:

ExperimentNMR[mySamples,

 	NumberOfScans -> 250,

 	AcquisitionTime -> (5 * Second),

 	PulseWidth -> (15 * Microsecond),

 	SpectralDomain -> Span[-10 * PPM, 20 * PPM]

 ]

Sample handling

Specify how the NMR sample ought to be prepared, including how much sample to use, how much solvent to use, and what solvent to use:

ExperimentNMR[mySamples,

 	SampleAmount -> (10 * Milligram),

 	DeuteratedSolvent -> Water,

 	SolventVolume -> (425 * Microliter)

 ]

Specify the temperature at which the sample should be kept prior to and during data collection:

Copy to clipboard.

ExperimentNMR[mySamples, SampleTemperature -> (40 * Celsius)]



Data Processing

Plot a sample one-dimensional spectrum:

PlotNMR[Object[Data, NMR, "id:P5ZnEjd6DmLL"]]

Pick peaks of a spectrum using AnalyzePeaks:

AnalyzePeaks[Object[Data, NMR, "id:P5ZnEjd6DmLL"]];

PlotNMR[Object[Data, NMR, "id:P5ZnEjd6DmLL"]]

Automatically identify peak splittings in NMR data:

PlotNMR[

 	Object[Data, NMR, "2pentanone NMR data for unit testing"],

 	Peaks ->

  AnalyzePeaks[

   Object[Data, NMR, "2pentanone NMR data for unit testing"]],

 	PlotRange -> {{-0.5, 3.}, Automatic}

 ]

Provide a molecule or molecule(s) in KnownSpecies to automatially assign peaks to atoms in each molecule:

PlotNMR[

 	Object[Data, NMR, "2pentanone NMR data for unit testing"],

 	Peaks -> AnalyzePeaks[

   		Object[Data, NMR, "2pentanone NMR data for unit testing"],

   		KnownSpecies -> {Molecule["CCCC(C)=O"]}

   	],

 	PlotRange -> {{-0.5, 5.}, Automatic}

 ]

Override the automatic assignment of Peak Group 3 as a sextet by explicitly setting it as a generic multiplet:

PlotNMR[

 	Object[Data, NMR, "2pentanone NMR data for unit testing"],

 	Peaks -> AnalyzePeaks[

   		Object[Data, NMR, "2pentanone NMR data for unit testing"],

   		PeakGroupMultiplicity -> {"Singlet (s)", "Triplet (t)",

     "Multiplet (m)", "Singlet (s)", "Triplet (t)"}

   	],

 	PlotRange -> {{-0.5, 3.}, Automatic}

 ]



Possible Issues

Sample too concentrated

If too much sample is dissolved in too little solvent, the instrument may have a hard time locking onto the solvent's deuterium signal. This may cause substantial tailing in peaks.

Volume too small

If SolventVolume is set too low, the instrument may have trouble shimming. The resulting spectrum may show peak tailing and lower resolution. Recommended SolventVolume is at least 700 μL.

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

You are working on a research project to use machine learning for drug discovery. Your goals are the following: (1) the project must have high clinical value, meaning the research contributes to helping patients, (2) the project must include a scientifically impactful application of machine learning to drug discovery, and (3) the project must use Emerald Cloud Labs (ECL) for all experimental validation with a 3-month limit on experiments. Your team previously decided to pursue peptide-based therapeutics. You previously designed experimental protocols for synthesis and validation of peptides that are designed to bind to a given protein drug target. Now you must implement one of these protocols using ECL. Please implement the ExperimentNMR protocol using the appropriate commands and syntax from ECL, writing out the experiment in the form ExperimentNMR[inputs] where you fill in "inputs" with the appropriate inputs. Please refer to the ECL documentation that is provided as context with example function calls and the full set of options for the experiment. In general, leave most options at their default values and therefore do not include them in your experiment function call. Only specify options that must be changed from their default value for your specific experiment. For every option that you specify, please state the default value, the different value you chose, and why you chose that value instead of the default.

Medicinal Chemist, please provide your response to the agenda.

## Medicinal Chemist

To implement the `ExperimentNMR` protocol using Emerald Cloud Labs (ECL), we need to carefully select and specify the necessary parameters for our peptide-based therapeutic validation. Based on the context and previous discussions, here is how we can set up the experiment:

### ExperimentNMR Protocol Implementation

#### Inputs and Parameters

1. **Sample**: The peptide sample that needs to be validated. This will be the primary input for the NMR experiment.

2. **Nucleus**: 
   - **Default Value**: `1H`
   - **Chosen Value**: `1H`
   - **Reason**: Proton NMR is typically used for structural validation of peptides due to its sensitivity and the abundance of hydrogen atoms in organic molecules.

3. **DeuteratedSolvent**:
   - **Default Value**: `Deuterium oxide`
   - **Chosen Value**: `DMSO-d6`
   - **Reason**: DMSO-d6 is often used for peptides as it provides good solubility and a clear spectral window for proton NMR.

4. **SampleAmount**:
   - **Default Value**: `Automatic`
   - **Chosen Value**: `5 Milligram`
   - **Reason**: A specific amount is chosen to ensure sufficient concentration for NMR detection without overloading the spectrometer.

5. **SolventVolume**:
   - **Default Value**: `Automatic`
   - **Chosen Value**: `700 Microliter`
   - **Reason**: Ensures optimal shimming and resolution of the NMR spectrum, as recommended for NMR experiments.

6. **AcquisitionTime**:
   - **Default Value**: `4 Second` for `1H`
   - **Chosen Value**: `4 Second`
   - **Reason**: This is sufficient for capturing the necessary data for proton NMR.

7. **NumberOfScans**:
   - **Default Value**: `16` for `1H`
   - **Chosen Value**: `16`
   - **Reason**: Provides a good balance between signal-to-noise ratio and experiment time.

#### Experiment Function Call

```plaintext
ExperimentNMR[
    Object[Sample, "id:yourSampleID"],
    Nucleus -> "1H",
    DeuteratedSolvent -> DMSO-d6,
    SampleAmount -> 5 Milligram,
    SolventVolume -> 700 Microliter
]
```

### Explanation

- **Sample**: Replace `"id:yourSampleID"` with the actual ID of your peptide sample in ECL.
- **Nucleus**: We are using `1H` NMR to analyze the peptide structure.
- **DeuteratedSolvent**: DMSO-d6 is chosen for its solubility properties and compatibility with peptide samples.
- **SampleAmount** and **SolventVolume**: These are specified to ensure optimal conditions for NMR analysis, avoiding issues like peak tailing or poor resolution.

### Conclusion

This setup ensures that the NMR experiment is tailored to the specific needs of peptide validation, providing reliable data for structural confirmation. By using ECL, we can efficiently manage and execute this protocol within the 3-month experimental limit, contributing to the project's goals of high clinical value and impactful scientific application.

