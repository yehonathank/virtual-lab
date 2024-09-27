## User

This is the beginning of an individual meeting with Medicinal Chemist to discuss your research project.

Here is context for this meeting:

[begin context 1]

ExperimentBioconjugation[SamplePools, NewIdentityModels]⟹Protocol

generates a Protocol object to covalently bind SamplePools through chemical crosslinking to create a sample composed of NewIdentityModels. Bioconjugation reactions are a restricted form of synthesis where conjugations: 1) occur in aqueous solution, 2) occur at atmospheric conditions, 3) are low volume, 4) do not require slow addition of reagents, 5) and do not require reaction monitoring.



Bioconjugation chemically links molecules together where the resulting molecule takes on properties of all parent molecules. This procedure is typically used to modify proteins, antibodies, solid phase supports, and oligomers. Common conjugates are fluorophores, nanoparticles, biotin, and horseradish peroxidase. First, if necessary, the input sample is functionalized or activated to prepare covalent binding sites to accept the conjugate. The activated input sample is then incubated with the conjugates and a covalent bond is formed. The reaction can be quenched to deactivate any unreacted binding sites. Downstream purification may be used to separate conjugated samples from the reaction components prior to use in other assays.



Experimental Principles

Figure 1.1: Bioconjugation covalently binds a biomolecule to a molecule of interest. Optional Step 1: Biomolecules can be activated to prepare and expose binding sites prior to conjugation. Activation parameters can be used to specify the activation reagent (ActivationReagent, ActivationReagentVolume), mixing of the activation sample (ActivationMix, ActivationMixType, etc.), the incubation time (ActivationTime), the incubation temperature (ActivationTemperature), and any post activation washing if desired (PostActivationWash). Step 2: The conjugation samples are mixed (ConjugationMix, ConjugationMixType, etc) at the desired ratio incubated for the ConjugationTime at the ConjugationTemperature. During this step, covalent bonds are formed between the conjugation samples to create a new molecule characterized by properties of each individual conjugation molecule. Optional Step 3: Unreacted conjugates can be quenched using the QuenchReaction option to deactivate any reactive sites or inhibit the molecular properties of any unconjugated molecules. Step 4: The resulting conjugated molecule can be further purified using PostConjugationWorkup options or used in downstream assays. This process is ideal for small volume conjugations of antibodies, proteins, oligomers, and microbeads including xMap Luminex beads. All steps of this experiment use ExperimentSampleManipulation primitives such as Transfer, Incubate, Filter, and Pellet. For more information on options available in these primitives or to understand how ExperimentSampleManipulation works please see the corresponding help file.



Instrumentation

Hamilton STARlet

Model[Instrument, LiquidHandler, "id:kEJ9mqaW7xZP"]

Figure 2.1.1: An overview of the robotic workcell. It is capable of processing plate operations including incubation, shaking, and magnetic bead separation on-deck and filtration and absorbance/fluorescence/luminescence measurement off-deck, with a robot arm facilitating the plate movements.

Figure 2.1.2: Overhead view of the liquid handling instrument deck.

Super STAR

Model[Instrument, LiquidHandler, "id:7X104vnRbRXd"]

Figure 2.2.1: An overview of the robotic workcell. It is capable of processing plate operations including incubation, shaking, and magnetic bead separation on-deck and centrifugation, filtration, and absorbance/fluorescence/luminescence measurement off-deck, with a robot arm facilitating the plate movements.

Figure 2.2.2: Overhead view of the liquid handling instrument deck.





Experiment Options

General

ReactionChemistry

Indicates the reactive group that forms the covalent bond between conjugation samples. Null indicates a custom reaction chemistry.

Default Value: Null

Pattern Description: An object of type or subtype Model[ReactionMechanism] or NHSester, Carbodiimide, or Maleimide or Null.

Programmatic Pattern: ((NHSester | Carbodiimide | Maleimide) | ObjectP[{Model[ReactionMechanism]}]) | Null

Index Matches to: experiment samples

ReactantsStoichiometricCoefficients

The number of reactant molecules that participate in the balanced conjugation reaction.

Default Value: Automatic

Pattern Description: Greater than or equal to 1 and less than or equal to 1000.

Programmatic Pattern: RangeP[1, 1000] | Automatic

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

ProductStoichiometricCoefficient

The number of conjugated molecules created by reaction of input molecules at the ratio indicated by ReactantsStoichiometricCoefficients.

Default Value: Automatic

Pattern Description: Greater than or equal to 1 and less than or equal to 1000.

Programmatic Pattern: RangeP[1, 1000] | Automatic

Index Matches to: experiment samples

ExpectedYield

The percentage of input molecules that will be converted into conjugated product upon completion of the experiment.

Default Value: 100 percent

Pattern Description: Greater than or equal to 0 percent and less than or equal to 100 percent.

Programmatic Pattern: RangeP[0*Percent, 100*Percent]

Index Matches to: experiment samples

ProcessingOrder

The order for processing the conjugation reactions, where Parallel indicates all samples are processed together from activation to quenching. Parallel processing is ideal for experiments with long reaction times where precision is not a concern and/or when instrumentation that can accommodate all reactions simultaneously is used. Batch indicates certain groups of samples are processed together such that all reactions from activation to quenching are completed for a given group before processing the next group of samples. Grouped processing is ideal for experiments where the instrumentation used cannot accommodate all samples simultaneously. Serial indicates samples are processed sequentially such at all reactions from activation to quenching are completed for a given sample before proceeding to the next sample. Sequential processing is ideal when reaction times are short and must be precise and/or the instruments used can only process one sample at a time.

Default Value: Parallel

Pattern Description: Parallel, Batch, or Serial.

Programmatic Pattern: Parallel | Batch | Serial

ProcessingBatchSize

The number of samples to be simultaneously processed when ProcessingOrder is Batch.

Default Value: Automatic

Default Calculation: Automatically set to 1 if ProcessingOrder is Batch otherwise set to Null.

Pattern Description: Greater than or equal to 1 and less than or equal to 1000 in increments of 1 or Null.

Programmatic Pattern: (RangeP[1, 1000, 1] | Automatic) | Null

ProcessingBatches

The groups of sample pools to process together in the experiment, applicable if ProcessingOrder->Batch.

Default Value: Automatic

Default Calculation: Automatically set based on ProcessingOrder and ProcessingBatchSize.

Pattern Description: List of one or more list of one or more list of one or more an object of type or subtype Model[Sample] or Object[Sample] or a prepared sample entries entries entries or Null.

Programmatic Pattern: ({{{(ObjectP[{Model[Sample], Object[Sample]}] | _String)..}..}..} | Automatic) | Null

ReactionVessel

The containers in which samples are mixed with ConjugationReactionBuffer and incubated to covalently link the samples. Indices indicate specific grouping of samples if desired. Solid phase sample containers will be prioritized such that solid phase samples are not moved during conjugation reaction assembly.

Default Value: Automatic

Default Calculation: Automatically set to the smallest tube that will fit all the reaction components.

Pattern Description: An object of type or subtype Object[Container] or Model[Container] or a prepared sample or {Index, Container} or Null.

Programmatic Pattern: (((ObjectP[{Object[Container], Model[Container]}] | _String) | {GreaterEqualP[1, 1], ObjectP[{Model[Container], Object[Container]}] | _String}) | Automatic) | Null

Index Matches to: experiment samples

PreWash

PreWash

Indicates if the solid phase samples should be washed before the activation and/or conjugation reaction.

Default Value: Automatic

Default Calculation: Automatically set to True if any PreWash options are specified, otherwise set to False.

Pattern Description: True or False.

Programmatic Pattern: BooleanP | Automatic

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashMethod

The method used to wash the solid phase samples prior to activation or conjugation.

Default Value: Automatic

Default Calculation: When PreWash is True, automatically set based on PreWash method options. If filtration related options are specified will resolve to Filter, if pellet related options are specified will resolve to Pellet, and if magnetic transfer options are specified will resolve to Magnetic. Otherwise defaults to Pellet.

Pattern Description: Magnetic, Pellet, or Filter or Null.

Programmatic Pattern: ((Magnetic | Pellet | Filter) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashNumberOfWashes

The number of times the sample is repeatedly mixed with wash buffer and wash buffer is removed.

Default Value: Automatic

Default Calculation: Automatically set to 3 if PreWash is True. Otherwise, set to Null.

Pattern Description: Greater than or equal to 0 and less than or equal to 100 in increments of 1 or Null.

Programmatic Pattern: (RangeP[0, 100, 1] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashTime

The length of the PreWash incubation.

Default Value: Automatic

Default Calculation: Automatically, set to 1 Minute when PreWash is True. Otherwise, set to Null.

Pattern Description: Greater than or equal to 0 minutes and less than or equal to 4000 minutes or Null.

Programmatic Pattern: (RangeP[0*Minute, 4000*Minute] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashTemperature

The temperature the sample is held at during the PreWash.

Default Value: Automatic

Default Calculation: Automatically, set to Ambient when PreWash is True. Otherwise, set to Null.

Pattern Description: Ambient or greater than or equal to 0 degrees Celsius and less than or equal to 100 degrees Celsius or Null.

Programmatic Pattern: ((RangeP[0*Celsius, 100*Celsius] | Ambient) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashBuffer

The reagent used to wash the sample prior to activation or conjugation.

Default Value: Automatic

Default Calculation: Automatically set to 1x PBS if PreWash is True. Otherwise, set to Null.

Pattern Description: An object of type or subtype Object[Sample] or Model[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Object[Sample], Model[Sample]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashBufferVolume

The volume of the PreWashBuffer used to wash the sample prior to activation or conjugation.

Default Value: Automatic

Default Calculation: Automatically set to half the sample container volume PreWash is True. Otherwise, set to Null.

Pattern Description: Greater than or equal to 1 microliter and less than or equal to 1000000 microliters or Null.

Programmatic Pattern: (RangeP[1*Microliter, 1000000*Microliter] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashMix

Indicates if the sample should be mixed after dispensing of the wash buffer.

Default Value: Automatic

Default Calculation: Automatically set to True if PreWash is True. Otherwise, set to Null.

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashMixType

The method used to mix the samples and wash buffer. Mixing methods Pipette and Invert with occur only at the start of the PreWashTime. All other methods will occur continuously for the duration of the PreWashTime.

Default Value: Automatic

Default Calculation: Automatically, set to Pipette if PreWashMix is True. Otherwise, set to Null.

Pattern Description: Roll, Vortex, Sonicate, Pipette, Invert, Stir, Shake, Homogenize, Swirl, Disrupt, or Nutate or Null.

Programmatic Pattern: (MixTypeP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashMixVolume

The volume used to mix the samples by pipetting after dispensing of the wash buffer.

Default Value: Automatic

Default Calculation: Automatically set to half the PreWashBufferVolume if PreWashMixType is Pipette. Otherwise, set to Null.

Pattern Description: Greater than or equal to 1 microliter and less than or equal to 1000000 microliters or Null.

Programmatic Pattern: (RangeP[1*Microliter, 1000000*Microliter] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashNumberOfMixes

The number of aspirate and dispense or inversion cycles used to mix the sample during washing.

Default Value: Automatic

Default Calculation: Automatically set to 5 if PreWashMixType is Pipette or Invert. Otherwise, set to Null.

Pattern Description: Greater than or equal to 0 and less than or equal to 100 in increments of 1 or Null.

Programmatic Pattern: (RangeP[0, 100, 1] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashMixRate

The intensity at which the sample and wash buffer are mixed during incubation.

Default Value: Automatic

Default Calculation: Automatically, set to based on the PreWashMixType.

Pattern Description: Greater than or equal to 0 revolutions per minute and less than or equal to 10000 revolutions per minute or Null.

Programmatic Pattern: (RangeP[0*RPM, 10000*RPM] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashFiltrationType

The method that should be used to perform the prewash filtration.

Default Value: Automatic

Default Calculation: Automatically set to a filtration type appropriate for the volume of sample being filtered when PreWashMethod is Filter.

Pattern Description: PeristalticPump, Centrifuge, Vacuum, Syringe, or AirPressure or Null.

Programmatic Pattern: (FiltrationTypeP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashInstrument

The instrument that should be used to perform the PreWash.

Default Value: Automatic

Default Calculation: Will automatically resolve to an instrument appropriate for the PreWashMethod.

Pattern Description: An object of type or subtype Model[Instrument, FilterBlock], Object[Instrument, FilterBlock], Model[Instrument, PeristalticPump], Object[Instrument, PeristalticPump], Model[Instrument, VacuumPump], Object[Instrument, VacuumPump], Model[Instrument, Centrifuge], Object[Instrument, Centrifuge], Model[Instrument, SyringePump], or Object[Instrument, SyringePump] or Null.

Programmatic Pattern: (ObjectP[{Model[Instrument, FilterBlock], Object[Instrument, FilterBlock], Model[Instrument, PeristalticPump], Object[Instrument, PeristalticPump], Model[Instrument, VacuumPump], Object[Instrument, VacuumPump], Model[Instrument, Centrifuge], Object[Instrument, Centrifuge], Model[Instrument, SyringePump], Object[Instrument, SyringePump]}] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashFilter

The filter that should be used to remove impurities from the sample.

Default Value: Automatic

Default Calculation: Automatically set to a filter appropriate for the filtration type and instrument if PreWashMethod is Filter.

Pattern Description: An object of type or subtype Model[Container, Plate, Filter], Object[Container, Plate, Filter], Model[Container, Vessel, Filter], Object[Container, Vessel, Filter], Model[Item, Filter], or Object[Item, Filter] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Container, Plate, Filter], Object[Container, Plate, Filter], Model[Container, Vessel, Filter], Object[Container, Vessel, Filter], Model[Item, Filter], Object[Item, Filter]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashFilterStorageCondition

The conditions under which any filters used for PreWash should be stored after the wash is completed.

Default Value: Disposal

Pattern Description: Storage Object or Storage Type.

Programmatic Pattern: (SampleStorageTypeP | Disposal) | ObjectP[Model[StorageCondition]]

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashFilterMembraneMaterial

The material from which the filtration membrane should be made of.

Default Value: Automatic

Default Calculation: Will automatically resolve to PES or to the MembraneMaterial of Filter if it is specified.

Pattern Description: Cellulose, Cotton, Polyethylene, Polypropylene, PTFE, Nylon, PES, PLUS, PVDF, GlassFiber, GHP, UHMWPE, EPDM, DuraporePVDF, GxF, ZebaDesaltingResin, NickelResin, Silica, or HLB or Null.

Programmatic Pattern: (FilterMembraneMaterialP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashPrefilterMembraneMaterial

The material from which the prefilter filtration membrane should be made of.

Default Value: Automatic

Default Calculation: Will automatically resolve to GxF if a prefilter pore size is specified.

Pattern Description: Cellulose, Cotton, Polyethylene, Polypropylene, PTFE, Nylon, PES, PLUS, PVDF, GlassFiber, GHP, UHMWPE, EPDM, DuraporePVDF, GxF, ZebaDesaltingResin, NickelResin, Silica, or HLB or Null.

Programmatic Pattern: (FilterMembraneMaterialP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashFilterPoreSize

The pore size of the filter; all particles larger than this should be removed during the filtration.

Default Value: Automatic

Default Calculation: Will automatically resolve to .22 Micron or to the PoreSize of Filter if it is specified. Will automatically resolve to Null if MolecularWeightCutoff is specified.

Pattern Description: 0.008 micrometers, 0.1 micrometers, 0.2 micrometers, 0.22 micrometers, 0.45 micrometers, 1. micrometer, 1.1 micrometers, 2.5 micrometers, 6. micrometers, 20. micrometers, 30. micrometers, or 100. micrometers or Null.

Programmatic Pattern: (FilterSizeP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashFilterMolecularWeightCutoff

The molecular weight cutoff of the filter; all particles larger than this should be removed during the filtration.

Default Value: Automatic

Default Calculation: Will automatically resolve to Null or to the MolecularWeightCutoff of Filter if it is specified.

Pattern Description: 3 kilograms per mole, 3. kilograms per mole, 10 kilograms per mole, 10. kilograms per mole, 30 kilograms per mole, 30. kilograms per mole, 40 kilograms per mole, 40. kilograms per mole, 50 kilograms per mole, 50. kilograms per mole, 100 kilograms per mole, 100. kilograms per mole, 300 kilograms per mole, 300. kilograms per mole, 7 kilograms per mole, 7. kilograms per mole, 40 kilograms per mole, 40. kilograms per mole, or 30.8328 kilograms per mole or Null.

Programmatic Pattern: (FilterMolecularWeightCutoffP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashPrefilterPoreSize

The pore size of the prefilter; all particles larger than this should be removed during the filtration.

Default Value: Automatic

Default Calculation: Will automatically resolve to .45 Micron if a prefilter membrane material is specified

Pattern Description: 0.008 micrometers, 0.1 micrometers, 0.2 micrometers, 0.22 micrometers, 0.45 micrometers, 1. micrometer, 1.1 micrometers, 2.5 micrometers, 6. micrometers, 20. micrometers, 30. micrometers, or 100. micrometers or Null.

Programmatic Pattern: (FilterSizeP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashFiltrationSyringe

The syringe used to force that sample through a filter.

Default Value: Automatic

Default Calculation: Resolves to an syringe appropriate to the volume of sample being filtered.

Pattern Description: An object of type or subtype Model[Container, Syringe] or Object[Container, Syringe] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Container, Syringe], Object[Container, Syringe]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashSterileFiltration

Indicates if the filtration of the samples should be done in a sterile environment.

Default Value: False

Pattern Description: True or False.

Programmatic Pattern: BooleanP

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashFilterHousing

The filter housing that should be used to hold the filter membrane when filtration is performed using a standalone filter membrane, or a filter plate for vacuum filtration..

Default Value: Automatic

Default Calculation: Resolves to an housing capable of holding the size of the membrane being used, if filter with Membrane FilterType is being used, or a filter plate for vacuum filtration..

Pattern Description: An object of type or subtype Model[Instrument, FilterHousing], Object[Instrument, FilterHousing], Model[Instrument, FilterBlock], or Object[Instrument, FilterBlock] or Null.

Programmatic Pattern: (ObjectP[{Model[Instrument, FilterHousing], Object[Instrument, FilterHousing], Model[Instrument, FilterBlock], Object[Instrument, FilterBlock]}] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashCentrifugationIntensity

The rotational speed or force at which the samples will be centrifuged during PreWash.

Default Value: Automatic

Default Calculation: Will automatically resolve to 2000 GravitationalAcceleration if filtering type is Centrifuge or PreWashMethod is Pellet.

Pattern Description: Force or Speed or Null.

Programmatic Pattern: ((GreaterP[0*RPM] | GreaterP[0*GravitationalAcceleration]) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashCentrifugationTime

The amount of time for which the samples will be centrifuged during PreWash.

Default Value: Automatic

Default Calculation: Will automatically resolve to 5 Minute if filtering type is Centrifuge or PreWashMethod is Pellet.

Pattern Description: Greater than 0 minutes or Null.

Programmatic Pattern: (GreaterP[0*Minute] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashCentrifugationTemperature

The temperature at which the centrifuge chamber will be held while the samples are being centrifuged during PreWash.

Default Value: Automatic

Default Calculation: Will automatically resolve to 22 Celsius if filtering type is Centrifuge or PreWashMethod is Pellet.

Pattern Description: Greater than or equal to -10 degrees Celsius or Null.

Programmatic Pattern: (GreaterEqualP[-10*Celsius] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashMagnetizationRack

The magnetized rack that the source/intermediate container will be placed in during the PreWash.

Default Value: Automatic

Default Calculation: Automatically set to a magnetized rack that can hold the source/intermediate container, if PreWashMethod->Magnetic is specified.

Pattern Description: An object of type or subtype Model[Container, Rack] or Object[Container, Rack] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Container, Rack], Object[Container, Rack]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashResuspension

Indicates if samples should be resuspended in PreWashResuspensionBuffer after washing and before activation or conjugation reactions.

Default Value: Automatic

Default Calculation: Automatically set based on PreWash and prewash resuspension options. If PreWash is False, set to False.

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashResuspensionTime

The length of the PreWashResuspension incubation.

Default Value: Automatic

Default Calculation: Automatically, set to 1 Minute when PreWashResuspension is True. Otherwise, set to Null.

Pattern Description: Greater than or equal to 0 minutes and less than or equal to 4000 minutes or Null.

Programmatic Pattern: (RangeP[0*Minute, 4000*Minute] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashResuspensionTemperature

The temperature the sample is held at during the PreWashResuspension.

Default Value: Automatic

Default Calculation: Automatically, set to Ambient when PreWashResuspension is True. Otherwise, set to Null.

Pattern Description: Ambient or greater than or equal to 0 degrees Celsius and less than or equal to 100 degrees Celsius or Null.

Programmatic Pattern: ((RangeP[0*Celsius, 100*Celsius] | Ambient) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashResuspensionDiluent

The reagent used to resuspend the sample after the PreWash complete.

Default Value: Automatic

Default Calculation: Automatically set to 1xPBS if PreWashResuspension is True. Otherwise, set to Null.

Pattern Description: An object of type or subtype Object[Sample] or Model[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Object[Sample], Model[Sample]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashResuspensionDiluentVolume

The volume of the PreWashResuspensionDiluent used to resuspend the sample after the PreWash is complete.

Default Value: Automatic

Default Calculation: Automatically set to the original sample volume PreWashResuspension is True. Otherwise, set to Null.

Pattern Description: Greater than or equal to 1 microliter and less than or equal to 1000000 microliters or Null.

Programmatic Pattern: (RangeP[1*Microliter, 1000000*Microliter] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashResuspensionMix

Indicates if the sample should be mixed by pipetting after dispensing of the resuspension buffer.

Default Value: Automatic

Default Calculation: Automatically set to True if PreWashResuspenion is True. Otherwise, set to Null.

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashResuspensionMixType

The method used to mix the resuspended samples in PreWashResuspensionDiluent.

Default Value: Automatic

Default Calculation: Automatically, set to Pipette if PreWashResuspensionMix is True. Otherwise, set to Null.

Pattern Description: Roll, Vortex, Sonicate, Pipette, Invert, Stir, Shake, Homogenize, Swirl, Disrupt, or Nutate or Null.

Programmatic Pattern: (MixTypeP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashResuspensionMixVolume

The volume used to mix the samples by pipetting after dispensing of the PreWashResuspensionDiluent.

Default Value: Automatic

Default Calculation: Automatically set to half the PreWashResuspensionDiluentVolume if PreWashResuspensionMixType is Pipette. Otherwise, set to Null.

Pattern Description: Greater than or equal to 1 microliter and less than or equal to 1000000 microliters or Null.

Programmatic Pattern: (RangeP[1*Microliter, 1000000*Microliter] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashResuspensionNumberOfMixes

The number of aspirate and dispense cycles or inversions cycles used to mix the sample during resuspension.

Default Value: Automatic

Default Calculation: Automatically set to 5 if PreWashResuspensionMixType is Pipette or Invert. Otherwise, set to Null.

Pattern Description: Greater than or equal to 0 and less than or equal to 100 in increments of 1 or Null.

Programmatic Pattern: (RangeP[0, 100, 1] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PreWashResuspensionMixRate

The rate at which the sample and PreWashResuspensionDiluent are mixed during incubation.

Default Value: Automatic

Default Calculation: Automatically, set to 800 RPM based on PreWashResuspensionMixType.

Pattern Description: Greater than or equal to 0 revolutions per minute and less than or equal to 10000 revolutions per minute or Null.

Programmatic Pattern: (RangeP[0*RPM, 10000*RPM] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

Activation

Activate

Indicates if functional groups on each of the conjugation samples need to be activated of modified prior to conjugation.

Default Value: Automatic

Default Calculation: Automatically set to True if ReactionChemistry is Maleimide and the sample is a protein or if any Activation options are specified.

Pattern Description: True or False.

Programmatic Pattern: BooleanP | Automatic

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

ActivationReactionVolume

The total volume of the activation reaction including ActivationSampleVolume, ActivationReagentVolume, and ActivationDiluentVolume.

Default Value: Automatic

Default Calculation: When Activate is True, automatically set to 0.5 mL. Otherwise, set to Null.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 1000 milliliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 1000*Milliliter] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

TargetActivationSampleConcentration

The desired concentration of each conjugation sample in the activation reaction.

Default Value: Automatic

Default Calculation: Automatically, set to 1 mg/mL when Activate is True. Otherwise, set to Null.

Pattern Description: Greater than 0 milligrams per milliliter or greater than 0 micromolar or Null.

Programmatic Pattern: ((GreaterP[0*(Milligram/Milliliter)] | GreaterP[0*Micromolar]) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

ActivationSampleVolume

The volume of each conjugation sample that is used in the activation reaction.

Default Value: Automatic

Default Calculation: When Activate is True, automatically set to the sample volume that results in TargetActivationSampleConcentration when added to ActivationReactionVolume. Otherwise, set to Null.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 1000 milliliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 1000*Milliliter] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

ActivationReagent

The reagent that activates or modifies functional groups on the corresponding sample in preparation for conjugation. For Maleimide reactions, 100X molar excess of TCEP is recommended to reduce protein cysteine disulfide bonds.

Default Value: Automatic

Default Calculation: Automatically set to 10mM TCEP in 50mM Tris-HCL pH 7.5 if ReactionChemsitry is Maleimide. TCEP unlike other reducing agents does not contain thiols that may interfere with conjugation, therefore it is not necessary to remove this reagent prior to the maleimide conjugation reaction.

Pattern Description: An object of type or subtype Object[Sample] or Model[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Object[Sample], Model[Sample]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

TargetActivationReagentConcentration

The desired concentration of ActivationReagent in the activation reaction.

Default Value: Automatic

Default Calculation: Automatically, set to 1 mg/mL when Activate is True. Otherwise, set to Null.

Pattern Description: Greater than 0 milligrams per milliliter or greater than 0 micromolar or Null.

Programmatic Pattern: ((GreaterP[0*(Milligram/Milliliter)] | GreaterP[0*Micromolar]) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

ActivationReagentVolume

The volume of the ActivationReagent that is used in the activation reaction.

Default Value: Automatic

Default Calculation: When Activate is True, automatically set to the volume of ActivationReagent that results in TargetActivationReagentConcentration when added to ActivationVolume. Otherwise, set to Null.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 1000 milliliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 1000*Milliliter] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

ActivationDiluent

The reagent used to dilute the ActivationSampleVolume + ActivationReagentVolume to the final ActivationReactionVolume.

Default Value: Automatic

Default Calculation: Automatically set to 1X PBS.

Pattern Description: An object of type or subtype Object[Sample] or Model[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Object[Sample], Model[Sample]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

ActivationDiluentVolume

The volume of the ActivationDiluent that is used in the activation reaction.

Default Value: Automatic

Default Calculation: When Activate is True, automatically set to the difference in volume between (ActivationVolume + ActivationReagentVolume) and ActivationReactionVolume. Otherwise, set to Null.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 1000 milliliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 1000*Milliliter] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

ActivationContainer

The containers in which each sample is activated by mixing and incubation with ActivationReagent and ActivationDiluent, with indices indicating specific grouping of samples if desired. If Null, the activation reaction will occur in the sample's current container.

Default Value: Null

Pattern Description: An object of type or subtype Object[Container] or Model[Container] or a prepared sample or {Index, Container} or Null.

Programmatic Pattern: ((ObjectP[{Object[Container], Model[Container]}] | _String) | {GreaterEqualP[1, 1], ObjectP[{Model[Container], Object[Container]}] | _String}) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

ActivationTime

The length of the activation reaction incubation. To mix the activation reagent and sample immediately prior to addition to the conjugation reaction set this value to zero.

Default Value: Automatic

Default Calculation: Automatically, set to 15 Minutes when Activate is True. Otherwise, set to Null.

Pattern Description: Greater than or equal to 0 minutes and less than or equal to 4000 minutes or Null.

Programmatic Pattern: (RangeP[0*Minute, 4000*Minute] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

ActivationTemperature

The temperature the sample is held at during the activation reaction.

Default Value: Automatic

Default Calculation: Automatically, set to Ambient when Activate is True and ActivationTime is greater than zero. Otherwise, set to Null.

Pattern Description: Ambient or greater than or equal to 0 degrees Celsius and less than or equal to 100 degrees Celsius or Null.

Programmatic Pattern: ((RangeP[0*Celsius, 100*Celsius] | Ambient) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

ActivationMix

Indicates if the activation reaction should be mixed.

Default Value: Automatic

Default Calculation: Automatically, set to True when Activate is True. Otherwise, set to Null.

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

ActivationMixType

The method used to mix the activation reaction before or during incubation. Mixing methods Pipette and Invert with occur only at the start of the ActivationTime. All other methods will occur continuously for the duration of the ActivationTime.

Default Value: Automatic

Default Calculation: Automatically, set to Shake if Activate is True. Otherwise, set to Null.

Pattern Description: Roll, Vortex, Sonicate, Pipette, Invert, Stir, Shake, Homogenize, Swirl, Disrupt, or Nutate or Null.

Programmatic Pattern: (MixTypeP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

ActivationMixRate

The rate at which the activation reaction is mixed during incubation.

Default Value: Automatic

Default Calculation: Automatically, set to 800 RPM based on ActivationMixType.

Pattern Description: Greater than or equal to 0 revolutions per minute and less than or equal to 10000 revolutions per minute or Null.

Programmatic Pattern: (RangeP[0*RPM, 10000*RPM] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

ActivationMixVolume

The volume used to mix the activation reaction.

Default Value: Automatic

Default Calculation: Automatically, set to half the activation reaction volume if ActivationMixType is Pipette. Otherwise, set to Null.

Pattern Description: Greater than or equal to 1 microliter and less than or equal to 50000 microliters or Null.

Programmatic Pattern: (RangeP[1*Microliter, 50000*Microliter] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

ActivationNumberOfMixes

The number of aspirate and dispense cycles or inversion cycles used to mix the activation reaction.

Default Value: Automatic

Default Calculation: Automatically, set to 5 if ActivationMixType is Pipette or Invert. Otherwise, set to Null.

Pattern Description: Greater than or equal to 0 and less than or equal to 100 in increments of 1 or Null.

Programmatic Pattern: (RangeP[0, 100, 1] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationWash

Indicates if samples should be washed after the activation reaction and before the conjugation reaction.

Default Value: Automatic

Default Calculation: Automatically set to True if Activate is True and the sample is a solid phase support. Otherwise, set to Null.

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationWashMethod

The method used to wash the samples after activation.

Default Value: Automatic

Default Calculation: If PostActivationWash is True, automatically set based on method specific PostActivationWash options.

Pattern Description: Magnetic, Pellet, or Filter or Null.

Programmatic Pattern: ((Magnetic | Pellet | Filter) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationNumberOfWashes

The number of times the sample is repeatedly mixed with wash buffer and wash buffer is removed.

Default Value: Automatic

Default Calculation: Automatically set to 3 if PostActivationWash is True. Otherwise, set to Null.

Pattern Description: Greater than or equal to 0 and less than or equal to 100 in increments of 1 or Null.

Programmatic Pattern: (RangeP[0, 100, 1] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationWashTime

The length of the post activation wash incubation.

Default Value: Automatic

Default Calculation: Automatically, set to 1 Minute when PostActivationWash is True. Otherwise, set to Null.

Pattern Description: Greater than or equal to 0 minutes and less than or equal to 4000 minutes or Null.

Programmatic Pattern: (RangeP[0*Minute, 4000*Minute] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationWashTemperature

The temperature the sample is held at during the post-activation wash.

Default Value: Automatic

Default Calculation: Automatically, set to Ambient when PostActivationWash is True. Otherwise, set to Null.

Pattern Description: Ambient or greater than or equal to 0 degrees Celsius and less than or equal to 100 degrees Celsius or Null.

Programmatic Pattern: ((RangeP[0*Celsius, 100*Celsius] | Ambient) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationWashBuffer

The reagent used to wash the sample after the activation reaction is complete.

Default Value: Automatic

Default Calculation: Automatically set to 1X PBS if PostActivationWash is True. Otherwise, set to Null.

Pattern Description: An object of type or subtype Object[Sample] or Model[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Object[Sample], Model[Sample]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationWashBufferVolume

The volume of the PostActivationWashBuffer used to wash the sample after the activation reaction is complete.

Default Value: Automatic

Default Calculation: Automatically set to 200 Microliter PostActivationWash is True. Otherwise, set to Null.

Pattern Description: Greater than or equal to 1 microliter and less than or equal to 1000000 microliters or Null.

Programmatic Pattern: (RangeP[1*Microliter, 1000000*Microliter] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationWashMix

Indicates if the sample should be mixed after dispensing of the wash buffer.

Default Value: Automatic

Default Calculation: Automatically set to True if PostActivationWash is True. Otherwise, set to Null.

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationWashMixType

The method used to mix the samples and wash buffer. Mixing methods Pipette and Invert with occur only at the start of the PostActivationWashTime. All other methods will occur continuously for the duration of the PostActivationWashTime.

Default Value: Automatic

Default Calculation: Automatically, set to Pipette if PostActivationWash is True. Otherwise, set to Null.

Pattern Description: Roll, Vortex, Sonicate, Pipette, Invert, Stir, Shake, Homogenize, Swirl, Disrupt, or Nutate or Null.

Programmatic Pattern: (MixTypeP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationWashMixVolume

The volume used to mix the samples by pipetting after dispensing of the wash buffer.

Default Value: Automatic

Default Calculation: Automatically set to half the PostActivationWashBufferVolume if PostActivationWashMixType is Pipette. Otherwise, set to Null.

Pattern Description: Greater than or equal to 1 microliter and less than or equal to 1000000 microliters or Null.

Programmatic Pattern: (RangeP[1*Microliter, 1000000*Microliter] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationWashNumberOfMixes

The number of aspirate and dispense cycles or inversion cycles used to mix the sample during washing.

Default Value: Automatic

Default Calculation: Automatically set to 5 if PostActivationWashMixType is Pipette or Invert. Otherwise, set to Null.

Pattern Description: Greater than or equal to 0 and less than or equal to 100 in increments of 1 or Null.

Programmatic Pattern: (RangeP[0, 100, 1] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationWashMixRate

The rate at which the sample and wash buffer are mixed during incubation.

Default Value: Automatic

Default Calculation: Automatically, set to 800 RPM based on PostActivationWashMixType.

Pattern Description: Greater than or equal to 0 revolutions per minute and less than or equal to 10000 revolutions per minute or Null.

Programmatic Pattern: (RangeP[0*RPM, 10000*RPM] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationWashFiltrationType

The method that should be used to perform the PostActivationwash filtration.

Default Value: Automatic

Default Calculation: Automatically set to a filtration type appropriate for the volume of sample being filtered when PostActivationWashMethod is Filter.

Pattern Description: PeristalticPump, Centrifuge, Vacuum, Syringe, or AirPressure or Null.

Programmatic Pattern: (FiltrationTypeP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationWashInstrument

The instrument that should be used to perform the PostActivationWash.

Default Value: Automatic

Default Calculation: Will automatically resolve to an instrument appropriate for the PostActivationWashMethod.

Pattern Description: An object of type or subtype Model[Instrument, FilterBlock], Object[Instrument, FilterBlock], Model[Instrument, PeristalticPump], Object[Instrument, PeristalticPump], Model[Instrument, VacuumPump], Object[Instrument, VacuumPump], Model[Instrument, Centrifuge], Object[Instrument, Centrifuge], Model[Instrument, SyringePump], or Object[Instrument, SyringePump] or Null.

Programmatic Pattern: (ObjectP[{Model[Instrument, FilterBlock], Object[Instrument, FilterBlock], Model[Instrument, PeristalticPump], Object[Instrument, PeristalticPump], Model[Instrument, VacuumPump], Object[Instrument, VacuumPump], Model[Instrument, Centrifuge], Object[Instrument, Centrifuge], Model[Instrument, SyringePump], Object[Instrument, SyringePump]}] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationWashFilter

The filter that should be used to remove impurities from the sample.

Default Value: Automatic

Default Calculation: Automatically set to a filter appropriate for the filtration type and instrument if PostActivationWashType is Filter.

Pattern Description: An object of type or subtype Model[Container, Plate, Filter], Object[Container, Plate, Filter], Model[Container, Vessel, Filter], Object[Container, Vessel, Filter], Model[Item, Filter], or Object[Item, Filter] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Container, Plate, Filter], Object[Container, Plate, Filter], Model[Container, Vessel, Filter], Object[Container, Vessel, Filter], Model[Item, Filter], Object[Item, Filter]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationWashFilterStorageCondition

The conditions under which any filters used for PostActivationWash should be stored after the wash is completed.

Default Value: Disposal

Pattern Description: Storage Object or Storage Type.

Programmatic Pattern: (SampleStorageTypeP | Disposal) | ObjectP[Model[StorageCondition]]

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationWashFilterMembraneMaterial

The material from which the filtration membrane should be made of.

Default Value: Automatic

Default Calculation: Will automatically resolve to PES or to the MembraneMaterial of Filter if it is specified.

Pattern Description: Cellulose, Cotton, Polyethylene, Polypropylene, PTFE, Nylon, PES, PLUS, PVDF, GlassFiber, GHP, UHMWPE, EPDM, DuraporePVDF, GxF, ZebaDesaltingResin, NickelResin, Silica, or HLB or Null.

Programmatic Pattern: (FilterMembraneMaterialP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationWashPrefilterMembraneMaterial

The material from which the Prefilter filtration membrane should be made of.

Default Value: Automatic

Default Calculation: Will automatically resolve to GxF if a Prefilter pore size is specified.

Pattern Description: Cellulose, Cotton, Polyethylene, Polypropylene, PTFE, Nylon, PES, PLUS, PVDF, GlassFiber, GHP, UHMWPE, EPDM, DuraporePVDF, GxF, ZebaDesaltingResin, NickelResin, Silica, or HLB or Null.

Programmatic Pattern: (FilterMembraneMaterialP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationWashFilterPoreSize

The pore size of the filter; all particles larger than this should be removed during the filtration.

Default Value: Automatic

Default Calculation: Will automatically resolve to .22 Micron or to the PoreSize of Filter if it is specified. Will automatically resolve to Null if MolecularWeightCutoff is specified.

Pattern Description: 0.008 micrometers, 0.1 micrometers, 0.2 micrometers, 0.22 micrometers, 0.45 micrometers, 1. micrometer, 1.1 micrometers, 2.5 micrometers, 6. micrometers, 20. micrometers, 30. micrometers, or 100. micrometers or Null.

Programmatic Pattern: (FilterSizeP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationWashFilterMolecularWeightCutoff

The molecular weight cutoff of the filter; all particles larger than this should be removed during the filtration.

Default Value: Automatic

Default Calculation: Will automatically resolve to Null or to the MolecularWeightCutoff of Filter if it is specified.

Pattern Description: 3 kilograms per mole, 3. kilograms per mole, 10 kilograms per mole, 10. kilograms per mole, 30 kilograms per mole, 30. kilograms per mole, 40 kilograms per mole, 40. kilograms per mole, 50 kilograms per mole, 50. kilograms per mole, 100 kilograms per mole, 100. kilograms per mole, 300 kilograms per mole, 300. kilograms per mole, 7 kilograms per mole, 7. kilograms per mole, 40 kilograms per mole, 40. kilograms per mole, or 30.8328 kilograms per mole or Null.

Programmatic Pattern: (FilterMolecularWeightCutoffP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationWashPrefilterPoreSize

The pore size of the Prefilter; all particles larger than this should be removed during the filtration.

Default Value: Automatic

Default Calculation: Will automatically resolve to .45 Micron if a Prefilter membrane material is specified

Pattern Description: 0.008 micrometers, 0.1 micrometers, 0.2 micrometers, 0.22 micrometers, 0.45 micrometers, 1. micrometer, 1.1 micrometers, 2.5 micrometers, 6. micrometers, 20. micrometers, 30. micrometers, or 100. micrometers or Null.

Programmatic Pattern: (FilterSizeP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationWashFiltrationSyringe

The syringe used to force that sample through a filter.

Default Value: Automatic

Default Calculation: Resolves to an syringe appropriate to the volume of sample being filtered.

Pattern Description: An object of type or subtype Model[Container, Syringe] or Object[Container, Syringe] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Container, Syringe], Object[Container, Syringe]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationWashSterileFiltration

Indicates if the filtration of the samples should be done in a sterile environment.

Default Value: False

Pattern Description: True or False.

Programmatic Pattern: BooleanP

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationWashFilterHousing

The filter housing that should be used to hold the filter membrane when filtration is performed using a standalone filter membrane, or a filter plate for vacuum filtration..

Default Value: Automatic

Default Calculation: Resolves to an housing capable of holding the size of the membrane being used, if filter with Membrane FilterType is being used, or a filter plate for vacuum filtration..

Pattern Description: An object of type or subtype Model[Instrument, FilterHousing], Object[Instrument, FilterHousing], Model[Instrument, FilterBlock], or Object[Instrument, FilterBlock] or Null.

Programmatic Pattern: (ObjectP[{Model[Instrument, FilterHousing], Object[Instrument, FilterHousing], Model[Instrument, FilterBlock], Object[Instrument, FilterBlock]}] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationWashCentrifugationIntensity

The rotational speed or force at which the samples will be centrifuged during PostActivationWash.

Default Value: Automatic

Default Calculation: Will automatically resolve to 2000 GravitationalAcceleration if filtering type is Centrifuge or PostActivationWashMethod is Pellet.

Pattern Description: Force or Speed or Null.

Programmatic Pattern: ((GreaterP[0*RPM] | GreaterP[0*GravitationalAcceleration]) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationWashCentrifugationTime

The amount of time for which the samples will be centrifuged during PostActivationWash.

Default Value: Automatic

Default Calculation: Will automatically resolve to 5 Minute if filtering type is Centrifuge or PostActivationWashMethod is Pellet.

Pattern Description: Greater than 0 minutes or Null.

Programmatic Pattern: (GreaterP[0*Minute] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationWashCentrifugationTemperature

The temperature at which the centrifuge chamber will be held while the samples are being centrifuged during PostActivationWash.

Default Value: Automatic

Default Calculation: Will automatically resolve to 22 Celsius if filtering type is Centrifuge or PostActivationWashMethod is Pellet.

Pattern Description: Greater than or equal to -10 degrees Celsius or Null.

Programmatic Pattern: (GreaterEqualP[-10*Celsius] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationWashMagnetizationRack

The magnetized rack that the source/intermediate container will be placed in during the PostActivationWash.

Default Value: Automatic

Default Calculation: Automatically set to a magnetized rack that can hold the source/intermediate container, if PostActivationWashMethod->Magnetic is specified.

Pattern Description: An object of type or subtype Model[Container, Rack] or Object[Container, Rack] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Container, Rack], Object[Container, Rack]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationResuspension

Indicates if samples should be resuspended in PostActivationResuspensionDiluent after washing and before the conjugation reaction.

Default Value: Automatic

Default Calculation: Automatically set based on other PostActivationResuspension.

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationResuspensionTime

The length of the PostActivationResuspension incubation.

Default Value: Automatic

Default Calculation: Automatically, set to 1 Minute when PostActivationResuspension is True. Otherwise, set to Null.

Pattern Description: Greater than or equal to 0 minutes and less than or equal to 4000 minutes or Null.

Programmatic Pattern: (RangeP[0*Minute, 4000*Minute] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationResuspensionTemperature

The temperature the sample is held at during the PostActivationResuspension.

Default Value: Automatic

Default Calculation: Automatically, set to Ambient when PostActivationResuspension is True. Otherwise, set to Null.

Pattern Description: Ambient or greater than or equal to 0 degrees Celsius and less than or equal to 100 degrees Celsius or Null.

Programmatic Pattern: ((RangeP[0*Celsius, 100*Celsius] | Ambient) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationResuspensionDiluent

The reagent used to resuspend the sample after the PostActivationWash complete.

Default Value: Automatic

Default Calculation: Automatically set to 1X PBS if PostActivationWash is True. Otherwise, set to Null.

Pattern Description: An object of type or subtype Object[Sample] or Model[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Object[Sample], Model[Sample]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationResuspensionDiluentVolume

The volume of the PostActivationResuspensionDiluent used to resuspend the sample after the PostActivationWash is complete.

Default Value: Automatic

Default Calculation: Automatically set to 200 Microliter PostActivationWash is True. Otherwise, set to Null.

Pattern Description: Greater than or equal to 1 microliter and less than or equal to 1000000 microliters or Null.

Programmatic Pattern: (RangeP[1*Microliter, 1000000*Microliter] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationResuspensionMix

Indicates if the sample should be mixed after dispensing of the resuspension buffer.

Default Value: Automatic

Default Calculation: Automatically set to True if PostActivationWash is True. Otherwise, set to Null.

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationResuspensionMixType

The method used to resuspend the samples in PostActivationResuspensionDiluent.

Default Value: Automatic

Default Calculation: Automatically, set to Pipette if PostActivationResuspensionMix is True. Otherwise, set to Null.

Pattern Description: Roll, Vortex, Sonicate, Pipette, Invert, Stir, Shake, Homogenize, Swirl, Disrupt, or Nutate or Null.

Programmatic Pattern: (MixTypeP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationResuspensionMixVolume

The volume used to mix the samples by pipetting after dispensing of the PostActivationResuspensionDiluent.

Default Value: Automatic

Default Calculation: Automatically set to half the PostActivationResuspensionDiluentVolume if PostActivationResuspensionMixType is Pipette. Otherwise, set to Null.

Pattern Description: Greater than or equal to 1 microliter and less than or equal to 1000000 microliters or Null.

Programmatic Pattern: (RangeP[1*Microliter, 1000000*Microliter] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationResuspensionNumberOfMixes

The number of aspirate and dispense cycles or inversion cycles used to mix the sample during resuspension.

Default Value: Automatic

Default Calculation: Automatically set to 5 if PostActivationResuspensionMixType is Pipette or Invert. Otherwise, set to Null.

Pattern Description: Greater than or equal to 0 and less than or equal to 100 in increments of 1 or Null.

Programmatic Pattern: (RangeP[0, 100, 1] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PostActivationResuspensionMixRate

The rate at which the sample and PostActivationResuspensionDiluent are mixed during incubation.

Default Value: Automatic

Default Calculation: Automatically, set to 800 RPM based on PostActivationResuspensionMixType.

Pattern Description: Greater than or equal to 0 revolutions per minute and less than or equal to 10000 revolutions per minute or Null.

Programmatic Pattern: (RangeP[0*RPM, 10000*RPM] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

ActivationSamplesOutStorageCondition

The conditions under which any leftover samples from the activation reaction are stored after the samples are transferred to the ConjugationContainer.

Default Value: Automatic

Default Calculation: Automatically set to Disposal.

Pattern Description: {AmbientStorage, Refrigerator, Freezer, DeepFreezer, CryogenicStorage, YeastIncubation, YeastShakingIncubation, BacterialIncubation, BacterialShakingIncubation, MammalianIncubation, ViralIncubation, CrystalIncubation, AcceleratedTesting, IntermediateTesting, LongTermTesting, UVVisLightTesting} or Disposal or Null.

Programmatic Pattern: ((Alternatives[SampleStorageTypeP | Disposal]) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

Conjugation

ConjugationReactionVolume

The total volume of the conjugation reaction including ConjugationAmount and ConjugationReactionBufferVolume.

Default Value: Automatic

Default Calculation: Automatically, set to the full volume of the conjugate samples or 500 uL if all samples are solid.

Pattern Description: Greater than or equal to 1 microliter and less than or equal to 1000000 microliters.

Programmatic Pattern: RangeP[1*Microliter, 1000000*Microliter] | Automatic

Index Matches to: experiment samples

TargetConjugationSampleConcentration

The desired concentration of each sample in the total ConjugationReactionVolume.

Default Value: Automatic

Default Calculation: Automatically set to the concentration given by ConjugationAmount/ConjugationReactionVolume.

Pattern Description: Greater than 0 milligrams per milliliter or greater than 0 micromolar or Null.

Programmatic Pattern: ((GreaterP[0*(Milligram/Milliliter)] | GreaterP[0*Micromolar]) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

ConjugationAmount

The volume or mass of each sample that is used in the conjugation reaction. By default the entire volume or mass of the sample is used. If ConjugationAmount is All and the sample is solid, the aqueous samples and reagents for the conjugation reaction will be transferred into the solid sample container.

Default Value: All

Pattern Description: All or greater than or equal to 0 micrograms and less than or equal to 50 grams or greater than or equal to 0 microliters and less than or equal to 50 milliliters.

Programmatic Pattern: RangeP[0*Microliter, 50*Milliliter] | RangeP[0*Microgram, 50*Gram] | All

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

ConjugationReactionBuffer

Indicates the reagent used to dilute or resuspend the conjugate sample during the conjugation reaction.

Default Value: Null

Pattern Description: An object of type or subtype Object[Sample] or Model[Sample] or a prepared sample or Null.

Programmatic Pattern: (ObjectP[{Object[Sample], Model[Sample]}] | _String) | Null

Index Matches to: experiment samples

ConjugationReactionBufferVolume

The volume of the ConjugationReactionBuffer that is mixed with the corresponding conjugation samples to assemble the conjugation reaction.

Default Value: Automatic

Default Calculation: Automatically, set to the conjugation reaction volume such that the sample is diluted 2-fold.

Pattern Description: Greater than or equal to 1 microliter and less than or equal to 1000000 microliters or Null.

Programmatic Pattern: (RangeP[1*Microliter, 1000000*Microliter] | Automatic) | Null

Index Matches to: experiment samples

ConcentratedConjugationReactionBuffer

Indicates the concentrated reagent used to dilute or resuspend the conjugate sample during the conjugation reaction.

Default Value: Null

Pattern Description: An object of type or subtype Object[Sample] or Model[Sample] or a prepared sample or Null.

Programmatic Pattern: (ObjectP[{Object[Sample], Model[Sample]}] | _String) | Null

Index Matches to: experiment samples

ConcentratedConjugationReactionBufferDilutionFactor

The relative amount that the ConcentratedConjugateBuffer should be diluted prior to use in the conjugation reaction.

Default Value: Automatic

Default Calculation: Automatically, set to 1 when ConcentratedConjugationBuffer is specified.

Pattern Description: Greater than or equal to 1 and less than or equal to 5000 or Null.

Programmatic Pattern: (RangeP[1, 5000] | Automatic) | Null

Index Matches to: experiment samples

ConjugationReactionBufferDiluent

The diluent used to decrease the ConcentratedConjugationBuffer concentration by ConjugationBufferDilutionFactor prior to use in the conjugation reaction.

Default Value: Automatic

Default Calculation: If ConcentratedConjugationReactionBuffer is specified, automatically resolves to 1x PBS.

Pattern Description: An object of type or subtype Object[Sample] or Model[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Object[Sample], Model[Sample]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

ConjugationDiluentVolume

The volume of the ConjugationBufferDiluent that is mixed with ConcentratedConjugateBuffer prior to use in the conjugation reaction.

Default Value: Automatic

Default Calculation: Automatically set to the ConjugationBufferVolume*(1 - ConjugationReactionBufferVolume/ConcentratedConjugationReactionBufferDilutionFactor).

Pattern Description: Greater than or equal to 1 microliter and less than or equal to 1000000 microliters or Null.

Programmatic Pattern: (RangeP[1*Microliter, 1000000*Microliter] | Automatic) | Null

Index Matches to: experiment samples

ConjugationTime

The incubation time of the conjugation reaction.

Default Value: Automatic

Default Calculation: Automatically set based on the reaction chemistry to a literature-based recommended value.

Pattern Description: Greater than or equal to 1 minute and less than or equal to 4000 minutes.

Programmatic Pattern: RangeP[1*Minute, 4000*Minute] | Automatic

Index Matches to: experiment samples

ConjugationTemperature

The incubation temperature of the conjugation reaction.

Default Value: Automatic

Default Calculation: Automatically set based on the reaction chemistry to a literature-based recommended value.

Pattern Description: Ambient or greater than or equal to 0 degrees Celsius and less than or equal to 100 degrees Celsius.

Programmatic Pattern: (RangeP[0*Celsius, 100*Celsius] | Ambient) | Automatic

Index Matches to: experiment samples

ConjugationMix

Indicates if the conjugation reaction should be mixed.

Default Value: True

Pattern Description: True or False.

Programmatic Pattern: BooleanP

Index Matches to: experiment samples

ConjugationMixType

The method used to mix the samples for conjugation. Mixing methods Pipette and Invert with occur only at the start of the ConjugationTime. All other methods will occur continuously for the duration of the ConjugationTime.

Default Value: Automatic

Default Calculation: Automatically, set to based on mix options when ConjugationMix is True. Otherwise, set to Null.

Pattern Description: Roll, Vortex, Sonicate, Pipette, Invert, Stir, Shake, Homogenize, Swirl, Disrupt, or Nutate or Null.

Programmatic Pattern: (MixTypeP | Automatic) | Null

Index Matches to: experiment samples

ConjugationMixVolume

The volume used to mix the samples by pipetting at the start of the conjugation reaction.

Default Value: Automatic

Default Calculation: Automatically set to half the ConjugationReactionVolume if ConjugationMixType is Pipette. Otherwise, set to Null.

Pattern Description: Greater than or equal to 1 microliter and less than or equal to 1000000 microliters or Null.

Programmatic Pattern: (RangeP[1*Microliter, 1000000*Microliter] | Automatic) | Null

Index Matches to: experiment samples

ConjugationNumberOfMixes

The number of aspirate and dispense or inversion cycles used to mix the sample at the start of the conjugation reaction.

Default Value: Automatic

Default Calculation: Automatically set to 5 if ConjugationMixType is Pipette or Invert. Otherwise, set to Null.

Pattern Description: Greater than or equal to 0 and less than or equal to 100 in increments of 1 or Null.

Programmatic Pattern: (RangeP[0, 100, 1] | Automatic) | Null

Index Matches to: experiment samples

ConjugationMixRate

The rate at which the samples are mixed during ConjugationTime.

Default Value: Automatic

Default Calculation: Automatically, set to 800 RPM based on ConjugationMixType.

Pattern Description: Greater than or equal to 0 revolutions per minute and less than or equal to 10000 revolutions per minute or Null.

Programmatic Pattern: (RangeP[0*RPM, 10000*RPM] | Automatic) | Null

Index Matches to: experiment samples

Quenching

QuenchConjugation

Indicates if the conjugation reaction should be quenched after the desired incubation time.

Default Value: Automatic

Default Calculation: Automatically, set based on the ReactionChemistry.

Pattern Description: True or False.

Programmatic Pattern: BooleanP | Automatic

Index Matches to: experiment samples

PredrainReactionMixture

Indicates if the aqueous reaction reagents should be removed from any solid phase samples or precipitates after the conjugation reaction is complete to prepare the sample for quenching or subsequent workup.

Default Value: False

Pattern Description: True or False.

Programmatic Pattern: BooleanP

Index Matches to: experiment samples

PredrainMethod

The method used to separate the aqueous and solid reaction components when PredrainReactionMixture is True.

Default Value: Automatic

Default Calculation: Automatically set to Pellet if PredrainReactionMixture is True. Otherwise set to Null.

Pattern Description: Pellet or Magnetic or Null.

Programmatic Pattern: ((Pellet | Magnetic) | Automatic) | Null

Index Matches to: experiment samples

PredrainInstrument

The instrument that should be used to perform the PredrainReactionReagents.

Default Value: Automatic

Default Calculation: Will automatically resolve to an instrument appropriate for the PredrainMethod.

Pattern Description: An object of type or subtype Model[Instrument, Centrifuge] or Object[Instrument, Centrifuge] or Null.

Programmatic Pattern: (ObjectP[{Model[Instrument, Centrifuge], Object[Instrument, Centrifuge]}] | Automatic) | Null

Index Matches to: experiment samples

PredrainCentrifugationIntensity

The rotational speed or force at which the samples will be centrifuged during PredrainReactionReagents.

Default Value: Automatic

Default Calculation: Will automatically resolve to 2000 GravitationalAcceleration if PredrainMethod is Pellet.

Pattern Description: Force or Speed or Null.

Programmatic Pattern: ((GreaterP[0*RPM] | GreaterP[0*GravitationalAcceleration]) | Automatic) | Null

Index Matches to: experiment samples

PredrainCentrifugationTime

The amount of time for which the samples will be centrifuged during PredrainReactionReagents.

Default Value: Automatic

Default Calculation: Will automatically resolve to 5 Minute if PredrainMethod is Pellet.

Pattern Description: Greater than 0 minutes or Null.

Programmatic Pattern: (GreaterP[0*Minute] | Automatic) | Null

Index Matches to: experiment samples

PredrainTemperature

The temperature at which the samples will be held during centrifugation or magnetic separation when PredrainReactionReagents is True.

Default Value: Automatic

Default Calculation: Will automatically resolve to Ambient if PredrainReactionReagents is True.

Pattern Description: Ambient or greater than or equal to -10 degrees Celsius or Null.

Programmatic Pattern: ((GreaterEqualP[-10*Celsius] | Ambient) | Automatic) | Null

Index Matches to: experiment samples

PredrainMagnetizationRack

The magnetized rack that the source/intermediate container will be placed in during the PredrainReactionMixture.

Default Value: Automatic

Default Calculation: Automatically set to a magnetized rack that can hold the source/intermediate container, if PredrainMethod->Magnetic is specified.

Pattern Description: An object of type or subtype Model[Container, Rack] or Object[Container, Rack] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Container, Rack], Object[Container, Rack]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

PredrainMagnetizationTime

The time that the source sample should be left on the magnetic rack until the magnetic components are settled at the side of the container.

Default Value: Automatic

Default Calculation: Automatically set to 15 Second if PredrainMethod->Magnetic. Otherwise, set to Null.

Pattern Description: Greater than or equal to 0 minutes and less than or equal to 72 hours or Null.

Programmatic Pattern: (RangeP[0*Minute, $MaxExperimentTime] | Automatic) | Null

Index Matches to: experiment samples

QuenchReactionVolume

The total volume of the quenching reaction including the ConjugationReactionVolume + QuenchReagentVolume.

Default Value: Automatic

Default Calculation: Automatically, based on the QuenchReagentDilutionFactor. Otherwise, set to Null.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 1000 milliliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 1000*Milliliter] | Automatic) | Null

Index Matches to: experiment samples

QuenchReagent

The reagent that should be used to stop the conjugation reaction and render any unbound functional groups inactive.

Default Value: Automatic

Default Calculation: Automatically set based on the ReactionChemistry.

Pattern Description: An object of type or subtype Object[Sample] or Model[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Object[Sample], Model[Sample]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

QuenchReagentDilutionFactor

The relative amount that the QuenchReagent should be diluted in QuenchReaction to reach its final active concentration.

Default Value: Automatic

Default Calculation: Automatically, set to 1 when QuenchReagent is specified.

Pattern Description: Greater than or equal to 1 and less than or equal to 5000 or Null.

Programmatic Pattern: (RangeP[1, 5000] | Automatic) | Null

Index Matches to: experiment samples

QuenchReagentVolume

The volume of the QuenchReagent that is used in the quenching reaction.

Default Value: Automatic

Default Calculation: Automatically, set to 1 uL QuenchReagent when QuenchConjugation is True. Otherwise, set to Null.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 1000 milliliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 1000*Milliliter] | Automatic) | Null

Index Matches to: experiment samples

QuenchTime

The length of the quenching reaction incubation.

Default Value: Automatic

Default Calculation: Automatically, set to 5 Minutes when QuenchConjugation is True. Otherwise, set to Null.

Pattern Description: Greater than or equal to 1 minute and less than or equal to 4000 minutes or Null.

Programmatic Pattern: (RangeP[1*Minute, 4000*Minute] | Automatic) | Null

Index Matches to: experiment samples

QuenchTemperature

The temperature of the sample is held at during the quenching reaction.

Default Value: Automatic

Default Calculation: Automatically, set to Ambient QuenchConjugation is True. Otherwise, set to Null.

Pattern Description: Ambient or greater than or equal to 0 degrees Celsius and less than or equal to 100 degrees Celsius or Null.

Programmatic Pattern: ((RangeP[0*Celsius, 100*Celsius] | Ambient) | Automatic) | Null

Index Matches to: experiment samples

QuenchMix

Indicates if the quenching reaction should be mixed during incubation.

Default Value: Automatic

Default Calculation: Automatically, set to True QuenchConjugation is True. Otherwise, set to Null.

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

Index Matches to: experiment samples

QuenchMixType

The method used to mix the samples with QuenchReagent. Mixing methods Pipette and Invert with occur only at the start of the QuenchTime. All other methods will occur continuously for the duration of the QuenchTime.

Default Value: Automatic

Default Calculation: Automatically, set to Shake if QuenchMix is True. Otherwise, set to Null.

Pattern Description: Roll, Vortex, Sonicate, Pipette, Invert, Stir, Shake, Homogenize, Swirl, Disrupt, or Nutate or Null.

Programmatic Pattern: (MixTypeP | Automatic) | Null

Index Matches to: experiment samples

QuenchMixVolume

The volume used to mix the sample and QuenchReagent by pipetting at the start of the quench reaction.

Default Value: Automatic

Default Calculation: Automatically set to half the QuenchReactionVolume if QuenchMixType is Pipette. Otherwise, set to Null.

Pattern Description: Greater than or equal to 1 microliter and less than or equal to 1000000 microliters or Null.

Programmatic Pattern: (RangeP[1*Microliter, 1000000*Microliter] | Automatic) | Null

Index Matches to: experiment samples

QuenchNumberOfMixes

The number of aspirate and dispense or inversion cycles used to mix the sample at the start of the quench reaction.

Default Value: Automatic

Default Calculation: Automatically set to 5 if QuenchMixType is Pipette or Invert. Otherwise, set to Null.

Pattern Description: Greater than or equal to 0 and less than or equal to 100 in increments of 1 or Null.

Programmatic Pattern: (RangeP[0, 100, 1] | Automatic) | Null

Index Matches to: experiment samples

QuenchMixRate

The rate at which the samples are mixed during QuenchTime.

Default Value: Automatic

Default Calculation: Automatically, set to 800 RPM based on QuenchMixType.

Pattern Description: Greater than or equal to 0 revolutions per minute and less than or equal to 10000 revolutions per minute or Null.

Programmatic Pattern: (RangeP[0*RPM, 10000*RPM] | Automatic) | Null

Index Matches to: experiment samples

Post-Conjugation Workup

PostConjugationWorkup

Indicates if samples should be processed after the conjugation reaction.

Default Value: False

Pattern Description: True or False.

Programmatic Pattern: BooleanP

Index Matches to: experiment samples

PostConjugationWorkupMethod

The method used to process the samples after conjugation.

Default Value: Automatic

Default Calculation: Automatically set to Pellet if PostConjugationWorkup is True.

Pattern Description: Magnetic, Pellet, or Filter or Null.

Programmatic Pattern: ((Magnetic | Pellet | Filter) | Automatic) | Null

Index Matches to: experiment samples

PostConjugationWorkupBuffer

Indicates the reagent used to process the sample after the conjugation and quenching reactions are complete.

Default Value: Null

Pattern Description: An object of type or subtype Object[Sample] or Model[Sample] or a prepared sample or Null.

Programmatic Pattern: (ObjectP[{Object[Sample], Model[Sample]}] | _String) | Null

Index Matches to: experiment samples

PostConjugationWorkupBufferVolume

The volume of the PostConjugationWashBuffer used to wash the sample after the conjugation reaction is complete.

Default Value: Null

Pattern Description: Greater than or equal to 1 microliter and less than or equal to 1000000 microliters or Null.

Programmatic Pattern: RangeP[1*Microliter, 1000000*Microliter] | Null

Index Matches to: experiment samples

PostConjugationWorkupIncubationTime

The incubation time of the sample with the PostConjugationWorkupBuffer.

Default Value: Null

Pattern Description: Greater than or equal to 0 minutes and less than or equal to 4000 minutes or Null.

Programmatic Pattern: RangeP[0*Minute, 4000*Minute] | Null

Index Matches to: experiment samples

PostConjugationWorkupIncubationTemperature

The temperature the sample is held at during the PostConjugationWorkupIncubationTime.

Default Value: Null

Pattern Description: Ambient or greater than or equal to 0 degrees Celsius and less than or equal to 100 degrees Celsius or Null.

Programmatic Pattern: (RangeP[0*Celsius, 100*Celsius] | Ambient) | Null

Index Matches to: experiment samples

PostConjugationWorkupMix

Indicates if the sample should be mixed the PostConjugationWorkupBuffer.

Default Value: Automatic

Default Calculation: Automatically set to True if PostConjugationWorkupBuffer is specified. Otherwise, set to False.

Pattern Description: True or False.

Programmatic Pattern: BooleanP | Automatic

Index Matches to: experiment samples

PostConjugationWorkupMixType

The method used to mix the samples and PostConjugationWorkupBuffer.

Default Value: Automatic

Default Calculation: Automatically, set to Pipette if PostConjugationWorkup is True. Otherwise, set to Null.

Pattern Description: Roll, Vortex, Sonicate, Pipette, Invert, Stir, Shake, Homogenize, Swirl, Disrupt, or Nutate or Null.

Programmatic Pattern: (MixTypeP | Automatic) | Null

Index Matches to: experiment samples

PostConjugationWorkupMixVolume

The volume used to mix the samples after dispensing of the PostConjugationWorkupBuffer.

Default Value: Automatic

Default Calculation: Automatically set to half the sample volume if PostConjugationWorkupMix is True. Otherwise, set to Null.

Pattern Description: Greater than or equal to 1 microliter and less than or equal to 1000000 microliters or Null.

Programmatic Pattern: (RangeP[1*Microliter, 1000000*Microliter] | Automatic) | Null

Index Matches to: experiment samples

PostConjugationWorkupNumberOfMixes

The number of aspirate and dispense cycles or inversion cycles used to mix the sample prior to PostConjugationWorkupIncubationTime.

Default Value: Automatic

Default Calculation: Automatically set to 5 if PostConjugationWorkupMix is True. Otherwise, set to Null.

Pattern Description: Greater than or equal to 0 and less than or equal to 100 in increments of 1 or Null.

Programmatic Pattern: (RangeP[0, 100, 1] | Automatic) | Null

Index Matches to: experiment samples

PostConjugationWorkupMixRate

The rate at which the sample and PostConjugationWorkupBuffer are mixed during incubation.

Default Value: Automatic

Default Calculation: Automatically, set to 800 RPM based on PostConjugationWorkupMixType.

Pattern Description: Greater than or equal to 0 revolutions per minute and less than or equal to 10000 revolutions per minute or Null.

Programmatic Pattern: (RangeP[0*RPM, 10000*RPM] | Automatic) | Null

Index Matches to: experiment samples

PostConjugationFiltrationType

The method that should be used to perform the filtration.

Default Value: Automatic

Default Calculation: Will automatically resolve to a filtration type appropriate for the volume of sample being filtered.

Pattern Description: PeristalticPump, Centrifuge, Vacuum, Syringe, or AirPressure or Null.

Programmatic Pattern: (FiltrationTypeP | Automatic) | Null

Index Matches to: experiment samples

PostConjugationWorkupInstrument

The instrument that should be used to perform the PostConjugationWorkup.

Default Value: Automatic

Default Calculation: Will automatically resolve to an instrument appropriate for the PostConjugationWorkupMethod.

Pattern Description: An object of type or subtype Model[Instrument, FilterBlock], Object[Instrument, FilterBlock], Model[Instrument, PeristalticPump], Object[Instrument, PeristalticPump], Model[Instrument, VacuumPump], Object[Instrument, VacuumPump], Model[Instrument, Centrifuge], Object[Instrument, Centrifuge], Model[Instrument, SyringePump], or Object[Instrument, SyringePump] or Null.

Programmatic Pattern: (ObjectP[{Model[Instrument, FilterBlock], Object[Instrument, FilterBlock], Model[Instrument, PeristalticPump], Object[Instrument, PeristalticPump], Model[Instrument, VacuumPump], Object[Instrument, VacuumPump], Model[Instrument, Centrifuge], Object[Instrument, Centrifuge], Model[Instrument, SyringePump], Object[Instrument, SyringePump]}] | Automatic) | Null

Index Matches to: experiment samples

PostConjugationFilter

The filter that should be used to remove impurities from the sample.

Default Value: Automatic

Default Calculation: Will automatically resolve to a filter appropriate for the filtration type and instrument.

Pattern Description: An object of type or subtype Model[Container, Plate, Filter], Object[Container, Plate, Filter], Model[Container, Vessel, Filter], Object[Container, Vessel, Filter], Model[Item, Filter], or Object[Item, Filter] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Container, Plate, Filter], Object[Container, Plate, Filter], Model[Container, Vessel, Filter], Object[Container, Vessel, Filter], Model[Item, Filter], Object[Item, Filter]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

PostConjugationFilterStorageCondition

The conditions under which any filters used by this experiment should be stored after the protocol is completed.

Default Value: Disposal

Pattern Description: Storage Object or Storage Type.

Programmatic Pattern: (SampleStorageTypeP | Disposal) | ObjectP[Model[StorageCondition]]

Index Matches to: experiment samples

PostConjugationFilterMembraneMaterial

The material from which the filtration membrane should be made of.

Default Value: Automatic

Default Calculation: Will automatically resolve to PES or to the MembraneMaterial of Filter if it is specified.

Pattern Description: Cellulose, Cotton, Polyethylene, Polypropylene, PTFE, Nylon, PES, PLUS, PVDF, GlassFiber, GHP, UHMWPE, EPDM, DuraporePVDF, GxF, ZebaDesaltingResin, NickelResin, Silica, or HLB or Null.

Programmatic Pattern: (FilterMembraneMaterialP | Automatic) | Null

Index Matches to: experiment samples

PostConjugationPrefilterMembraneMaterial

The material from which the prefilter filtration membrane should be made of.

Default Value: Automatic

Default Calculation: Will automatically resolve to GxF if a prefilter pore size is specified.

Pattern Description: Cellulose, Cotton, Polyethylene, Polypropylene, PTFE, Nylon, PES, PLUS, PVDF, GlassFiber, GHP, UHMWPE, EPDM, DuraporePVDF, GxF, ZebaDesaltingResin, NickelResin, Silica, or HLB or Null.

Programmatic Pattern: (FilterMembraneMaterialP | Automatic) | Null

Index Matches to: experiment samples

PostConjugationFilterPoreSize

The pore size of the filter; all particles larger than this should be removed during the filtration.

Default Value: Automatic

Default Calculation: Will automatically resolve to .22 Micron or to the PoreSize of Filter if it is specified. Will automatically resolve to Null if MolecularWeightCutoff is specified.

Pattern Description: 0.008 micrometers, 0.1 micrometers, 0.2 micrometers, 0.22 micrometers, 0.45 micrometers, 1. micrometer, 1.1 micrometers, 2.5 micrometers, 6. micrometers, 20. micrometers, 30. micrometers, or 100. micrometers or Null.

Programmatic Pattern: (FilterSizeP | Automatic) | Null

Index Matches to: experiment samples

PostConjugationFilterMolecularWeightCutoff

The molecular weight cutoff of the filter; all particles larger than this should be removed during the filtration.

Default Value: Automatic

Default Calculation: Will automatically resolve to Null or to the MolecularWeightCutoff of Filter if it is specified.

Pattern Description: 3 kilograms per mole, 3. kilograms per mole, 10 kilograms per mole, 10. kilograms per mole, 30 kilograms per mole, 30. kilograms per mole, 40 kilograms per mole, 40. kilograms per mole, 50 kilograms per mole, 50. kilograms per mole, 100 kilograms per mole, 100. kilograms per mole, 300 kilograms per mole, 300. kilograms per mole, 7 kilograms per mole, 7. kilograms per mole, 40 kilograms per mole, 40. kilograms per mole, or 30.8328 kilograms per mole or Null.

Programmatic Pattern: (FilterMolecularWeightCutoffP | Automatic) | Null

Index Matches to: experiment samples

PostConjugationPrefilterPoreSize

The pore size of the prefilter; all particles larger than this should be removed during the filtration.

Default Value: Automatic

Default Calculation: Will automatically resolve to .45 Micron if a prefilter membrane material is specified

Pattern Description: 0.008 micrometers, 0.1 micrometers, 0.2 micrometers, 0.22 micrometers, 0.45 micrometers, 1. micrometer, 1.1 micrometers, 2.5 micrometers, 6. micrometers, 20. micrometers, 30. micrometers, or 100. micrometers or Null.

Programmatic Pattern: (FilterSizeP | Automatic) | Null

Index Matches to: experiment samples

PostConjugationFiltrationSyringe

The syringe used to force that sample through a filter.

Default Value: Automatic

Default Calculation: Resolves to an syringe appropriate to the volume of sample being filtered.

Pattern Description: An object of type or subtype Model[Container, Syringe] or Object[Container, Syringe] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Container, Syringe], Object[Container, Syringe]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

PostConjugationSterileFiltration

Indicates if the filtration of the samples should be done in a sterile environment.

Default Value: False

Pattern Description: True or False.

Programmatic Pattern: BooleanP

Index Matches to: experiment samples

PostConjugationFilterHousing

The filter housing that should be used to hold the filter membrane when filtration is performed using a standalone filter membrane, or a filter plate for vacuum filtration.

Default Value: Automatic

Default Calculation: Resolves to an housing capable of holding the size of the membrane being used, if filter with Membrane FilterType is being used, or a filter plate for vacuum filtration.

Pattern Description: An object of type or subtype Model[Instrument, FilterHousing], Object[Instrument, FilterHousing], Model[Instrument, FilterBlock], or Object[Instrument, FilterBlock] or Null.

Programmatic Pattern: (ObjectP[{Model[Instrument, FilterHousing], Object[Instrument, FilterHousing], Model[Instrument, FilterBlock], Object[Instrument, FilterBlock]}] | Automatic) | Null

Index Matches to: experiment samples

PostConjugationCentrifugationIntensity

The rotational speed or force at which the samples will be centrifuged during PostConjugationWorkup.

Default Value: Automatic

Default Calculation: Will automatically resolve to 2000 GravitationalAcceleration if filtering type is Centrifuge or PostConjugationWorkupMethod is Pellet.

Pattern Description: Force or Speed or Null.

Programmatic Pattern: ((GreaterP[0*RPM] | GreaterP[0*GravitationalAcceleration]) | Automatic) | Null

Index Matches to: experiment samples

PostConjugationCentrifugationTime

The amount of time for which the samples will be centrifuged during PostConjugationWorkup.

Default Value: Automatic

Default Calculation: Will automatically resolve to 5 Minute if filtering type is Centrifuge or PostConjugationWorkupMethod is Pellet.

Pattern Description: Greater than 0 minutes or Null.

Programmatic Pattern: (GreaterP[0*Minute] | Automatic) | Null

Index Matches to: experiment samples

PostConjugationCentrifugationTemperature

The temperature at which the centrifuge chamber will be held while the samples are being centrifuged during PostConjugationWorkup.

Default Value: Automatic

Default Calculation: Will automatically resolve to 22 Celsius if filtering type is Centrifuge or PostConjugationWorkupMethod is Pellet.

Pattern Description: Greater than or equal to -10 degrees Celsius or Null.

Programmatic Pattern: (GreaterEqualP[-10*Celsius] | Automatic) | Null

Index Matches to: experiment samples

PostConjugationMagnetizationRack

The magnetized rack that the source/intermediate container will be placed in during the PostConjugationWorkup.

Default Value: Automatic

Default Calculation: Automatically set to a magnetized rack that can hold the source/intermediate container, if PostConjugationWorkupMethod->Magnetic is specified.

Pattern Description: An object of type or subtype Model[Container, Rack] or Object[Container, Rack] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Container, Rack], Object[Container, Rack]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

PostConjugationResuspension

Indicates whether the sample should be resuspended in PostConjugationResuspensionDiluent after PostConjugationWorkup is complete.

Default Value: Automatic

Default Calculation: Automatically set to True if any resuspension options are specified. Otherwise set to False.

Pattern Description: True or False.

Programmatic Pattern: BooleanP | Automatic

Index Matches to: experiment samples

PostConjugationResuspensionDiluent

The reagent used to resuspend the sample after the PostConjugationWorkup is complete.

Default Value: Automatic

Default Calculation: Automatically set to 1X PBS if PostConjugationResuspension is True. Otherwise, set to Null.

Pattern Description: An object of type or subtype Object[Sample] or Model[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Object[Sample], Model[Sample]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

PostConjugationResuspensionDiluentVolume

The volume of the PostConjugationResuspensionDiluent used to resuspend the sample after the PostConjugationWash is complete.

Default Value: Automatic

Default Calculation: Automatically set to 200 Microliter PostConjugationResuspension is True. Otherwise, set to Null.

Pattern Description: Greater than or equal to 1 microliter and less than or equal to 1000000 microliters or Null.

Programmatic Pattern: (RangeP[1*Microliter, 1000000*Microliter] | Automatic) | Null

Index Matches to: experiment samples

PostConjugationResuspensionMix

Indicates if the sample should be mixed after dispensing of the resuspension buffer.

Default Value: Automatic

Default Calculation: Automatically set to True if PostConjugationResuspension is True. Otherwise, set to Null.

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

Index Matches to: experiment samples

PostConjugationResuspensionMixType

The method used to mix the samples with PostConjugationResuspensionDiluent.

Default Value: Automatic

Default Calculation: Automatically, set to Pipette if PostConjugationResuspensionMix is True. Otherwise, set to Null.

Pattern Description: Roll, Vortex, Sonicate, Pipette, Invert, Stir, Shake, Homogenize, Swirl, Disrupt, or Nutate or Null.

Programmatic Pattern: (MixTypeP | Automatic) | Null

Index Matches to: experiment samples

PostConjugationResuspensionMixRate

The rate at which the sample and PostConjugationResuspensionDiluent are mixed during incubation.

Default Value: Automatic

Default Calculation: Automatically, set to 800 RPM based on PostConjugationResuspensionMixType.

Pattern Description: Greater than or equal to 0 revolutions per minute and less than or equal to 10000 revolutions per minute or Null.

Programmatic Pattern: (RangeP[0*RPM, 10000*RPM] | Automatic) | Null

Index Matches to: experiment samples

PostConjugationResuspensionMixVolume

The volume used to mix the samples by pipetting after dispensing of the resuspension buffer.

Default Value: Automatic

Default Calculation: Automatically set to half the PostConjugationResuspensionDiluentVolume if PostConjugationResuspensionMix is True. Otherwise, set to Null.

Pattern Description: Greater than or equal to 1 microliter and less than or equal to 1000000 microliters or Null.

Programmatic Pattern: (RangeP[1*Microliter, 1000000*Microliter] | Automatic) | Null

Index Matches to: experiment samples

PostConjugationResuspensionNumberOfMixes

The number of aspirate and dispense cycles used to mix the sample during resuspension.

Default Value: Automatic

Default Calculation: Automatically set to 5 if PostConjugationResuspensionMix is True. Otherwise, set to Null.

Pattern Description: Greater than or equal to 0 and less than or equal to 100 in increments of 1 or Null.

Programmatic Pattern: (RangeP[0, 100, 1] | Automatic) | Null

Index Matches to: experiment samples

PostConjugationResuspensionMixUntilDissolved

Indicates if the sample should be mixed in an attempt to completed dissolve any solid components following addition of liquid.

Default Value: Automatic

Default Calculation: Automatically set to True if MaxMixTime or MaxNumberOfMixes are specified, or False otherwise.

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

Index Matches to: experiment samples

PostConjugationResuspensionMaxNumberOfMixes

The maximum number of aspirate and dispense cycles used to mix the sample during resuspension.

Default Value: Automatic

Default Calculation: Automatically set to 50 if PostConjugationResuspensionMixUntilDissolved is True. Otherwise, set to Null.

Pattern Description: Greater than or equal to 0 and less than or equal to 100 in increments of 1 or Null.

Programmatic Pattern: (RangeP[0, 100, 1] | Automatic) | Null

Index Matches to: experiment samples

PostConjugationResuspensionTime

The duration for which the sample should be mixed/incubated following addition of liquid.

Default Value: Automatic

Default Calculation: Automatically set to 30 minutes unless MixType is set to Pipette or Invert, in which case it is set to Null.

Pattern Description: Greater than or equal to 0 hours and less than or equal to 72 hours or Null.

Programmatic Pattern: (RangeP[0*Hour, 72*Hour] | Automatic) | Null

Index Matches to: experiment samples

PostConjugationResuspensionMaxTime

The maximum duration for which the samples should be mixed/incubated in an attempt to dissolve any solid components following addition of liquid.

Default Value: Automatic

Default Calculation: Automatically set based on the MixType if PostConjugationResuspensionMixUntilDissolved is set to True. If PostConjugationResuspensionMixUntilDissolved is False, resolves to Null.

Pattern Description: Greater than or equal to 1 second and less than or equal to 72 hours or Null.

Programmatic Pattern: (RangeP[1*Second, 72*Hour] | Automatic) | Null

Index Matches to: experiment samples

PostConjugationResuspensionTemperature

Temperature at which the sample should be incubated during PostConjugationResuspension.

Default Value: Automatic

Pattern Description: Ambient or greater than or equal to 22 degrees Celsius and less than or equal to 500 degrees Celsius or Null.

Programmatic Pattern: ((RangeP[22*Celsius, $MaxIncubationTemperature] | Ambient) | Automatic) | Null

Index Matches to: experiment samples

Post Experiment

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

Pattern Description: Cellulose, Cotton, Polyethylene, Polypropylene, PTFE, Nylon, PES, PLUS, PVDF, GlassFiber, GHP, UHMWPE, EPDM, DuraporePVDF, GxF, ZebaDesaltingResin, NickelResin, Silica, or HLB or Null.

Programmatic Pattern: (FilterMembraneMaterialP | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

PrefilterMaterial

The material from which the prefilter filtration membrane should be made of to remove impurities from the SamplesIn prior to starting the experiment.

Default Value: Automatic

Default Calculation: By default, no prefiltration is performed on samples, even when Filter->True.

Pattern Description: Cellulose, Cotton, Polyethylene, Polypropylene, PTFE, Nylon, PES, PLUS, PVDF, GlassFiber, GHP, UHMWPE, EPDM, DuraporePVDF, GxF, ZebaDesaltingResin, NickelResin, Silica, or HLB or Null.

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

Aliquoting

Aliquot

Indicates if aliquots should be taken from the SamplesIn and transferred into new AliquotSamples used in lieu of the SamplesIn for the experiment. Note that if NumberOfReplicates is specified this indicates that the input samples will also be aliquoted that number of times. Note that Aliquoting (if specified) occurs after any Sample Preparation (if specified).

Default Value: Automatic

Pattern Description: True or False.

Programmatic Pattern: BooleanP | Automatic

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

AliquotAmount

The amount of a sample that should be transferred from the input samples into aliquots.

Default Value: Automatic

Default Calculation: Automatically set as the smaller between the current sample volume and the maximum volume of the destination container if a liquid, or the current Mass or Count if a solid or counted item, respectively.

Pattern Description: All or Count or Count or Mass or Volume or Null.

Programmatic Pattern: ((RangeP[1*Microliter, 20*Liter] | RangeP[1*Milligram, 20*Kilogram] | GreaterP[0*Unit, 1*Unit] | GreaterP[0., 1.] | All) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

TargetConcentration

The desired final concentration of analyte in the AliquotSamples after dilution of aliquots of SamplesIn with the ConcentratedBuffer and BufferDiluent which should be used in lieu of the SamplesIn for the experiment.

Default Value: Automatic

Default Calculation: Automatically calculated based on aliquot and buffer volumes.

Pattern Description: Greater than 0 molar or greater than 0 grams per liter or Null.

Programmatic Pattern: ((GreaterP[0*Molar] | GreaterP[0*(Gram/Liter)]) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

TargetConcentrationAnalyte

The substance whose final concentration is attained with the TargetConcentration option.

Default Value: Automatic

Default Calculation: Automatically set to the first value in the Analytes field of the input sample, or, if not populated, to the first analyte in the Composition field of the input sample, or if none exist, the first identity model of any kind in the Composition field.

Pattern Description: An object of type or subtype Model[Molecule], Model[Molecule, cDNA], Model[Molecule, Oligomer], Model[Molecule, Transcript], Model[Molecule, Protein], Model[Molecule, Protein, Antibody], Model[Molecule, Carbohydrate], Model[Molecule, Polymer], Model[Resin], Model[Resin, SolidPhaseSupport], Model[Lysate], Model[ProprietaryFormulation], Model[Virus], Model[Cell], Model[Cell, Mammalian], Model[Cell, Bacteria], Model[Cell, Yeast], Model[Tissue], Model[Material], or Model[Species] or Null.

Programmatic Pattern: (ObjectP[IdentityModelTypes] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

AssayVolume

The desired total volume of the aliquoted sample plus dilution buffer.

Default Value: Automatic

Default Calculation: Automatically determined based on Volume and TargetConcentration option values.

Pattern Description: Greater than or equal to 1 microliter and less than or equal to 20 liters or Null.

Programmatic Pattern: (RangeP[1*Microliter, 20*Liter] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

ConcentratedBuffer

The concentrated buffer which should be diluted by the BufferDilutionFactor in the final solution (i.e., the combination of the sample, ConcentratedBuffer, and BufferDiluent). The ConcentratedBuffer and BufferDiluent will be combined and then mixed with the sample, where the combined volume of these buffers is the difference between the AliquotAmount and the total AssayVolume.

Default Value: Automatic

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

BufferDilutionFactor

The dilution factor by which the concentrated buffer should be diluted in the final solution (i.e., the combination of the sample, ConcentratedBuffer, and BufferDiluent). The ConcentratedBuffer and BufferDiluent will be combined and then mixed with the sample, where the combined volume of these buffers is the difference between the AliquotAmount and the total AssayVolume.

Default Value: Automatic

Default Calculation: If ConcentratedBuffer is specified, automatically set to the ConcentratedBufferDilutionFactor of that sample; otherwise, set to Null.

Pattern Description: Greater than or equal to 1 in increments of 1 or Null.

Programmatic Pattern: (GreaterEqualP[1, 1] | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

BufferDiluent

The buffer used to dilute the aliquot sample such that ConcentratedBuffer is diluted by BufferDilutionFactor in the final solution. The ConcentratedBuffer and BufferDiluent will be combined and then mixed with the sample, where the combined volume of these buffers is the difference between the AliquotAmount and the total AssayVolume.

Default Value: Automatic

Default Calculation: Automatically resolves to Model[Sample, "Milli-Q water"] if ConcentratedBuffer is specified; otherwise, resolves to Null.

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

AssayBuffer

The buffer that should be added to any aliquots requiring dilution, where the volume of this buffer added is the difference between the AliquotAmount and the total AssayVolume.

Default Value: Automatic

Default Calculation: Automatically resolves to Model[Sample, "Milli-Q water"] if ConcentratedBuffer is not specified; otherwise, resolves to Null.

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

AliquotSampleStorageCondition

The non-default conditions under which any aliquot samples generated by this experiment should be stored after the protocol is completed.

Default Value: Automatic

Pattern Description: {AmbientStorage, Refrigerator, Freezer, DeepFreezer, CryogenicStorage, YeastIncubation, YeastShakingIncubation, BacterialIncubation, BacterialShakingIncubation, MammalianIncubation, ViralIncubation, CrystalIncubation, AcceleratedTesting, IntermediateTesting, LongTermTesting, UVVisLightTesting} or Disposal or Null.

Programmatic Pattern: ((SampleStorageTypeP | Disposal) | Automatic) | Null

Index Matches to: experiment samples

Nested Index Matches to: experiment samples

DestinationWell

The desired position in the corresponding AliquotContainer in which the aliquot samples will be placed.

Default Value: Automatic

Default Calculation: Automatically resolves to A1 in containers with only one position. For plates, fills wells in the order provided by the function AllWells.

Pattern Description: Any well from A1 to H12 or list of one or more any well from A1 to H12 or any well from A1 to H12 entries or list of one or more any well from A1 to H12 or any well from A1 to H12 or list of one or more any well from A1 to H12 or any well from A1 to H12 entries entries or Null.

Programmatic Pattern: ((WellPositionP | {((Automatic | Null) | WellPositionP)..} | {(((Automatic | Null) | WellPositionP) | {((Automatic | Null) | WellPositionP)..})..}) | Automatic) | Null

AliquotContainer

The desired type of container that should be used to prepare and house the aliquot samples, with indices indicating grouping of samples in the same plates, if desired. This option will resolve to be the length of the SamplesIn * NumberOfReplicates.

Default Value: Automatic

Default Calculation: Automatically set as the PreferredContainer for the AssayVolume of the sample. For plates, attempts to fill all wells of a single plate with the same model before aliquoting into the next.

Pattern Description: An object of type or subtype Model[Container] or Object[Container] or a prepared sample or Automatic or Null or {Index, Container} or list of one or more an object of type or subtype Model[Container] or Object[Container] or a prepared sample or Automatic or Null entries or list of one or more Automatic or Null or {Index, Container} entries or list of one or more list of one or more an object of type or subtype Model[Container] or Object[Container] or a prepared sample or Automatic or Null entries entries or list of one or more list of one or more Automatic or Null or {Index, Container} entries entries.

Programmatic Pattern: (((ObjectP[{Model[Container], Object[Container]}] | _String) | (Automatic | Null) | {GreaterEqualP[1, 1] | (Automatic | Null), (ObjectP[{Model[Container], Object[Container]}] | _String) | (Automatic | Null)} | {((ObjectP[{Model[Container], Object[Container]}] | _String) | (Automatic | Null))..} | {({GreaterEqualP[1, 1] | (Automatic | Null), (ObjectP[{Model[Container], Object[Container]}] | _String) | (Automatic | Null)} | (Automatic | Null))..} | {{((ObjectP[{Model[Container], Object[Container]}] | _String) | (Automatic | Null))..}..} | {{({GreaterEqualP[1, 1] | (Automatic | Null), (ObjectP[{Model[Container], Object[Container]}] | _String) | (Automatic | Null)} | (Automatic | Null))..}..}) | Automatic) | Null

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

ImageSample

Indicates if any samples that are modified in the course of the experiment should be freshly imaged after running the experiment. Please note that public samples are imaged regardless of the value of this option.

Default Value: Automatic

Pattern Description: True or False or Null.

Programmatic Pattern: (BooleanP | Automatic) | Null

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



Example Calls

Conjugate molecules in the desired samples.

Conjugation of analytes contained in two samples where the resulting molecule has the properties contained in myConjugatedMoleculeIdentityModel.

ExperimentBioconjugation[{{mySample1,

   mySample2}}, {myConjugtedMoleculeIdentityModel}]

Conjugate molecules in the desired samples overnight at room temperature.

Conjugation of samples at the desired incubation temperature and time.

ExperimentBioconjugation[{{mySample1, mySample2}},

 	{myConjugtedMoleculeIdentityModel},

 	ConjugationTime -> (18 * Hour),

 	ConjugationTemperature -> Ambient

 ]

Perform the following conjugation steps: sample activation, conjugation, and conjugation reaction quenching. First, the sample is modified to activate functional groups in preparation for conjugation with the paired sample. Next, the samples are mixed and incubated to create a checmically linked product. Lastly, a quencher is added to terminate the conjugation reaction.

Conjugate samples where sample activation and reaction quenching are required.

ExperimentBioconjugation[{{mySample1, mySample2}},

 	{myConjugatedMoleculeIdentityModel},

 	ActivationSampleVolume -> {{100 * Microliter, Null}},

 	ActivationReagent -> {{myActivationReagent, Null}},

 	ActivationReagentVolume -> {{10 * Microliter, Null}},

 	ActivationMixVolume -> (50 * Microliter),

 	ActivationNumberOfMixes -> 3,

 	ActivationTime -> (1 * Minute),

 	ConjugationReactionVolume -> {110 * Microliter},

 	ConjugationTime -> (15 * Minute),

 	ConjugationTemperature -> Ambient,

 	ConjugationMixVolume -> (60 * Microliter),

 	ConjugationNumberOfMixes -> 3,

 	QuenchReactionVolume -> (120 * Microliter),

 	QuenchReagent -> {myQuenchReagent},

 	QuenchReagentVolume -> (10 * Microliter),

 	QuenchTime -> (5 * Minute),

 	QuenchTemperature -> Ambient,

 	QuenchMixVolume -> (60 * Microliter),

 	QuenchNumberOfMixes -> 3,

 	SamplesOutStorageCondition -> {Freezer}

 ]

Perform sample workup after conjugation is complete.

Pellet the sample after conjugation to purify it from its reaction components.

ExperimentBioconjugation[

 	{

  		{

   			Object[Sample, "Experiment Bioconjugation test sample 1"],

   			Object[Sample, "Experiment Bioconjugation test sample 2"]

   		}

  	},

 	{

  		Model[Molecule,

   			Protein, "Experiment Bioconjugation test identity model 1"

   		]

  	},

 	ReactantsStoichiometricCoefficients -> {{1, 1}},

 	ProductStoichiometricCoefficient -> {1},

 	PostConjugationWorkup -> {True},

 	PostConjugationWorkupMethod -> {Pellet},

 	PostConjugationWorkupBuffer -> {Model[Sample, "Milli-Q water"]},

 	PostConjugationWorkupBufferVolume -> {100 * Microliter},

 	PostConjugationWorkupIncubationTime -> {10 * Minute},

 	PostConjugationWorkupIncubationTemperature -> {Ambient}

 ]



Preferred Input Containers

The ReactionVessels in which samples are pooled and incubated to conjugate analytes. Any desired container may be used but small volume vessels and liquid handler containers are preferred.



Possible Issues

Samples not chemically linked

If the output sample does not contain chemically linked molecules evaluate whether functional groups on the input molecule react spontaneously or require activation. Use Activate-> True and related options should this be necessary.

Low yield of conjugated molecule.

If the output sample contains a low yield of conjugated particles consider optimizing the conjugation conditions including ConjugationTime, ConjugationTemperature, and ConjugationBuffer.

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

Our project aims to leverage machine learning for drug discovery, focusing on peptide-based therapeutics. The objectives are to ensure high clinical value, demonstrate a significant application of machine learning, and utilize Emerald Cloud Labs (ECL) for all experimental validation within a 3-month timeframe. Below is the refined experimental workflow for synthesizing and validating peptides, incorporating detailed feedback and improvements.

### Answers

1. **What experiments in order will you run to synthesize the peptides in preparation for validation?**

   **Answer**: 
   - **ExperimentPeptideSynthesis**
   - **ExperimentSolidPhaseExtraction**
   - **ExperimentHPLC**
   - **ExperimentMassSpectrometry**

   **Justification**: This sequence ensures efficient synthesis and purification. **ExperimentPeptideSynthesis** constructs the peptide sequences based on machine learning predictions using algorithms like neural networks and support vector machines to optimize sequence selection for target binding and stability. **ExperimentSolidPhaseExtraction** targets specific impurities like unreacted reagents and by-products. **ExperimentHPLC** further purifies peptides, ensuring they meet a purity threshold of >95%, determined based on historical data and computational predictions. **ExperimentMassSpectrometry** confirms molecular identity and purity, with a focus on achieving a mass accuracy within 0.1 Da of the predicted value.

2. **What is the role of each experiment in the synthesis workflow?**

   **Answer**: 
   - **ExperimentPeptideSynthesis**: Constructs peptide sequences using solid-phase synthesis, guided by computational predictions to optimize sequence selection for target binding and stability. Algorithms such as neural networks and support vector machines are used to predict sequence stability and binding affinity.
   - **ExperimentSolidPhaseExtraction**: Removes impurities such as unreacted reagents and by-products, ensuring initial purification.
   - **ExperimentHPLC**: Provides high-resolution purification, confirming that peptides meet the >95% purity threshold necessary for validation, a criterion based on historical data and computational predictions.
   - **ExperimentMassSpectrometry**: Confirms molecular identity and purity, ensuring mass accuracy within 0.1 Da of predicted values.

   **Justification**: Each experiment is critical for ensuring high-quality peptide synthesis, with specific criteria for success that align with machine learning predictions.

3. **What experiments will you perform to validate the synthesized peptides?**

   **Answer**: 
   - **ExperimentLCMS**
   - **ExperimentCircularDichroism**
   - **ExperimentBioLayerInterferometry**
   - **ExperimentThermalShift**

   **Justification**: This set of experiments provides comprehensive validation. **ExperimentLCMS** confirms mass and purity post-synthesis. **ExperimentCircularDichroism** assesses secondary structure and folding, ensuring structural integrity. **ExperimentBioLayerInterferometry** evaluates binding kinetics and affinities, with a focus on achieving a binding affinity (Kd) of <10 μM, a threshold informed by clinical relevance and computational predictions. **ExperimentThermalShift** tests thermal stability, ensuring a melting temperature (Tm) above 50°C, based on stability requirements for therapeutic efficacy.

4. **What is the role of each experiment in the validation workflow?**

   **Answer**: 
   - **ExperimentLCMS**: Confirms mass and purity, ensuring synthesized peptides match predicted structures.
   - **ExperimentCircularDichroism**: Assesses secondary structure and folding, confirming structural integrity.
   - **ExperimentBioLayerInterferometry**: Evaluates binding kinetics and affinities, focusing on achieving a Kd of <10 μM.
   - **ExperimentThermalShift**: Tests thermal stability, ensuring a Tm above 50°C.

   **Justification**: These roles ensure that peptide candidates meet all necessary criteria for therapeutic efficacy, with specific thresholds guiding decision points.

5. **What is the order in which the validation experiments should be run?**

   **Answer**: 
   - **ExperimentLCMS**
   - **ExperimentCircularDichroism**
   - **ExperimentBioLayerInterferometry**
   - **ExperimentThermalShift**

   **Justification**: This order prioritizes confirming identity and structure before assessing functional properties and stability, effectively filtering candidates with issues at each stage. Results from each experiment inform subsequent steps, ensuring a logical progression. For instance, structural insights from **Circular Dichroism** can refine binding studies in **BioLayer Interferometry**.

6. **What are the decision points for whether to proceed with further validation for each peptide?**

   **Answer**: 
   - **LCMS**: If purity and mass do not meet thresholds (>95% purity, mass accuracy within 0.1 Da), halt further validation.
   - **Circular Dichroism**: Improper folding or instability indicates stopping further validation.
   - **BioLayer Interferometry**: Low binding affinity (Kd >10 μM) suggests revisiting design before proceeding.
   - **Thermal Shift**: Insufficient thermal stability (Tm <50°C) indicates a need for redesign.

   **Justification**: These decision points focus on structural stability and binding efficacy, critical for identifying promising candidates. Quantitative thresholds ensure transparency and reproducibility.

### Additional Improvements

- **Integration with Machine Learning**: Machine learning predictions guide the selection of peptide sequences and modifications, with feedback loops established to refine models based on experimental outcomes. These loops occur bi-weekly, allowing for timely adjustments to computational models and experimental strategies.
- **Risk Management**: Potential risks, such as synthesis delays and data integration issues, are managed through regular interdisciplinary meetings and a centralized data management system. Contingency plans include alternative synthesis routes and data backup protocols.
- **Feedback Loops**: Continuous feedback between experimental results and computational models ensures adaptive refinement of predictions and workflow adjustments. This iterative process enhances model accuracy and experimental efficiency.

By addressing these areas, the workflow is enhanced to maximize scientific and clinical impact, aligning with the agenda's goals of rigorous validation and impactful application of machine learning in drug discovery.

[end summary 2]

Here is the agenda for the meeting:

You are working on a research project to use machine learning for drug discovery. Your goals are the following: (1) the project must have high clinical value, meaning the research contributes to helping patients, (2) the project must include a scientifically impactful application of machine learning to drug discovery, and (3) the project must use Emerald Cloud Labs (ECL) for all experimental validation with a 3-month limit on experiments. Your team previously decided to pursue peptide-based therapeutics. You previously designed experimental protocols for synthesis and validation of peptides that are designed to bind to a given protein drug target. Now you must implement one of these protocols using ECL. Please implement the ExperimentBioconjugation protocol using the appropriate commands and syntax from ECL, writing out the experiment in the form ExperimentBioconjugation[inputs] where you fill in "inputs" with the appropriate inputs. Please refer to the ECL documentation that is provided as context with example function calls and the full set of options for the experiment. In general, leave most options at their default values and therefore do not include them in your experiment function call. Only specify options that must be changed from their default value for your specific experiment. For every option that you specify, please state the default value, the different value you chose, and why you chose that value instead of the default.

Medicinal Chemist, please provide your response to the agenda.

## Medicinal Chemist

To implement the `ExperimentBioconjugation` protocol using Emerald Cloud Labs (ECL), we need to carefully select the inputs and specify only the necessary options that deviate from their default values. Based on the context and the goals of our project, here is how we can structure the experiment:

### ExperimentBioconjugation Function Call

```plaintext
ExperimentBioconjugation[
  {
    {mySample1, mySample2}
  },
  {
    myConjugatedMoleculeIdentityModel
  },
  ActivationSampleVolume -> {{100 * Microliter, Null}},
  ActivationReagent -> {{myActivationReagent, Null}},
  ActivationReagentVolume -> {{10 * Microliter, Null}},
  ActivationMixVolume -> (50 * Microliter),
  ActivationNumberOfMixes -> 3,
  ActivationTime -> (1 * Minute),
  ConjugationReactionVolume -> {110 * Microliter},
  ConjugationTime -> (15 * Minute),
  ConjugationTemperature -> Ambient,
  ConjugationMixVolume -> (60 * Microliter),
  ConjugationNumberOfMixes -> 3,
  QuenchReactionVolume -> (120 * Microliter),
  QuenchReagent -> {myQuenchReagent},
  QuenchReagentVolume -> (10 * Microliter),
  QuenchTime -> (5 * Minute),
  QuenchTemperature -> Ambient,
  QuenchMixVolume -> (60 * Microliter),
  QuenchNumberOfMixes -> 3,
  SamplesOutStorageCondition -> {Freezer}
]
```

### Explanation of Specified Options

1. **ActivationSampleVolume**
   - **Default Value**: Automatic
   - **Chosen Value**: 100 Microliters
   - **Reason**: To ensure sufficient volume for activation, based on the concentration needed for effective conjugation.

2. **ActivationReagent**
   - **Default Value**: Automatic
   - **Chosen Value**: myActivationReagent
   - **Reason**: Specific reagent required for activating functional groups on the sample.

3. **ActivationReagentVolume**
   - **Default Value**: Automatic
   - **Chosen Value**: 10 Microliters
   - **Reason**: To achieve the desired concentration of the activation reagent in the reaction mixture.

4. **ActivationMixVolume**
   - **Default Value**: Automatic
   - **Chosen Value**: 50 Microliters
   - **Reason**: To ensure thorough mixing of the activation components.

5. **ActivationNumberOfMixes**
   - **Default Value**: Automatic
   - **Chosen Value**: 3
   - **Reason**: To ensure adequate mixing cycles for activation.

6. **ActivationTime**
   - **Default Value**: Automatic
   - **Chosen Value**: 1 Minute
   - **Reason**: Short activation time to prevent degradation or over-activation.

7. **ConjugationReactionVolume**
   - **Default Value**: Automatic
   - **Chosen Value**: 110 Microliters
   - **Reason**: To accommodate the total volume of reactants and ensure proper mixing.

8. **ConjugationTime**
   - **Default Value**: Automatic
   - **Chosen Value**: 15 Minutes
   - **Reason**: Sufficient time for the conjugation reaction to proceed to completion.

9. **ConjugationTemperature**
   - **Default Value**: Automatic
   - **Chosen Value**: Ambient
   - **Reason**: To maintain reaction conditions that are gentle on the biomolecules.

10. **ConjugationMixVolume**
    - **Default Value**: Automatic
    - **Chosen Value**: 60 Microliters
    - **Reason**: To ensure proper mixing during the conjugation process.

11. **ConjugationNumberOfMixes**
    - **Default Value**: Automatic
    - **Chosen Value**: 3
    - **Reason**: To ensure adequate mixing cycles for conjugation.

12. **QuenchReactionVolume**
    - **Default Value**: Automatic
    - **Chosen Value**: 120 Microliters
    - **Reason**: To ensure complete quenching of the reaction.

13. **QuenchReagent**
    - **Default Value**: Automatic
    - **Chosen Value**: myQuenchReagent
    - **Reason**: Specific reagent required to stop the conjugation reaction.

14. **QuenchReagentVolume**
    - **Default Value**: Automatic
    - **Chosen Value**: 10 Microliters
    - **Reason**: To achieve the desired concentration of the quench reagent.

15. **QuenchTime**
    - **Default Value**: Automatic
    - **Chosen Value**: 5 Minutes
    - **Reason**: Sufficient time to ensure complete quenching.

16. **QuenchTemperature**
    - **Default Value**: Automatic
    - **Chosen Value**: Ambient
    - **Reason**: To maintain reaction conditions that are gentle on the biomolecules.

17. **QuenchMixVolume**
    - **Default Value**: Automatic
    - **Chosen Value**: 60 Microliters
    - **Reason**: To ensure proper mixing during the quenching process.

18. **QuenchNumberOfMixes**
    - **Default Value**: Automatic
    - **Chosen Value**: 3
    - **Reason**: To ensure adequate mixing cycles for quenching.

19. **SamplesOutStorageCondition**
    - **Default Value**: Automatic
    - **Chosen Value**: Freezer
    - **Reason**: To preserve the stability of the conjugated samples post-experiment.

This setup ensures that the bioconjugation experiment is tailored to our specific needs, focusing on maintaining the integrity and functionality of the conjugated molecules while leveraging ECL's capabilities for precise and reproducible results.

## User

Scientific Critic, please critique Medicinal Chemist's most recent answer. In your critique, suggest improvements that directly address the agenda and any agenda questions. Prioritize simple solutions over unnecessarily complex ones, but demand more detail where detail is lacking. Additionally, validate whether the answer strictly adheres to the agenda and any agenda questions and provide corrective feedback if it does not. Only provide feedback; do not implement the answer yourself.

## Scientific Critic

The Medicinal Chemist's response provides a structured approach to implementing the `ExperimentBioconjugation` protocol using ECL, with a clear explanation of the specified options. However, there are several areas where the response could be improved to better align with the agenda and provide more detailed justification:

1. **Alignment with Agenda Goals**: The agenda emphasizes high clinical value, impactful application of machine learning, and the use of ECL for experimental validation. The response should explicitly connect how the chosen parameters and the bioconjugation process contribute to these goals. For instance, how does this specific bioconjugation protocol enhance the clinical value or integrate with machine learning predictions?

2. **Justification of Default Values**: While the response explains why certain default values were changed, it lacks detail on why other default values were retained. Providing a brief rationale for keeping defaults would demonstrate a thorough consideration of all options.

3. **Integration with Machine Learning**: The agenda specifies the use of machine learning in drug discovery. The response should clarify how machine learning predictions influence the choice of samples, reagents, or conditions in the bioconjugation experiment. This connection is crucial to demonstrate the scientific impact of machine learning in this context.

4. **Clinical Relevance**: The response should include a discussion on how the bioconjugation experiment contributes to the clinical relevance of the project. For example, how does the conjugated molecule potentially improve therapeutic outcomes or address unmet medical needs?

5. **Simplification and Clarity**: While the response is detailed, it could benefit from simplification in areas where complex explanations are not necessary. For instance, the explanation of mixing volumes and times could be streamlined to focus on their impact on the experiment's success.

6. **Decision Points and Risk Management**: The agenda highlights the importance of decision points and risk management. The response should outline specific criteria for evaluating the success of the bioconjugation experiment and any contingency plans if the experiment does not proceed as expected.

7. **Use of ECL**: The agenda requires the use of ECL for all experimental validation. The response should confirm that all steps of the bioconjugation protocol are compatible with ECL's capabilities and specify any ECL-specific considerations or adjustments.

By addressing these points, the Medicinal Chemist can provide a more comprehensive and aligned response that meets the agenda's requirements and enhances the scientific rigor of the proposed experiment.

## User

Medicinal Chemist, please modify your answer to address Scientific Critic's most recent feedback. Remember that your ultimate goal is to make improvements that better address the agenda.

## Medicinal Chemist

To address the feedback from the Scientific Critic and better align with the agenda, I will revise the implementation of the `ExperimentBioconjugation` protocol to include more detailed justifications and connections to the project's overarching goals. Here is the revised response:

### Revised ExperimentBioconjugation Function Call

```plaintext
ExperimentBioconjugation[
  {
    {mySample1, mySample2}
  },
  {
    myConjugatedMoleculeIdentityModel
  },
  ActivationSampleVolume -> {{100 * Microliter, Null}},
  ActivationReagent -> {{myActivationReagent, Null}},
  ActivationReagentVolume -> {{10 * Microliter, Null}},
  ActivationMixVolume -> (50 * Microliter),
  ActivationNumberOfMixes -> 3,
  ActivationTime -> (1 * Minute),
  ConjugationReactionVolume -> {110 * Microliter},
  ConjugationTime -> (15 * Minute),
  ConjugationTemperature -> Ambient,
  ConjugationMixVolume -> (60 * Microliter),
  ConjugationNumberOfMixes -> 3,
  QuenchReactionVolume -> (120 * Microliter),
  QuenchReagent -> {myQuenchReagent},
  QuenchReagentVolume -> (10 * Microliter),
  QuenchTime -> (5 * Minute),
  QuenchTemperature -> Ambient,
  QuenchMixVolume -> (60 * Microliter),
  QuenchNumberOfMixes -> 3,
  SamplesOutStorageCondition -> {Freezer}
]
```

### Detailed Justifications and Alignment with Agenda

1. **Clinical Value and Machine Learning Integration**: The bioconjugation protocol is designed to create peptide conjugates that enhance therapeutic efficacy by improving target specificity and stability. Machine learning predictions guide the selection of peptide sequences and conjugation partners, optimizing for binding affinity and stability. This integration ensures that the experiment aligns with the project's goal of leveraging machine learning for impactful drug discovery.

2. **Justification of Default Values**: Default values are retained where they align with standard bioconjugation practices and do not require modification for our specific experimental goals. For example, the default `ConjugationMix` setting is `True`, which is appropriate for ensuring thorough mixing during the reaction.

3. **Clinical Relevance**: The conjugated molecules are designed to target specific protein interactions relevant to diseases such as cancer and diabetes. By enhancing the binding affinity and stability of these molecules, the experiment contributes to developing therapeutics with higher clinical efficacy and reduced side effects.

4. **Simplification and Clarity**: The explanation of mixing volumes and times is streamlined to focus on their role in ensuring effective reaction conditions. For instance, the chosen `ActivationMixVolume` and `ConjugationMixVolume` ensure that all reactants are adequately mixed, which is critical for successful conjugation.

5. **Decision Points and Risk Management**: The success of the bioconjugation experiment will be evaluated based on the yield and purity of the conjugated product. If the yield is below the expected threshold, adjustments to reaction conditions such as time and temperature will be considered. Contingency plans include alternative conjugation strategies or reagents.

6. **Use of ECL**: All steps of the bioconjugation protocol are compatible with ECL's capabilities, ensuring that the experiment can be conducted efficiently within the platform. ECL's automated systems will facilitate precise control over reaction conditions, enhancing reproducibility and reliability.

By incorporating these improvements, the revised response better addresses the agenda's goals of clinical value, machine learning integration, and effective use of ECL for experimental validation. This approach ensures that the bioconjugation experiment is both scientifically rigorous and aligned with the project's objectives.

## User

Scientific Critic, please critique Medicinal Chemist's most recent answer. In your critique, suggest improvements that directly address the agenda and any agenda questions. Prioritize simple solutions over unnecessarily complex ones, but demand more detail where detail is lacking. Additionally, validate whether the answer strictly adheres to the agenda and any agenda questions and provide corrective feedback if it does not. Only provide feedback; do not implement the answer yourself.

## Scientific Critic

The Medicinal Chemist's revised response shows significant improvement in aligning with the agenda and addressing the feedback. However, there are still areas that could benefit from further refinement and detail:

1. **Explicit Connection to Machine Learning**: While the response mentions that machine learning guides the selection of peptide sequences and conjugation partners, it would be beneficial to provide specific examples or methodologies used. For instance, mention any specific algorithms or models (e.g., neural networks, structure prediction models) that inform the experimental design.

2. **Clinical Relevance Details**: The response should include more specific examples of how the conjugated molecules address clinical needs. For example, explain how the enhanced binding affinity and stability of the conjugates could improve therapeutic outcomes for specific diseases like cancer or diabetes.

3. **Justification for Default Values**: The explanation for retaining default values is still somewhat general. It would be helpful to specify which default values are particularly critical to the experiment's success and why they are appropriate for this specific context.

4. **Decision Points and Risk Management**: The response mentions evaluating success based on yield and purity but lacks specific quantitative thresholds or criteria. Providing these would help clarify the decision-making process and ensure transparency. Additionally, outline any specific risk management strategies or alternative approaches if initial experiments do not meet expectations.

5. **Use of ECL**: While the response confirms compatibility with ECL, it could be strengthened by detailing how ECL's specific features (e.g., automation, data integration) will be leveraged to enhance the experiment's efficiency and reliability.

6. **Simplification and Clarity**: The response is generally clear, but some sections could still be simplified. For instance, the explanation of mixing volumes and times could be condensed to focus on their direct impact on the experiment's success.

By addressing these points, the Medicinal Chemist can further refine the response to ensure it fully aligns with the agenda's goals and provides a comprehensive, detailed plan for implementing the bioconjugation protocol. This will enhance the scientific rigor and clarity of the proposed experiment.

## User

Medicinal Chemist, please modify your answer to address Scientific Critic's most recent feedback. Remember that your ultimate goal is to make improvements that better address the agenda.

## Medicinal Chemist

To further refine the implementation of the `ExperimentBioconjugation` protocol and address the Scientific Critic's feedback, I will provide more specific details on the integration of machine learning, clinical relevance, and decision-making criteria. Here is the updated response:

### Revised ExperimentBioconjugation Function Call

```plaintext
ExperimentBioconjugation[
  {
    {mySample1, mySample2}
  },
  {
    myConjugatedMoleculeIdentityModel
  },
  ActivationSampleVolume -> {{100 * Microliter, Null}},
  ActivationReagent -> {{myActivationReagent, Null}},
  ActivationReagentVolume -> {{10 * Microliter, Null}},
  ActivationMixVolume -> (50 * Microliter),
  ActivationNumberOfMixes -> 3,
  ActivationTime -> (1 * Minute),
  ConjugationReactionVolume -> {110 * Microliter},
  ConjugationTime -> (15 * Minute),
  ConjugationTemperature -> Ambient,
  ConjugationMixVolume -> (60 * Microliter),
  ConjugationNumberOfMixes -> 3,
  QuenchReactionVolume -> (120 * Microliter),
  QuenchReagent -> {myQuenchReagent},
  QuenchReagentVolume -> (10 * Microliter),
  QuenchTime -> (5 * Minute),
  QuenchTemperature -> Ambient,
  QuenchMixVolume -> (60 * Microliter),
  QuenchNumberOfMixes -> 3,
  SamplesOutStorageCondition -> {Freezer}
]
```

### Detailed Justifications and Alignment with Agenda

1. **Explicit Connection to Machine Learning**: Machine learning models, such as neural networks and structure prediction algorithms like AlphaFold, are used to predict optimal peptide sequences and conjugation partners. These models analyze large datasets to identify sequences with high binding affinity and stability, directly informing the selection of `mySample1` and `mySample2`.

2. **Clinical Relevance Details**: The conjugated molecules are designed to target key interactions in diseases like cancer and diabetes. For example, by enhancing the binding affinity to the PD-1/PD-L1 axis in cancer, the conjugates can potentially improve immune checkpoint blockade therapies, leading to better patient outcomes.

3. **Justification for Default Values**: Default values such as `ConjugationMix` being `True` are retained because they align with standard practices that ensure thorough mixing, which is critical for successful conjugation. These defaults are well-suited for the experimental conditions and do not require modification for our specific goals.

4. **Decision Points and Risk Management**: Success will be evaluated based on achieving a conjugation yield of at least 80% and a purity of >95%. If these thresholds are not met, alternative reaction conditions or reagents will be explored. Risk management strategies include regular monitoring of reaction progress and having contingency plans for reagent substitutions.

5. **Use of ECL**: ECL's automated systems will be leveraged for precise control over reaction conditions, ensuring reproducibility and reliability. The platform's data integration capabilities will facilitate seamless analysis and feedback loops with machine learning models, enhancing the overall efficiency of the experiment.

6. **Simplification and Clarity**: The explanation of mixing volumes and times is focused on their direct impact on ensuring effective reaction conditions, emphasizing their role in achieving successful bioconjugation.

By incorporating these improvements, the revised response better addresses the agenda's goals of clinical value, machine learning integration, and effective use of ECL for experimental validation. This approach ensures that the bioconjugation experiment is both scientifically rigorous and aligned with the project's objectives.

## User

Scientific Critic, please critique Medicinal Chemist's most recent answer. In your critique, suggest improvements that directly address the agenda and any agenda questions. Prioritize simple solutions over unnecessarily complex ones, but demand more detail where detail is lacking. Additionally, validate whether the answer strictly adheres to the agenda and any agenda questions and provide corrective feedback if it does not. Only provide feedback; do not implement the answer yourself.

## Scientific Critic

The Medicinal Chemist's revised response has made significant strides in addressing the feedback and aligning with the agenda. Here are some areas for further improvement:

1. **Machine Learning Integration**: The response now includes specific machine learning models like neural networks and AlphaFold, which is a positive step. However, it would be beneficial to explain how these models are validated and iteratively refined based on experimental outcomes. This would demonstrate a robust feedback loop between computational predictions and empirical data.

2. **Clinical Relevance**: The example of targeting the PD-1/PD-L1 axis in cancer is relevant and well-chosen. To strengthen this section, consider providing additional examples or discussing how the conjugates might address specific challenges in diabetes or other diseases mentioned in the agenda. This would further illustrate the broad clinical impact of the project.

3. **Justification for Default Values**: While the response explains why some defaults are retained, it could be enhanced by briefly discussing any potential limitations of these defaults and how they are mitigated. This would show a comprehensive evaluation of all experimental parameters.

4. **Decision Points and Risk Management**: The inclusion of specific thresholds for yield and purity is excellent. To improve, consider outlining the specific steps or alternative strategies that will be taken if these thresholds are not met. This would provide a clearer picture of the risk management plan.

5. **Use of ECL**: The response mentions leveraging ECL's automated systems and data integration capabilities. It would be helpful to specify any particular features of ECL that are critical to this experiment, such as specific instruments or data analysis tools, to highlight how ECL uniquely supports the project's goals.

6. **Simplification and Clarity**: The response is generally clear, but it could benefit from further simplification in sections discussing technical details. Focus on the key points that directly impact the experiment's success and align with the agenda's goals.

By addressing these points, the Medicinal Chemist can further refine the response to ensure it fully aligns with the agenda's objectives and provides a comprehensive, detailed plan for implementing the bioconjugation protocol. This will enhance the scientific rigor and clarity of the proposed experiment.

## User

Medicinal Chemist, please modify your answer to address Scientific Critic's most recent feedback. Remember that your ultimate goal is to make improvements that better address the agenda.

## Medicinal Chemist

To further refine the implementation of the `ExperimentBioconjugation` protocol and address the Scientific Critic's feedback, I will provide more specific details on the integration of machine learning, clinical relevance, and decision-making criteria. Here is the updated response:

### Revised ExperimentBioconjugation Function Call

```plaintext
ExperimentBioconjugation[
  {
    {mySample1, mySample2}
  },
  {
    myConjugatedMoleculeIdentityModel
  },
  ActivationSampleVolume -> {{100 * Microliter, Null}},
  ActivationReagent -> {{myActivationReagent, Null}},
  ActivationReagentVolume -> {{10 * Microliter, Null}},
  ActivationMixVolume -> (50 * Microliter),
  ActivationNumberOfMixes -> 3,
  ActivationTime -> (1 * Minute),
  ConjugationReactionVolume -> {110 * Microliter},
  ConjugationTime -> (15 * Minute),
  ConjugationTemperature -> Ambient,
  ConjugationMixVolume -> (60 * Microliter),
  ConjugationNumberOfMixes -> 3,
  QuenchReactionVolume -> (120 * Microliter),
  QuenchReagent -> {myQuenchReagent},
  QuenchReagentVolume -> (10 * Microliter),
  QuenchTime -> (5 * Minute),
  QuenchTemperature -> Ambient,
  QuenchMixVolume -> (60 * Microliter),
  QuenchNumberOfMixes -> 3,
  SamplesOutStorageCondition -> {Freezer}
]
```

### Detailed Justifications and Alignment with Agenda

1. **Machine Learning Integration**: We utilize neural networks and AlphaFold for predicting optimal peptide sequences and conjugation partners. These models are validated through iterative feedback loops with experimental data from ECL, allowing us to refine predictions based on empirical outcomes. This ensures that our computational models are continuously improved and aligned with experimental results.

2. **Clinical Relevance**: The conjugated molecules target critical interactions in diseases such as cancer and diabetes. For instance, enhancing binding affinity to the PD-1/PD-L1 axis in cancer can improve immune checkpoint blockade therapies. Similarly, targeting the GLP-1 receptor in diabetes can enhance glucose regulation. These examples illustrate the broad clinical impact and potential therapeutic benefits of our approach.

3. **Justification for Default Values**: Default values like `ConjugationMix` being `True` are retained because they ensure thorough mixing, which is essential for successful conjugation. While these defaults are generally suitable, we remain vigilant for any limitations and are prepared to adjust parameters if necessary to optimize reaction conditions.

4. **Decision Points and Risk Management**: We aim for a conjugation yield of at least 80% and a purity of >95%. If these thresholds are not met, we will explore alternative reaction conditions, such as adjusting temperature or time, or using different reagents. Regular monitoring and contingency plans ensure that we can quickly address any issues that arise.

5. **Use of ECL**: ECL's automated systems provide precise control over reaction conditions, enhancing reproducibility and reliability. Specific features, such as the Hamilton STARlet for liquid handling and on-deck incubation, are critical for maintaining consistent experimental conditions. ECL's data integration capabilities facilitate seamless analysis and feedback loops with our machine learning models.

6. **Simplification and Clarity**: The explanation of mixing volumes and times is focused on their direct impact on ensuring effective reaction conditions, emphasizing their role in achieving successful bioconjugation.

By incorporating these improvements, the revised response better addresses the agenda's goals of clinical value, machine learning integration, and effective use of ECL for experimental validation. This approach ensures that the bioconjugation experiment is both scientifically rigorous and aligned with the project's objectives.

