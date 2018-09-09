#### A National Land Use And Land Cover Projection For Threat Assessment And Conservation Planning
How would a business as usual growth scenario affect ecosystems across the USA, by 2061? 

#### Purpose
This biogeographical analysis package displays and summarizes a land use change projection from Kreitler and Sleeter (2018), "A national land use and land cover projection for threat assessment and conservation planning". The classified threat layer from this dataset is used to project the amount of area threatened by development in each Omernik Level III Ecoregion. Threat is defined in the data release as no/low/medium/high threat according to likelihood of developed land use change (0%, <33%, <66%, <100%, respectively). This information could be used in analyses to determine how much area is expected to transition into a developed class by for each ecoregions in the Continental USA. Further detail excerpted from the data release:

> This dataset contains a projection of land use and land cover for the conterminous United States for the period 2001 - 2061. This projection used the USGS's LUCAS (Land Use and Carbon Scenario Simulator) model to project a business as usual scenario of land cover and land use change. By running the LUCAS model on the USGS's YETI high performance computer and parallelizing the computation, we ran 100 Monte Carlo simulations based on empirically observed rates of change at a relatively fine scale (270m). We sampled from multiple observed rates of change at the county level to introduce heterogeneity into the Monte Carlo simulations. Using this approach allowed the model to project different outcomes that were summarized to produce estimates of likelihood of development at any given location. These estimates can then be used in conservation planning to determine where, and at what rate, land use change would occur according to this scenario.

#### Inputs
- [Omernik level 3 ecoregions from EPA](https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states)
- [Threat.tif](https://www.sciencebase.gov/catalog/item/5a87249de4b00f54eb3a2e1e)
- [DevelopmentPercent2061.tif](https://www.sciencebase.gov/catalog/item/5a87249de4b00f54eb3a2e1e)

#### Outputs
- [Threat by Ecoregions](https://github.com/usgs-bis/expected-land-use-change/blob/readme-edits.md/Threat_30m_L3_Ecoregions.txt) Tabular output of area in the High, Med, Low, and No threat classes summarized by L3 ecoregions. Also includes 'All Threat' (sum of High, Med, and Low threat), and the percent of ecoregion threatened as 'All Threat/Total Area'. 

#### Constraints
These data are meant to be used at a scale of 1:100,000 or smaller (such as 1:250,000 or 1:500,000) for the purpose of assessing land use change, and the potential consequences of that change over large geographic regions.
Scale: These data have been resmapled using nearest neighbor methods from 270m down to 30m to match the output resolution of other primary datasets on the National Biogeographic Map. The data were produced with intended analysis at the ecoregion level, that is, geographic areas from several hundred thousand to millions of hectares in size. The data provide a coarse-filter approach to analysis, and are a projection of potential land use change, based on observed trends. 

#### Citations
Kreitler, J., and Sleeter, B.M., 2018, A national land use and land cover projection for threat assessment and conservation planning: U.S. Geological Survey data release, https://doi.org/10.5066/F77080Q7.

#### USGS Provisional Software
This software is preliminary or provisional and is subject to revision. It is being provided to meet the need for timely best science. The software has not received final approval by the U.S. Geological Survey (USGS). No warranty, expressed or implied, is made by the USGS or the U.S. Government as to the functionality of the software and related material nor shall the fact of release constitute any such warranty. The software is provided on the condition that neither the USGS nor the U.S. Government shall be held liable for any damages resulting from the authorized or unauthorized use of the software.
