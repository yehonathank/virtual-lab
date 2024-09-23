## User

This is the beginning of an individual meeting with Medicinal Chemist to discuss your research project.

Here is context for this meeting:

[begin context 1]

ExperimentFluorescencePolarization[Samples]⟹Protocol

generates a Protocol for measuring fluorescence polarization of the provided Samples.



Fluorescence Polarization (FP) assesses the fraction of tracer bound to receptor by measuring the the molecular rotation of a fluorophore. The principle of FP is that a fluorophore excited by polarized light emits light oriented in a parallel plane. After a fluorescent molecule absorbs excitation light, it tumbles and rotates in solution during the time between excitation and emission. If the molecule is large, it rotates slowly, and the emission light remains largely polarized. Whereas a small, rapidly tumbling molecule rotates quickly and emits depolarized light. Measuring the degree of polarization provides a measure of the fraction of tracer bound to receptor, with applications in receptor-ligand binding, enzymatic degradation, and DNA hybridization studies.



Experimental Principles

Figure 1.1: Procedural overview of a Fluorescence Polarization experiment. Step 1: Samples are prepared in a reader-compatible shallow well plate. Step 2: Injection lines are cleaned and primed. Step 3: The assay plate is optionally held at a specified temperature. Step 4: Injection samples are dispensed into the assay plate. Step 5: The assay plate is shaken. Step 6: The plate reader excites samples with horizontally polarized light and measures emitted light in the horizontal and vertical planes. Large molecules rotate slower than small molecules and reflect more polarized light. Step 7: Optionally follow-up analysis, such as standard curve fitting, can be performed.



Instrumentation

PHERAstar FS

Model[Instrument, PlateReader, "id:01G6nvkKr3o7"]

Figure 2.1.1: The PHERAstar uses optic modules to package excitation and emission filters into a single package. This means wavelength combinations are restricted to those which already exist in the optic module. Up to five excitation/emission pairs can be recorded in a single experiment. Additionally, the PHERAstar supports dual emission so it's possible to record emission data at 2 different wavelengths simultaneously. The plate chamber can be heated up to 45°C and it can mix the plate at up to 700 RPM before and/or during the run. The reader has two 300μL syringe pump injectors which can be used for 0.5 - 300 μL injections of two unique samples at up to four time points during the run. There are two primary kinetics read modes. It can perform all readings, injections and mixing for a single well before moving onto the next well or it can read in cycles, reading all the assay wells in the plate again and again until the RunTime has been reached. The second mode is recommended for most assays, except those that use very fast kinetics.



Experiment Options

Optics

ExcitationWavelength

The wavelength(s) which should be used to excite fluorescence in the samples.

Default Value: Automatic

Pattern Description: Greater than or equal to 320 nanometers and less than or equal to 740 nanometers.

Programmatic Pattern: RangeP[320*Nanometer, 740*Nanometer] | Automatic

Index Matches to: ExcitationWavelength

EmissionWavelength

The wavelength(s) at which fluorescence emitted from the sample should be measured.

Default Value: Automatic

Pattern Description: Greater than or equal to 320 nanometers and less than or equal to 740 nanometers.

Programmatic Pattern: RangeP[320*Nanometer, 740*Nanometer] | Automatic

Index Matches to: ExcitationWavelength

DualEmissionWavelength

The wavelength at which fluorescence emitted from the sample should be measured with the secondary detector (simultaneous to the measurement at the emission wavelength done by the primary detector).

Default Value: Automatic

Pattern Description: Greater than or equal to 320 nanometers and less than or equal to 740 nanometers or Null.

Programmatic Pattern: (RangeP[320*Nanometer, 740*Nanometer] | Automatic) | Null

Index Matches to: ExcitationWavelength

Instrument

The plate reader used to measure fluorescence intensity.

Default Value: Automatic

Pattern Description: An object of type or subtype Model[Instrument, PlateReader] or Object[Instrument, PlateReader]

Programmatic Pattern: ObjectP[{Model[Instrument, PlateReader], Object[Instrument, PlateReader]}] | Automatic

General

Gain

The gain which should be applied to the signal reaching the primary detector. This may be specified either as a direct voltage, or as a percentage (which indicates that the gain should be set such that the AdjustmentSample fluoresces at that percentage of the instrument's dynamic range).

Default Value: Automatic

Default Calculation: If unspecified defaults to 90% if an adjustment sample is provided or if the instrument can scan the entire plate to determine gain. Otherwise defaults to 2500 Microvolt

Pattern Description: Greater than or equal to 1 microvolt and less than or equal to 4095 microvolts or greater than or equal to 1 percent and less than or equal to 95 percent.

Programmatic Pattern: (RangeP[1*Percent, 95*Percent] | RangeP[1*Microvolt, 4095*Microvolt]) | Automatic

Index Matches to: ExcitationWavelength

DualEmissionGain

The gain to apply to the signal reaching the secondary detector. This may be specified either as a direct voltage, or as a percentage relative to the AdjustmentSample option.

Default Value: Automatic

Pattern Description: Greater than or equal to 1 microvolt and less than or equal to 4095 microvolts or greater than or equal to 1 percent and less than or equal to 95 percent or Null.

Programmatic Pattern: ((RangeP[1*Percent, 95*Percent] | RangeP[1*Microvolt, 4095*Microvolt]) | Automatic) | Null

Index Matches to: ExcitationWavelength

AdjustmentSample

The sample which should be used to perform automatic adjustments of gain and/or focal height values at run time. The focal height will be set so that the highest signal-to-noise ratio can be achieved for the AdjustmentSample. The gain will be set such that the AdjustmentSample fluoresces at the specified percentage of the instrument's dynamic range. When multiple aliquots of the same sample is used in the experiment, an index can be specified to use the desired aliquot for adjustments.

Default Value: Automatic

Pattern Description: An object of type or subtype Object[Sample] or a prepared sample or {Index, Sample} or Null.

Programmatic Pattern: (((ObjectP[Object[Sample]] | _String) | {RangeP[1, 384, 1], ObjectP[Object[Sample]] | _String}) | Automatic) | Null

TargetPolarization

The target polarization value which should be used to perform automatic adjustments of gain and/or focal height values at run time on the chosen adjustment sample.

Default Value: Automatic

Pattern Description: Greater than or equal to 0 PolarizationUnits and less than or equal to 500 PolarizationUnits.

Programmatic Pattern: RangeP[0*PolarizationUnit, 500*PolarizationUnit] | Automatic

RetainCover

Indicates if the plate seal or lid on the assay container should not be taken off during measurement to decrease evaporation. When this option is set to True, injections cannot be performed as it's not possible to inject samples through the cover.

Default Value: False

Pattern Description: True or False.

Programmatic Pattern: BooleanP

ReadLocation

Indicates if fluorescence should be measured using an optic above the plate or one below the plate.

Default Value: Automatic

Default Calculation: Defaults to Bottom if RetainCover is set to True, otherwise defaults to Top.

Pattern Description: Top or Bottom.

Programmatic Pattern: ReadLocationP | Automatic

Temperature

The temperature at which the experiment will be performed, if using a plate reader with temperature incubation controls.

Default Value: Ambient

Pattern Description: Ambient or greater than or equal to 25 degrees Celsius and less than or equal to 45 degrees Celsius.

Programmatic Pattern: RangeP[$AmbientTemperature, 45*Celsius] | Ambient

EquilibrationTime

The length of time for which the assay plates should equilibrate at the assay temperature in the plate reader before being read.

Default Value: Automatic

Default Calculation: Defaults to 0 Second if Temperature is set to Ambient. Otherwise defaults to 5 Minute.

Pattern Description: Greater than or equal to 0 minutes and less than or equal to 1 hour.

Programmatic Pattern: RangeP[0*Minute, 1*Hour] | Automatic

NumberOfReadings

Number of redundant readings which should be taken by the detector to determine a single averaged fluorescence intensity reading.

Default Value: 100

Pattern Description: Greater than or equal to 1 and less than or equal to 200.

Programmatic Pattern: RangeP[1, 200]

FocalHeight

The distance from the bottom of the plate carrier to the focal point. If set to Automatic, the focal height will be adjusted based on the Gain adjustment, which will occur only if the gain values are set to percentages.

Default Value: Automatic

Pattern Description: Auto or greater than or equal to 0 millimeters and less than or equal to 25 millimeters or Null.

Programmatic Pattern: ((RangeP[0*Millimeter, 25*Millimeter] | Auto) | Automatic) | Null

WorkCell

Indicates the work cell that this primitive will be run on if Preparation->Robotic.

Default Value: Automatic

Default Calculation: Automatically set to STAR if Preparation->Robotic.

Pattern Description: STAR, bioSTAR, microbioSTAR, or qPix or Null.

Programmatic Pattern: (WorkCellP | Automatic) | Null

Preparation

Indicates if this unit operation is carried out primarily robotically or manually. Manual unit operations are executed by a laboratory operator and robotic unit operations are executed by a liquid handling work cell.

Default Value: Automatic

Pattern Description: Manual or Robotic.

Programmatic Pattern: PreparationMethodP | Automatic

NumberOfReplicates

Number of times each of the input samples should be analyzed using identical experimental parameters.

Default Value: Null

Pattern Description: Greater than or equal to 2 in increments of 1 or Null.

Programmatic Pattern: GreaterEqualP[2, 1] | Null

Sample Handling

MoatSize

Indicates the number of concentric perimeters of wells which should be should be filled with MoatBuffer in order to decrease evaporation from the assay samples during the run.

Figure 3.1: Use the moat options, MoatBuffer, MoatVolume and MoatSize to create an outer ring of wells filled with buffer. This has been shown to decrease evaporation during long reads.

Default Value: Automatic

Pattern Description: Greater than 0 in increments of 1 or Null.

Programmatic Pattern: (GreaterP[0, 1] | Automatic) | Null

MoatVolume

Indicates the volume which should be added to each moat well.

Default Value: Automatic

Pattern Description: Greater than 0 microliters or Null.

Programmatic Pattern: (GreaterP[0*Microliter] | Automatic) | Null

MoatBuffer

Indicates the buffer which should be used to fill each moat well.

Default Value: Automatic

Pattern Description: An object of type or subtype Object[Sample] or Model[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Object[Sample], Model[Sample]}] | _String) | Automatic) | Null

PrimaryInjectionSample

The sample to be injected in the first round of injections in order to introduce a time sensitive reagent/sample into the plate before/during fluorescence measurement.

Default Value: Null

Pattern Description: An object of type or subtype Object[Sample] or Model[Sample] or a prepared sample or Null.

Programmatic Pattern: (ObjectP[{Object[Sample], Model[Sample]}] | _String) | Null

Index Matches to: experiment samples

SecondaryInjectionSample

The sample to be injected in the second round of injections.

Default Value: Null

Pattern Description: An object of type or subtype Object[Sample] or Model[Sample] or a prepared sample or Null.

Programmatic Pattern: (ObjectP[{Object[Sample], Model[Sample]}] | _String) | Null

Index Matches to: experiment samples

PrimaryInjectionVolume

The amount of the primary sample which should be injected in the first round of injections.

Default Value: Null

Pattern Description: Greater than or equal to 0.5 microliters and less than or equal to 300 microliters or Null.

Programmatic Pattern: RangeP[0.5*Microliter, 300*Microliter] | Null

Index Matches to: experiment samples

SecondaryInjectionVolume

The amount of the secondary sample which should be injected in the second round of injections.

Default Value: Null

Pattern Description: Greater than or equal to 0.5 microliters and less than or equal to 300 microliters or Null.

Programmatic Pattern: RangeP[0.5*Microliter, 300*Microliter] | Null

Index Matches to: experiment samples

PrimaryInjectionFlowRate

The speed at which to transfer injection samples into the assay plate in the first round of injections.

Default Value: Automatic

Default Calculation: Defaults to 300 Microliter/Second if primary injections are specified.

Pattern Description: 430 microliters per second, 400 microliters per second, 350 microliters per second, 300 microliters per second, 260 microliters per second, 220 microliters per second, 190 microliters per second, 170 microliters per second, 150 microliters per second, 135 microliters per second, 115 microliters per second, 100 microliters per second, 85 microliters per second, 65 microliters per second, or 50 microliters per second or Null.

Programmatic Pattern: (BMGFlowRateP | Automatic) | Null

SecondaryInjectionFlowRate

The speed at which to transfer injection samples into the assay plate in the second round of injections.

Default Value: Automatic

Default Calculation: Defaults to 300 Microliter/Second if secondary injections are specified.

Pattern Description: 430 microliters per second, 400 microliters per second, 350 microliters per second, 300 microliters per second, 260 microliters per second, 220 microliters per second, 190 microliters per second, 170 microliters per second, 150 microliters per second, 135 microliters per second, 115 microliters per second, 100 microliters per second, 85 microliters per second, 65 microliters per second, or 50 microliters per second or Null.

Programmatic Pattern: (BMGFlowRateP | Automatic) | Null

PlateReaderMix

Indicates if samples should be mixed inside the plate reader chamber.

Default Value: Automatic

Default Calculation: Automatically set to True if any other plate reader mix options are specified.

Pattern Description: True or False.

Programmatic Pattern: BooleanP | Automatic

PlateReaderMixTime

The amount of time samples should be mixed inside the plate reader chamber.

Default Value: Automatic

Default Calculation: Automatically set to 30 second if any other plate reader mix options are specified.

Pattern Description: Greater than or equal to 1 second and less than or equal to 1 hour or Null.

Programmatic Pattern: (RangeP[1*Second, 1*Hour] | Automatic) | Null

PlateReaderMixRate

The rate at which the plate should be agitated inside the plate reader chamber.

Default Value: Automatic

Default Calculation: Automatically set to 700 RPM if any other plate reader mix options are specified.

Pattern Description: Greater than or equal to 100 revolutions per minute and less than or equal to 700 revolutions per minute or Null.

Programmatic Pattern: (RangeP[100*RPM, 700*RPM] | Automatic) | Null

PlateReaderMixMode

The pattern of motion which should be employed to shake the plate.

Default Value: Automatic

Default Calculation: Automatically set to DoubleOrbital if any other plate reader mix options are specified.

Pattern Description: Orbital, DoubleOrbital, or Linear or Null.

Programmatic Pattern: (MechanicalShakingP | Automatic) | Null

ReadDirection

Indicates the order in which wells should be read by specifying the plate path the instrument should follow when measuring fluorescence.

Figure 3.2: Use the ReadDirection option to control how the plate reader scans the plate during each read cycle. Choosing a more efficient path will lead to a shorter DetectionInterval. Also note that you may want to consider dripping injectors if you're working with low viscosity injection samples.

Default Value: Row

Pattern Description: Row, Column, SerpentineRow, or SerpentineColumn.

Programmatic Pattern: ReadDirectionP

InjectionSampleStorageCondition

The non-default conditions under which any injection samples used by this experiment should be stored after the protocol is completed.

Default Value: Null

Pattern Description: {AmbientStorage, Refrigerator, Freezer, DeepFreezer, CryogenicStorage, YeastIncubation, BacteriaIncubation, MammalianIncubation, TissueCultureCellsIncubation, MicrobialCellsIncubation, MicrobialCellsShakingIncubation, YeastCellsIncubation, YeastCellsShakingIncubation, ViralIncubation, AcceleratedTesting, IntermediateTesting, LongTermTesting, UVVisLightTesting} or Disposal or Null.

Programmatic Pattern: (SampleStorageTypeP | Disposal) | Null

Sampling

SamplingPattern

Indicates where in the well measurements are taken.

Default Value: Automatic

Pattern Description: Matrix, Spiral, Ring, or Center.

Programmatic Pattern: PlateReaderSamplingP | Automatic

SamplingDistance

Indicates the length of the region over which sampling measurements are taken.

Default Value: Automatic

Default Calculation: Automatically resolves to Null if SamplingPattern is set to Center otherwise resolves to 80% of the diameter of the well.

Pattern Description: Greater than or equal to 1 millimeter and less than or equal to 6 millimeters or Null.

Programmatic Pattern: (RangeP[1*Millimeter, 6*Millimeter] | Automatic) | Null

SamplingDimension

Specifies the size of the grid used for Matrix sampling. For example SamplingDimension->5 will scan a 5 x 5 grid.

Default Value: Automatic

Default Calculation: If the SamplingPattern is set to Matrix, SamplingDimension will be set to 3.

Pattern Description: Greater than or equal to 2 and less than or equal to 30 or Null.

Programmatic Pattern: (RangeP[2, 30] | Automatic) | Null

Post Experiment

SamplesInStorageCondition

The non-default conditions under which the SamplesIn of this experiment should be stored after the protocol is completed. If left unset, SamplesIn will be stored according to their current StorageCondition.

Default Value: Null

Pattern Description: {AmbientStorage, Refrigerator, Freezer, DeepFreezer, CryogenicStorage, YeastIncubation, BacteriaIncubation, MammalianIncubation, TissueCultureCellsIncubation, MicrobialCellsIncubation, MicrobialCellsShakingIncubation, YeastCellsIncubation, YeastCellsShakingIncubation, ViralIncubation, AcceleratedTesting, IntermediateTesting, LongTermTesting, UVVisLightTesting} or Disposal or Null.

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

Pattern Description: Cellulose, Cotton, Polyethylene, PTFE, Nylon, PES, PLUS, PVDF, GlassFiber, GHP, UHMWPE, EPDM, DuraporePVDF, GxF, ZebaDesaltingResin, NickelResin, Silica, or HLB or Null.

Programmatic Pattern: (FilterMembraneMaterialP | Automatic) | Null

Index Matches to: experiment samples

PrefilterMaterial

The material from which the prefilter filtration membrane should be made of to remove impurities from the SamplesIn prior to starting the experiment.

Default Value: Automatic

Default Calculation: By default, no prefiltration is performed on samples, even when Filter->True.

Pattern Description: Cellulose, Cotton, Polyethylene, PTFE, Nylon, PES, PLUS, PVDF, GlassFiber, GHP, UHMWPE, EPDM, DuraporePVDF, GxF, ZebaDesaltingResin, NickelResin, Silica, or HLB or Null.

Programmatic Pattern: (FilterMembraneMaterialP | Automatic) | Null

Index Matches to: experiment samples

FilterPoreSize

The pore size of the filter that should be used when removing impurities from the SamplesIn prior to starting the experiment.

Default Value: Automatic

Default Calculation: Resolves to an appropriate filter pore size for the given sample is Filtration is set to True.

Pattern Description: 0.008 micrometers, 0.1 micrometers, 0.22 micrometers, 0.45 micrometers, 1. micrometer, 1.1 micrometers, 2.5 micrometers, 6. micrometers, 20. micrometers, 30. micrometers, or 100. micrometers or Null.

Programmatic Pattern: (FilterSizeP | Automatic) | Null

Index Matches to: experiment samples

PrefilterPoreSize

The pore size of the filter; all particles larger than this should be removed during the filtration.

Default Value: Automatic

Default Calculation: By default, no prefiltration is performed on samples, even when Filter->True.

Pattern Description: 0.008 micrometers, 0.1 micrometers, 0.22 micrometers, 0.45 micrometers, 1. micrometer, 1.1 micrometers, 2.5 micrometers, 6. micrometers, 20. micrometers, 30. micrometers, or 100. micrometers or Null.

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

Default Calculation: If ConcentratedBuffer is specified, automatically set to the ConcentrationFactor of that sample; otherwise, set to Null.

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

Pattern Description: {AmbientStorage, Refrigerator, Freezer, DeepFreezer, CryogenicStorage, YeastIncubation, BacteriaIncubation, MammalianIncubation, TissueCultureCellsIncubation, MicrobialCellsIncubation, MicrobialCellsShakingIncubation, YeastCellsIncubation, YeastCellsShakingIncubation, ViralIncubation, AcceleratedTesting, IntermediateTesting, LongTermTesting, UVVisLightTesting} or Disposal or Null.

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

Pattern Description: An object of type or subtype Model[Container] or Object[Container] or a prepared sample or Automatic or Null or {Index, Container} or list of one or more an object of type or subtype Model[Container] or Object[Container] or a prepared sample or Automatic or Null entries or list of one or more Automatic or Null or {Index, Container} entries or Null.

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

Pattern Description: False or Null.

Programmatic Pattern: (False | Automatic) | Null



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

Excitation and Emission Wavelengths

Select a single excitation wavelength to excite the sample and one wavelength at which emitted light should be read:

ExperimentFluorescencePolarization[mySamples,

 	ExcitationWavelength -> (485 * Nanometer),

 	EmissionWavelength -> (520 * Nanometer)

 ]

Plate Reader Mixing

The assay plate can be mixed during readings by specifying any of the PlateReaderMix options:

ExperimentFluorescencePolarization[mySamples,

 	PlateReaderMix -> True,

 	PlateReaderMixTime -> (1 * Minute),

 	PlateReaderMixRate -> (700 * RPM)

 ]

Gain Setting

Gain can be set as a percentage of the maximum signal the reader can record:

ExperimentFluorescencePolarization[mySamples,

 PrimaryGain -> (50 * Percent)]

Alternatively directly specify the voltage to apply to the PMT. This is generally more helpful in repeat experiments. The gain can be taken from Object[Data, FluorescencePolarization][Gains]

ExperimentFluorescencePolarization[mySamples,

 PrimaryGain -> (2500 * Microvolt)]



Preferred Input Containers

The plate readers can read standard SBS shallow well plates.

The plate readers can inject samples from samples from 2mL, 15mL and 50 mL tubes while recording kinetic signal.



Possible Issues

Evaporation

During long runs evaporation can cause signal drift over time. Additionally using a high NumberOfReadings can lead to an initial hump while the PMT heats up.

Slow Injections

If the injection speed is not sufficient mixing may be inadequate.

Variable Detection Interval

The detection interval is determined by the instrument at run time. It depends on the number of wells being read, mixing parameters, the number of multichromatics, and the NumberOfReadings.

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

You are working on a research project to use machine learning for drug discovery. Your goals are the following: (1) the project must have high clinical value, meaning the research contributes to helping patients, (2) the project must include a scientifically impactful application of machine learning to drug discovery, and (3) the project must use Emerald Cloud Labs (ECL) for all experimental validation with a 3-month limit on experiments. Your team previously decided to pursue peptide-based therapeutics. You previously designed experimental protocols for synthesis and validation of peptides that are designed to bind to a given protein drug target. Now you must implement one of these protocols using ECL. Please implement the ExperimentFluorescencePolarization protocol using the appropriate commands and syntax from ECL, writing out the experiment in the form ExperimentFluorescencePolarization[inputs] where you fill in "inputs" with the appropriate inputs. Please refer to the ECL documentation that is provided as context with example function calls and the full set of options for the experiment. In general, leave most options at their default values and therefore do not include them in your experiment function call. Only specify options that must be changed from their default value for your specific experiment. For every option that you specify, please state the default value, the different value you chose, and why you chose that value instead of the default.

Medicinal Chemist, please provide your response to the agenda.

## Medicinal Chemist

To implement the `ExperimentFluorescencePolarization` protocol using Emerald Cloud Labs (ECL), we will focus on the specific requirements for our peptide-based therapeutics project. The goal is to measure the binding affinity of synthesized peptides to their target proteins using fluorescence polarization. Below is the experiment setup with specified options that deviate from their defaults, along with justifications for each choice.

### Experiment Setup

```plaintext
ExperimentFluorescencePolarization[
  myPeptideSamples,
  ExcitationWavelength -> (485 * Nanometer),
  EmissionWavelength -> (520 * Nanometer),
  PlateReaderMix -> True,
  PlateReaderMixTime -> (1 * Minute),
  PlateReaderMixRate -> (700 * RPM),
  NumberOfReplicates -> 3
]
```

### Specified Options and Justifications

1. **ExcitationWavelength**
   - **Default Value**: Automatic
   - **Chosen Value**: 485 nanometers
   - **Justification**: The chosen excitation wavelength of 485 nm is optimal for the fluorophore used in our peptide labeling, ensuring efficient excitation and maximizing the signal-to-noise ratio.

2. **EmissionWavelength**
   - **Default Value**: Automatic
   - **Chosen Value**: 520 nanometers
   - **Justification**: The emission wavelength of 520 nm corresponds to the emission peak of the fluorophore, allowing accurate measurement of fluorescence polarization.

3. **PlateReaderMix**
   - **Default Value**: Automatic
   - **Chosen Value**: True
   - **Justification**: Mixing is enabled to ensure homogeneity of the samples and prevent sedimentation, which could affect the accuracy of polarization measurements.

4. **PlateReaderMixTime**
   - **Default Value**: Automatic (30 seconds if other mix options are specified)
   - **Chosen Value**: 1 minute
   - **Justification**: Extended mixing time ensures thorough mixing, especially important for high-viscosity samples or those prone to aggregation.

5. **PlateReaderMixRate**
   - **Default Value**: Automatic (700 RPM if other mix options are specified)
   - **Chosen Value**: 700 RPM
   - **Justification**: The maximum mixing rate is selected to achieve rapid and effective mixing, minimizing the risk of sample settling during the experiment.

6. **NumberOfReplicates**
   - **Default Value**: Null
   - **Chosen Value**: 3
   - **Justification**: Conducting three replicates provides statistical robustness to the data, allowing for reliable assessment of binding interactions and reducing the impact of any outliers.

### Conclusion

This setup is designed to optimize the fluorescence polarization assay for our peptide samples, ensuring accurate and reproducible measurements. By specifying these options, we align the experiment with the specific needs of our project, leveraging ECL's capabilities to validate our peptide-based therapeutics effectively.

