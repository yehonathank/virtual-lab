## User

This is the beginning of an individual meeting with Medicinal Chemist to discuss your research project.

Here is context for this meeting:

[begin context 1]

ExperimentLCMS[Samples]⟹Protocol

generates a Protocol to separate and analyze Samples via Liquid Chromatography Mass Spectrometry (LCMS).



Liquid chromatography - Mass Spectrometry (LC-MS) separates samples injected into a liquid flow by passage through an adsorbent column (see ExperimentHPLC). After separation, analytes are ionized, selected, and detected in the Mass Spectrometer device (see ExperimentMassSpectrometry). Within, ions are resolved by their mass versus charge state. Optionally, ions can be fragmented by collision with an inert gas, and the resulting product ions can, in turn, be resolved and detected for more information. In total, LC-MS can answer composition questions; for example, proteins, lipids, and metabolites can be identified in a sample. Furthermore, LC-MS can answer concentration questions; for instance, nucleotides can be quantified in a biological sample.



Experimental Principles

Figure 1.1: Procedural overview of a LCMS experiment. Step 1: The system is rinsed with cleaning solutions. Step 2: The stationary column is installed and equilibrated to measurement conditions. Step 3: Samples are then introduced into the flow path. Step 4: The analytes are selectively retained on the downstream column. Step 5: Upon exit from the column, the now separated analytes are analyzed according to their physical property using a mass spectrometer. Step 6: After final sample measurement, the Column(s) are rinsed, removed from the system, and stowed. Step 7: After the column is removed, the system is rinsed with cleaning solution.



Instrumentation

Waters Acquity UPLC I-Class PDA

Model[Instrument, HPLC, "id:4pO6dM5lRrl7"]

Figure 2.1.1: Instrument diagram for the H-Class and I-Class systems. Buffer solutions (up to 4) are steadily pumped through the instrument, consisting of a 6-port valve system, adsorbent column, detectors, and terminates at fraction collection or waste. Samples within the autosampler are loaded into the sample loop via positive displacement from the syringe. The rotation of the valve exposes the sample loop, thereby carrying the sample downstream to the column. Within the column, molecular constituents are separated by adsorption -- a function of the buffers, column, sample properties and temperature. Analytes are continuously carried downstream to the detectors, where they can elicit quantifiable peak signals.

Figure 2.1.2: Principle of PhotodiodeArray detection. Filtered light (across a range of wavelengths) passes through the flow downstream of the column. Presence of light-absorbing molecules will result in less light transmission to the recipient Diode, thereby producing a chromatographic peak for each specific wavelength.

Xevo G2-XS QTOF

Model[Instrument, MassSpectrometer, "id:aXRlGn6KaWdO"]

Figure 2.2.1: Principles of an electrospray quadrupole time of flight mass spectrometer (QTOF). Analytes are flowed through a capillary tube into a heated source box (SourceTemeprature) at the desired InfusionFlowRate. A confluence of the source box temperature, DesolvationTemperature, DesolvationGasFlow, and ESICapillaryVolage result in neubilization, vaporization, and ionization of the analyte stream to generate an electrospray. The electrospray enters the mass spectrometer through the source cone, which serves to focus the ions and excludes contimation via a ConeGasFlow. Within the mass spectrometer, the electrospray is futher refined via an applied voltage (DeclusteringVoltage) to yeild isolated gas-phase ions. Ions are then focused through a stepwave ion guide path via another applied voltage (StepwaveVoltage) into an ion beam. The ions travel through a quadrupole and a collision cell. Lastly, they enter a time-of-flight analyzer which resolves the ions by their mass to charge ratio according to their travel time. Spectra are continuously acquired for ions inside MassDetection hitting the detector during ScanTime until the end of RunDuration. For time independent samples, an average mass spectrum is generated. When coupled with liquid chromatography (see ExperimentLCMS) time-dependent mass spectra are generated instead.

QTRAP 6500

Model[Instrument, MassSpectrometer, "id:N80DNj1aROOD"]

Figure 2.3.1: Principles of an electrospray triple quadrupole mass spectrometer (ESI-QQQ). Analytes are injected through the capillary tube into the source block at the desired InfusionFlowRate. Once the sample enters the source block, it is evaporated at the DesolvationTemperature under a stream of nitrogen gas with a pressure of DesolvationGasFlow. ESICapillaryVoltage is then applied to the capillary tubing tip to produce an electrospray, which turns into single gas-phase ions due to additional evaporation and desolvation SourceTemperature. Ions, focused by the ConeGasFlow, enter the mass spectrometer through the source cone and follow the ion path via an applied voltage (DeclusteringVoltage). They are then guided through an ion guide path via another applied voltage (IonGuideVoltange) to generate a focused ion beam. Ions travel through the first quadrupole mass analyzer (MS1), where their mass is resolved by their mass-to-charge ratio (m/z, MassDetection). After the MS1, ions enter the collision cell, where they can be fragmented by collision-induced dissociation, resulting in bond breakage and the fragmentation of the molecular ions into smaller fragments. CollisionCellExitVoltage accelerates and guides the fragmented ions to enter the second quadrupole mass analyzer (MS2), where their mass can be resolved again by their m/z (FragmentMassDetection). Spectra are continuously acquired for ions either inside MassDetection as a ranged value or as a fixed value, hitting the detector during ScanTime until the end of RunDuration, and a total mass spectrum is generated.



Experiment Options

General

SeparationMode

The category of method used to elicit differential column retention due to interaction between molecules in the mobile phase with those on the stationary phase (column).

Default Value: Automatic

Default Calculation: Automatically set to match the Separation Mode listed with the provided column.

Pattern Description: NormalPhase, ReversePhase, IonExchange, SizeExclusion, Affinity, or Chiral.

Programmatic Pattern: SeparationModeP | Automatic

MassAnalyzer

The manner of detection used to resolve and detect molecules. QTOF accelerates ions through an elongated flight tube and separates ions by their flight time (related to mass to charge ratio).

Default Value: Automatic

Default Calculation: Is automatically set to the QTOF.

Pattern Description: QTOF or TripleQuadrupole.

Programmatic Pattern: (QTOF | TripleQuadrupole) | Automatic

ChromatographyInstrument

The device used to separate molecules from the sample mixture using mobile liquid through an adsorbent column.

Default Value: Model[Instrument, HPLC, Waters Acquity UPLC I-Class PDA]

Default Calculation: Automatically set to an instrument model that is available for the best MassSpectrometerInstrument.

Pattern Description: An object of type or subtype Model[Instrument, HPLC] or Object[Instrument, HPLC]

Programmatic Pattern: ObjectP[{Model[Instrument, HPLC], Object[Instrument, HPLC]}]

MassSpectrometerInstrument

The device used to ionize, separate, fragment (optionally), and detect analyte species.

Default Value: Automatic

Default Calculation: Is automatically set according to MassAnalyzer: Model[Instrument, MassSpectrometer, "Xevo G2-XS QTOF"] for QTOF, Model[Instrument, MassSpectrometer, "QTRAP 6500"] for using TripleQuadrupole.

Pattern Description: An object of type or subtype Model[Instrument, MassSpectrometer] or Object[Instrument, MassSpectrometer]

Programmatic Pattern: ObjectP[{Model[Instrument, MassSpectrometer], Object[Instrument, MassSpectrometer]}] | Automatic

Detector

Additional measurements to employ in concert with MassSpectrometry. Other measurements include: PhotoDiodeArray (measures the absorbance of a range of wavelengths), system Temperature (QTOF only), and system Pressure (QTOF only).

Default Value: {Temperature, Pressure, PhotoDiodeArray}

Pattern Description: List of one or more Temperature, Pressure, or PhotoDiodeArray entries or Temperature, Pressure, or PhotoDiodeArray.

Programmatic Pattern: (Temperature | Pressure | PhotoDiodeArray) | {(Temperature | Pressure | PhotoDiodeArray)..}

GuardColumn

The protective device placed in the flow path before the Column in order to adsorb fouling contaminants and, thus, preserve the Column lifetime.

Default Value: Automatic

Default Calculation: Automatically set from the column model's PreferredGuardColumn. If Column is Null, GuardColumn is automatically set to Null.

Pattern Description: An object of type or subtype Model[Item, Column], Object[Item, Column], Model[Item, Cartridge, Column], or Object[Item, Cartridge, Column] or Null.

Programmatic Pattern: (ObjectP[{Model[Item, Column], Object[Item, Column], Model[Item, Cartridge, Column], Object[Item, Cartridge, Column]}] | Automatic) | Null

NumberOfReplicates

The number of times to repeat measurements on each provided sample(s). If Aliquot -> True, this also indicates the number of times each provided sample will be aliquoted. For experiment samples {A,B,C} if NumberOfReplicates is specified as 3, the order of samples to run on the instrument will be {A,A,A,B,B,B,C,C,C}.

Default Value: Null

Pattern Description: Greater than or equal to 1 and less than or equal to 96 in increments of 1 or Null.

Programmatic Pattern: RangeP[1, 96, 1] | Null

Chromatography

Column

The item containing the stationary phase through which the mobile phase and input samples flow. It adsorbs and separates the molecules within the sample based on the properties of the mobile phase, Samples, Column material, and Column Temperature.

Default Value: Automatic

Default Calculation: Automatically set to a column model compatible for the instrument selected and specified separation Mode.

Pattern Description: An object of type or subtype Model[Item, Column] or Object[Item, Column] or Null.

Programmatic Pattern: (ObjectP[{Model[Item, Column], Object[Item, Column]}] | Automatic) | Null

SecondaryColumn

The additional stationary phase through which the mobile phase and input samples flow. The SecondaryColumn selectively adsorb analytes and is connected to flow path, downstream of the Column.

Default Value: Automatic

Default Calculation: If ColumnSelector is specified, set from there; otherwise, set to Null.

Pattern Description: An object of type or subtype Model[Item, Column] or Object[Item, Column] or Null.

Programmatic Pattern: (ObjectP[{Model[Item, Column], Object[Item, Column]}] | Automatic) | Null

TertiaryColumn

The additional stationary phase through which the mobile phase and input samples flow. The TertiaryColumn selectively adsorb analytes and is connected to flow path, downstream of the SecondaryColumn.

Default Value: Automatic

Default Calculation: If ColumnSelector is specified, set from there; otherwise, set to Null.

Pattern Description: An object of type or subtype Model[Item, Column] or Object[Item, Column] or Null.

Programmatic Pattern: (ObjectP[{Model[Item, Column], Object[Item, Column]}] | Automatic) | Null

ColumnSelector

The set of all the columns loaded into the Instrument's column selector and referenced in Column, SecondaryColumn, TertiaryColumn. The Serial configuration indicates one fluid line for all the samples, Standard and Blank. The Selector configuration indicates use of a column selector where the column line is programmatically switchable between samples.

Default Value: Automatic

Default Calculation: Automatically set to match the values in Column, SecondaryColumn, TertiaryColumn and GuardColumn options.

Pattern Description: {Guard Column, Column, Secondary Column, Tertiary Column}

Programmatic Pattern: {ObjectP[{Model[Item, Column], Object[Item, Column]}] | (Automatic | Null), ObjectP[{Model[Item, Column], Object[Item, Column]}] | (Automatic | Null), ObjectP[{Model[Item, Column], Object[Item, Column]}] | (Automatic | Null), ObjectP[{Model[Item, Column], Object[Item, Column]}] | (Automatic | Null)} | Automatic

BufferA

A solvent or buffer placed in the 'A' bottle as shown in Figure 2.1.1 of ExperimentLCMS help file, pumped through the instrument as part of the mobile phase, the compositions of which is determined by the GradientA option.

Default Value: Automatic

Default Calculation: Automatically set from SeparationMode (e.g. Water buffer if ReversePhase) or the objects specified by the Gradient option.

Pattern Description: An object of type or subtype Object[Sample] or Model[Sample] or a prepared sample.

Programmatic Pattern: (ObjectP[{Object[Sample], Model[Sample]}] | _String) | Automatic

BufferB

A solvent or buffer placed in the 'B' bottle as shown in Figure 2.1.1 of ExperimentLCMS help file, pumped through the instrument as part of the mobile phase, the compositions of which is determined by the GradientB option.

Default Value: Automatic

Default Calculation: Automatically set from SeparationMode (e.g. Acetonitrile buffer if ReversePhase) or the objects specified by the Gradient option.

Pattern Description: An object of type or subtype Object[Sample] or Model[Sample] or a prepared sample.

Programmatic Pattern: (ObjectP[{Object[Sample], Model[Sample]}] | _String) | Automatic

BufferC

A solvent or buffer placed in the 'C' bottle as shown in Figure 2.1.1 of ExperimentLCMS help file, pumped through the instrument as part of the mobile phase, the compositions of which is determined by the GradientC option.

Default Value: Automatic

Default Calculation: Automatically set from SeparationMode or the objects specified by the Gradient option.

Pattern Description: An object of type or subtype Object[Sample] or Model[Sample] or a prepared sample.

Programmatic Pattern: (ObjectP[{Object[Sample], Model[Sample]}] | _String) | Automatic

BufferD

A solvent or buffer placed in the 'D' bottle as shown in Figure 2.1.1 of ExperimentLCMS help file, pumped through the instrument as part of the mobile phase, the compositions of which is determined by the GradientD option.

Default Value: Automatic

Default Calculation: Automatically set from SeparationMode or the objects specified by the Gradient option.

Pattern Description: An object of type or subtype Object[Sample] or Model[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Object[Sample], Model[Sample]}] | _String) | Automatic) | Null

Sample Parameters

InjectionTable

The order of Sample, Standard and Blank sample injected into the Instrument during measurement and/or collection. This also includes the priming and flushing of the column(s).

Default Value: Automatic

Default Calculation: Samples are inserted in the order of the input samples based with the number of replicates. Standard and Blank samples are inserted based on the determination of StandardFrequency and BlankFrequency options. For example, StandardFrequency -> FirstAndLast and BlankFrequency -> Null result in Standard samples injected first, then samples, and then the Standard sample set again at the end. Column priming is inserted at the beginning and repeated according to ColumnPrimeFrequency. Column flushing is inserted at the end.

Pattern Description: List of one or more {Type, Sample, InjectionVolume, Column Temperature, Gradient, Mass Spectrometry} entries.

Programmatic Pattern: {{Standard | Sample | Blank | ColumnPrime | ColumnFlush, (ObjectP[{Model[Sample], Object[Sample]}] | _String) | (Automatic | Null), RangeP[0*Microliter, 50*Microliter, 1*Microliter] | (Automatic | Null), RangeP[30*Celsius, 90*Celsius] | (Ambient | Automatic), ObjectP[Object[Method, Gradient]] | (Automatic | New), ObjectP[Object[Method, MassAcquisition]] | (Automatic | New)}..} | Automatic

SampleTemperature

The temperature of the chamber in which the samples, Standard, and Blank are stored while waiting for the Injection.

Default Value: Ambient

Pattern Description: Ambient or greater than or equal to 5 degrees Celsius and less than or equal to 40 degrees Celsius.

Programmatic Pattern: RangeP[5*Celsius, 40*Celsius] | Ambient

ColumnTemperature

The temperature of the Column throughout the measurement and/or collection. If ColumnnTemperature is set to Ambient, column oven temperature control is not used. Otherwise, ColumnTemperature is maintained by temperature control of the column oven.

Default Value: Automatic

Default Calculation: Automatically set to the corresponding gradient temperature specified in the Gradient option or the column temperature for the sample in the InjectionTable option; otherwise, set to Ambient.

Pattern Description: Ambient or greater than or equal to 30 degrees Celsius and less than or equal to 90 degrees Celsius.

Programmatic Pattern: (RangeP[30*Celsius, 90*Celsius] | Ambient) | Automatic

Index Matches to: experiment samples

InjectionVolume

The physical quantity of sample loaded into the flow path for measurement.

Default Value: Automatic

Default Calculation: If InjectionTable is specified, automatically set from the Injection Volume entry for the sample. Otherwise set to 5 Microliter.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 50 microliters.

Programmatic Pattern: RangeP[0*Microliter, 50*Microliter] | Automatic

Index Matches to: experiment samples

NeedleWashSolution

The solvent used to wash the injection needle before each sample introduction.

Default Value: Automatic

Default Calculation: Defaults to Model[Sample, "Milli-Q water"] for IonExchange and SizeExclusion SeparationType or Model[Sample, StockSolution, "20% Methanol in MilliQ Water"] for other SeparationType.

Pattern Description: An object of type or subtype Object[Sample] or Model[Sample] or a prepared sample.

Programmatic Pattern: (ObjectP[{Object[Sample], Model[Sample]}] | _String) | Automatic

Gradient

GradientA

The composition of BufferA within the flow, defined for specific time points. The composition is linearly interpolated for the intervening periods between the defined time points. For example for GradientA->{{0 Minute, 10 Percent},{30 Minute, 90 Percent}}, the percentage of BufferA in the flow will rise such that at 15 minutes, the composition should be 50 Percent.

Default Value: Automatic

Default Calculation: If Gradient option is specified, set from it or implicitly determined from the GradientB, GradientC, and GradientD options such that the total amounts to 100%.

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or list of one or more {Time, Buffer A Composition} entries.

Programmatic Pattern: (RangeP[0*Percent, 100*Percent] | {{RangeP[0*Minute, $MaxExperimentTime], RangeP[0*Percent, 100*Percent]}..}) | Automatic

Index Matches to: experiment samples

GradientB

The composition of BufferB within the flow, defined for specific time points. The composition is linearly interpolated for the intervening periods between the defined time points. For example for GradientB->{{0 Minute, 10 Percent},{30 Minute, 90 Percent}}, the percentage of BufferB in the flow will rise such that at 15 minutes, the composition should be 50 Percent.

Default Value: Automatic

Default Calculation: If Gradient option is specified, set from it or implicitly determined from the GradientA, GradientC, and GradientD options such that the total amounts to 100%. If no other gradient options are specified, a Buffer B gradient of 10% to 100% over 45 minutes is used.

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or list of one or more {Time, Buffer B Composition} entries.

Programmatic Pattern: (RangeP[0*Percent, 100*Percent] | {{RangeP[0*Minute, $MaxExperimentTime], RangeP[0*Percent, 100*Percent]}..}) | Automatic

Index Matches to: experiment samples

GradientC

The composition of BufferC within the flow, defined for specific time points. The composition is linearly interpolated for the intervening periods between the defined time points. For example for GradientC->{{0 Minute, 10 Percent},{30 Minute, 90 Percent}}, the percentage of BufferC in the flow will rise such that at 15 minutes, the composition should be 50 Percent.

Default Value: Automatic

Default Calculation: If Gradient option is specified, set from it or implicitly determined from the GradientA, GradientB, and GradientD options such that the total amounts to 100%.

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or list of one or more {Time, Buffer C Composition} entries.

Programmatic Pattern: (RangeP[0*Percent, 100*Percent] | {{RangeP[0*Minute, $MaxExperimentTime], RangeP[0*Percent, 100*Percent]}..}) | Automatic

Index Matches to: experiment samples

GradientD

The composition of BufferD within the flow, defined for specific time points. The composition is linearly interpolated for the intervening periods between the defined time points. For example for GradientD->{{0 Minute, 10 Percent},{30 Minute, 90 Percent}}, the percentage of BufferD in the flow will rise such that at 15 minutes, the composition should be 50 Percent.

Default Value: Automatic

Default Calculation: If Gradient option is specified, set from it or implicitly determined from the GradientA, GradientB, and GradientC options such that the total amounts to 100%.

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent or list of one or more {Time, Buffer D Composition} entries or Null.

Programmatic Pattern: ((RangeP[0*Percent, 100*Percent] | {{RangeP[0*Minute, $MaxExperimentTime], RangeP[0*Percent, 100*Percent]}..}) | Automatic) | Null

Index Matches to: experiment samples

FlowRate

The net speed of the fluid flowing through the pump inclusive of the composition of BufferA, BufferB, BufferC, and BufferD specified in the gradient options. This speed is linearly interpolated such that consecutive entries of {Time, Flow Rate} will define the intervening fluid speed. For example, {{0 Minute, 0.3 Milliliter/Minute},{30 Minute, 0.5 Milliliter/Minute}} means flow rate of 0.4 Milliliter/Minute at 15 minutes into the run.

Figure 3.1: ESI source settings should be adjusted according to the flow rate used to infuse the sample into the mass spectrometer to ensure successful spray formation and solvent desolvation. This table provides recommended settings for typical flow rate ranges for both ESI-QTOF and ESI-QQQ. Note that ESI-QTOF and ESI-QQQ take different input ranges and units. Desolvation gas flow is input as gas flow rate for ESI-QTOF and gas pressure for ESI-QQQ; ESI-QQQ has different polarity for the capillary voltage for positive and negative ion mode, while ESI-QTOF only takes positive capillary voltage as the input.

Default Value: Automatic

Default Calculation: If Gradient option is specified, automatically set from the method given in the Gradient option. If NominalFlowRate of the column model is specified, set to lesser of the NominalFlowRate for each of the columns, guard columns or the instrument's MaxFlowRate. Otherwise set to 1 Milliliter / Minute.

Pattern Description: Greater than or equal to 0 milliliters per minute and less than or equal to 2 milliliters per minute or list of one or more {Time, Flow Rate} entries.

Programmatic Pattern: (RangeP[0*(Milliliter/Minute), 2*(Milliliter/Minute)] | {{RangeP[0*Minute, $MaxExperimentTime], RangeP[0*(Milliliter/Minute), 2*(Milliliter/Minute)]}..}) | Automatic

Index Matches to: experiment samples

Gradient

The composition of different specified buffers in BufferA, BufferB, BufferC and BufferD over time in the fluid flow. Specific parameters of a gradient object can be overridden by specific options.

Default Value: Automatic

Default Calculation: Automatically set to best meet all the Gradient options (e.g. GradientA, GradientB, GradientC, GradientD, FlowRate).

Pattern Description: An object of type or subtype Object[Method, Gradient] or list of one or more {Time, Buffer A Composition, Buffer B Composition, Buffer C Composition, Buffer D Composition, Flow Rate} entries.

Programmatic Pattern: (ObjectP[Object[Method, Gradient]] | {{RangeP[0*Minute, $MaxExperimentTime], RangeP[0*Percent, 100*Percent], RangeP[0*Percent, 100*Percent], RangeP[0*Percent, 100*Percent], RangeP[0*Percent, 100*Percent], RangeP[0*(Milliliter/Minute), 2*(Milliliter/Minute)]}..}) | Automatic

Index Matches to: experiment samples

Separation

MaxAcceleration

When ramping up the FlowRate of solvent through the instrument, the maximum allowed change per time in the FlowRate.

Default Value: Automatic

Default Calculation: For Waters instruments, automatically set to the lowest value from Max the Column, Instrument, and GuardColumn models. For other instruments, automatically set to Null.

Pattern Description: Greater than 0 milliliters per minute squared or Null.

Programmatic Pattern: (GreaterP[0*(Milliliter/Minute/Minute)] | Automatic) | Null

Mass Analysis

Calibrant

The sample with components of known mass-to-charge ratios (m/z) used to calibrate the mass spectrometer. In the chosen ion polarity mode, the calibrant should contain at least 3 masses spread over the mass range of interest.

Figure 3.2: Various calibrants available.

Default Value: Automatic

Default Calculation: If using QTOF as the mass analyzer, set to sodium iodide for peptide samples, cesium iodide for intact protein analysis. For other types of samples, is set to cesium iodide if molecular weight is above 2000 Da, to sodium iodide if molecular weight between 1200 and 2000 Da, and to sodium formate for all others (small molecule range). If using TripleQuadrupole as the mass analyzer, this option will be set automatically based on the first IonMode: Model[Sample, "id:zGj91a71kXEO"] or Model[Sample, "id:bq9LA0JA1YJz"] for Positive and Negative, respectively.

Pattern Description: An object of type or subtype Object[Sample] or Model[Sample] or a prepared sample.

Programmatic Pattern: (ObjectP[{Object[Sample], Model[Sample]}] | _String) | Automatic

SecondCalibrant

The additional sample with components of known mass-to-charge ratios (m/z) used to calibrate the mass spectrometer. In the chosen ion polarity mode, the calibrant should contain at least 3 masses spread over the mass range of interest.

Default Value: Automatic

Default Calculation: Set to Model[Sample, "id:zGj91a71kXEO"] or Model[Sample, "id:bq9LA0JA1YJz"] for Positive and Negative, respectively, when using TripleQuandrupole as the MassAnalyzer. Otherwise set to Null.

Pattern Description: An object of type or subtype Object[Sample] or Model[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Object[Sample], Model[Sample]}] | _String) | Automatic) | Null

Analytes

The compounds of interest that are present in the given samples, used to determine the other settings for the Mass Spectrometer (e.g. MassRange).

Default Value: Automatic

Default Calculation: If populated, will resolve to the user-specified Analytes field in the Object[Sample]. Otherwise, will resolve to the larger compounds in the sample, in the order of Proteins, Peptides, Oligomers, then other small molecules. Otherwise, set Null.

Pattern Description: List of one or more an object of type or subtype Model[Molecule], Model[Molecule, cDNA], Model[Molecule, Oligomer], Model[Molecule, Transcript], Model[Molecule, Protein], Model[Molecule, Protein, Antibody], Model[Molecule, Carbohydrate], Model[Molecule, Polymer], Model[Resin], Model[Resin, SolidPhaseSupport], Model[Lysate], Model[ProprietaryFormulation], Model[Virus], Model[Cell], Model[Cell, Mammalian], Model[Cell, Bacteria], Model[Cell, Yeast], Model[Tissue], Model[Material], or Model[Species] entries or Null.

Programmatic Pattern: ({ObjectP[IdentityModelTypes]..} | Automatic) | Null

Index Matches to: experiment samples

IonMode

Indicates if positively or negatively charged ions are analyzed.

Default Value: Automatic

Default Calculation: For oligomer samples of the types Peptide, DNA, and other synthetic oligomers, is automatically set to positive ion mode. For other types of samples, defaults to positive ion mode, unless the sample is acid (pH<=5 or pKa<=8).

Pattern Description: Negative or Positive.

Programmatic Pattern: IonModeP | Automatic

Index Matches to: experiment samples

MassSpectrometryMethod

The previously specified instruction(s) for the analyte ionization, selection, fragmentation, and detection.

Default Value: Automatic

Default Calculation: If set in the InjectionTable option, set to that; otherwise, set to New.

Pattern Description: An object of type or subtype Object[Method, MassAcquisition] or New or Null.

Programmatic Pattern: ((ObjectP[Object[Method, MassAcquisition]] | New) | Automatic) | Null

Index Matches to: experiment samples

AcquisitionWindow

The time range with respect to the chromatographic separation to conduct analyte ionization, selection/survey, optional fragmentation, and detection.

Default Value: Automatic

Default Calculation: Set to the entire gradient window 0 Minute to the last time point in Gradient.

Pattern Description: A span from anything greater than or equal to 0 minutes and less than or equal to 8 hours to anything greater than or equal to 0 minutes and less than or equal to 8 hours or list of one or more a span from anything greater than or equal to 0 minutes and less than or equal to 8 hours to anything greater than or equal to 0 minutes and less than or equal to 8 hours or {Automatic, Null} entries.

Programmatic Pattern: (RangeP[0*Minute, 8*Hour] ;; RangeP[0*Minute, 8*Hour] | {(RangeP[0*Minute, 8*Hour] ;; RangeP[0*Minute, 8*Hour] | (Automatic | Null))..}) | Automatic

Index Matches to: experiment samples

AcquisitionMode

The method by which spectra are collected. DataDependent will depend on the properties of the measured mass spectrum of the intact ions. DataIndependent will systemically scan through all of the intact ions. MS1 will focus on defined intact masses. MS1MS2 will focus on fragmented masses.

Figure 3.3: (a),(b) and (c):Various acquisition modes available for ExperimentLCMS using QTOF as the MassAnalyzer. For MS1FullScan mode, the collision cell is turned off, and ions are measured and resolved with just the quadrupole time of flight. For MS1FullScanMS2 mode, one intact mass (MassDetection) is selected in the first quadruple and disassociated into fragment ions with the collision cell. Fragment ions are resolved and detected with the quadrupole time of flight. For DataIndependent mode, scans are alternated between scanning a range of MS1FullScan masses (no fragmentation) and scanning fragmentation of a range of masses (MS2). For DataDependent mode, acquisition is split into cycles. For the first scan of each cycle, a survey is taken where the collision cell is off and only intact masses are measured. The top ranking intact ions are noted, then for each consequent scan of the cycle, a ranking intact ion is fragmented, and the resultant fragment ions are resolved and measured on the quadrupole time of flight. A suite of options are available to control how many ions are ranked, which ones are, and to eliminate redundancies. (d):Various mass spectrometry scan modes available for ExperimentLCMS using TripleQuad as the MassAnalyzer. In Full Scan Mode, the entire MS1 range is scanned and fragmentation is off. In SelectedIonMonitoring, select MS1 masses (per the MassDetection option) are monitored and measured without fragmentation. In PrecursorIonScan mode, fragmentation is on, and fragment ion is selected (per the FragmentMassDetection option), while MS1 masses are scanned across a range (MassDetection). In NeutralIonLoss mode, both MS1 and MS2 masses are scanned, to track specific MS1/MS2 combinations for neutral ion loss. In ProductIonScan, an MS1 mass is selected (MassDetection) and a range of MS2 mass is scanned to survey fragmentation patterns of the parent mass. In MultipleReactionMonitoring mode, both MS1 and MS2 are selected - specific intact and fragment ion pairs are monitored.

Default Value: Automatic

Default Calculation: Set to MS1FullScan unless DataDependent related options are set, then set to DataDependent.

Pattern Description: DataIndependent, DataDependent, MS1FullScan, MS1MS2ProductIonScan, SelectedIonMonitoring, NeutralIonLoss, PrecursorIonScan, or MultipleReactionMonitoring or list of one or more DataIndependent, DataDependent, MS1FullScan, MS1MS2ProductIonScan, SelectedIonMonitoring, NeutralIonLoss, PrecursorIonScan, or MultipleReactionMonitoring entries.

Programmatic Pattern: (MSAcquisitionModeP | {MSAcquisitionModeP..}) | Automatic

Index Matches to: experiment samples

Fragment

Indicates if ions should be collided with neutral gas and dissociated in order to measure the resulting product ions. Also known as tandem mass spectrometry or MS/MS (as opposed to MS).

Default Value: Automatic

Default Calculation: Set to True if AcquisitionMode is MS1MS2ProductIonScan, DataDependent, or DataIndependent. Set True if any of the Fragmentation related options are set (e.g. FragmentMassDetection).

Pattern Description: List of one or more True or False entries or True or False.

Programmatic Pattern: (BooleanP | {BooleanP..}) | Automatic

Index Matches to: experiment samples

MassDetection

The lowest and the highest mass-to-charge ratio (m/z) to be recorded or selected for intact masses. When Fragment is True, the intact ions will be selected for fragmentation.

Figure 3.3: (a),(b) and (c):Various acquisition modes available for ExperimentLCMS using QTOF as the MassAnalyzer. For MS1FullScan mode, the collision cell is turned off, and ions are measured and resolved with just the quadrupole time of flight. For MS1FullScanMS2 mode, one intact mass (MassDetection) is selected in the first quadruple and disassociated into fragment ions with the collision cell. Fragment ions are resolved and detected with the quadrupole time of flight. For DataIndependent mode, scans are alternated between scanning a range of MS1FullScan masses (no fragmentation) and scanning fragmentation of a range of masses (MS2). For DataDependent mode, acquisition is split into cycles. For the first scan of each cycle, a survey is taken where the collision cell is off and only intact masses are measured. The top ranking intact ions are noted, then for each consequent scan of the cycle, a ranking intact ion is fragmented, and the resultant fragment ions are resolved and measured on the quadrupole time of flight. A suite of options are available to control how many ions are ranked, which ones are, and to eliminate redundancies. (d):Various mass spectrometry scan modes available for ExperimentLCMS using TripleQuad as the MassAnalyzer. In Full Scan Mode, the entire MS1 range is scanned and fragmentation is off. In SelectedIonMonitoring, select MS1 masses (per the MassDetection option) are monitored and measured without fragmentation. In PrecursorIonScan mode, fragmentation is on, and fragment ion is selected (per the FragmentMassDetection option), while MS1 masses are scanned across a range (MassDetection). In NeutralIonLoss mode, both MS1 and MS2 masses are scanned, to track specific MS1/MS2 combinations for neutral ion loss. In ProductIonScan, an MS1 mass is selected (MassDetection) and a range of MS2 mass is scanned to survey fragmentation patterns of the parent mass. In MultipleReactionMonitoring mode, both MS1 and MS2 are selected - specific intact and fragment ion pairs are monitored.

Default Value: Automatic

Default Calculation: Set to MS1FullScan unless DataDependent related options are set, then set to DataDependent.

Pattern Description: DataIndependent, DataDependent, MS1FullScan, MS1MS2ProductIonScan, SelectedIonMonitoring, NeutralIonLoss, PrecursorIonScan, or MultipleReactionMonitoring or list of one or more DataIndependent, DataDependent, MS1FullScan, MS1MS2ProductIonScan, SelectedIonMonitoring, NeutralIonLoss, PrecursorIonScan, or MultipleReactionMonitoring entries.

Programmatic Pattern: (MSAcquisitionModeP | {MSAcquisitionModeP..}) | Automatic

Index Matches to: experiment samples

Fragment

Indicates if ions should be collided with neutral gas and dissociated in order to measure the resulting product ions. Also known as tandem mass spectrometry or MS/MS (as opposed to MS).

Default Value: Automatic

Default Calculation: Set to True if AcquisitionMode is MS1MS2ProductIonScan, DataDependent, or DataIndependent. Set True if any of the Fragmentation related options are set (e.g. FragmentMassDetection).

Pattern Description: List of one or more True or False entries or True or False.

Programmatic Pattern: (BooleanP | {BooleanP..}) | Automatic

Index Matches to: experiment samples

MassDetection

The lowest and the highest mass-to-charge ratio (m/z) to be recorded or selected for intact masses. When Fragment is True, the intact ions will be selected for fragmentation.



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



Example Calls

Basics

High performance liquid chromatography (HPLC) separates sample mixtures into analyzable molecular constituents by injection into flowing liquid that passes through a retentive column:

ExperimentLCMS[mySamples]

MassAnalyzer

Use MassAnalyzer option to select TripleQuadruploe as the mass analyzer

ExperimentLCMS[mySamples,

 	MassAnalyzer -> TripleQuadruploe,

 	ConeGasFlow -> (90 * PSI)

 ]

Separation Mode and Gradient

More specific buffers and gradient profiles can also be articulated. For example:

ExperimentLCMS[mySamples,

 	BufferB -> Model[Sample, "Methanol - LCMS grade"],

 	GradientB -> {

   		{0 * Minute, 5 * Percent},

   		{20 * Minute, 40 * Percent}

   	}

 ]

A full gradient table can be specified:

ExperimentLCMS[mySamples,

 	Gradient -> {

   		{0 * Minute, 95 * Percent, 5 * Percent, 0 * Percent,

    0 * Percent, 1 * Milliliter / Minute},

   		{15 * Minute, 50 * Percent, 50 * Percent, 0 * Percent,

    0 * Percent, 1 * Milliliter / Minute},

   		{30 * Minute, 5 * Percent, 95 * Percent, 0 * Percent,

    0 * Percent, 1 * Milliliter / Minute}

   	}

 ]

Ionization

The polarity of the ions analyzed can be set along with the desired reference solution for the sample masses:

ExperimentLCMS[mySamples,

 	IonMode -> Positive,

 	Calibrant ->

  Model[Sample, StockSolution, Standard, "Cesium Iodide ESI Calibrant"]

 ]

Specific settings for electrospray ionization source can be controlled in order to maximize ionization capability:

ExperimentLCMS[mySamples,

 	ESICapillaryVoltage -> (1 * Kilovolt),

 	ConeGasFlow -> (300 * Liter / Hour)

 ]

Acquisition Windows and Modes

Different acquisition modes can be specified within different time periods for the same chromatogram. Here, for all of the samples, during the time period from 2 minutes to 5 minutes, an MS1FullScan acquisition is employed (no fragmentation; measure intact ions). From 7 minutes to 9, a data dependent acquisition is performed (see the appropriate section above):

ExperimentLCMS[mySamples,

 	AcquisitionWindow -> {

   		Span[2 * Minute, 5 * Minute],

   		Span[7 * Minute, 9 * Minute]

   	},

 	AcquisitionMode -> {MS1FullScan, DataDependent}

 ]

Similarly, different fragmentation instructions can be specified for different time periods:

ExperimentLCMS[mySamples,

 	AcquisitionWindow -> {

   		Span[2 * Minute, 5 * Minute],

   		Span[7 * Minute, 9 * Minute]

   	},

 	Fragment -> {True, False},

 	MassDetection -> {650 * Gram / Mole, Protein},

 	FragmentMassDetection -> {Span[300 * Gram / Mole,

    1000 * Gram / Mole], Null}

 ]

Multiple Reaction Monitoring

Specified MassAnalyzer, AcquisitionMode, MassSelection and FragmentMassSelection to conduct multiple reaction monitoring analysis by using QTRAP 6500:

ExperimentLCMS[mySamples,

 	AcquisitionWindow -> {

   		{

    			Span[2 * Minute, 5 * Minute],

    			Span[7 * Minute, 9 * Minute]

    		}

   	},

 	AcquisitionMode -> {{MS1FullScan, MultipleReactionMonitoring}},

 	MassAnalyzer -> TripleQuadrupole,

 	MassDetection -> {

   		{

    			Span[Quantity[5, "Grams" / "Moles"],

     				Quantity[1250, "Grams" / "Moles"]

     			]

    		},

   		{

    			{

     				609.3 * Gram / Mole,

     				609.3 * Gram / Mole,

     				609.3 * Gram / Mole,

     				609.3 * Gram / Mole

     			}

    		}

   	},

 	FragmentMassDetection -> {

   		{Null},

   		{

    			{

     				174.1 * Gram / Mole,

     				195. * Gram / Mole,

     				397.1 * Gram / Mole,

     				448.2 * Gram / Mole

     			}

    		}

   	}

 ]

Specified MassAnalyzer, AcquisitionMode and MultipleReactionMonitoringAssays to conduct multiple reaction monitoring analysis by using QTRAP 6500:

ExperimentLCMS[mySamples,

 	AcquisitionMode -> {{MultipleReactionMonitoring}},

 	MassAnalyzer -> TripleQuadrupole,

 	MultipleReactionMonitoringAssays -> {

   		{

    			{

     				Quantity[356, "Grams" / "Moles"],

     				Quantity[30, "Volts"],

     				Quantity[234, "Grams" / "Moles"],

     				Quantity[4, "Seconds"]

     			},

    			{

     				Quantity[456, "Grams" / "Moles"],

     				Quantity[40, "Volts"],

     				Quantity[345, "Grams" / "Moles"],

     				Quantity[2, "Seconds"]

     			},

    			{

     				Quantity[453, "Grams" / "Moles"],

     				Quantity[65, "Volts"],

     				Quantity[345, "Grams" / "Moles"],

     				Quantity[3, "Seconds"]

     			},

    			{

     				Quantity[764, "Grams" / "Moles"],

     				Quantity[30, "Volts"],

     				Quantity[345, "Grams" / "Moles"],

     				Quantity[2, "Seconds"]

     			}

    		}

   	}

 ]

Data Dependent Acquisition

In data dependent acquisition, the measurement is split into cycles (see the figure above). In the first part of the cycle, the intact ions (no fragmentations) are surveyed and considered for fragmentation analysis:

ExperimentLCMS[mySamples,

 	AcquisitionMode -> DataDependent,

 	AcquisitionSurvey -> 20

 ]

A threshold can be specified on whether to consider an intact ion for fragmentation analysis. Likewise, a limit can be placed so that a highly abundant ion is not overly analyzed:

ExperimentLCMS[mySamples,

 	AcquisitionMode -> DataDependent,

 	MinimumThreshold -> (100000 * ArbitraryUnit),

 	AcquisitionLimit -> (2000000 * ArbitraryUnit)

 ]

Various m/z can be excluded from the acquisition program:

ExperimentLCMS[mySamples,

 	AcquisitionMode -> DataDependent,

 	ExclusionMass -> {

   		{All, 656 * Gram / Mole},

   		{All, 657 * Gram / Mole}

   	}

 ]

Masses can be prioritized for fragmentation as they surface during the surveys:

ExperimentLCMS[mySamples,

 	AcquisitionMode -> DataDependent,

 	InclusionMass -> {

   		{Preferential, 987 * Gram / Mole},

   		{Preferential, 1013 * Gram / Mole}

   	}

 ]

Masses can be prioritized for fragmentation as they surface during the surveys:

ExperimentLCMS[mySamples,

 	AcquisitionMode -> DataDependent,

 	InclusionMass -> {

   		{Preferential, 987 * Gram / Mole},

   		{Preferential, 1013 * Gram / Mole}

   	}

 ]

Redundant isotopes can excluded from acquisition surveys:

ExperimentLCMS[mySamples, SurveyIsotopeExclusion -> True]

Redundant charge states can excluded from acquisition surveys:

ExperimentLCMS[mySamples, SurveyChargeStateExclusion -> True]

Standards and Blanks

ExperimentLCMS can be used to quantify analytes in a sample, in which case, a Standard sample is employed to serve as reference. A standard can be submitted before and after the injection sequence of the samples simply by running:

ExperimentLCMS[mySamples, StandardFrequency -> FirstAndLast]

Likewise, a Blank sample can be used to see if there is any background from the injection process. To run a blank to occur between every 5 samples, use the following command:

ExperimentLCMS[mySamples, BlankFrequency -> 5]

PhotoDiodeArray detection

PhotoDiodeArray detection involves passes light across a range of wavelengths and measures how much light is absorbed for each even wavelength:

ExperimentLCMS[mySamples,

 	AbsorbanceWavelength -> Span[400, 500 * Nanometer],

 	UVFilter -> True

 ]

Injection Table

In addition to specifying frequencies of running standards and blanks, now the injection sequence of samples, standards, blanks, and column primes/flushes can be explicitly articulated as well. In this case, an additional column flush is specified after the injection of the second sample:

customInjectionTable = customInjectionTable = {

    	{ColumnPrime, Null, Null, myGradientMethod1,

     myMassAcquisitionMethod1},

    	{Sample, mySample1, 2 * Microliter, myGradientMethod2,

     myMassAcquisitionMethod2},

    	{Blank, myBlank1, 5 * Microliter, myGradientMethod2,

     myMassAcquisitionMethod2},

    	{Sample, mySample2, 3 * Microliter, myGradientMethod2,

     myMassAcquisitionMethod2},

    	{ColumnFlush, Null, Null, myGradientMethod1,

     myMassAcquisitionMethod1},

    	{Standard, myStandard1, 2 * Microliter, myGradientMethod2,

     myMassAcquisitionMethod2},

    	{Sample, mySample3, 5 * Microliter, myGradientMethod2,

     myMassAcquisitionMethod2},

    	{ColumnFlush, Null, Null, myGradientMethod1,

     myMassAcquisitionMethod1}

    }

ExperimentLCMS[{mySample1, mySample2, mySample3},

 	InjectionTable -> customInjectionTable

 ]



Preferred Input Containers

The autosampler can take 2mL deep well plates.

The autosampler can take normal vials routinely used in HPLC analysis.



Data Processing

The data can be viewed by PlotChromatographyMassSpectra:

PlotChromatographyMassSpectra[

 	Object[Data, ChromatographyMassSpectra, "Sample LCMS Data"]

 ]

The data can be viewed by different types by spcifying PlotType options:

PlotChromatographyMassSpectra[

 	Object[Data, ChromatographyMassSpectra, "Sample LCMS Data"],

 	PlotType -> AbsorbanceChromatogram

 ]

Use the PlotType and MassSpectrumTimeRange to plot mass spectrum data with in a certain time range:

PlotChromatographyMassSpectra[

 	Object[Data, ChromatographyMassSpectra, "Sample LCMS Data"],

 	MassSpectrumTimeRange -> {Span[5 * Minute, 5.5 * Minute]},

 	PlotType -> MassSpectrum

 ]

Use ExcludeRange to specify one or more ranges of m/z values to exclude from different type of plots:

PlotChromatographyMassSpectra[

 	Object[Data, ChromatographyMassSpectra, "Sample LCMS Data"],

 	MassSpectrumTimeRange -> {Span[5 * Minute, 5.5 * Minute]},

 	PlotType -> WaterfallPlot,

 	ExcludeRange -> {

   		Span[0 * Dalton, 300 * Dalton],

   		Span[500 * Dalton, 700 * Dalton]

   	}

 ]



Possible Issues

Equilibration

Equilibrate to the correct buffer conditions at the end of each gradient to reach a state that is appropriate for the start of the next gradient.

Column flush

The column will end up being stored in whatever the final gradient solvent conditions are so that should be considered for column protection.

Column fouling

Consider using a GuardColumn to preserve column lifetime. Examine injections of standards over time to ensure that the column is performing to satisfaction.

Filter sample and buffer

Samples should not have particulates; otherwise, the system will over-pressurize. Consider filtering any samples or buffers used for the LCMS experiment.

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

You are working on a research project to use machine learning for drug discovery. Your goals are the following: (1) the project must have high clinical value, meaning the research contributes to helping patients, (2) the project must include a scientifically impactful application of machine learning to drug discovery, and (3) the project must use Emerald Cloud Labs (ECL) for all experimental validation with a 3-month limit on experiments. Your team previously decided to pursue peptide-based therapeutics. You previously designed experimental protocols for synthesis and validation of peptide-based therapeutics for a given protein drug target. Now you must implement one of these protocols using ECL. Please implement the ExperimentLCMS protocol using the appropriate commands and syntax from ECL, writing out the experiment in the form ExperimentLCMS[<options>] where you fill in <options> with the appropriate options. Please refer to the ECL documentation that is provided as context. In general, leave most options at their default values (and therefore do not specify them) except for those options that should be changed based on your specific experimental design. For every option that you do specify, please explain why you chose that value.

Medicinal Chemist, please provide your response to the agenda.

## Medicinal Chemist

To implement the `ExperimentLCMS` protocol using Emerald Cloud Labs (ECL) for the validation of peptide-based therapeutics, we need to carefully select and specify options that align with our experimental design. Below is the proposed setup for the `ExperimentLCMS` protocol, along with explanations for each specified option:

```plaintext
ExperimentLCMS[
    MassAnalyzer -> QTOF,
    IonMode -> Positive,
    Calibrant -> Model[Sample, StockSolution, Standard, "Cesium Iodide ESI Calibrant"],
    Gradient -> {
        {0 * Minute, 95 * Percent, 5 * Percent, 0 * Percent, 0 * Percent, 1 * Milliliter / Minute},
        {15 * Minute, 50 * Percent, 50 * Percent, 0 * Percent, 0 * Percent, 1 * Milliliter / Minute},
        {30 * Minute, 5 * Percent, 95 * Percent, 0 * Percent, 0 * Percent, 1 * Milliliter / Minute}
    },
    AcquisitionWindow -> {
        Span[2 * Minute, 5 * Minute],
        Span[7 * Minute, 9 * Minute]
    },
    AcquisitionMode -> {MS1FullScan, DataDependent},
    Fragment -> {True, False},
    MassDetection -> {650 * Gram / Mole, Protein},
    FragmentMassDetection -> {Span[300 * Gram / Mole, 1000 * Gram / Mole], Null}
]
```

### Explanation of Specified Options:

1. **MassAnalyzer -> QTOF**: 
   - **Reason**: The Quadrupole Time-of-Flight (QTOF) mass analyzer is chosen for its high resolution and accuracy, which is essential for the detailed analysis of peptides and their modifications.

2. **IonMode -> Positive**: 
   - **Reason**: Peptides typically ionize better in positive mode due to the presence of basic amino acids, which enhances sensitivity and detection.

3. **Calibrant -> Model[Sample, StockSolution, Standard, "Cesium Iodide ESI Calibrant"]**: 
   - **Reason**: Cesium Iodide is a suitable calibrant for ensuring accurate mass measurements across a wide range of m/z values, which is critical for peptide analysis.

4. **Gradient**: 
   - **Reason**: A gradient is specified to effectively separate peptide components over time. The gradient starts with a high percentage of aqueous buffer to retain hydrophilic components and gradually increases the organic phase to elute more hydrophobic peptides.

5. **AcquisitionWindow -> {Span[2 * Minute, 5 * Minute], Span[7 * Minute, 9 * Minute]}**: 
   - **Reason**: Specific time windows are chosen to focus on regions of the chromatogram where peptide elution is expected, optimizing data collection and reducing unnecessary data acquisition.

6. **AcquisitionMode -> {MS1FullScan, DataDependent}**: 
   - **Reason**: MS1FullScan is used initially to survey intact ions, while DataDependent acquisition allows for targeted fragmentation of selected ions based on their abundance, providing detailed structural information.

7. **Fragment -> {True, False}**: 
   - **Reason**: Fragmentation is enabled during the DataDependent acquisition mode to obtain structural information from product ions, while it is disabled during the MS1FullScan to focus on intact ions.

8. **MassDetection -> {650 * Gram / Mole, Protein}**: 
   - **Reason**: This range is set to capture the mass-to-charge ratios typical of peptides, ensuring that the relevant ions are detected and analyzed.

9. **FragmentMassDetection -> {Span[300 * Gram / Mole, 1000 * Gram / Mole], Null}**: 
   - **Reason**: This range is specified to capture the fragment ions resulting from peptide fragmentation, providing insights into peptide sequence and modifications.

By specifying these options, we ensure that the LCMS experiment is tailored to the analysis of peptide-based therapeutics, aligning with our project's goals of high clinical value and impactful scientific application. This setup will be implemented using ECL to validate our peptide synthesis and modifications within the 3-month experimental timeframe.

