#### A National Land Use And Land Cover Projection For Threat Assessment And Conservation Planning
How would a business as usual scenario affect ecosystems across the USA, by 2061? 

#### Purpose
This biogeographical analysis package displays and summarizes land use change data from Kreitler and Sleeter (2018), "A national land use and land cover projection for threat assessment and conservation planning". The classified threat layer from this dataset is used to understand the amount of area threatened by development in each Omernik Level III Ecoregion. Threat is defined in the data release as no/low/medium/high threat according to likelihood of developed land use change (0%, <33%, <66%, <100%, respectively). This information could be used in analyses to determine how much area is expected to transition into a developed class by for each ecoregions in the Continental USA. 

> This dataset contains a projection of land use and land cover for the conterminous United States for the period 2001 - 2061. This projection used the USGS's LUCAS (Land Use and Carbon Scenario Simulator) model to project a business as usual scenario of land cover and land use change. By running the LUCAS model on the USGS's YETI high performance computer and parallelizing the computation, we ran 100 Monte Carlo simulations based on empirically observed rates of change at a relatively fine scale (270m). We sampled from multiple observed rates of change at the county level to introduce heterogeneity into the Monte Carlo simulations. Using this approach allowed the model to project different outcomes that were summarized to produce estimates of likelihood of development at any given location. These estimates can then be used in conservation planning to determine where, and at what rate, land use change would occur according to this scenario.

#### Inputs
> Omernik L3 from ? 
>"Threat.tif" from https://www.sciencebase.gov/catalog/item/5a87249de4b00f54eb3a2e1e
> "DevelopmentPercent2061.tif" from https://www.sciencebase.gov/catalog/item/5a87249de4b00f54eb3a2e1e

#### Outputs
Area of High, Med, Low threat summarized by L3 ecoregions in .csv. UPLOAD

#### Constraints
spatial

#### Dependencies
#### Code
#### Tests
#### Provenance

#### Citations
Kreitler, J., and Sleeter, B.M., 2018, A national land use and land cover projection for threat assessment and conservation planning: U.S. Geological Survey data release, https://doi.org/10.5066/F77080Q7.

#### USGS Provisional Software

This software is preliminary or provisional and is subject to revision. It is being provided to meet the need for timely best science. The software has not received final approval by the U.S. Geological Survey (USGS). No warranty, expressed or implied, is made by the USGS or the U.S. Government as to the functionality of the software and related material nor shall the fact of release constitute any such warranty. The software is provided on the condition that neither the USGS nor the U.S. Government shall be held liable for any damages resulting from the authorized or unauthorized use of the software.

# test "#"
## test "##"
### test "###"
#### test "####"
> test ">"
