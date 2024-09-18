## User

This is the beginning of an individual meeting with Medicinal Chemist to discuss your research project.

Here is context for this meeting:

[begin context 1]

ExperimentELISA[Samples]⟹Protocol

creates a Protocol to run Enzyme-Linked Immunosorbent Assay (ELISA) experiment on the provided Samples for the detection and quantification of certain analytes.



Enzyme-Linked Immunosorbent Assay (ELISA) uses antigen-antibody interaction to quantitatively measure the concentration of an antigen in samples or compare antibody binding affinity. There are many forms of ELISA, such as direct ELISA, indirect ELISA, sandwich ELISA, competitive ELISA, and fast ELISA that apply antigens and antibodies in varied sequences. During an ELISA experiment, protein standards and samples are loaded onto ELISA plates and the target antigen is bound by antibodies. Antigen concentration is revealed by an enzyme, which converts its substrate into a colored product. Results are measured using colorimetric detection, and antigen concentrations are calculated using the standard curve generated from protein standards.



Experimental Principles

Figure 1.1: Overview of ELISA methods. In a DirectELISA experiment, the Sample is coated on the ELISAPlate, and then a primary antibody is used to detect the target antigen. In a DirectSandwichELISA experiment, a capture antibody is coated onto the ELISAPlate to pull down the target antigen from the sample. Then primary antibody is used to detect the target antigen. In a DirectCompetitiveELISA experiment, a reference antigen is used to coat the ELISAPlate. Samples are incubated with the primary antibody. Then, when the Sample-Antibody-Complex solution is loaded on the ELISAPlate, the remaining free primary antibody binds to the reference antigen. In a FastELISA experiment, a coating antibody against a tag is coated to the ELISAPlate. A capture antibody containing this small tag and a primary antibody for antigen detection is incubated with the sample to form a CaptureAntibody-TargetAntigen-PrimaryAntibody complex. Then this complex is pulled down by the coating antibody to the surface of the plate. Compared with the Direct methods where the primary antibody is conjugated with an enzyme (such as Horse Radish Peroxidase/HRP or Alkaline Phosphatas/AP) for detection, in Indirect methods a secondary antibody is, instead, conjugated with this enzyme. During Indirect methods, an additional step of SecondaryAntibody incubation is added to the corresponding Direct methods.

Figure 1.2: DirectELISA process: 1. If required, antibodies are diluted. 2. Sample, Spike, Standard, Blank and any dilutions are assembled in 96-well 2ml deep well plate. 3. Assembled samples from the previous step are transferred to the ELISA plate and incubated to coat the plate. 4. Blocking buffer is added to the ELISA plate to prevent non-specific binding. 5. Primary antibody is added to the plate for immunosorbence. 5. SubstrateSolution and StopSolution (if required) are added to the plate for colorimetric detection.

Figure 1.3: IndirectELISA process: 1. If required, antibodies are diluted. 2. Sample, Spike, Standard, Blank and any dilutions are assembled in 96-well 2ml deep well plate. 3. Assembled samples from the previous step are transferred to the ELISA plate and incubated to coat the plate. 4. Blocking buffer is added to the ELISA plate to prevent non-specific binding. 5. Primary antibody and secondary antibody are sequentially added to the plate for immunosorbence. 5. SubstrateSolution and StopSolution (if required) are added to the plate for colorimetric detection.

Figure 1.4: DirectSandwichELISA process: 1. If required, antibodies are diluted. 2. Capture antibody is added to the ELISA plate for coating. 3. Sample, Spike, Standard, Blank and any dilutions are assembled in 96-well 2ml deep well plate. 4. Blocking buffer is added to the ELISA plate to prevent non-specific binding. 5. Assembled samples and primary antibody are added to the plate sequentially for immunosorbence. 6. SubstrateSolution and StopSolution (if required) are added to the plate for colorimetric detection.

Figure 1.5: IndirectSandwichELISA process: 1. If required, antibodies are diluted. 2. Capture antibody is added to the ELISA plate for coating. 3. Sample, Spike, Standard, Blank and any dilutions are assembled in 96-well 2ml deep well plate. 4. Blocking buffer is added to the ELISA plate to prevent non-specific binding. 5. Assembled samples, primary antibody, and secondary antibody are added to the plate sequentially for immunosorbence. 6. SubstrateSolution and StopSolution (if required) are added to the plate for colorimetric detection.

Figure 1.6: DirectCompetitiveELISA process: 1. If required, antibodies and reference antigen are diluted. 2. Reference antigen is added to the ELISA plate for coating. 3. Sample, Spike, Standard, Blank and any dilutions are assembled in 96-well 2ml deep well plate and primary antibody is mixed with each sample and incubated (if required). 4. Blocking buffer is added to the ELISA plate to prevent non-specific binding. 5. The Sample-antibody mixture from step 3 is added to the ELISA plate for immunosorbence. 6. SubstrateSolution and StopSolution (if required) are added to the plate for colorimetric detection.

Figure 1.7: IndirectCompetitiveELISA process: 1. If required, antibodies and reference antigen are diluted. 2. Reference antigen is added to the ELISA plate for coating. 3. Sample, Spike, Standard, Blank and any dilutions are assembled in 96-well 2ml deep well plate and primary antibody is mixed with each sample and incubated (if required). 4. Blocking buffer is added to the ELISA plate to prevent non-specific binding. 5. The Sample-antibody mixture from step 3 is added to the ELISA plate, and then the secondary antibody is added, for immunosorbence. 6. SubstrateSolution and StopSolution (if required) are added to the plate for colorimetric detection.

Figure 1.8: FastELISA process: 1. If required, antibodies are diluted. 2. Coating antibody is added to the ELISA plate for coating. 3. Sample, Spike, Standard, Blank and any dilutions are assembled in 96-well 2ml deep well plate. Then primary antibody and capture antibody are mixed with each sample and incubated (if required). 4. Blocking buffer is added to the ELISA plate to prevent non-specific binding. 5. The Sample-antibody mixture from step 3 is added to the ELISA plate for immunosorbence. 6. SubstrateSolution and StopSolution (if required) are added to the plate for colorimetric detection.



Instrumentation

Hamilton Nimbus HD

Model[Instrument, LiquidHandler, "id:rea9jlRLr5qb"]

Figure 2.1.1: An overview of the ELISA robotic workcell. It is capable of processing plate operations including liquid handling with 4 indipendent pipettes, microplate movements, plate incubation-shaking, plate washing, and plate absorbance measurements.



Experiment Options

General

Method

Defines the type of ELISA experiment to be performed. Types include DirectELISA, IndirectELISA, DirectSandwichELISA, IndirectSandwichELISA, DirectCompetitiveELISA, IndirectCompetitiveELISA, and FastELISA. Compared with the Direct methods where the primary antibody is conjugated with an enzyme (such as Horse Radish Peroxidase/HRP or Alkaline Phosphatas/AP) for detection, in all Indirect methods a secondary antibody is, instead, conjugated with this enzyme. In Indirect methods, an additional step of SecondaryAntibody incubation is added to the corresponding Direct methods. In a DirectELISA experiment, the Sample is coated on the ELISAPlate, and then a primary antibody is used to detect the target antigen. In a DirectSandwichELISA experiment, a capture antibody is coated onto the ELISAPlate to pull down the target antigen from the sample. Then a primary antibody is used to detect the target antigen. In a DirectCompetitiveELISA experiment, a reference antigen is used to coat the ELISAPlate. Samples are incubated with the primary antibody. Then, when the Sample-Antibody-Complex solution is loaded on the ELISAPlate, the remaining free primary antibody binds to the reference antigen. In a FastELISA experiment, a coating antibody against a tag is coated to the ELISAPlate. A capture antibody containing this tag and a primary antibody for antigen detection is incubated with the sample to form a CaptureAntibody-TargetAntigen-PrimaryAntibody complex. Then this complex is pulled down by the coating antibody to the surface of the plate (See Figure 1.1).

Default Value: DirectELISA

Pattern Description: DirectELISA, IndirectELISA, DirectSandwichELISA, IndirectSandwichELISA, DirectCompetitiveELISA, IndirectCompetitiveELISA, or FastELISA.

Programmatic Pattern: ELISAMethodP

TargetAntigen

The Analyte molecule (e.g., peptide, protein, and hormone) detected and quantified in the samples by Antibodies in the ELISA experiment. This option is used to automatically set sample Antibodies and the corresponding experiment conditions of Standards and Blanks.

Default Value: Automatic

Default Calculation: Automatically set to the Model[Molecule] in the Analyte field of the sample.

Pattern Description: An object of type or subtype Model[Molecule] or Null.

Programmatic Pattern: (ObjectP[{Model[Molecule]}] | Automatic) | Null

Index Matches to: experiment samples

NumberOfReplicates

The number of times an ELISA assay will be repeated in parallel wells. Samples, Standards, or Blanks will be loaded this number of times in the plates. Replications are conducted at the same time, and if possible, in the same ELISAPlate. If set to Null, each Sample, Standard, or Blank will be assayed once.

Default Value: Automatic

Default Calculation: Automatically set to 2 unless method is DirectELISA or IndirectELISA and Coating is False, in which case it is set to Null.

Pattern Description: Greater than or equal to 2 and less than or equal to 192 in increments of 1 or Null.

Programmatic Pattern: (RangeP[2, 192, 1] | Automatic) | Null

WashingBuffer

The solution used to rinse off unbound molecules from the assay plate.

Default Value: Model[Sample, StockSolution, Phosphate Buffered Saline with 0.05% TWEEN 20, pH 7.4]

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample.

Programmatic Pattern: ObjectP[{Model[Sample], Object[Sample]}] | _String

Sample Assembly

Spike

The sample with a known concentration of analyte. Spike is to be mixed with the input sample. The purpose of spiking is to perform a spike-and-recovery assessment to determine whether the ELISA can accurately test the concentration of analyte within the context of the sample. If the recovery observed for the spiked sample is identical to the analyte prepared in standard diluent, the sample is considered not to interfere with the assay. For example, if molecules in the sample inhibits the binding between the antibody and TargetAntigen, the results from the ELISA becomes inaccurate. In a Spike-and-Recovery experiment,an aliquot of a sample is mixed with Spike. ELISA is performed on the Sample alone (also called Neat Sample) and the Spiked Sample at the same time, where the Spike concentration in the sample can be measured. This measured Spike concentration can be then compared with the known Spike concentration. Typically a 20% difference between measured Spike concentration and the known Spike concentration is acceptable. Spiked sample can be further diluted to perform linearity-of-dilution assessment. The plate used for sample spiking and dilution will be discarded after the experiment.

Default Value: Null

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: (ObjectP[{Model[Sample], Object[Sample]}] | _String) | Null

Index Matches to: experiment samples

SpikeDilutionFactor

The dilution ratio by which the Spike is mixed with the input sample before further dilution is performed.

Default Value: Automatic

Default Calculation: Automatically set to 0.1 if Spike is not Null.

Pattern Description: Greater than or equal to 0 and less than or equal to 1 or Null.

Programmatic Pattern: (RangeP[0, 1] | Automatic) | Null

Index Matches to: experiment samples

SpikeStorageCondition

The condition under which the unused portion of spike should be stored.

Default Value: Automatic

Default Calculation: Automatically set to Refrigerator if Spike is not Null.

Pattern Description: {AmbientStorage, Refrigerator, Freezer, DeepFreezer, CryogenicStorage, YeastIncubation, BacteriaIncubation, MammalianIncubation, TissueCultureCellsIncubation, MicrobialCellsIncubation, MicrobialCellsShakingIncubation, YeastCellsIncubation, YeastCellsShakingIncubation, ViralIncubation, AcceleratedTesting, IntermediateTesting, LongTermTesting, UVVisLightTesting} or Disposal or Null.

Programmatic Pattern: ((SampleStorageTypeP | Disposal) | Automatic) | Null

Index Matches to: experiment samples

SampleSerialDilutionCurve

The collection of serial dilutions that will be performed on each sample: if spiking was performed, the dilution will be performed on the spiked sample; otherwise, the dilutions will be performed on the sample. This Linearity-of-Dilution step assesses whether the ELISA experiment can reliably measure TargetAntigen concentration at different concentration ranges. For example, a sample with TargetAntigen concentration of 100ng/ul, if diluted 1:2, 1:4, and 1:8, should yield ELISA measurements of 50ng/ul, 25ng/ul, and 12.5ng/ul (or should follow a concentration ratio of 4:2:1). Typically a 20% difference between the measured and expected concentrations is considered acceptable. For Serial Dilution Volumes, the Transfer Volume is taken out of the sample and added to a second well with the Diluent Volume of the Diluent. It is mixed, then the Transfer Volume is taken out of that well to be added to a third well. This is repeated to make Number Of Dilutions diluted samples. For example, if a 100 ug/ ml sample with a Transfer Volume of 20 Microliters, a Diluent Volume of 60 Microliters and a Number of Dilutions of 3 is used, it will create a DilutionCurve of 25 ug/ ml, 6.25 ug/ ml, and 1.5625 ug/ ml with each dilution having a volume of 60 Microliters. For Serial Dilution Factors, the sample will be diluted by the dilution factor at each transfer step. IMPORTANT: because the dilution curve does not intrinsically include the original sample, in the case of sample dilution the first diluting factor should be 1 or Diluent Volume should be 0 Microliter to include the original sample. For example, if a Spike-and-Recovery assay is to be performed, the first dilution factor must be 1 in order to include the original spiked sample. During experiment, an 5% extra volume than specified is going to be prepared in order to offset pipetting errors. Therefore, the total volume for each well specified in this option should be equal or greater than the volume needed for the experiment. Because the dilution of each assay (well) is prepared independently, the Number of Replications should not be considered when determining the Spike Volume. The plate used for sample dilutions will be discarded after the experiment. Note: if spike or antibodies are to be mixed with samples, their volumes are counted towards diluent volume.

Figure 3.1: Use the SerialDilutionCuve option to create a collection of serial dilutions that will be performed on samples.

Default Value: Automatic

Default Calculation: The option is automatically set Null if or a SampleDilutionCurve is specified.

Pattern Description: Serial Dilution Factor or Serial Dilution Volumes or Null.

Programmatic Pattern: (({RangeP[10*Microliter, 1500*Milliliter], {RangeP[0, 1], GreaterP[0, 1]} | {RangeP[0, 1]..}} | {RangeP[0*Microliter, 1000*Microliter], RangeP[0*Microliter, 1000*Microliter], GreaterP[0, 1]}) | Automatic) | Null

Index Matches to: experiment samples

SampleDilutionCurve

The collection of dilutions that will be performed on each sample: the dilutions will be performed on the sample. Spiked samples should only be further diluted with serial dilution. This Linearity-of-Dilution step assesses whether the ELISA experiment can reliably measure TargetAntigen concentration at different concentration ranges. For example, a sample with TargetAntigen concentration of 100ng/ul, if diluted 1:2, 1:4, and 1:8, should yield ELISA measurements of 50ng/ul, 25ng/ul, and 12.5ng/ul (or should follow a concentration ratio of 8:4:2:1). Typically a 20% difference between the measured and expected concentrations is considered acceptable. Linearity-of-Dilution experiment can be done with Spiked or non-Spiked samples. For Fixed Dilution Volume Dilution Curves, the Spike Amount is the volume of the sample that will be mixed the Diluent Volume of the Diluent to create a desired concentration. The Assay Volume is the TOTAL volume of the sample that will be created after being diluted by the Dilution Factor. IMPORTANT: because the dilution curve does not intrinsically include the original sample, in the case of sample dilution the first diluting factor must be 1, or Diluent Volume should be 0 to include the original sample. During experiment, an 5% extra volume than specified is going to be prepared in order to offset pipetting errors. Therefore, the total volume for each well specified in this option should be equal or greater than the volume needed for the experiment. Because the dilution of each assay (well) is prepared independently, the Number of Replications should not be considered when determining the Spike Volume. The plate used for sample dilutions will be discarded after the experiment. Note: if spike or antibodies are to be mixed with samples, their volumes are counted towards diluent volume.

Figure 3.2: Use the DilutionCuve option to create a collection of dilutions that will be performed on samples.

Default Value: Automatic

Default Calculation: The option is automatically set Null if or a SampleSerialDilutionCurve is specified.

Pattern Description: Fixed Dilution Factor or Fixed Dilution Volume or Null.

Programmatic Pattern: (({{RangeP[10*Microliter, 1500*Microliter], RangeP[0, 1]}..} | {{RangeP[0*Microliter, 1000*Microliter], RangeP[0*Microliter, 1000*Microliter]}..}) | Automatic) | Null

Index Matches to: experiment samples

SampleDiluent

The buffer used to perform multiple dilutions of samples or spiked samples.

Default Value: Automatic

Default Calculation: If SampleDilutionCurve and SampleSerialDilutionCurve are not both Null, in the case when Method is set to DirectELISA and IndirectELISA, the option is automatically set to Model[Sample, StockSolution, "1x Carbonate-Bicarbonate Buffer pH10"]; in all other cases, the option is automatically set to Model[Sample,"ELISA Blocker Blocking Buffer"].

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

Antibody Antigen Preparation

CoatingAntibody

The sample containing the antibody that is used for coating in FastELISA.

Default Value: Automatic

Default Calculation: If Method is FastELISA, automatically set to an antibody against a tag which is conjugated to a the CaptureAntibody.

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

CoatingAntibodyDilutionFactor

The dilution ratio of CoatingAntibody. CoatingAntibody is diluted with CoatingAntibodyDiluent. Either CoatingAntibodyDilutionFactor or CoatingAntibodyVolume should be provided but not both.

Default Value: Automatic

Default Calculation: Automatically set to 0.001 (1:1,000) for FastELISA.

Pattern Description: Greater than or equal to 0 and less than or equal to 1 or Null.

Programmatic Pattern: (RangeP[0, 1] | Automatic) | Null

Index Matches to: experiment samples

CoatingAntibodyVolume

The volume of undiluted CoatingAntibody added into the corresponding well of the assay plate. CoatingAntibody is diluted with CoatingAntibodyDiluent. CoatingAntibodyVolume is used as an alternative to CoatingAntibodyDilutionFactor. During antibody preparation, a master mix will be made for antibody dilution, and the diluted Antibodies will be aliquoted into each well.

Default Value: Null

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: RangeP[0*Microliter, 200*Microliter] | Null

Index Matches to: experiment samples

CoatingAntibodyDiluent

The buffer used to dilute CoatingAntibodies.

Default Value: Automatic

Default Calculation: If Method is set to FastELISA, the option is automatically set to Model[Sample, StockSolution, "1x Carbonate-Bicarbonate Buffer pH10"].

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

CoatingAntibodyStorageCondition

The condition under which the unused portion of Coating Antibody stock sample should be stored.

Default Value: Automatic

Default Calculation: Automatically set to Refrigerator if Method is set to FastELISA.

Pattern Description: {AmbientStorage, Refrigerator, Freezer, DeepFreezer, CryogenicStorage, YeastIncubation, BacteriaIncubation, MammalianIncubation, TissueCultureCellsIncubation, MicrobialCellsIncubation, MicrobialCellsShakingIncubation, YeastCellsIncubation, YeastCellsShakingIncubation, ViralIncubation, AcceleratedTesting, IntermediateTesting, LongTermTesting, UVVisLightTesting} or Disposal or Null.

Programmatic Pattern: ((SampleStorageTypeP | Disposal) | Automatic) | Null

Index Matches to: experiment samples

CaptureAntibody

The sample containing the antibody that is used to pull down the antigen from sample solution to the surface of the assay plate wells in DirectSandwichELISA, IndirectSandwichELISA, and FastELISA.

Default Value: Automatic

Default Calculation: If Method is FastELISA, automatically set to an antibody containing an affinity tag and against the TargetAntigen. If Method is DirectSandwichELISA or IndirectSandwichELISA, automatically set to an un-tagged antibody against TargetAntigen.

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

CaptureAntibodyDilutionFactor

The dilution ratio of CaptureAntibody. For DirectSandwichELISA and IndirectSandwichELISA, CaptureAntibody is diluted with CaptureAntibodyDiluent. For FastELISA, CaptureAntibody is diluted in the corresponding sample. Either CaptureAntibodyDilutionFactor or CaptureAntibodyVolume should be provided but not both.

Default Value: Automatic

Default Calculation: For DirectSandwichELISA and IndirectSandwichELISA, automatically set to 0.001 (1:1,000). For FastELISA, automatically set to 0.01 (1:100).

Pattern Description: Greater than or equal to 0 and less than or equal to 1 or Null.

Programmatic Pattern: (RangeP[0, 1] | Automatic) | Null

Index Matches to: experiment samples

CaptureAntibodyVolume

The volume of undiluted CaptureAntibody added into the corresponding well of the assay plate. CaptureAntibodyVolume is used as an alternative to CaptureAntibodyDilutionFactor. During antibody preparation, a master mix will be made for antibody dilution, and the diluted Antibodies will be aliquoted into each well.

Default Value: Null

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: RangeP[0*Microliter, 200*Microliter] | Null

Index Matches to: experiment samples

CaptureAntibodyDiluent

The buffer used to dilute CaptureAntibodies. Set to Null when CapturaAntibody should be diluted into samples (in FastELISA).

Default Value: Automatic

Default Calculation: If Method is set to DirectSandwichELISA or IndirectSandwichELISA, the option is automatically set to Model[Sample, StockSolution, "1x Carbonate-Bicarbonate Buffer pH10"].

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

CaptureAntibodyStorageCondition

The condition under which the unused portion of Capture Antibody stock sample should be stored.

Default Value: Automatic

Default Calculation: If Method is set to DirectSandwichELISA, IndirectSandwichELISA, or FastELISA, Automatically set to Refrigerator.

Pattern Description: {AmbientStorage, Refrigerator, Freezer, DeepFreezer, CryogenicStorage, YeastIncubation, BacteriaIncubation, MammalianIncubation, TissueCultureCellsIncubation, MicrobialCellsIncubation, MicrobialCellsShakingIncubation, YeastCellsIncubation, YeastCellsShakingIncubation, ViralIncubation, AcceleratedTesting, IntermediateTesting, LongTermTesting, UVVisLightTesting} or Disposal or Null.

Programmatic Pattern: ((SampleStorageTypeP | Disposal) | Automatic) | Null

Index Matches to: experiment samples

ReferenceAntigen

The sample containing the antigen that is used in DirectCompetitiveELISA or IndirectCompetitiveELISA. The ReferenceAntigen competes with TargetAntigen in the samples for the binding of the PrimaryAntibody. Reference Antigen is also referred to as Inhibitor Antigen.

Default Value: Automatic

Default Calculation: Automatically set to a sample containing known amount of TargetAntigen when Method is set to DirectCompetitiveELISA or IndirectCompetitiveELISA.

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

ReferenceAntigenDilutionFactor

The dilution ratio of ReferenceAntigen. The ReferenceAntigenSample is always diluted in ReferenceAntigenDiluent. Either ReferenceAntigenDilutionFactor or ReferenceAntigenVolume should be provided but not both.

Default Value: Automatic

Default Calculation: If Method is DirectCompetitiveELISA or IndirectCompetitiveELISA, automatically set to 0.001 (1:1,000).

Pattern Description: Greater than or equal to 0 and less than or equal to 1 or Null.

Programmatic Pattern: (RangeP[0, 1] | Automatic) | Null

Index Matches to: experiment samples

ReferenceAntigenVolume

The volume of undiluted ReferenceAntigen added into the corresponding well of the assay plate. ReferenceAntigenVolume is used as an alternative to ReferenceAntigenDilutionFactor. During antibody preparation, a master mix will be made for antibody dilution, and the diluted Antibodies will be aliquoted into each well.

Default Value: Null

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: RangeP[0*Microliter, 200*Microliter] | Null

Index Matches to: experiment samples

ReferenceAntigenDiluent

The buffer used to dilute the ReferenceAntigen.

Default Value: Automatic

Default Calculation: Method is DirectCompetitiveELISA and IndirectCompetitiveELISA, the option is automatically set to Model[Sample, StockSolution, "1x Carbonate-Bicarbonate Buffer pH10"].

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

ReferenceAntigenStorageCondition

The condition under which the unused portion of Reference Antigen stock sample should be stored.

Default Value: Automatic

Default Calculation: Automatically set to Refrigerator if Method is DirectCompetitiveELISA and IndirectCompetitiveELISA.

Pattern Description: {AmbientStorage, Refrigerator, Freezer, DeepFreezer, CryogenicStorage, YeastIncubation, BacteriaIncubation, MammalianIncubation, TissueCultureCellsIncubation, MicrobialCellsIncubation, MicrobialCellsShakingIncubation, YeastCellsIncubation, YeastCellsShakingIncubation, ViralIncubation, AcceleratedTesting, IntermediateTesting, LongTermTesting, UVVisLightTesting} or Disposal or Null.

Programmatic Pattern: ((SampleStorageTypeP | Disposal) | Automatic) | Null

Index Matches to: experiment samples

PrimaryAntibody

The antibody that directly binds with the TargetAntigen (analyte).

Default Value: Automatic

Default Calculation: The option will be automatically set to an antibody against the TargetAntigen.

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

PrimaryAntibodyDilutionFactor

The dilution ratio of PrimaryAntibody. For DirectELISA, IndirectELISA, DirectSandwichELISA, and IndirectSandwichELISA, the antibody is diluted with PrimaryAntibodyDiluent. For DirectCompetitiveELISA, IndirectCompetitiveELISA, and FastELISA, the antibody is diluted with the corresponding sample. Either PrimaryAntibodyDilutionFactor or PrimaryAntibodyVolume should be provided but not both.

Default Value: Automatic

Default Calculation: If used for DirectELISA, IndirectELISA, DirectSandwichELISA, IndirectSandwichELISA, automatically set to 0.001 (1:1,000). If used for DirectCompetitiveELISA, IndirectCompetitiveELISA, or FastELISA, automatically set to 0.01 (1:100).

Pattern Description: Greater than or equal to 0 and less than or equal to 1 or Null.

Programmatic Pattern: (RangeP[0, 1] | Automatic) | Null

Index Matches to: experiment samples

PrimaryAntibodyVolume

The volume of undiluted PrimaryAntibody added into the corresponding well of the assay plate. PrimaryAntibodyVolume is used as an alternative to PrimaryAntibodyDilutionFactor. During antibody preparation, a master mix will be made for antibody dilution, and the diluted Antibodies will be aliquoted into each well.

Default Value: Null

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: RangeP[0*Microliter, 200*Microliter] | Null

Index Matches to: experiment samples

PrimaryAntibodyDiluent

The buffer used to dilute the PrimaryAntibody.Set to Null when PrimaryAntibody should be diluted into samples (in DirectCompetitiveELISA, IndirectCompetitiveELISA, and FastELISA).

Default Value: Automatic

Default Calculation: If Method is set to DirectELISA, IndirectELISA, DirectSandwichELISA, IndirectSandwichELISA, the options will be automatically set to Model[Sample,"ELISA Blocker Blocking Buffer"].

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

PrimaryAntibodyStorageCondition

The condition under which the unused portion of PrimaryAntibody stock sample should be stored.

Default Value: Refrigerator

Pattern Description: {AmbientStorage, Refrigerator, Freezer, DeepFreezer, CryogenicStorage, YeastIncubation, BacteriaIncubation, MammalianIncubation, TissueCultureCellsIncubation, MicrobialCellsIncubation, MicrobialCellsShakingIncubation, YeastCellsIncubation, YeastCellsShakingIncubation, ViralIncubation, AcceleratedTesting, IntermediateTesting, LongTermTesting, UVVisLightTesting} or Disposal.

Programmatic Pattern: SampleStorageTypeP | Disposal

Index Matches to: experiment samples

SecondaryAntibody

The antibody that binds to the primary antibody.

Default Value: Automatic

Default Calculation: If Method is IndirectELISA, IndirectSandwichELISA, or IndirectCompetitiveELISA, the option is automatically set to a stocked secondary antibody for the primary antibody.

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

SecondaryAntibodyDilutionFactor

The dilution ratio of SecondaryAntibody. SecondaryAntibody is always diluted in the SecondryAntibodyDiluent. Either SecondaryAntibodyDilutionFactor or SecondaryAntibodyVolume should be provided but not both.

Default Value: Automatic

Default Calculation: For IndirectELISA, IndirectSandwichELISA, IndirectCompetitiveELISA, automatically set to 0.001 (1:1,000).

Pattern Description: Greater than or equal to 0 and less than or equal to 1 or Null.

Programmatic Pattern: (RangeP[0, 1] | Automatic) | Null

Index Matches to: experiment samples

SecondaryAntibodyVolume

The volume of SecondaryAntibody added into the corresponding well of the assay plate. SecondaryAntibodyVolume is used as an alternative to SecondaryAntibodyDilutionFactor. During antibody preparation, a master mix will be made for antibody dilution, and the diluted Antibodies will be aliquoted into each well.

Default Value: Null

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: RangeP[0*Microliter, 200*Microliter] | Null

Index Matches to: experiment samples

SecondaryAntibodyDiluent

The buffer used to dilute SecondaryAntibody.

Default Value: Automatic

Default Calculation: If Method is set to IndirectELISA, IndirectSandwichELISA, IndirectCompetitiveELISA, the option will automatically set to Model[Sample,"ELISA Blocker Blocking Buffer"].

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

SecondaryAntibodyStorageCondition

The condition under which the unused portion of Secondary Antibody stock sample should be stored.

Default Value: Automatic

Default Calculation: If method is IndirectELISA, IndirectSandwichELISA, or IndirectCompetitiveELISA, the option is automatically set to Refrigerator.

Pattern Description: {AmbientStorage, Refrigerator, Freezer, DeepFreezer, CryogenicStorage, YeastIncubation, BacteriaIncubation, MammalianIncubation, TissueCultureCellsIncubation, MicrobialCellsIncubation, MicrobialCellsShakingIncubation, YeastCellsIncubation, YeastCellsShakingIncubation, ViralIncubation, AcceleratedTesting, IntermediateTesting, LongTermTesting, UVVisLightTesting} or Disposal or Null.

Programmatic Pattern: ((SampleStorageTypeP | Disposal) | Automatic) | Null

Index Matches to: experiment samples

Sample Antibody Complex Incubation

SampleAntibodyComplexIncubation

Indicates if the pre-mixed samples and antibodies should be incubated before loaded into the assay plate. The plate used for sample-antibody mixing will be discarded after the experiment.

Default Value: Automatic

Default Calculation: Automatically set to True if Method is set to DirectCompetitiveELISA, IndirectCompetitiveELISA, and FastELISA.

Pattern Description: {True, False}

Programmatic Pattern: BooleanP | Automatic

SampleAntibodyComplexIncubationTime

The duration of sample-antibody complex incubation (If needed). In DirectCompetitiveELISA and IndirectCompetitiveELISA, PrimaryAntibody is incubated with the sample. In FastELISA, PrimaryAntibody and CaptureAntibody is incubated with the sample. If Null, the prepared sample-antibody complex will be kept at 4 degree Celsius till ready to use.

Default Value: Automatic

Default Calculation: If the Method is set to DirectCompetitiveELISA, IndirectCompetitiveELISA, or FastELISA, the option is automatically set to 2 Hours.

Pattern Description: Greater than or equal to 0 minutes and less than or equal to 24 hours or Null.

Programmatic Pattern: (RangeP[0*Minute, 24*Hour] | Automatic) | Null

SampleAntibodyComplexIncubationTemperature

The temperature at which sample mixed with Antibodies are incubated. In DirectCompetitiveELISA and IndirectCompetitiveELISA, PrimaryAntibody is incubated with the sample. In FastELISA, PrimaryAntibody and CaptureAntibody are incubated with the sample. If Null, the prepared sample-antibody complex will be used directly.

Default Value: Automatic

Default Calculation: If the Method is set to DirectCompetitiveELISA, IndirectCompetitiveELISA, or FastELISA, the option is automatically set to Ambient.

Pattern Description: Ambient or greater than or equal to 4 degrees Celsius and less than or equal to 50 degrees Celsius or Null.

Programmatic Pattern: ((Ambient | RangeP[4*Celsius, 50*Celsius]) | Automatic) | Null

Coating

Coating

Indicates if Coating is required. Coating is a procedure to non-specifically adsorb protein molecules to the surface of wells of the assay plate.

Default Value: True

Pattern Description: {True, False}

Programmatic Pattern: BooleanP

SampleCoatingVolume

The amount of Sample that is aliquoted into the assay plate, in order for the Sample to be adsorbed to the surface of the well.

Default Value: Automatic

Default Calculation: If Method is DirectELISA or IndirectELISA, CoatingVolume is automatically set to 100 Microliter.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 200*Microliter] | Automatic) | Null

Index Matches to: experiment samples

CoatingAntibodyCoatingVolume

The amount of diluted CoatingAntibody that is aliquoted into the assay plate, in order for the CoatingAntibody to be adsorbed to the surface of the well.

Default Value: Automatic

Default Calculation: If Method is FastELISA, the option is automatically set to 100 Microliter.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 300 microliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 300*Microliter] | Automatic) | Null

Index Matches to: experiment samples

ReferenceAntigenCoatingVolume

The amount of diluted ReferenceAntigen that is aliquoted into the assay plate, in order for the ReferenceAntigen to be adsorbed to the surface of the well.

Default Value: Automatic

Default Calculation: If Method is DirectCompetitiveELISA or IndirectCompetitiveELISA, CoatingVolume is automatically set to 100 Microliter.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 200*Microliter] | Automatic) | Null

Index Matches to: experiment samples

CaptureAntibodyCoatingVolume

The amount of diluted CaptureAntibody that is aliquoted into the assay plate, in order for the CaptureAntibody to be adsorbed to the surface of the well.

Default Value: Automatic

Default Calculation: If Method is DirectSandwichELISA or IndirectSandwichELISA, the option is automatically set to 100 Microliter.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 200*Microliter] | Automatic) | Null

Index Matches to: experiment samples

CoatingTemperature

The temperature at which the Coating Solution is kept in the assay plate, in order for the coating molecules to be adsorbed to the surface of the well.

Default Value: Automatic

Default Calculation: If Coating is set to True, the option is automatically set to 4 degree Celsius.

Pattern Description: Ambient or greater than or equal to 4 degrees Celsius and less than or equal to 50 degrees Celsius or Null.

Programmatic Pattern: ((Ambient | RangeP[4*Celsius, 50*Celsius]) | Automatic) | Null

CoatingTime

The duration when the Coating Solution is kept in the assay plate, in order for the coating molecules to be adsorbed to the surface of the well.

Default Value: Automatic

Default Calculation: If Coating is set to True, the option is automatically set to 16 Hours.

Pattern Description: Greater than or equal to 0 hours and less than or equal to 20 hours or Null.

Programmatic Pattern: (RangeP[0*Hour, 20*Hour] | Automatic) | Null

CoatingWashVolume

The volume of WashBuffer added to rinse off unbound molecule. When Coating is False but Blocking is True, the pre-coated plate must be washed at least once to ensure no liquid is left in the plate.

Default Value: Automatic

Default Calculation: If Coating is set to True, or Coating is False but Blocking is True, the option is automatically set to 250 Microliters.

Pattern Description: Greater than or equal to 25 microliters and less than or equal to 300 microliters or Null.

Programmatic Pattern: (RangeP[25*Microliter, 300*Microliter] | Automatic) | Null

CoatingNumberOfWashes

The number of washes performed after coating. When Coating is False but Blocking is True, the pre-coated plate must be washed at least once to ensure no liquid is left in the plate.

Default Value: Automatic

Default Calculation: If Coating is set to True,or Coating is False but Blocking is True, the option is automatically set to 3.

Pattern Description: Greater than 0 in increments of 1 or Null.

Programmatic Pattern: (GreaterP[0, 1] | Automatic) | Null

Blocking

Blocking

Indicates if a protein solution should be incubated with the assay plate to prevent non-specific binding of molecules to the assay plate.

Default Value: True

Pattern Description: {True, False}

Programmatic Pattern: BooleanP

BlockingBuffer

The protein-containing solution used to prevent non-specific binding of antigen or antibody to the surface of the assay plate.

Default Value: Automatic

Default Calculation: If Blocking is True, automatically set to Model[Sample,"ELISA Blocker Blocking Buffer"].

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

BlockingVolume

The amount of BlockingBuffer that is aliquoted into the appropriate wells of the assay plate, in order to prevent non-specific binding of molecules to the assay plate.

Default Value: Automatic

Default Calculation: If Blocking is True, the option is automatically set to 100 Microliters.

Pattern Description: Greater than or equal to 25 microliters and less than or equal to 300 microliters or Null.

Programmatic Pattern: (RangeP[25*Microliter, 300*Microliter] | Automatic) | Null

Index Matches to: experiment samples

BlockingTime

The duration when the BlockingBuffer is kept with the assay plate, in order to prevent non-specific binding of molecules to the assay plate.

Default Value: Automatic

Default Calculation: If Blocking is True, the option is automatically set to 1 Hour.

Pattern Description: Greater than or equal to 0 hours and less than or equal to 20 hours or Null.

Programmatic Pattern: (RangeP[0*Hour, 20*Hour] | Automatic) | Null

BlockingTemperature

The duration of time when the BlockingBuffer is kept with the assay plate, in order to prevent non-specific binding of molecules to the assay plate.

Default Value: Automatic

Default Calculation: If Blocking is True, the option is automatically set to 25 degree Celsius.

Pattern Description: Greater than or equal to 25 degrees Celsius and less than or equal to 50 degrees Celsius or Null.

Programmatic Pattern: (RangeP[25*Celsius, 50*Celsius] | Automatic) | Null

BlockingMixRate

The speed at which the plate is shaken (orbitally, at a radius of 2 mm) during Blocking incubation. Mixing is not recommended when incubation volume is high, in which case the option should be set to Null.

Default Value: Null

Pattern Description: Greater than or equal to 40 revolutions per minute and less than or equal to 1000 revolutions per minute or Null.

Programmatic Pattern: RangeP[40*RPM, 1000*RPM] | Null

BlockingWashVolume

The volume of WashBuffer added after Blocking, in order to rinse off the unbound molecules from the surface of the wells. If Coating and Blocking are both False, at least one blocking wash is required to ensure no liquid is remaining in the assay plate.

Default Value: Automatic

Default Calculation: If Blocking is True, or Coating and Blocking are both False, the option is automatically set to 250 Microliters.

Pattern Description: Greater than or equal to 25 microliters and less than or equal to 300 microliters or Null.

Programmatic Pattern: (RangeP[25*Microliter, 300*Microliter] | Automatic) | Null

BlockingNumberOfWashes

The number of washes performed after Blocking, in order to rinse off the unbound molecules from the surface of the wells.

Default Value: Automatic

Default Calculation: If Blocking is True, or Coating and Blocking are both False, the option is automatically set to 3.

Pattern Description: Greater than 0 in increments of 1 or Null.

Programmatic Pattern: (GreaterP[0, 1] | Automatic) | Null

Immunosorbent Step

SampleAntibodyComplexImmunosorbentVolume

The volume of the sample-antibody complex to be loaded on each well of the ELISAPlate. In DirectCompetitiveELISA and IndirectCompetitiveELISA, this step enables the free primary antibody to bind to the ReferenceAntigen coated on the plate. In FastELISA, this step enables the PrimaryAntibody-TargetAntigen-CaptureAntibody complex to bind to the CoatingAntibody on the plate.

Default Value: Automatic

Default Calculation: If the Method is set to DirectCompetitiveELISA, IndirectCompetitiveELISA, or FastELISA, the option is automatically set to 100 Microliter.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 200*Microliter] | Automatic) | Null

Index Matches to: experiment samples

SampleAntibodyComplexImmunosorbentTime

The duration of sample-antibody complex incubation.

Default Value: Automatic

Default Calculation: If the Method is set to DirectCompetitiveELISA, IndirectCompetitiveELISA, or FastELISA, the option is automatically set to 2 Hour.

Pattern Description: Greater than or equal to 0 minutes and less than or equal to 24 hours or Null.

Programmatic Pattern: (RangeP[0*Minute, 24*Hour] | Automatic) | Null

SampleAntibodyComplexImmunosorbentTemperature

The temperature of the sample-antibody complex incubation.

Default Value: Automatic

Default Calculation: If the Method is set to DirectCompetitiveELISA, IndirectCompetitiveELISA, or FastELISA, the option is automatically set to 25 Celsius.

Pattern Description: Ambient or greater than or equal to 4 degrees Celsius and less than or equal to 50 degrees Celsius or Null.

Programmatic Pattern: ((Ambient | RangeP[4*Celsius, 50*Celsius]) | Automatic) | Null

SampleAntibodyComplexImmunosorbentMixRate

The speed at which the plate is shaken (orbitally, at a radius of 2 mm) during SampleAntibody mixture incubation in the assay plate. Mixing is not recommended when incubation volume is higher than 200 Microliters, in which case the options should be set to Null.

Default Value: Null

Pattern Description: Greater than or equal to 40 revolutions per minute and less than or equal to 1000 revolutions per minute or Null.

Programmatic Pattern: RangeP[40*RPM, 1000*RPM] | Null

SampleAntibodyComplexImmunosorbentWashVolume

The volume of WashBuffer added to rinse off the unbound primary antibody after sample-antibody complex incubation.

Default Value: Automatic

Default Calculation: If the Method is set to DirectCompetitiveELISA, IndirectCompetitiveELISA, or FastELISA, the option is automatically set to 250 Microliter.

Pattern Description: Greater than or equal to 25 microliters and less than or equal to 300 microliters or Null.

Programmatic Pattern: (RangeP[25*Microliter, 300*Microliter] | Automatic) | Null

SampleAntibodyComplexImmunosorbentNumberOfWashes

The number of rinses performed after sample-antibody complex incubation.

Default Value: Automatic

Default Calculation: If the Method is set to DirectCompetitiveELISA, IndirectCompetitiveELISA, or FastELISA, the option is automatically set to 4.

Pattern Description: Greater than 0 in increments of 1 or Null.

Programmatic Pattern: (GreaterP[0, 1] | Automatic) | Null

SampleImmunosorbentVolume

The volume of the Sample to be loaded on the ELISAPlate for the target antigen to bind to the capture antibody in DirectSandwichELISA and IndirectSandwichELISA.

Default Value: Automatic

Default Calculation: If the Method is set to DirectSandwichELISA and IndirectSandwichELISA, the option is automatically set to 100 Microliters.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 200*Microliter] | Automatic) | Null

Index Matches to: experiment samples

SampleImmunosorbentTime

The duration of Sample incubation.

Default Value: Automatic

Default Calculation: If the Method is set to DirectSandwichELISA and IndirectSandwichELISA, the option is automatically set to 2 Hour.

Pattern Description: Greater than or equal to 0 minutes and less than or equal to 24 hours or Null.

Programmatic Pattern: (RangeP[0*Minute, 24*Hour] | Automatic) | Null

SampleImmunosorbentTemperature

The temperature of the Sample incubation.

Default Value: Automatic

Default Calculation: If the Method is set to DirectSandwichELISA and IndirectSandwichELISA, the option is automatically set to 25 Celsius.

Pattern Description: Greater than or equal to 25 degrees Celsius and less than or equal to 50 degrees Celsius or Null.

Programmatic Pattern: (RangeP[25*Celsius, 50*Celsius] | Automatic) | Null

SampleImmunosorbentMixRate

The speed at which the plate is shaken (orbitally, at a radius of 2 mm) during Sample incubation. Mixing is not recommended when incubation volume is higher than 200 Microliters, in which case the options should be set to Null.

Default Value: Null

Pattern Description: Greater than or equal to 40 revolutions per minute and less than or equal to 1000 revolutions per minute or Null.

Programmatic Pattern: RangeP[40*RPM, 1000*RPM] | Null

SampleImmunosorbentWashVolume

The volume of WashBuffer added to rinse off the unbound Sample after Sample incubation.

Default Value: Automatic

Default Calculation: If the Method is set to DirectSandwichELISA and IndirectSandwichELISA, the option is automatically set to 250 Microliters.

Pattern Description: Greater than or equal to 25 microliters and less than or equal to 300 microliters or Null.

Programmatic Pattern: (RangeP[25*Microliter, 300*Microliter] | Automatic) | Null

SampleImmunosorbentNumberOfWashes

The number of rinses performed after Sample incubation.

Default Value: Automatic

Default Calculation: If the Method is set to DirectSandwichELISA and IndirectSandwichELISA, the option is automatically set to 4.

Pattern Description: Greater than 0 in increments of 1 or Null.

Programmatic Pattern: (GreaterP[0, 1] | Automatic) | Null

PrimaryAntibodyImmunosorbentVolume

The volume of the PrimaryAntibody to be loaded on the ELISA Plate for immunosorbent step.

Default Value: Automatic

Default Calculation: If

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 200*Microliter] | Automatic) | Null

Index Matches to: experiment samples

PrimaryAntibodyImmunosorbentTime

The duration of PrimaryAntibody incubation.

Default Value: Automatic

Default Calculation: If the Method is set to DirectELISA, IndirectELISA, DirectSandwichELISA, or IndirectSandwichELISA, the option is automatically set to 2 Hour.

Pattern Description: Greater than or equal to 0 minutes and less than or equal to 24 hours or Null.

Programmatic Pattern: (RangeP[0*Minute, 24*Hour] | Automatic) | Null

PrimaryAntibodyImmunosorbentTemperature

The temperature of the PrimaryAntibody incubation.

Default Value: Automatic

Default Calculation: If the Method is set to DirectELISA, IndirectELISA, DirectSandwichELISA, or IndirectSandwichELISA, the option is automatically set to 25 Celsius.

Pattern Description: Greater than or equal to 25 degrees Celsius and less than or equal to 50 degrees Celsius or Null.

Programmatic Pattern: (RangeP[25*Celsius, 50*Celsius] | Automatic) | Null

PrimaryAntibodyImmunosorbentMixRate

The speed at which the plate is shaken (orbitally, at a radius of 2 mm) during PrimaryAntibody incubation. Mixing is not recommended when incubation volume is higher than 200 Microliters, in which case the options should be set to Null.

Default Value: Null

Pattern Description: Greater than or equal to 40 revolutions per minute and less than or equal to 1000 revolutions per minute or Null.

Programmatic Pattern: RangeP[40*RPM, 1000*RPM] | Null

PrimaryAntibodyImmunosorbentWashVolume

The volume of WashBuffer added to rinse off the unbound primary antibody after PrimaryAntibody incubation.

Default Value: Automatic

Default Calculation: If the Method is set to DirectELISA, IndirectELISA, DirectSandwichELISA, or IndirectSandwichELISA, the option is automatically set to 250 Microliters.

Pattern Description: Greater than or equal to 25 microliters and less than or equal to 300 microliters or Null.

Programmatic Pattern: (RangeP[25*Microliter, 300*Microliter] | Automatic) | Null

PrimaryAntibodyImmunosorbentNumberOfWashes

The number of rinses performed after PrimaryAntibody incubation.

Default Value: Automatic

Default Calculation: If the Method is set to DirectELISA, IndirectELISA, DirectSandwichELISA, or IndirectSandwichELISA, the option is automatically set to 4.

Pattern Description: Greater than 0 in increments of 1 or Null.

Programmatic Pattern: (GreaterP[0, 1] | Automatic) | Null

SecondaryAntibodyImmunosorbentVolume

The volume of the Secondary Antibody to be loaded on the ELISAPlate for the immunosorbent step.

Default Value: Automatic

Default Calculation: If the Method is set to IndirectELISA, IndirectSandwichELISA, and IndirectCompetitiveELISA, the option is automatically set to 100 Microliter.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 200*Microliter] | Automatic) | Null

Index Matches to: experiment samples

SecondaryAntibodyImmunosorbentTime

The duration of Secondary Antibody incubation.

Default Value: Automatic

Default Calculation: If the Method is set to IndirectELISA, IndirectSandwichELISA, and IndirectCompetitiveELISA, the option is automatically set to 1 Hour.

Pattern Description: Greater than or equal to 0 minutes and less than or equal to 24 hours or Null.

Programmatic Pattern: (RangeP[0*Minute, 24*Hour] | Automatic) | Null

SecondaryAntibodyImmunosorbentTemperature

The temperature of the Secondary Antibody incubation.

Default Value: Automatic

Default Calculation: If the Method is set to IndirectELISA, IndirectSandwichELISA, and IndirectCompetitiveELISA, the option is automatically set to 25 Celsius.

Pattern Description: Greater than or equal to 25 degrees Celsius and less than or equal to 50 degrees Celsius or Null.

Programmatic Pattern: (RangeP[25*Celsius, 50*Celsius] | Automatic) | Null

SecondaryAntibodyImmunosorbentMixRate

The speed at which the plate is shaken (orbitally, at a radius of 2 mm) during Secondary Antibody incubation. Mixing is not recommended when incubation volume is higher than 200 Microliters, in which case the options should be set to Null.

Default Value: Null

Pattern Description: Greater than or equal to 40 revolutions per minute and less than or equal to 1000 revolutions per minute or Null.

Programmatic Pattern: RangeP[40*RPM, 1000*RPM] | Null

SecondaryAntibodyImmunosorbentWashVolume

The volume of WashBuffer added to rinse off the unbound Secondary antibody after SecondaryAntibody incubation.

Default Value: Automatic

Default Calculation: If the Method is set to IndirectELISA, IndirectSandwichELISA, and IndirectCompetitiveELISA, the option is automatically set to 250 Microliters.

Pattern Description: Greater than or equal to 25 microliters and less than or equal to 300 microliters or Null.

Programmatic Pattern: (RangeP[25*Microliter, 300*Microliter] | Automatic) | Null

SecondaryAntibodyImmunosorbentNumberOfWashes

The number of rinses performed after SecondaryAntibody incubation.

Default Value: Automatic

Default Calculation: If the Method is set to IndirectELISA, IndirectSandwichELISA, and IndirectCompetitiveELISA, the option is automatically set to 4.

Pattern Description: Greater than 0 in increments of 1 or Null.

Programmatic Pattern: (GreaterP[0, 1] | Automatic) | Null

Detection

SubstrateSolution

Defines the substrate solution to the enzyme conjugated to the antibody.

Default Value: Automatic

Default Calculation: If enzyme is Horseredish Peroxidase, the option will be automatically set to Model[Sample,"ELISA TMB Stabilized Chromogen"]. If enzyme is Alkaline Phosphatase, then the option is automatically set to Model[Sample,"AP Substrate PNPP Solution"].

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample.

Programmatic Pattern: (ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic

Index Matches to: experiment samples

StopSolution

The reagent that is used to stop the reaction between the enzyme and its substrate.

Default Value: Automatic

Default Calculation: If enzyme is Horseradish Peroxidase, then the option is automatically set to Model[Sample,"ELISA HRP-TMB Stop Solution"]. If enzyme is Alkaline Phosphatase, then the option is automatically set to Model[Sample,"AP Substrate Stop Solution"].

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

Index Matches to: experiment samples

SubstrateSolutionVolume

The volume of substrate to be added to the corresponding well.

Default Value: Automatic

Default Calculation: If SubstrateSolution is populated, then the option is automatically set to 100ul.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters.

Programmatic Pattern: RangeP[0*Microliter, 200*Microliter] | Automatic

Index Matches to: experiment samples

StopSolutionVolume

The volume of StopSolution to be added to the corresponding well.

Default Value: Automatic

Default Calculation: If StopSolution is selected, the StopSolutionVolume is automatically set to 100ul.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 200*Microliter] | Automatic) | Null

Index Matches to: experiment samples

SubstrateIncubationTime

The time during which the the colorimetric reaction occurs.

Default Value: 30 minutes

Pattern Description: Greater than or equal to 0 minutes and less than or equal to 24 hours.

Programmatic Pattern: RangeP[0*Minute, 24*Hour]

SubstrateIncubationTemperature

The temperature of the Substrate incubation, in order for the detection reaction to take place where the antibody-conjugated enzyme (such as Horseradish Peroxidase or Alkaline Phosphatase) catalyzes the colorimetric reaction.

Default Value: 25 degrees Celsius

Pattern Description: Greater than or equal to 25 degrees Celsius and less than or equal to 50 degrees Celsius.

Programmatic Pattern: RangeP[25*Celsius, 50*Celsius]

SubstrateIncubationMixRate

The speed at which the plate is shaken (orbitally, at a radius of 2 mm) during Substrate incubation. Mixing is not recommended when incubation volume is higher than 200 Microliters, in which case the options should be set to Null.

Default Value: Null

Pattern Description: Greater than or equal to 40 revolutions per minute and less than or equal to 1000 revolutions per minute or Null.

Programmatic Pattern: RangeP[40*RPM, 1000*RPM] | Null

AbsorbanceWavelength

The wavelength used to detect the absorbance of light by the product of the detection reaction.

Default Value: 450 nanometers

Pattern Description: {405 nanometers, 450 nanometers, 492 nanometers, 620 nanometers} or list of one or more {405 nanometers, 450 nanometers, 492 nanometers, 620 nanometers} entries.

Programmatic Pattern: (405*Nanometer | 450*Nanometer | 492*Nanometer | 620*Nanometer) | {(405*Nanometer | 450*Nanometer | 492*Nanometer | 620*Nanometer)..}

PrereadBeforeStop

Indicate if colorimetric reactions between the enzyme and its substrate will be checked by the plate reader before the stopping reagent was added to terminate the reaction.

Default Value: Automatic

Default Calculation: Is set automatically to True if either or both of PrereadTimepoints and PrereadAbsorbanceWavelength are specified. Otherwise is set to False.

Pattern Description: True or False.

Programmatic Pattern: BooleanP | Automatic

PrereadTimepoints

The list of time points when absorbance intensitied at each PreparedAbsorbanceWavelength during the Preread process (before the colorimetric reaction was terminated).

Default Value: Automatic

Default Calculation: If PrereadBeforeStop is True, this option is set to one single value: the half of the SubstrateIncubationTime. Otherwise is set to Null.

Pattern Description: Greater than or equal to 0 minutes and less than or equal to 72 hours or list of one or more greater than or equal to 0 minutes and less than or equal to 72 hours entries or Null.

Programmatic Pattern: ((RangeP[0*Minute, $MaxExperimentTime] | {RangeP[0*Minute, $MaxExperimentTime]..}) | Automatic) | Null

PrereadAbsorbanceWavelength

The wavelength used to detect the absorbance of light during the Preread process (before the colorimetric reaction was terminated).

Default Value: Automatic

Default Calculation: If PrereadBeforeStop is True, this option is set to {450 Nanometer}. Otherwise is set to Null.

Pattern Description: {405 nanometers, 450 nanometers, 492 nanometers, 620 nanometers} or list of one or more {405 nanometers, 450 nanometers, 492 nanometers, 620 nanometers} entries or Null.

Programmatic Pattern: (((405*Nanometer | 450*Nanometer | 492*Nanometer | 620*Nanometer) | {(405*Nanometer | 450*Nanometer | 492*Nanometer | 620*Nanometer)..}) | Automatic) | Null

SignalCorrection

The absorbance reading that is used to eliminate the interference of background absorbance (such as from ELISAPlate material and dust). If True, a reading at 620 nm is read at the same time of the AbsorbanceWavelength. The correction is done by subtracting the reading at 620nm from that at the AbsorbanceWavelength.

Default Value: False

Pattern Description: {True, False} or Null.

Programmatic Pattern: BooleanP | Null

Standard

Standard

A sample containing known amount of TargetAntigen molecule. Standard is used for the quantification of Standard analyte.

Default Value: Automatic

Default Calculation: If TargetAntigen is specified, standard will be automatically set to the DefaultSampleModel of the target antigen.

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

Index Matches to: Standard

StandardTargetAntigen

The Analyte molecule(e.g., peptide, protein, and hormone) detected and quantified in the Standard samples by Antibodies in the ELISA experiment. This option is used to automatically set sample Antibodies and the corresponding experiment conditions of Standards and Blanks.

Default Value: Automatic

Default Calculation: Automatically set to the Model[Molecule] in the Analyte field of the sample.

Pattern Description: An object of type or subtype Model[Molecule] or Null.

Programmatic Pattern: (ObjectP[{Model[Molecule]}] | Automatic) | Null

Index Matches to: Standard

StandardSerialDilutionCurve

The collection of serial dilutions that will be performed on sample. StandardLoadingVolume of each dilution will be transferred to the ELISAPlate. For Serial Dilution Volumes, the Transfer Volume is taken out of the sample and added to a second well with the Diluent Volume of the Diluent. It is mixed, then the Transfer Volume is taken out of that well to be added to a third well. This is repeated to make Number Of Dilutions diluted samples. For example, if a 100 ug/ ml sample with a Transfer Volume of 20 Microliters, a Diluent Volume of 60 Microliters and a Number of Dilutions of 3 is used, it will create a DilutionCurve of 25 ug/ ml, 6.25 ug/ ml, and 1.5625 ug/ ml with each dilution having a volume of 60 Microliters. For Serial Dilution Factors, the sample will be diluted by the dilution factor at each transfer step. IMPORTANT: because the dilution curve does not intrinsically include the original sample, if the original standard solution is to be included in the dilution curve, the first diluting factor should be set to 1 or Diluent Volume should be 0 Microliters. During experiment, an 5% extra volume than specified is going to be prepared in order to offset pipetting errors. Therefore, the total volume for each well specified in this option should be equal or greater than the volume needed for the experiment. Because the dilution of each assay (well) is prepared independently, the NumberOfReplications should not be considered when determining the Standard Volume. The plate used for sample dilutions will be discarded after the experiment. Note: if spike or antibodies are to be mixed with samples, their volumes are counted towards diluent volume.

Figure 3.3: Use the SerialDilutionCuve option to create a collection of serial dilutions that will be performed on standards.

Default Value: Automatic

Default Calculation: Automatically set to Null if the StandardDilutionCurve is specified. In all other cases it is automatically set to a Standard Volume of 100 Microliters and a Constant Dilution Factor of 0.5. The Number Of Dilutions is automatically set to 6.

Pattern Description: Serial Dilution Factor or Serial Dilution Volumes or Null.

Programmatic Pattern: (({GreaterEqualP[0*Microliter], {RangeP[0, 1], GreaterP[0, 1]} | {RangeP[0, 1]..}} | {RangeP[0*Microliter, 1000*Microliter], RangeP[40*Microliter, 1000*Microliter], GreaterP[0, 1]}) | Automatic) | Null

Index Matches to: Standard

StandardDilutionCurve

The collection of dilutions that will be performed on each sample. For Fixed Dilution Volume Dilution Curves, the Standard Amount is the volume of the sample that will be mixed the Diluent Volume of the Diluent to create a desired concentration. The Standard Volume is the TOTAL volume of the sample that will created after being diluted by the Dilution Factor. For example, a 1 ug/ ml sample with a dilution factor of 0.7 will be diluted to a concentration 0.7 ug/ ml. IMPORTANT: because the dilution curve does not intrinsically include the original sample, if the original standard solution is to be included in the dilution curve, the first diluting factor should be set to 1 or Diluent Volume must be 0 Microliter. During experiment, an 5% extra volume than specified is going to be prepared in order to offset pipetting errors. Therefore, the total volume for each well specified in this option should be equal or greater than the volume needed for the experiment. Because the dilution of each assay (well) is prepared independently, the NumberOfReplications should not be considered when determining the Standard Volume. The plate used for sample dilutions will be discarded after the experiment. Note: if spike or antibodies are to be mixed with samples, their volumes are counted towards diluent volume.

Figure 3.4: Use the DilutionCuve option to create a collection of dilutions that will be performed on standards.

Default Value: Automatic

Default Calculation: Automatically set to Null if the SerialDilutionCurve is specified. If SerialDilutionCurve is set to Null, then automatically set Standard Assay Volume to 100ul, dilution factor to 0.5, 0,25, 0.125, 0.0625, 0.03125, 0.015625.

Pattern Description: Fixed Dilution Factor or Fixed Dilution Volume or Null.

Programmatic Pattern: (({{RangeP[0*Microliter, 1000*Microliter], RangeP[0*Microliter, 1000*Microliter]}..} | {{RangeP[40*Microliter, 1500*Microliter], RangeP[0, 1]}..}) | Automatic) | Null

Index Matches to: Standard

StandardDiluent

The buffer used to perform multiple dilutions on Standards.

Default Value: Automatic

Default Calculation: If StandardDilutionCurve and StandardSerialDilutionCurve are not both Null, in the case when Method is set to DirectELISA and IndirectELISA, the option is automatically set to Model[Sample, StockSolution, "1x Carbonate-Bicarbonate Buffer pH10"]; in all other cases, the option is automatically set to Model[Sample,"ELISA Blocker Blocking Buffer"].

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

StandardStorageCondition

The condition under which the unused portion of Standard stock sample should be stored.

Default Value: Automatic

Default Calculation: If Standard is Specified, the option is automatically set to Freezer.

Pattern Description: {AmbientStorage, Refrigerator, Freezer, DeepFreezer, CryogenicStorage, YeastIncubation, BacteriaIncubation, MammalianIncubation, TissueCultureCellsIncubation, MicrobialCellsIncubation, MicrobialCellsShakingIncubation, YeastCellsIncubation, YeastCellsShakingIncubation, ViralIncubation, AcceleratedTesting, IntermediateTesting, LongTermTesting, UVVisLightTesting} or Disposal or Null.

Programmatic Pattern: ((SampleStorageTypeP | Disposal) | Automatic) | Null

Index Matches to: Standard

StandardCoatingAntibody

The sample containing the antibody that is used for coating in FastELISA.

Default Value: Automatic

Default Calculation: If Method is FastELISA and Standard is not Null, automatically set to an antibody against a tag which is conjugated to a the StandardCaptureAntibody.

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

Index Matches to: Standard

StandardCoatingAntibodyDilutionFactor

The dilution ratio of StandardCoatingAntibody. StandardCoatingAntibody is diluted with CoatingAntibodyDiluent. Either StandardCoatingAntibodyDilutionFactor or StandardCoatingAntibodyVolume should be provided but not both.

Default Value: Automatic

Default Calculation: If Method is FastELISA and Standard is not Null, automatically set to 0.001 (1:1,000)

Pattern Description: Greater than or equal to 0 and less than or equal to 1 or Null.

Programmatic Pattern: (RangeP[0, 1] | Automatic) | Null

Index Matches to: Standard

StandardCoatingAntibodyVolume

The volume of undiluted StandardCoatingAntibody added into the corresponding well of the assay plate. StandardCoatingAntibody is diluted with CoatingAntibodyDiluent. StandardCoatingAntibodyVolume is used as an alternative to StandardCoatingAntibodyDilutionFactor. During antibody preparation, a master mix will be made for antibody dilution, and the diluted Antibodies will be aliquoted into each well.

Default Value: Null

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: RangeP[0*Microliter, 200*Microliter] | Null

Index Matches to: Standard

StandardCaptureAntibody

The sample containing the antibody that is used to pull down the antigen from sample solution to the plate in DirectSandwichELISA, IndirectSandwichELISA, and FastELISA.

Default Value: Automatic

Default Calculation: Automatically set to Null is Standard is Null. If Method is FastELISA, automatically set to an antibody containing an affinity tag and against the TargetAntigen. If Method is DirectSandwichELISA or IndirectSandwichELISA, automatically set to an un-tagged antibody against TargetAntigen.

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

Index Matches to: Standard

StandardCaptureAntibodyDilutionFactor

The dilution ratio of StandardCaptureAntibody. For DirectSandwichELISA and IndirectSandwichELISA, StandardCaptureAntibody is diluted with CaptureAntibodyDiluent. For FastELISA, StandardCaptureAntibody is diluted in the corresponding standard. Either StandardCaptureAntibodyDilutionFactor or StandardCaptureAntibodyVolume should be provided but not both.

Default Value: Automatic

Default Calculation: When Standard is not Null, if Method is DirectSandwichELISA or IndirectSandwichELISA, automatically set to 0.001 (1:1,000). If Method is FastELISA, automatically set to 0.01 (1:100).

Pattern Description: Greater than or equal to 0 and less than or equal to 1 or Null.

Programmatic Pattern: (RangeP[0, 1] | Automatic) | Null

Index Matches to: Standard

StandardCaptureAntibodyVolume

The volume of undiluted CaptureAntibody added into the corresponding well of the assay plate. StandardCaptureAntibodyVolume is used as an alternative to StandardCaptureAntibodyDilutionFactor. During antibody preparation, a master mix will be made for antibody dilution, and the diluted Antibodies will be aliquoted into each well.

Default Value: Null

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: RangeP[0*Microliter, 200*Microliter] | Null

Index Matches to: Standard

StandardReferenceAntigen

The sample containing the antigen that is used in DirectCompetitiveELISA or IndirectCompetitiveELISA. The StandardReferenceAntigen competes with sample antigen for the binding of the StandardPrimaryAntibody. Reference antigen is sometimes also referred to as inhibitor antigen.

Default Value: Automatic

Default Calculation: Automatically set to a sample containing known amount of TargetAntigen when Method is set to DirectCompetitiveELISA or IndirectCompetitiveELISA and Standard is not Null.

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

Index Matches to: Standard

StandardReferenceAntigenDilutionFactor

The dilution ratio of StandardReferenceAntigen. For DirectCompetitiveELISA and IndirectCompetitiveELISA, the StandardReferenceAntigenStandard is diluted in ReferenceAntigenDiluent. Either StandardReferenceAntigenDilutionFactor or StandardReferenceAntigenVolume should be provided but not both.

Default Value: Automatic

Default Calculation: Automatically set to 0.001 (1:1,000) if Method is DirectCompetitiveELISA or IndirectCompetitiveELISA.

Pattern Description: Greater than or equal to 0 and less than or equal to 1 or Null.

Programmatic Pattern: (RangeP[0, 1] | Automatic) | Null

Index Matches to: Standard

StandardReferenceAntigenVolume

The volume of ReferenceAntigen added into the corresponding well of the assay plate. StandardReferenceAntigenVolume is used as an alternative to StandardReferenceAntigenDilutionFactor. During antibody preparation, a master mix will be made for antibody dilution, and the diluted Antibodies will be aliquoted into each well.

Default Value: Null

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: RangeP[0*Microliter, 200*Microliter] | Null

Index Matches to: Standard

StandardPrimaryAntibody

The antibody that directly binds to the analyte.

Default Value: Automatic

Default Calculation: If Standard is not Null, the option will be automatically set to an antibody against the TargetAntigen.

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

Index Matches to: Standard

StandardPrimaryAntibodyDilutionFactor

The dilution ratio of StandardPrimaryAntibody. For DirectELISA, IndirectELISA, DirectSandwichELISA, and IndirectSandwichELISA, the antibody is diluted with PrimaryAntibodyDiluent. For DirectCompetitiveELISA, IndirectCompetitiveELISA, and FastELISA, the antibody is diluted in the corresponding sample. Either StandardPrimaryAntibodyDilutionFactor or StandardPrimaryAntibodyVolume should be provided but not both.

Default Value: Automatic

Default Calculation: When Standard is not Null, if used for DirectELISA, IndirectELISA, DirectSandwichELISA, IndirectSandwichELISA, automatically set to 0.001 (1:1,000). If used for DirectCompetitiveELISA, IndirectCompetitiveELISA, or FastELISA, automatically set to 0.01 (1:100).

Pattern Description: Greater than or equal to 0 and less than or equal to 1 or Null.

Programmatic Pattern: (RangeP[0, 1] | Automatic) | Null

Index Matches to: Standard

StandardPrimaryAntibodyVolume

The volume of PrimaryAntibody added into the corresponding well of the assay plate. StandardPrimaryAntibodyVolume is used as an alternative to StandardPrimaryAntibodyDilutionFactor. During antibody preparation, a master mix will be made for antibody dilution, and the diluted Antibodies will be aliquoted into each well.

Default Value: Null

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: RangeP[0*Microliter, 200*Microliter] | Null

Index Matches to: Standard

StandardSecondaryAntibody

The antibody that binds to the primary antibody.

Default Value: Automatic

Default Calculation: If Method is IndirectELISA, IndirectSandwichELISA, or IndirectCompetitiveELISA, the option is automatically set to a stocked secondary antibody for the primary antibody.

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

Index Matches to: Standard

StandardSecondaryAntibodyDilutionFactor

The dilution ratio of StandardSecondaryAntibody. StandardSecondaryAntibody is always diluted in the SecondaryAntibodyDiluent. Either StandardSecondaryAntibodyDilutionFactor or StandardSecondaryAntibodyVolume should be provided but not both.

Default Value: Automatic

Default Calculation: If Standard is not Null, for IndirectELISA, IndirectSandwichELISA, IndirectCompetitiveELISA, automatically set to 0.001 (1:1,000).

Pattern Description: Greater than or equal to 0 and less than or equal to 1 or Null.

Programmatic Pattern: (RangeP[0, 1] | Automatic) | Null

Index Matches to: Standard

StandardSecondaryAntibodyVolume

The volume of SecondaryAntibody added into the corresponding well of the assay plate. StandardSecondaryAntibodyVolume is used as an alternative to StandardSecondaryAntibodyDilutionFactor. During antibody preparation, a master mix will be made for antibody dilution, and the diluted Antibodies will be aliquoted into each well.

Default Value: Null

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: RangeP[0*Microliter, 200*Microliter] | Null

Index Matches to: Standard

StandardCoatingVolume

The amount of Standard that is aliquoted into the ELISAPlate, in order for the Standard to be adsorbed to the surface of the well.

Default Value: Automatic

Default Calculation: If Method is DirectELISA or IndirectELISA, StandardCoatingVolume is automatically set to 200 Microliter.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 200*Microliter] | Automatic) | Null

Index Matches to: Standard

StandardReferenceAntigenCoatingVolume

The amount of StandardReferenceAntigen that is aliquoted into the assay plate, in order for the StandardReferenceAntigen to be adsorbed to the surface of the well.

Default Value: Automatic

Default Calculation: If Method is DirectCompetitiveELISA or IndirectCompetitiveELISA, CoatingVolume is automatically set to 200 Microliter.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 200*Microliter] | Automatic) | Null

Index Matches to: Standard

StandardCoatingAntibodyCoatingVolume

The amount of diluted StandardCoatingAntibody that is aliquoted into the ELISAPlate, in order for the StandardCoatingAntibody to be adsorbed to the surface of the well.

Default Value: Automatic

Default Calculation: If Method is FastELISA, the option is automatically set to 200 Microliter.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 200*Microliter] | Automatic) | Null

Index Matches to: Standard

StandardCaptureAntibodyCoatingVolume

The amount of diluted StandardCaptureAntibody that is aliquoted into the ELISAPlate, in order for the StandardCaptureAntibody to be adsorbed to the surface of the well.

Default Value: Automatic

Default Calculation: If Method is DirectSandwichELISA or IndirectSandwichELISA, the option is automatically set to 200 Microliter.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 200*Microliter] | Automatic) | Null

Index Matches to: Standard

StandardBlockingVolume

The amount of BlockingBuffer that is aliquoted into the appropriate wells of the ELISAPlate.

Default Value: Automatic

Default Calculation: If Blocking is True, the option is automatically set to 100 Microliter.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 300 microliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 300*Microliter] | Automatic) | Null

Index Matches to: Standard

StandardAntibodyComplexImmunosorbentVolume

The volume of the standard-antibody complex to be loaded on the ELISAPlate. In DirectCompetitiveELISA and IndirectCompetitiveELISA, this step enables the free StandardPrimaryAntibody to bind to the StandardReferenceAntigen coated on the plate. In FastELISA, this step enables the PrimaryAntibody-TargetAntigen-CaptureAntibody complex to bind to the CoatingAntibody on the plate.

Default Value: Automatic

Default Calculation: If the Method is set to DirectCompetitiveELISA, IndirectCompetitiveELISA, or FastELISA, the option is automatically set to 100 Microliter.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 200*Microliter] | Automatic) | Null

Index Matches to: Standard

StandardImmunosorbentVolume

The volume of the Standard to be loaded on the ELISAPlate for the target antigen to bind to the capture antibody in DirectSandwichELISA and IndirectSandwichELISA.

Default Value: Automatic

Default Calculation: If the Method is set to DirectSandwichELISA and IndirectSandwichELISA, the option is automatically set to 100 Microliter.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 200*Microliter] | Automatic) | Null

Index Matches to: Standard

StandardPrimaryAntibodyImmunosorbentVolume

The volume of the StandarPrimaryAntibody to be loaded on the ELISAPlate for Immunosorbent assay.

Default Value: Automatic

Default Calculation: If the Method is set to DirectELISA, IndirectELISA, DirectSandwichELISA, or IndirectSandwichELISA, the option is automatically set to 100 Microliter.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 200*Microliter] | Automatic) | Null

Index Matches to: Standard

StandardSecondaryAntibodyImmunosorbentVolume

The volume of the StandardSecondaryAntibody to be loaded on the ELISAPlate for immunosorbent step.

Default Value: Automatic

Default Calculation: If the Method is set to IndirectELISA, IndirectSandwichELISA, and IndirectCompetitiveELISA, the option is automatically set to 100 Microliter.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 200*Microliter] | Automatic) | Null

Index Matches to: Standard

StandardSubstrateSolution

Defines the substrate solution for the standard solution.

Default Value: Automatic

Default Calculation: If enzyme is Horseredish Peroxidase, the option will be automatically set to Model[Sample,"ELISA TMB Stabilized Chromogen"]. If enzyme is Alkaline Phosphatase, then the option is automatically set to Model[Sample,"AP Substrate PNPP Solution"].

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

Index Matches to: Standard

StandardStopSolution

The reagent that is used to stop the reaction between the enzyme and its substrate.

Default Value: Automatic

Default Calculation: If enzyme is Horseradish Peroxidase, then the option is automatically set to Model[Sample,"ELISA HRP-TMB Stop Solution"]. If enzyme is Alkaline Phosphatase, then the option is automatically set to Model[Sample,"AP Substrate Stop Solution"].

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

Index Matches to: Standard

StandardSubstrateSolutionVolume

The volume of StandardSubstrateSolution to be added to the corresponding well.

Default Value: Automatic

Default Calculation: If StandardSubstrateSolution is populated and Standard is not Null, then the option is automatically set to 100ul.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 200*Microliter] | Automatic) | Null

Index Matches to: Standard

StandardStopSolutionVolume

The volume of StopSolution to be added to the corresponding well.

Default Value: Automatic

Default Calculation: If Model[Sample,"ELISA TMB Stabilized Chromogen"] or Model[Sample,"ELISA HRP-TMB Stop Solution"] is selected for StandardSubstrateSolution, the StopSolutionVolume is automatically set to 100ul.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 200*Microliter] | Automatic) | Null

Index Matches to: Standard

Blank

Blank

A sample containing no TargetAntigen, used as a baseline or negative control for the ELISA.

Default Value: Automatic

Default Calculation: If In DirectELISA and IndirectELISA, the option will be automatically set to Model[Sample, StockSolution, "1x Carbonate-Bicarbonate Buffer pH10"]. Otherwise, the option will be automatically set to Model[Sample, "ELISA Blocker Blocking Buffer"].

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

Index Matches to: Blank

BlankTargetAntigen

The Analyte molecule(e.g., peptide, protein, and hormone) detected and quantified in the blanks by Antibodies in the ELISA experiment. This option is used to automatically set Antibodies and the corresponding experiment conditions.

Default Value: Automatic

Default Calculation: Automatically set to the Model[Molecule] in the Analyte field of the sample.

Pattern Description: An object of type or subtype Model[Molecule] or Null.

Programmatic Pattern: (ObjectP[{Model[Molecule]}] | Automatic) | Null

Index Matches to: Blank

BlankStorageCondition

The condition under which the unused portion of Blank should be stored.

Default Value: Automatic

Default Calculation: Automatically set to Refrigerator if Blank is not Null.

Pattern Description: {AmbientStorage, Refrigerator, Freezer, DeepFreezer, CryogenicStorage, YeastIncubation, BacteriaIncubation, MammalianIncubation, TissueCultureCellsIncubation, MicrobialCellsIncubation, MicrobialCellsShakingIncubation, YeastCellsIncubation, YeastCellsShakingIncubation, ViralIncubation, AcceleratedTesting, IntermediateTesting, LongTermTesting, UVVisLightTesting} or Disposal or Null.

Programmatic Pattern: ((SampleStorageTypeP | Disposal) | Automatic) | Null

Index Matches to: Blank

BlankCoatingAntibody

The sample containing the antibody that is used for coating in FastELISA.

Default Value: Automatic

Default Calculation: If Method is FastELISA and Blank is not Null, automatically set to an antibody against a tag which is conjugated to a the StandardCaptureAntibody.

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

Index Matches to: Blank

BlankCoatingAntibodyDilutionFactor

The dilution ratio of BlankCoatingAntibody. BlankCoatingAntibody is diluted with CoatingAntibodyDiluent. Either BlankCoatingAntibodyDilutionFactor or BlankCoatingAntibodyVolume should be provided but not both.

Default Value: Automatic

Default Calculation: If Method is FastELISA and Blank is not Null, automatically set to 0.001 (1:1,000)

Pattern Description: Greater than or equal to 0 and less than or equal to 1 or Null.

Programmatic Pattern: (RangeP[0, 1] | Automatic) | Null

Index Matches to: Blank

BlankCoatingAntibodyVolume

The volume of BlankCoatingAntibody added into the corresponding well of the assay plate. BlankCoatingAntibody is diluted with CoatingAntibodyDiluent. BlankCoatingAntibodyVolume is used as an alternative to BlankCoatingAntibodyDilutionFactor. During antibody preparation, a master mix will be made for antibody dilution, and the diluted Antibodies will be aliquoted into each well.

Default Value: Null

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: RangeP[0*Microliter, 200*Microliter] | Null

Index Matches to: Blank

BlankCaptureAntibody

The sample containing the antibody that is used to pull down the antigen from sample solution to the plate in DirectSandwichELISA, IndirectSandwichELISA, and FastELISA.

Default Value: Automatic

Default Calculation: Automatically set to Null is Blank is Null. If Method is FastELISA, automatically set to an antibody containing an affinity tag and against the TargetAntigen. If Method is DirectSandwichELISA or IndirectSandwichELISA, automatically set to an un-tagged antibody against TargetAntigen.

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

Index Matches to: Blank

BlankCaptureAntibodyDilutionFactor

The dilution ratio of BlankCaptureAntibody. For DirectSandwichELISA and IndirectSandwichELISA, BlankCaptureAntibody is diluted with CaptureAntibodyDiluent. For FastELISA, BlankCaptureAntibody is diluted in the corresponding sample. Either BlankCaptureAntibodyDilutionFactor or BlankCaptureAntibodyVolume should be provided but not both.

Default Value: Automatic

Default Calculation: If Method is DirectSandwichELISA or IndirectSandwichELISA, automatically set to 0.001 (1:1,000). If Method is FastELISA, automatically set to 0.01 (1:100).

Pattern Description: Greater than or equal to 0 and less than or equal to 1 or Null.

Programmatic Pattern: (RangeP[0, 1] | Automatic) | Null

Index Matches to: Blank

BlankCaptureAntibodyVolume

The volume of CaptureAntibody added into the corresponding well of the assay plate. BlankCaptureAntibodyVolume is used as an alternative to BlankCaptureAntibodyDilutionFactor. During antibody preparation, a master mix will be made for antibody dilution, and the diluted Antibodies will be aliquoted into each well.

Default Value: Null

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: RangeP[0*Microliter, 200*Microliter] | Null

Index Matches to: Blank

BlankReferenceAntigen

The Sample containing the antigen that is used in DirectCompetitiveELISA or IndirectCompetitiveELISA. The BlankReferenceAntigen competes with sample antigen for the binding of the BlankPrimaryAntibody. Reference antigen is sometimes also referred to as inhibitor antigen.

Default Value: Automatic

Default Calculation: Automatically set to a sample containing known amount of TargetAntigen when Method is set to DirectCompetitiveELISA or IndirectCompetitiveELISA and Blank is not Null.

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

Index Matches to: Blank

BlankReferenceAntigenDilutionFactor

The dilution ratio of BlankReferenceAntigen. For DirectCompetitiveELISA and IndirectCompetitiveELISA, the BlankReferenceAntigenBlank is diluted in ReferenceAntigenDiluent. Either BlankReferenceAntigenDilutionFactor or BlankReferenceAntigenVolume should be provided but not both.

Default Value: Automatic

Default Calculation: Automatically set to 0.001 (1:1,000) if Method is DirectCompetitiveELISA or IndirectCompetitiveELISA.

Pattern Description: Greater than or equal to 0 and less than or equal to 1 or Null.

Programmatic Pattern: (RangeP[0, 1] | Automatic) | Null

Index Matches to: Blank

BlankReferenceAntigenVolume

The volume of ReferenceAntigen added into the corresponding well of the assay plate. BlankReferenceAntigenVolume is used as an alternative to BlankReferenceAntigenDilutionFactor. During antibody preparation, a master mix will be made for antibody dilution, and the diluted Antibodies will be aliquoted into each well.

Default Value: Null

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: RangeP[0*Microliter, 200*Microliter] | Null

Index Matches to: Blank

BlankPrimaryAntibody

The antibody that directly binds with the analyte.

Default Value: Automatic

Default Calculation: The option will be automatically set to an antibody against the BlankTargetAntigen if Blank is not Null.

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

Index Matches to: Blank

BlankPrimaryAntibodyDilutionFactor

The dilution ratio of BlankPrimaryAntibody. For DirectELISA, IndirectELISA, DirectSandwichELISA, and IndirectSandwichELISA, the antibody is diluted with PrimaryAntibodyDiluent. For DirectCompetitiveELISA, IndirectCompetitiveELISA, and FastELISA, the antibody is diluted in the corresponding sample. Either BlankPrimaryAntibodyDilutionFactor or BlankPrimaryAntibodyVolume should be provided but not both.

Default Value: Automatic

Default Calculation: When Blank is not Null, if used for DirectELISA, IndirectELISA, DirectSandwichELISA, IndirectSandwichELISA, automatically set to 0.001 (1:1,000). If used for DirectCompetitiveELISA, IndirectCompetitiveELISA, or FastELISA, automatically set to 0.01 (1:100).

Pattern Description: Greater than or equal to 0 and less than or equal to 1 or Null.

Programmatic Pattern: (RangeP[0, 1] | Automatic) | Null

Index Matches to: Blank

BlankPrimaryAntibodyVolume

The volume of PrimaryAntibody added into the corresponding well of the assay plate. BlankPrimaryAntibodyVolume is used as an alternative to BlankPrimaryAntibodyDilutionFactor. During antibody preparation, a master mix will be made for antibody dilution, and the diluted Antibodies will be aliquoted into each well.

Default Value: Null

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: RangeP[0*Microliter, 200*Microliter] | Null

Index Matches to: Blank

BlankSecondaryAntibody

The antibody that binds to the primary antibody.

Default Value: Automatic

Default Calculation: If Method is IndirectELISA, IndirectSandwichELISA, or IndirectCompetitiveELISA and Blank is not Null, the option is automatically set to an stocked secondary antibody for the primary antibody.

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

Index Matches to: Blank

BlankSecondaryAntibodyDilutionFactor

The dilution ratio of BlankSecondaryAntibody. BlankSecondaryAntibody is always diluted in the SecondaryAntibodyDiluent. Either BlankSecondaryAntibodyDilutionFactor or BlankSecondaryAntibodyVolume should be provided but not both.

Default Value: Automatic

Default Calculation: If Blank is not Null, for IndirectELISA, IndirectSandwichELISA, IndirectCompetitiveELISA, automatically set to 0.001 (1:1,000).

Pattern Description: Greater than or equal to 0 and less than or equal to 1 or Null.

Programmatic Pattern: (RangeP[0, 1] | Automatic) | Null

Index Matches to: Blank

BlankSecondaryAntibodyVolume

The volume of BlankSecondaryAntibody added into the corresponding well of the assay plate. BlankSecondaryAntibodyVolume is used as an alternative to BlankSecondaryAntibodyDilutionFactor. During antibody preparation, a master mix will be made for antibody dilution, and the diluted Antibodies will be aliquoted into each well.

Default Value: Null

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: RangeP[0*Microliter, 200*Microliter] | Null

Index Matches to: Blank

BlankCoatingVolume

The amount of Blank that is aliquoted into the ELISAPlate.

Default Value: Automatic

Default Calculation: If Blank is not Null, and Method is DirectELISA or IndirectELISA, CoatingVolume is automatically set to 200 Microliter.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 200*Microliter] | Automatic) | Null

Index Matches to: Blank

BlankReferenceAntigenCoatingVolume

The amount of diluted BlankReferenceAntigen that is aliquoted into the assay plate, in order for the BlankReferenceAntigen to be adsorbed to the surface of the well.

Default Value: Automatic

Default Calculation: If Method is DirectCompetitiveELISA or IndirectCompetitiveELISA, CoatingVolume is automatically set to 200 Microliter.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 200*Microliter] | Automatic) | Null

Index Matches to: Blank

BlankCoatingAntibodyCoatingVolume

The amount of diluted BlankCoatingAntibody that is aliquoted into the ELISAPlate, in order for the BlankCoatingAntibody to be adsorbed to the surface of the well.

Default Value: Automatic

Default Calculation: If Method is FastELISA, the Option is automatically set to 200 Microliter.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 200*Microliter] | Automatic) | Null

Index Matches to: Blank

BlankCaptureAntibodyCoatingVolume

The amount of diluted BlankCaptureAntibody that is aliquoted into the ELISAPlate, in order for the BlankCaptureAntibody to be adsorbed to the surface of the well.

Default Value: Automatic

Default Calculation: If Method is DirectSandwichELISA or IndirectSandwichELISA, the option is automatically set to 200 Microliter.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 200*Microliter] | Automatic) | Null

Index Matches to: Blank

BlankBlockingVolume

The amount of BlankBlockingBuffer that is aliquoted into the appropriate wells of the ELISAPlate.

Default Value: Automatic

Default Calculation: If Blocking is True, the option is automatically set to 200 Microliter.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 300 microliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 300*Microliter] | Automatic) | Null

Index Matches to: Blank

BlankAntibodyComplexImmunosorbentVolume

The volume of the BlankAntibodyComplex to be loaded on the ELISAPlate. In DirectCompetitiveELISA and IndirectCompetitiveELISA, this step enables the free primary antibody to bind to the ReferenceAntigen coated on the plate. In FastELISA, this step enables the PrimaryAntibody-TargetAntigen-CaptureAntibody complex to bind to the CoatingAntibody on the plate.

Default Value: Automatic

Default Calculation: If the Method is set to DirectCompetitiveELISA, IndirectCompetitiveELISA, or FastELISA, the option is automatically set to 100 Microliter.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 200*Microliter] | Automatic) | Null

Index Matches to: Blank

BlankImmunosorbentVolume

The volume of the Blank to be loaded on the ELISAPlate for the target antigen to bind to the capture antibody in DirectSandwichELISA and IndirectSandwichELISA.

Default Value: Automatic

Default Calculation: If the Method is set to DirectSandwichELISA and IndirectSandwichELISA, the option is automatically set to 100 Microliter.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 200*Microliter] | Automatic) | Null

Index Matches to: Blank

BlankPrimaryAntibodyImmunosorbentVolume

The volume of the BlankPrimaryAntibody to be loaded on the ELISAPlate for Immunosorbent assay.

Default Value: Automatic

Default Calculation: If the Method is set to DirectELISA, IndirectELISA, DirectSandwichELISA, or IndirectSandwichELISA, the option is automatically set to 100 Microliter.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 200*Microliter] | Automatic) | Null

Index Matches to: Blank

BlankSecondaryAntibodyImmunosorbentVolume

The volume of the Secondary Antibody to be loaded on the ELISAPlate for immunosorbent step.

Default Value: Automatic

Default Calculation: If the Method is set to IndirectELISA, IndirectSandwichELISA, and IndirectCompetitiveELISA, the option is automatically set to 100 Microliter.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 200*Microliter] | Automatic) | Null

Index Matches to: Blank

BlankSubstrateSolution

Defines the substrate solution for the Blank.

Default Value: Automatic

Default Calculation: If enzyme is Horseredish Peroxidase, the option will be automatically set to Model[Sample,"ELISA TMB Stabilized Chromogen"]. If enzyme is Alkaline Phosphatase, then the option is automatically set to Model[Sample,"AP Substrate PNPP Solution"].

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

Index Matches to: Blank

BlankStopSolution

The reagent that is used to stop the reaction between the enzyme and its substrate.

Default Value: Automatic

Default Calculation: If enzyme is Horseradish Peroxidase, then the option is automatically set to Model[Sample,"ELISA HRP-TMB Stop Solution"]. If enzyme is Alkaline Phosphatase, then the option is automatically set to Model[Sample,"AP Substrate Stop Solution"].

Pattern Description: An object of type or subtype Model[Sample] or Object[Sample] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Sample], Object[Sample]}] | _String) | Automatic) | Null

Index Matches to: Blank

BlankSubstrateSolutionVolume

The volume of BlankSubstrateSolution to be added to the corresponding well.

Default Value: Automatic

Default Calculation: If SubstrateSolution is populated, then the option is automatically set to 100ul.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 200*Microliter] | Automatic) | Null

Index Matches to: Blank

BlankStopSolutionVolume

The volume of BlankStopSolution to be added to the corresponding well.

Default Value: Automatic

Default Calculation: If Model[Sample,"ELISA TMB Stabilized Chromogen"] or Model[Sample,"ELISA HRP-TMB Stop Solution"] is selected, the StopSolutionVolume is automatically set to 100ul.

Pattern Description: Greater than or equal to 0 microliters and less than or equal to 200 microliters or Null.

Programmatic Pattern: (RangeP[0*Microliter, 200*Microliter] | Automatic) | Null

Index Matches to: Blank

Assay Plate

ELISAPlate

The assay plate each sample, standard, and blank will be loaded into and the immunosorbent assay will take place. This plate can be pre-coated and blocked in advance.

Default Value: Automatic

Default Calculation: The option will be automatically set to an optical, flat-bottom 96 well plate made with polystyrene. If Samples are pre-coated to the a plate, the option will be automatically set to this plate.

Pattern Description: An object of type or subtype Model[Container, Plate] or Object[Container, Plate] or a prepared sample.

Programmatic Pattern: (ObjectP[{Model[Container, Plate], Object[Container, Plate]}] | _String) | Automatic

SecondaryELISAPlate

The second assay plate, if needed.

Default Value: Automatic

Default Calculation: If the total number of Sample (including spiked samples and dilutions), standards, and blanks, times NumberOfReplications exceeds 96, then the option will be automatically set to an optical, flat-bottom 96 well plate made with polystyrene. If Samples are pre-coated to two plates, the option will be automatically set to the second plate.

Pattern Description: An object of type or subtype Model[Container, Plate] or Object[Container, Plate] or a prepared sample or Null.

Programmatic Pattern: ((ObjectP[{Model[Container, Plate], Object[Container, Plate]}] | _String) | Automatic) | Null

ELISAPlateAssignment

Specifies the placement of samples and their corresponding spikes, dilutions, and antibodies in the first ELISAPlate.

Default Value: Automatic

Default Calculation: Samples are automatically assigned according to the input sequence (UnknownSamples,Standards,Blanks), to the ELISAPlate from the A1 position, consecutively, in a column-wise fashion. Each sample and their dilution curve will be placed next to each other, then each replicates are placed next to each other. When samples are pre-coated onto the plate, they are arranged from the A1 position, consequtively, in a column-wise fashion,regardless of the input sequence. If the first plate cannot accommodate all the samples, the samples will automatically be assigned to the SecondaryELISAPlate. Due to possible plate-to-plate variations, when two plates are needed, users are recommended to rearrange the samples so that the samples, standards, and blanks that are detected using the same conditions (i.e. same experiment) should be placed in the same plate. If impossible, additional standards and blanks should be included so that each sample has a corresponding set of standards and blanks on the same plate.

Pattern Description: List of one or more {Type, Sample, Spike, SpikeDilutionFactor, SampleDilutionFactors, CoatingAntibody, CoatingAntibodyDilutionFactor, CaptureAntibody, CaptureAntibodyDilutionFactor, ReferenceAntigen, ReferenceAntigenDilutionFactor, PrimaryAntibody, PrimaryAntibodyDilutionFactor, SecondaryAntibody, SecondaryAntibodyDilutionFactor, CoatingVolume, BlockingVolume, SampleAntibodyComplexImmunosorbentVolume, SampleImmunosorbentVolume, PrimaryAntibodyImmunosorbentVolume, SecondaryAntibodyImmunosorbentVolume, SubstrateSolution, StopSolution, SubstrateSolutionVolume, StopSolutionVolume} entries.

Programmatic Pattern: {{Unknown | Spike | Standard | Blank, ObjectP[{Model[Sample], Object[Sample]}] | _String, (ObjectP[{Model[Sample], Object[Sample]}] | _String) | Null, RangeP[0, 1] | Null, {RangeP[0, 1]..}, (ObjectP[{Model[Sample], Object[Sample]}] | _String) | Null, RangeP[0, 1] | Null, (ObjectP[{Model[Sample], Object[Sample]}] | _String) | Null, RangeP[0, 1] | Null, (ObjectP[{Model[Sample], Object[Sample]}] | _String) | Null, RangeP[0, 1] | Null, ObjectP[{Model[Sample], Object[Sample]}] | _String, RangeP[0, 1] | Null, (ObjectP[{Model[Sample], Object[Sample]}] | _String) | Null, RangeP[0, 1] | Null, RangeP[0*Microliter, 200*Microliter] | Null, RangeP[0*Microliter, 300*Microliter] | Null, RangeP[0*Microliter, 200*Microliter] | Null, RangeP[0*Microliter, 200*Microliter] | Null, RangeP[0*Microliter, 200*Microliter] | Null, RangeP[0*Microliter, 200*Microliter] | Null, ObjectP[{Model[Sample], Object[Sample]}] | _String, ObjectP[{Model[Sample], Object[Sample]}] | _String, RangeP[0*Microliter, 200*Microliter] | Null, RangeP[0*Microliter, 200*Microliter] | Null}..} | Automatic

SecondaryELISAPlateAssignment

Specifies the placement of samples and their corresponding spikes, dilutions, and antibodies in the second ELISAPlate.

Default Value: Automatic

Default Calculation: Samples are automatically assigned according to the input sequence (UnknownSamples,Standards,Blanks), to the ELISAPlate from the A1 position, consecutively, in a column-wise fashion. Each sample and their dilution curve will be placed next to each other, then each replicates are placed next to each other. When samples are pre-coated onto the plate, they are arranged from the A1 position, consequtively, in a column-wise fashion,regardless of the input sequence. If the first plate cannot accommodate all the samples, the samples will automatically be assigned to the SecondaryELISAPlate. Due to possible plate-to-plate variations, when two plates are needed, users are recommended to rearrange the samples so that the samples, standards, and blanks that are detected using the same conditions (i.e. same experiment) should be placed in the same plate. If impossible, additional standards and blanks should be included so that each sample has a corresponding set of standards and blanks on the same plate.

Pattern Description: List of one or more {Type, Sample, Spike, SpikeDilutionFactor, SampleDilutionFactors, CoatingAntibody, CoatingAntibodyDilutionFactor, CaptureAntibody, CaptureAntibodyDilutionFactor, ReferenceAntigen, ReferenceAntigenDilutionFactor, PrimaryAntibody, PrimaryAntibodyDilutionFactor, SecondaryAntibody, SecondaryAntibodyDilutionFactor, CoatingVolume, BlockingVolume, SampleAntibodyComplexImmunosorbentVolume, SampleImmunosorbentVolume, PrimaryAntibodyImmunosorbentVolume, SecondaryAntibodyImmunosorbentVolume, SubstrateSolution, StopSolution, SubstrateSolutionVolume, StopSolutionVolume} entries or Null.

Programmatic Pattern: ({{Unknown | Spike | Standard | Blank, ObjectP[{Model[Sample], Object[Sample]}] | _String, (ObjectP[{Model[Sample], Object[Sample]}] | _String) | Null, RangeP[0, 1] | Null, {RangeP[0, 1]..}, (ObjectP[{Model[Sample], Object[Sample]}] | _String) | Null, RangeP[0, 1] | Null, (ObjectP[{Model[Sample], Object[Sample]}] | _String) | Null, RangeP[0, 1] | Null, (ObjectP[{Model[Sample], Object[Sample]}] | _String) | Null, RangeP[0, 1] | Null, ObjectP[{Model[Sample], Object[Sample]}] | _String, RangeP[0, 1] | Null, (ObjectP[{Model[Sample], Object[Sample]}] | _String) | Null, RangeP[0, 1] | Null, RangeP[0*Microliter, 200*Microliter] | Null, RangeP[0*Microliter, 300*Microliter] | Null, RangeP[0*Microliter, 200*Microliter] | Null, RangeP[0*Microliter, 200*Microliter] | Null, RangeP[0*Microliter, 200*Microliter] | Null, RangeP[0*Microliter, 200*Microliter] | Null, ObjectP[{Model[Sample], Object[Sample]}] | _String, ObjectP[{Model[Sample], Object[Sample]}] | _String, RangeP[0*Microliter, 200*Microliter] | Null, RangeP[0*Microliter, 200*Microliter] | Null}..} | Automatic) | Null

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

ELISA Method

DirectELISA method detects the immobilized antigen by an antibody directly conjugated with an enzyme:

ExperimentELISA[mySamples, Method -> DirectELISA]

IndirectELISA method detects the immobilized antigen by an unlabled primary antibody and a secondary antibody conjugated to an enzyme:

ExperimentELISA[mySamples, Method -> IndirectELISA]

DirectSandwichELISA method first applies the antigen to a plate with pre-coated capture antibody before detecting in a DirectELISA configuration:

ExperimentELISA[mySamples, Method -> DirectSandwichELISA]

IndirectSandwichELISA method first applies the antigen to a plate with pre-coated capture antibody before detecting in a IndirectELISA configuration:

ExperimentELISA[mySamples, Method -> IndirectSandwichELISA]

DirectCompetitiveELISA method detects antigen by allowing the antigen to competes with a reference for binding to labeled antibodies in a DirectELISA configuration:

ExperimentELISA[mySamples, Method -> DirectCompetitiveELISA]

IndirectCompetitiveELISA method detects antigen by allowing the antigen to competes with a reference for binding to unlabeled antibodies in a IndirectELISA configuration:

ExperimentELISA[mySamples, Method -> IndirectCompetitiveELISA]

FastELISA method detects antigen by using a coated antibody against a tag which is conjugated to another antigen-targeting antibody:

ExperimentELISA[mySamples, Method -> FastELISA]

Sample Spiking

The input samples can be mixed with the desired spike samples with known concentration(s) of analyte(s), for evaluation of sample matrices in a new ELISA assay:

ExperimentELISA[{mySample1, mySample2, mySample3, mySample4},

 	Spike -> {mySpikeSample1, mySpikeSample2, Null, Null},

 	SpikeDilutionFactor -> {0.1, 0.2, Null, Null}

 ]

Sample Dilution

A serial dilution curve can be specified for an input sample by providing the volumes of the diluted samples, a constant dilution factor, and a number of dilutions. This should be used if you want the sample to be diluted by the same factor at each step of the serial dilution. The volume of the sample will be the final volume of the sample after the dilution is performed. The example call below will create a series of samples with dilution factors of (0.1,0.01) and a volume of 100 Microliters:

ExperimentELISA[mySamples,

 	SampleSerialDilutionCurve -> {100 * Microliter, {0.1, 2}}

 ]

A serial dilution curve can be specified for an input sample by providing the volumes of the diluted samples and each dilution factor.This should be used if you want the sample to be diluted by different factors at each step of the serial dilution. The volume of the sample will be the final volume of the sample after the dilution is performed. The example call below will create a series of samples with dilution factors of (0.5, 0.05, 0.005) and a volume of 100 Microliters:

ExperimentELISA[mySamples,

 	SampleSerialDilutionCurve -> {100 * Microliter, {0.5, 0.1, 0.1}}

 ]

A serial dilution curve can be specified for an input sample by providing the volume of sample to be transferred, the volume of diluent and the number of dilutions. This should be used if you want give the volumes the sample will be diluted by with instead of dilution factors. The example call below will create a series of samples with dilution factors of (0.9, 0.81) and a volume of 10 Microliters:

ExperimentELISA[mySamples,

 	SampleSerialDilutionCurve -> {90 * Microliter, 10 * Microliter, 2}

 ]

A dilution curve can be specified for an input sample by providing the volumes of the diluted samples and the dilution factor:

ExperimentELISA[mySamples,

 	SampleDilutionCurve -> {{100 * Microliter, 0.1}, {100 * Microliter,

    0.2}}

 ]

A dilution curve can be specified for an input sample by providing the volume of the sample:

ExperimentELISA[mySamples,

 	SampleDilutionCurve -> {

   		{50 * Microliter, 50 * Microliter},

   		{10 * Microliter, 90 * Microliter}

   	}

 ]

Standard and Blank

Standard samples can be added to ELISA experiment to provide information about the accuracy of the assay or be used for the generation of the standard curves:

ExperimentELISA[mySamples,

 	Standard -> myStandardSamples,

 	StandardSerialDilutionCurve -> {100 * Microliter, {0.5, 8}}

 ]

Blank samples can be added to ELISA experiment to measure the background signal from the reagents and the instrument:

ExperimentELISA[mySamples, Blank -> myBlankSamples]

Antibodies and Reference Antigen

PrimaryAntibody-- to specify primary antibody that binds selectively to the antigen of interest:

ExampleELISA[{mySample1, mySample2, mySample3},

 	Method -> DirectELISA,

 	PrimaryAntibody -> myAntibody1,

 PrimaryAntibodyDilutionFactor -> 0.005

 ]

SecondaryAntibody-- to specify secondary antibody that binds to the primary antibody-antigen complex

ExampleELISA[{mySample1, mySample2, mySample3},

 	Method -> IndirectELISA,

 	PrimaryAntibody -> myAntibody1,

 PrimaryAntibodyDilutionFactor -> 0.005,

 SecondaryAntibody -> myAntibody2,

 	SecondaryAntibodyDilutionFactor -> 0.0001

 ]

CaptureAntibody (for DierectSandwichELISA and IndirectSandwichELISA)-- to specify the antibody coated on the ELISA Plate that pulls down the target antigen from samples.

ExampleELISA[{mySample1, mySample2, mySample3},

 	Method -> IndirectSandwichELISA,

 	CaptureAntibody -> myAntibody2,

 CaptureAntibodyDilutionFactor -> 0.0001

 ]

ReferenceAntigen-- to specify the sample containing the target antigen coated on the ELISA Plate that competes with the antigen in the sample for the binding of the primary antibody.

ExampleELISA[{mySample1, mySample2, mySample3},

 	Method -> IndirectCompetitiveELISA,

 	Referenceantigen -> myAntigen1,

 ReferenceantigenDilutionFactor -> 0.005

 ]

CaptureAntibody (for FastELISA)--antibody that binds to the target antigen in the sample and contains an epitope that inables the antibody-antigen complex to be pulled down by the antibody coated on the ELISA plate:

ExperimentELISA[{mySample1, mySample2, mySample3},

 	Method -> FastELISA,

 	CaptureAntibody -> {myCaptureAntibody1, myCaptureAntibody2,

   myCaptureAntibody3},

 	CaptureAntibodyDilutionFactor -> {0.1, 0.2, 0.3}

 ]

CoatingAntibody--antibody that is immobilized on the ELISA plate and targets the special epitope on the capture antibody:

ExperimentELISA[{mySample1, mySample2, mySample3},

 	Method -> FastELISA,

 	CoatingAntibody -> myCoatingAntibody1,

 CoatingAntibodyDilutionFactor -> 0.001

 ]



Preferred Input Containers

The experiment takes common liquid handler compatible containers.



Possible Issues

Evaporation during prolonged incubation

All incubations after ELISAPlate coating are performed in a plate incubator without plate seals. Prolonged incubation at high temperature (such as 37 °C for 3 hours) may result in evaporation of samples. To reduce such effect, avoid long incubation of samples with very small volumes (such as under 50 Microliter) at a high temperature.

Uneven incubation time

The 4-channel pipette loads liquid into 4 wells at a time. When incubation time is short but number of wells is large, the time-difference between the loading of first and last wells may affect data. For this, we recommend incubation times to be longer than 30 minutes.

Sub-optimal Dilution

Dilutions of samples, standards, and antibodies should be empirically optimized for the best performance of the experiment. For example, if antibody is over dilute, the signal may be too weak to be detected.

Sub-optimal Diluent

Diluent for samples, standards and antibodies should be empirically optimized for the best performance of the experiment. Form example, biocarbonate buffer at PH 10 may result in better coating than phosphate-buffered saline at PH 6.7.

Detection reagent

Detection reagent such as TMB with H2O2 may have a short shelf life. We recommend using stablized detection reagent that do not require fresh mixing immediately before experiment.

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

You are working on a research project to use machine learning for drug discovery. Your goals are the following: (1) the project must have high clinical value, meaning the research contributes to helping patients, (2) the project must include a scientifically impactful application of machine learning to drug discovery, and (3) the project must use Emerald Cloud Labs (ECL) for all experimental validation with a 3-month limit on experiments. Your team previously decided to pursue peptide-based therapeutics. You previously designed experimental protocols for synthesis and validation of peptides that are designed to bind to a given protein drug target. Now you must implement one of these protocols using ECL. Please implement the ExperimentELISA protocol using the appropriate commands and syntax from ECL, writing out the experiment in the form ExperimentELISA[<inputs>] where you fill in <inputs> with the appropriate inputs. Please refer to the ECL documentation that is provided as context with example function calls and the full set of options for the experiment. In general, leave most options at their default values (and therefore do not specify them) except for those options that should be changed based on your specific experimental design. For every option that you do specify, please explain why you chose that value instead of the default.

Medicinal Chemist, please provide your response to the agenda.

## Medicinal Chemist

To implement the `ExperimentELISA` protocol using Emerald Cloud Labs (ECL) for the validation of peptide-based therapeutics, we need to carefully select the inputs and options based on our specific experimental design. Here's a proposed setup for the `ExperimentELISA` function call, along with explanations for the specified options:

### ExperimentELISA Function Call

```plaintext
ExperimentELISA[
    myPeptideSamples,
    Method -> DirectELISA,
    PrimaryAntibody -> myPrimaryAntibody,
    PrimaryAntibodyDilutionFactor -> 0.005,
    Standard -> myStandardSamples,
    StandardSerialDilutionCurve -> {100 * Microliter, {0.5, 8}},
    Blank -> myBlankSamples,
    SubstrateSolution -> Model[Sample, "ELISA TMB Stabilized Chromogen"],
    StopSolution -> Model[Sample, "ELISA HRP-TMB Stop Solution"]
]
```

### Explanation of Specified Options

1. **Method -> DirectELISA**: 
   - **Reason**: DirectELISA is chosen for its simplicity and speed, as it involves fewer steps compared to indirect methods. This is suitable for initial validation of peptide binding to the target protein.

2. **PrimaryAntibody -> myPrimaryAntibody**:
   - **Reason**: The primary antibody is selected based on its specificity to the target antigen (peptide). This ensures accurate detection of the peptide-antigen interaction.

3. **PrimaryAntibodyDilutionFactor -> 0.005**:
   - **Reason**: A dilution factor of 0.005 is chosen to optimize the signal-to-noise ratio, ensuring sufficient sensitivity without excessive background noise.

4. **Standard -> myStandardSamples**:
   - **Reason**: Including standard samples allows for the generation of a standard curve, which is essential for quantifying the concentration of the target antigen in the samples.

5. **StandardSerialDilutionCurve -> {100 * Microliter, {0.5, 8}}**:
   - **Reason**: A serial dilution curve with a starting volume of 100 microliters and a dilution factor of 0.5 over 8 dilutions provides a broad range for accurate quantification and helps in establishing a reliable standard curve.

6. **Blank -> myBlankSamples**:
   - **Reason**: Blank samples are included to measure the background signal, which is crucial for accurate data interpretation and ensuring the specificity of the assay.

7. **SubstrateSolution -> Model[Sample, "ELISA TMB Stabilized Chromogen"]**:
   - **Reason**: TMB is a common substrate for HRP, providing a colorimetric readout that is easy to measure and interpret. The stabilized form ensures consistency and reliability.

8. **StopSolution -> Model[Sample, "ELISA HRP-TMB Stop Solution"]**:
   - **Reason**: The stop solution is used to halt the enzymatic reaction, allowing for consistent timing in measurement and preventing overdevelopment of the colorimetric signal.

### General Considerations

- **Default Values**: Most options are left at their default values to streamline the setup and focus on critical parameters that directly impact the experimental outcomes.
- **ECL Utilization**: By using ECL for this experiment, we ensure high precision and reproducibility, which is essential for validating the peptide's binding efficacy within the 3-month experimental limit.

This setup aligns with our project goals by ensuring high clinical value through accurate validation of peptide interactions, leveraging machine learning predictions, and utilizing ECL for experimental validation.

