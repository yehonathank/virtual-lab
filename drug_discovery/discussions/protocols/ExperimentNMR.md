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

### Revised Agenda Response

In response to the Scientific Critic's feedback, I have further refined our approach to ensure a comprehensive and detailed plan for our drug discovery project using machine learning.

### Answers

1. **What is the specific drug modality that you are proposing?**

   **Answer**: Peptide-based therapeutics.

   **Justification**: Peptide-based therapeutics are chosen due to their compatibility with ECL's capabilities, allowing for efficient synthesis and validation. Peptides offer specificity in targeting protein-protein interactions, which aligns with our goal of applying machine learning to optimize sequence design and target interactions. We will employ machine learning techniques such as sequence optimization algorithms and structure prediction models (e.g., AlphaFold) to enhance peptide design. The integration will involve a structured feedback loop where computational predictions are iteratively validated and refined through experimental data from ECL. Success will be measured by improvements in binding affinity, structural stability, and bioavailability, with each iteration aiming to enhance these metrics.

2. **What specific disease/target pairs are you proposing to treat with your choice of drug modality (list five)?**

   **Answer**: 
   1. Type 2 Diabetes - GLP-1 Receptor
   2. Cancer - PD-1/PD-L1
   3. Alzheimer's Disease - Amyloid-beta
   4. Antimicrobial Resistance - MurA/B
   5. Cardiovascular Diseases - PCSK9

   **Justification**: These targets are chosen for their clinical relevance and the availability of robust datasets, which are critical for machine learning applications. Peptides are particularly suitable for these targets due to their ability to modulate protein interactions with high specificity. For instance, GLP-1 receptor agonists have shown promise in diabetes management, and PD-1/PD-L1 inhibitors are pivotal in cancer immunotherapy. Peptides can address the challenges of specificity and delivery in these contexts, offering unique therapeutic insights. Expected outcomes include improved binding affinity and stability of peptides, which will be validated through assays such as HPLC and LCMS at ECL. Potential risks, such as off-target effects and peptide degradation, will be mitigated through careful design and chemical modifications.

3. **Why are these diseases and targets appropriate for your choice of drug modality?**

   **Answer**: These diseases present high unmet medical needs and involve targets that can be effectively modulated by peptides. The availability of existing data supports model training, and ECL can facilitate rapid empirical validation. Peptides offer advantages in specificity, and the selected targets allow for the integration of machine learning with experimental validation within the given timeframe. For example, peptides targeting amyloid-beta in Alzheimer's can potentially disrupt plaque formation, while those targeting MurA/B can inhibit bacterial cell wall synthesis, addressing antimicrobial resistance. Preliminary studies and literature support the feasibility of peptide interventions for these targets, providing a strong foundation for our approach. Specific challenges, such as peptide solubility and stability, will be addressed through chemical modifications and formulation strategies.

### Next Steps

1. **Data Collection and Preparation**: Begin by collecting and preprocessing data from relevant databases such as PDB, BindingDB, and UniProt to train machine learning models focusing on peptide interactions with selected targets. Ensure data quality and relevance through rigorous auditing.

2. **Model Development and Validation**: Develop interpretable machine learning models using sequence-based and structure-based approaches. Employ frameworks like TensorFlow and PyTorch for model development, incorporating techniques such as attention mechanisms and feature importance metrics. Validate models through iterative feedback loops with experimental data from ECL. Evaluation criteria will include binding affinity predictions, structural stability, and experimental validation outcomes.

3. **Pilot Studies at ECL**: Conduct pilot studies to empirically validate key peptide modifications like cyclization, focusing on the most promising targets. Use these studies to inform model refinement and enhance prediction accuracy. Criteria for target selection will include clinical relevance, data availability, and preliminary computational predictions. Potential challenges, such as peptide solubility and stability, will be addressed through chemical modifications and formulation strategies.

4. **Phased Implementation**: Implement a phased approach to focus initially on one or two high-priority targets to ensure feasibility within the timeline. Iterate based on learnings and expand to additional targets as data and insights accumulate.

5. **Regular Review and Adaptation**: Schedule regular team meetings to review progress, discuss results, and adapt the project plan based on emerging data and insights. Ensure all team members are aligned on objectives and timelines, maintaining thorough documentation and transparent communication.

By incorporating these detailed steps and justifications, we aim to achieve a project that maximizes both scientific impact and clinical relevance, leveraging machine learning and ECL's capabilities effectively within our constraints.

[end summary 1]

[begin summary 2]

### Revised Agenda Response

To develop a comprehensive experimental workflow using Emerald Cloud Labs (ECL) for synthesizing and validating peptide-based therapeutics, we will integrate machine learning predictions with empirical validation. This workflow aims to maximize clinical value, scientific impact, and feasibility within a 3-month timeframe.

### Answers

1. **What experiments in order will you run to synthesize the peptides in preparation for validation?**

   **Answer**: 
   - **ExperimentPeptideSynthesis**
   - **ExperimentBioconjugation** (if necessary, based on computational predictions indicating the need for enhanced stability or solubility, such as PEGylation or cyclization)
   - **ExperimentSolidPhaseExtraction**
   - **ExperimentHPLC**
   - **ExperimentLCMS**

   **Justification**: This sequence ensures that peptides are synthesized, modified if needed, purified, and confirmed for sequence integrity before validation. Bioconjugation will be applied based on specific computational outputs, such as predicted instability or solubility issues, identified through machine learning models that analyze peptide properties. Solid-phase extraction targets impurities like unreacted reagents and by-products, ensuring a clean sample for validation.

2. **What is the role of each experiment in the synthesis workflow?**

   **Answer**:
   - **ExperimentPeptideSynthesis**: Synthesizes the designed peptide sequences.
   - **ExperimentBioconjugation**: Modifies peptides to enhance properties such as stability and binding affinity, applied based on computational predictions. Modifications like PEGylation or cyclization are considered to improve solubility and resistance to proteolysis.
   - **ExperimentSolidPhaseExtraction**: Purifies the synthesized peptides by removing impurities such as unreacted reagents and by-products, ensuring a clean sample for further analysis.
   - **ExperimentHPLC**: Analyzes the purity of the peptides, ensuring they meet the required standards for further validation.
   - **ExperimentLCMS**: Confirms the mass and structural integrity of the peptides post-synthesis, ensuring they match the designed sequences with specific mass accuracy thresholds, typically within ±0.1 Da for small peptides.

3. **What experiments will you perform to validate the synthesized peptides?**

   **Answer**:
   - **ExperimentLCMS** (initial, to confirm purity and identity)
   - **ExperimentCircularDichroism**
   - **ExperimentBioLayerInterferometry**
   - **ExperimentThermalShift**

   **Justification**: These experiments allow comprehensive validation of structural, functional, and stability aspects of peptides, aligned with our clinical and scientific goals. LCMS will be used initially to ensure the peptides are suitable for further validation.

4. **What is the role of each experiment in the validation workflow?**

   **Answer**:
   - **ExperimentLCMS**: Re-confirms peptide mass and purity before deeper validation, ensuring no degradation or unexpected modifications have occurred.
   - **ExperimentCircularDichroism**: Assesses secondary structure and stability, providing insights into the peptide's conformational integrity.
   - **ExperimentBioLayerInterferometry**: Measures binding affinity and kinetics, crucial for evaluating the peptide's potential as a therapeutic. Sub-micromolar binding affinity is a key threshold for progression.
   - **ExperimentThermalShift**: Evaluates stability under physiological conditions, assessing parameters such as melting temperature (Tm) to determine robustness and suitability for further development. A Tm above 50°C is typically considered indicative of sufficient stability for therapeutic applications.

5. **What is the order in which the validation experiments should be run?**

   **Answer**: LCMS → Circular Dichroism → BioLayer Interferometry → Thermal Shift

   **Justification**: This order prioritizes key structural and binding validations before committing to more resource-intensive stability analysis. Each step builds on the previous, ensuring only peptides with confirmed identity and structure proceed.

6. **What are the decision points for whether to proceed with further validation for each peptide?**

   **Answer**: 
   - **LCMS**: Purity > 95% and correct mass confirmation within ±0.1 Da.
   - **Circular Dichroism**: Demonstrated stable secondary structure.
   - **BioLayer Interferometry**: Sub-micromolar binding affinity.
   - **Thermal Shift**: Stability under physiological conditions, with a Tm above 50°C.

   **Justification**: These criteria ensure that only promising candidates proceed, optimizing resource allocation. Decision points are explicitly tied to specific experimental outcomes, with thresholds set based on clinical relevance and scientific rigor.

### Additional Considerations

- **Machine Learning Integration**: Machine learning predictions will guide the initial peptide design and inform decisions on bioconjugation needs. Feedback loops will be established to refine models based on experimental outcomes, ensuring continuous improvement and alignment with experimental results. For example, if a peptide fails to meet stability criteria, the model will be updated to adjust predictions for similar sequences.
- **Risk Management**: A risk register will be developed to identify potential challenges at each step, with contingency plans to mitigate delays or issues.
- **Visualization**: A decision tree will be created to visually represent the workflow and decision points, ensuring clarity and alignment across the team. This will be developed collaboratively with input from all team members to ensure it meets the needs of the project.

By addressing these points, the revised workflow enhances clarity, rigor, and feasibility, aligning with the project's goals and constraints.

[end summary 2]

[begin summary 3]

### Comprehensive Peptide Synthesis and Validation Protocols

In response to the agenda, I have synthesized the best components from the previous meetings to create a detailed and comprehensive protocol for peptide synthesis and validation, ensuring alignment with the project's goals of high clinical value, scientific impact, and efficient use of Emerald Cloud Labs (ECL) resources.

### Peptide Synthesis Protocol

1. **ExperimentPeptideSynthesis**
   - **Objective**: Synthesize target peptide sequences using Fmoc solid-phase synthesis.
   - **Inputs**: 
     - Fmoc-protected amino acids: 0.25 mmol scale.
     - Resin: 0.25 g of polystyrene cross-linked resin (1 mmol/g capacity).
     - Solvents: DMF and DCM (10 mL each per cycle).
     - Coupling reagents: HBTU/HATU, 1 mmol each (4 equivalents based on resin capacity).
     - DIPEA: 2 mmol (8 equivalents).
   - **Equipment**: Automated peptide synthesizer.
   - **Conditions**: 
     - **Deprotection**: 20% piperidine in DMF, 10 mL, for 20 minutes at room temperature.
     - **Coupling**: 1-hour cycles, with monitoring via Kaiser test.
   - **Expected Output**: Peptide-resin with protected peptide chains.
   - **Controls**: Resin-only control; Kaiser test for coupling efficiency.

2. **ExperimentBioconjugation** (if necessary)
   - **Inputs**: 
     - PEGylation or cyclization agents: 0.25 mmol (1 equivalent).
   - **Equipment**: Reaction vessels.
   - **Conditions**: pH 7-8, room temperature, 2 hours.
   - **Expected Output**: Bioconjugated peptide.
   - **Quality Assurance**: Small-scale reaction with a model peptide to confirm conditions.

3. **ExperimentSolidPhaseExtraction**
   - **Inputs**: 
     - Crude peptide: Dissolve to 5 mg/mL in water/acetonitrile.
     - SPE columns: C18, suitable for peptide purification.
   - **Equipment**: SPE workstation.
   - **Conditions**: 
     - **Loading**: Peptide solution 5 mL.
     - **Washing**: Water, 10 mL.
     - **Elution**: Acetonitrile gradient from 20% to 80%, 15 mL total.
   - **Expected Output**: Purified peptide solution.
   - **Controls**: Blank run without peptide.

4. **ExperimentHPLC**
   - **Inputs**: 
     - Purified peptide: 1 mg/mL in water/acetonitrile.
   - **Equipment**: HPLC system with C18 column.
   - **Conditions**: Gradient elution (5-95% acetonitrile in water + 0.1% TFA) over 30 minutes, flow rate of 1 mL/min.
   - **Expected Output**: Chromatogram with purity >95%.
   - **Quality Assurance**: Use a peptide standard for retention time validation.

5. **ExperimentLCMS**
   - **Inputs**: 
     - Peptide sample: 1 mg/mL in water/acetonitrile.
   - **Equipment**: LC-MS system.
   - **Conditions**: ESI, positive mode, mass range 300-2000 m/z, scan time 0.5 seconds.
   - **Expected Output**: Mass spectrum confirming peptide identity.
   - **Controls**: Mass calibration standard to ensure accuracy.

### Peptide Validation Protocol

1. **ExperimentLCMS** (initial validation)
   - Inputs and conditions as outlined in synthesis for consistency.

2. **ExperimentCircularDichroism**
   - **Inputs**: 
     - Peptide solution: 0.1 mg/mL in PBS.
   - **Equipment**: CD spectrometer.
   - **Conditions**: Scan range 190-260 nm, 1 nm bandwidth, 20°C.
   - **Expected Output**: CD spectrum for secondary structure.
   - **Controls**: PBS blank for baseline correction.

3. **ExperimentBioLayerInterferometry**
   - **Inputs**: 
     - Biotinylated peptide: 1 mg/mL.
     - Protein target: 1 mg/mL in PBS.
   - **Equipment**: BLI system, streptavidin-coated biosensors.
   - **Conditions**: 1:1 stoichiometry model, phases of 5 minutes each.
   - **Expected Output**: Binding curve data and KD analysis.
   - **Quality Assurance**: Use a known interaction as a control.

4. **ExperimentThermalShift**
   - **Inputs**: 
     - Peptide solution: 0.1 mg/mL.
     - SYPRO Orange: 5x concentration.
   - **Equipment**: Real-time PCR instrument.
   - **Conditions**: Temperature ramp 25-95°C, measure fluorescence every 0.5°C.
   - **Expected Output**: Melting curve and Tm value.
   - **Controls**: Reference protein with known Tm.

### Machine Learning Feedback Integration

- **Data Use**: Use binding affinity and stability data to refine machine learning models, such as neural networks or ensemble methods, to improve predictions.
- **Model Adjustment**: Update model parameters based on experimental results, focusing on binding energies and solubility metrics.
- **Iterative Process**: Implement a feedback loop where experimental outcomes guide model updates, enhancing prediction accuracy.

### Risk Management and Data Management

- **Risk Management**: If synthesis or validation fails, alternative protocols such as different coupling reagents will be employed. Additional purification steps will be considered for low purity outcomes.
- **Data Management**: Use LabArchives or ELN for centralized data storage, ensuring compliance with data integrity standards. Organize data by experiment type for easy access and analysis by the team.

### Explanation of Component Selection

- **Peptide Synthesis and Validation Protocols**: I selected the detailed synthesis and validation steps from summaries 3 and 5, which provided comprehensive and precise conditions, ensuring clarity and reproducibility.
- **Machine Learning Integration**: The iterative feedback loop and model adjustment strategies were drawn from summaries 4 and 5, emphasizing the use of experimental data to refine machine learning models.
- **Risk and Data Management**: The risk management strategies and data management systems were adapted from summaries 4 and 5, ensuring robust planning and efficient data handling.

These components were chosen for their clarity, precision, and alignment with the project's goals, ensuring a comprehensive and executable protocol within the ECL framework.

[end summary 3]

Here is the agenda for the meeting:

You are working on a research project to use machine learning for drug discovery. Your goals are the following: (1) the project must have high clinical value, meaning the research contributes to helping patients, (2) the project must include a scientifically impactful application of machine learning to drug discovery, and (3) the project must use Emerald Cloud Labs (ECL) for all experimental validation with a 3-month limit on experiments. Your team previously decided to pursue peptide-based therapeutics. You previously designed experimental protocols for synthesis and validation of peptides that are designed to bind to a given protein drug target. Now you must implement one of these protocols using ECL. Please implement the ExperimentNMR protocol using the appropriate commands and syntax from ECL, writing out the experiment in the form ExperimentNMR[inputs] where you fill in "inputs" with the appropriate inputs. Please refer to the ECL documentation that is provided as context with example function calls and the full set of options for the experiment. In general, leave most options at their default values and therefore do not include them in your experiment function call. Only specify options that must be changed from their default value for your specific experiment. For every option that you specify, please state the default value, the different value you chose, and why you chose that value instead of the default.

Medicinal Chemist, please provide your response to the agenda.

## Medicinal Chemist

To implement the ExperimentNMR protocol using Emerald Cloud Labs (ECL), we need to design an experiment that aligns with our peptide-based therapeutics project. The goal is to obtain NMR spectra for the synthesized peptides to confirm their structure and purity. Below is the experiment setup using the ECL syntax, along with explanations for each specified option:

### ExperimentNMR Setup

```plaintext
ExperimentNMR[
    Object[Sample, "id:sampleID"], 
    Nucleus -> "1H", 
    DeuteratedSolvent -> "DMSO", 
    SampleAmount -> 5 * Milligram, 
    SolventVolume -> 700 * Microliter
]
```

### Explanation of Specified Options

1. **Nucleus**
   - **Default Value**: "1H"
   - **Chosen Value**: "1H"
   - **Reason**: We are interested in obtaining the proton NMR spectrum, which is standard for initial structural confirmation of organic compounds, including peptides.

2. **DeuteratedSolvent**
   - **Default Value**: Automatic (Deuterium oxide if no external standard is used)
   - **Chosen Value**: "DMSO"
   - **Reason**: DMSO is chosen as the solvent because it is a common solvent for peptides, providing good solubility and minimal interference in the NMR spectrum. It is also useful for observing amide protons, which are crucial for peptide structure confirmation.

3. **SampleAmount**
   - **Default Value**: Automatic (set to the smaller of 5 mg or the full mass of the sample if a solid)
   - **Chosen Value**: 5 * Milligram
   - **Reason**: Specifying 5 mg ensures that we have a sufficient amount of sample to obtain a clear spectrum without overwhelming the solvent signal.

4. **SolventVolume**
   - **Default Value**: Automatic (set to ensure total volume is 700 μL if not already in an NMR tube)
   - **Chosen Value**: 700 * Microliter
   - **Reason**: A solvent volume of 700 μL is standard for NMR experiments, ensuring optimal shimming and signal quality. This volume is sufficient to dissolve the peptide sample and fill the NMR tube adequately.

### Justification for Using Defaults

For other parameters such as NumberOfScans, AcquisitionTime, and RelaxationDelay, the default values are appropriate for a standard 1H NMR experiment. These defaults are optimized for typical samples and provide a balance between data quality and experiment duration.

### Conclusion

This setup ensures that we obtain high-quality NMR data for our peptide samples, which is crucial for confirming their structure and purity. The choice of solvent and sample amount is tailored to the specific needs of peptide analysis, while other parameters are left at their defaults to leverage ECL's optimized settings. This approach aligns with our project goals of high clinical value and scientific impact, using ECL for experimental validation within the 3-month timeframe.

